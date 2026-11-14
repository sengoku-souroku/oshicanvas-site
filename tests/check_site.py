"""Validate the static public site without sending content or mail externally."""
import functools
import http.server
import pathlib
import threading
import unittest
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFIX = '/oshicanvas-site'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
PAGES = [pathlib.Path('index.html'), pathlib.Path('privacy/index.html'), pathlib.Path('support/index.html')]


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.stack, self.tags = [], [], [], []
        self.feed(content)
        assert not self.stack, f'Unclosed tags: {self.stack}'

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        assert tag not in {'script', 'iframe', 'form', 'object', 'embed'}, tag
        assert not any(k.startswith('on') for k in attrs), 'Inline event handler'
        if tag not in VOID:
            self.stack.append(tag)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ['href', 'src']:
            if key in attrs:
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'Unexpected closing tag: {tag}'
        self.stack.pop()


class SiteTests(unittest.TestCase):
    def test_structure_and_local_links(self):
        for name in PAGES:
            with self.subTest(page=str(name)):
                content = (ROOT / name).read_text('utf-8')
                page = Page(content)
                self.assertEqual(len(page.ids), len(set(page.ids)))
                self.assertEqual(sum(t == 'h1' for t, _ in page.tags), 1)
                self.assertIn(('html', {'lang': 'ja'}), page.tags)
                self.assertTrue(any(t == 'meta' and a.get('name') == 'viewport' for t, a in page.tags))
                self.assertTrue(any(t == 'title' for t, _ in page.tags))
                for link in page.links:
                    uri = urllib.parse.urlsplit(link)
                    if uri.scheme:
                        self.assertIn(uri.scheme, ['https', 'mailto'])
                        if uri.scheme == 'mailto':
                            self.assertEqual(link, 'mailto:oshicanvas@gmail.com')
                        continue
                    self.assertFalse(link.startswith('//'))
                    target = (ROOT / name.parent / urllib.parse.unquote(uri.path)).resolve() if uri.path else (ROOT / name).resolve()
                    self.assertTrue(target.is_relative_to(ROOT))
                    if target.is_dir():
                        target /= 'index.html'
                    self.assertTrue(target.is_file(), link)
                    if uri.fragment:
                        self.assertIn(uri.fragment, Page(target.read_text('utf-8')).ids)
                for marker in ['CONTACT_EMAIL', 'PUBLIC_DEVELOPER_NAME', 'YOUR_EMAIL', 'TODO']:
                    self.assertNotIn(marker, content)

    def test_no_remote_styles_or_tracking(self):
        self.assertTrue((ROOT / '.nojekyll').is_file())
        css = (ROOT / 'styles.css').read_text('utf-8')
        self.assertNotIn('@import', css)
        self.assertNotIn('url(', css)
        self.assertIn('overflow-wrap: anywhere', css)
        self.assertIn(':focus-visible', css)
        self.assertIn('min-height: 44px', css)
        for name in PAGES:
            page = Page((ROOT / name).read_text('utf-8'))
            styles = [a['href'] for t, a in page.tags if t == 'link' and a.get('rel') == 'stylesheet']
            self.assertEqual(len(styles), 1)
            self.assertFalse(urllib.parse.urlsplit(styles[0]).scheme)

    def test_privacy_matches_the_reviewed_ocr_and_save_flow(self):
        text = (ROOT / 'privacy/index.html').read_text('utf-8')
        for fragment in ['Apple Vision', 'Apple Foundation Models', 'OCRで得た文字と位置情報', '元画像を再入力',
                         'Proと対応端末', 'この内容で1件登録する', '操作ID', 'バックグラウンド',
                         '一時的な画像ファイル', '画像項目が1つ', '画像項目が複数', '画像項目がない',
                         '暗号化されていません', '診断ログ', '2026-11-14', 'oshicanvas@gmail.com']:
            self.assertIn(fragment, text)
        self.assertNotIn('一切外部通信しない', text)

    def test_support_does_not_request_sensitive_ocr_or_purchases(self):
        text = (ROOT / 'support/index.html').read_text('utf-8')
        for fragment in ['この内容で1件登録する', '結果不明', '新しい記録を作り直さない',
                         'OCR全文', '認証コード', '通常はスクリーンショット', 'TestFlight内部テスト',
                         '同じアプリの旧版から置き換える', 'oshicanvas@gmail.com']:
            self.assertIn(fragment, text)
        self.assertIn('一般提供はまだ開始していません', (ROOT / 'index.html').read_text('utf-8'))

    def test_project_site_http_paths(self):
        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                parsed = urllib.parse.urlsplit(self.path)
                if not parsed.path.startswith(PREFIX + '/'):
                    self.send_error(404)
                    return
                self.path = parsed.path[len(PREFIX):]
                super().do_GET()

            def log_message(self, *args):
                pass

        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for route, marker in [('/', '推しキャンバス'), ('/privacy/', 'プライバシーポリシー'),
                                  ('/support/', '困ったときは'), ('/styles.css', 'overflow-wrap')]:
                with urllib.request.urlopen(f'http://127.0.0.1:{server.server_port}{PREFIX}{route}', timeout=5) as response:
                    self.assertEqual(response.status, 200)
                    self.assertIn(marker, response.read().decode('utf-8'))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
