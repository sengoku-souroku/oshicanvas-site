# 推しキャンバス / OshiCanvas 公開サイト

iPhone向け推し活記録アプリ「推しキャンバス / OshiCanvas」の紹介・Privacy Policy・SupportをGitHub Pagesで運用するための、独立した公開用リポジトリです。

コンセプトは「推しごとに、自分だけの記録帳を。」。アプリ本体のprivate repositoryとは分離し、アプリのソースコード、実ユーザーデータ、写真、開発ログ、署名・認証情報は置きません。

**2026-11-14公開完了：ユーザーの明示承認後、サイトrepositoryのみpublic化し、承認済み原稿`6352b04`をmainへ統合・pushしました。GitHub Pagesはmain／root、HTTPSで公開中です。** Top・Privacy・Support・CSSは匿名HTTP200、公開HTML/CSSは承認済み原稿と一致します。アプリ本体のpush・merge、EAS Build／Submit、App Store公開は行っていません。

公開前はprivate、main=`322ccc9`、Pages未設定、URLはHTTP404でした。以下の公開手順と承認範囲は、今回の公開経緯および将来の更新時の確認用です。

## 構成

```text
oshicanvas-site/
├── .gitignore
├── .nojekyll
├── index.html
├── styles.css
├── README.md
├── privacy/
│   └── index.html
├── support/
│   └── index.html
└── tests/
    └── check_site.py
```

HTML/CSSのみ。npm、フレームワーク、ビルドコマンド、JavaScript、外部CDN、Webフォント、広告、アクセス解析、trackingは使いません。CSSはすべてローカルの`styles.css`にあります。`.nojekyll`は静的ファイルをそのまま公開するための指定です。

各ページのリンクとCSSは相対パスで指定し、GitHub Pagesのproject siteの`/oshicanvas-site/`配下で動作します。ブランドマークと記録帳のイメージはCSSで作成しており、アプリの実スクリーンショットではありません。実在する人物・キャラクターの名前や画像は使用していません。

## 確定した問い合わせ先・表示方針

問い合わせメールは **oshicanvas@gmail.com** です。SupportとPrivacy Policyの両ページに、表示文字列と`mailto:oshicanvas@gmail.com`を設定しています。

サイト本文には開発者名・運営者名を表示しません。個人名への置換は行わず、全ページから氏名用の仮表示を削除しました。問い合わせ窓口は上記メールへ統一します。

メールリンクの確認は、実際にメールの送受信を行ったことを意味しません。

Gitのauthor/committerはサイト本文とは別に公開される情報です。公開前には`git log --format=fuller`で履歴も確認してください。今回のcommitには公開ブランド名と上記問い合わせメールを使い、既存の履歴・アプリrepository・global Git設定は変更しません。

## 公開URL / App Store Connect

公開repository：`sengoku-souroku/oshicanvas-site`。

| 用途 | 公開URL |
| --- | --- |
| Top / Marketing URL候補 | https://sengoku-souroku.github.io/oshicanvas-site/ |
| Privacy Policy URL | https://sengoku-souroku.github.io/oshicanvas-site/privacy/ |
| Support URL | https://sengoku-souroku.github.io/oshicanvas-site/support/ |

上記3 URLとCSSは2026-11-14に匿名HTTP200と承認済み原稿との一致を確認しました。iPhone Safariの実表示と問い合わせメールの受信は未確認です。App Store Connectの対応するURL欄への登録は別工程であり、今回変更していません。

## GitHub Pages公開方法（今回実施した手順）

1. 下の公開前checklistで、実機・実装・Privacy照合など公開前にできる確認を済ませる。
2. 既存の`origin`が`sengoku-souroku/oshicanvas-site`であることを再確認する。新repositoryは作らず、privateからpublicへの変更は明示承認後だけ行う。
3. 完成したサイトbranch・公開履歴・差分を確認し、承認後にサイトの`main`へ統合して通常pushする。アプリ本体repositoryをpush・mergeせず、force pushもしない。
4. 公開repositoryの **Settings → Pages → Build and deployment → Source → Deploy from a branch** を選ぶ。
5. branchを **main**、folderを **/(root)** にし、Saveする。独自ビルドやnpmの設定は不要。
6. GitHub側の公開処理後、上記3 URL、CSS、ページ間リンク、メールリンクを確認する。HTTPSで表示されることも確認する。
7. 確認後にApp Store ConnectへURLを登録する。以後`main`へpushするとサイトが更新されるため、変更は公開前に確認する。

GitHub公式：[静的サイトの作成](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)、[公開元branchの設定](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。今回のリモート操作は明示承認されたサイトrepoの統合・push・public化・Pages設定だけです。

## Privacy文言の基準

- v1.0の端末内保存・Local AI方針に合わせ、運営者独自サーバーへ記録本文・写真を保存せず、クラウドAIへ送信して処理しないと説明する。
- 画像入力はApple Vision OCR＋OCR文字／位置を使うFoundation Models分類。原画像を分類へ再入力せず、クラウドAIへ送らない。画像入力のPro／対応端末・OS・Apple Intelligence条件を明示する。
- AIは提案であり、「この内容で1件登録する」が確認した値への明示承認。一般公開未開始を明記し、TestFlight準備と製品公開を混同しない。
- 画像項目1つ／複数／なしの添付方針、安全化済みコピー、一時画像、未保存本文のbackground破棄、ユーザーが保存した通常画像・文字のBackup対象を区別する。
- 保存結果不明時は再登録を促さず、内容を含まない操作ID等の端末内復旧metadataと通常の保存記録を区別する。
- Webオンライン取得・バックグラウンド常時監視・自動収集はv1.0で公開しない。
- 購入確認、配布・更新、iOS/iCloud等の通信と、運営者によるユーザーデータ収集を区別する。「完全に通信しない」「一切外部通信しない」と保証しない。
- backupは本文・写真を含み、暗号化されない。共有先はユーザーが選ぶ。アプリ削除・OS backup・独自backupの違いを説明する。
- 問い合わせメールには必要最小限の情報だけを求める。バックアップや写真の提出を前提にしない。
- GitHub Pagesには配信に伴う通信・セキュリティ目的のIP記録がある。サイト独自のtrackingを置かないことと区別し、Policy内で説明する。[GitHub公式の説明](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection)

## 公開前checklist

- [x] 問い合わせメールを`oshicanvas@gmail.com`に確定した
- [x] 仮の問い合わせメールをすべて解消し、Support・Privacyの表示とメールリンクを更新した
- [x] 開発者名・運営者名のplaceholderは不要と決定し、全ページとREADMEから削除した
- [x] 既存のprivate repository `sengoku-souroku/oshicanvas-site`とローカルmainの一致を確認した
- [x] OCR・画像添付・B1復旧・端末内処理とサイト原稿を照合した
- [ ] 公開範囲・push先・Pages設定の明示承認を得る
- [ ] 承認後に公開用の履歴・追跡ファイルを再確認し、通常pushする（force pushしない）
- [ ] GitHub Pagesを`main` / `/(root)`から有効化する
- [ ] 公開後、Top/Privacy/Supportの予定URLとページ間リンクがHTTPSでログインなしに開けることを確認する
- [ ] iPhone Safariで文字サイズ変更、縦横表示、リンク、横はみ出し、読み上げ・focusを確認する
- [ ] **Production/TestFlight buildの実際の機能・通信・権限と、Privacy Policy・Support・アプリ内Helpを最終照合した**
- [ ] **App Store ConnectのApp Privacy回答と、実装・第三者SDKのデータの扱い・本Policyを最終照合した**

Production/TestFlightとの照合には、Pro購入・購入の復元、AIの対応条件、backup/restoreの画面名、未公開機能を宣伝していないこと、Privacyの最終更新日（現原稿：2026年11月14日）を含めます。公開URL確認を終えるまでApp Store ConnectへURLを登録しません。

この原稿のローカル検証は、Production/TestFlight実機受入、公開URLの到達性、App Privacy回答の承認を意味しません。実装・SDK・課金・データ処理が変わるときは、文章と最終更新日も見直してください。

## 今回の公開承認対象（未実行）

新repositoryを作らず、`sengoku-souroku/oshicanvas-site`だけを再利用します。公開先は上表の3 URLです。アプリ本体repository、EASのchannel、Appleのアプリ公開範囲は変更しません。

推奨する承認単位は、完成したサイトbranchをサイトのmainへ統合し通常push、サイトrepoをpublicへ変更、GitHub Pagesを`main`／`/(root)`で有効化、匿名HTTPアクセスで3ページ・CSS・リンクを確認することです。privateを維持してPagesを使うには対応する有料planが必要です。現在のplanはAPIで確認できておらず、有料契約への変更は提案に含めません。

publicへ変更すると、HTML/CSSだけでなくREADME・テスト・Git履歴も閲覧可能になります。既存2commitのauthorは公開ブランド名と仮表示で、今回のcommitも`OshiCanvas <oshicanvas@gmail.com>`を使います。履歴を書き換えず、現在の連絡先と原稿を公開します。アプリコード、画像、ログ、AppleのID／証明書／認証情報は含めません。

## ローカル確認

`python tests/check_site.py`でHTML構造・リンク・anchor・連絡先・OCR説明・禁止された外部埋め込みを検査し、ローカルHTTPでproject siteのパス配下を検証します。外部サイトへの公開、メール送信、Appleログインは行わない標準ライブラリだけのテストです。iPhone Safariの実機表示や問い合わせメールの受信は未確認です。
