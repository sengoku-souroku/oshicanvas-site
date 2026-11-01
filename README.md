# 推しキャンバス / OshiCanvas 公開サイト

iPhone向け推し活記録アプリ「推しキャンバス / OshiCanvas」の紹介・Privacy Policy・SupportをGitHub Pagesで運用するための、独立した公開用リポジトリです。

コンセプトは「推しごとに、自分だけの記録帳を。」。アプリ本体のprivate repositoryとは分離し、アプリのソースコード、実ユーザーデータ、写真、開発ログ、署名・認証情報は置きません。

**現在はローカル作成のみ。未公開です。GitHub repository作成・push・Pages設定は行っていません。**

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
└── support/
    └── index.html
```

HTML/CSSのみ。npm、フレームワーク、ビルドコマンド、JavaScript、外部CDN、Webフォント、広告、アクセス解析、trackingは使いません。CSSはすべてローカルの`styles.css`にあります。`.nojekyll`は静的ファイルをそのまま公開するための指定です。

各ページのリンクとCSSは相対パスで指定し、GitHub Pagesのproject siteの`/oshicanvas-site/`配下で動作します。ブランドマークと記録帳のイメージはCSSで作成しており、アプリの実スクリーンショットではありません。実在する人物・キャラクターの名前や画像は使用していません。

## 確定した問い合わせ先・表示方針

問い合わせメールは **oshicanvas@gmail.com** です。SupportとPrivacy Policyの両ページに、表示文字列と`mailto:oshicanvas@gmail.com`を設定しています。

サイト本文には開発者名・運営者名を表示しません。個人名への置換は行わず、全ページから氏名用の仮表示を削除しました。問い合わせ窓口は上記メールへ統一します。

メールリンクの確認は、実際にメールの送受信を行ったことを意味しません。

Gitのauthor/committerはサイト本文とは別に公開される情報です。公開前には`git log --format=fuller`で履歴も確認してください。今回のcommitには公開ブランド名と上記問い合わせメールを使い、既存の履歴・アプリrepository・global Git設定は変更しません。

## 公開予定URL / App Store Connect

公開予定repository：`sengoku-souroku/oshicanvas-site`。

| 用途 | 公開後に使うURL |
| --- | --- |
| Top / Marketing URL候補 | https://sengoku-souroku.github.io/oshicanvas-site/ |
| Privacy Policy URL | https://sengoku-souroku.github.io/oshicanvas-site/privacy/ |
| Support URL | https://sengoku-souroku.github.io/oshicanvas-site/support/ |

これらは**予定URLであり、現在の公開・到達性を確認したURLではありません**。公開後にログアウト状態のブラウザとiPhone Safariで開けることを確認してから、App Store Connectの対応するURL欄に使用します。今回App Store Connectの変更は行いません。

## GitHub Pages公開方法（後日、明示的に公開するときだけ）

1. 下の公開前checklistで、実機・実装・Privacy照合など公開前にできる確認を済ませる。
2. GitHubで、公開用の空repository `sengoku-souroku/oshicanvas-site`を作成する。初期README等を自動生成せず、アプリ本体のrepositoryを転用しない。
3. このローカルrepositoryへ、その公開repositoryを`origin`として登録し、`main`を通常pushする。公開内容とcommit履歴を確認し、force pushはしない。
4. 公開repositoryの **Settings → Pages → Build and deployment → Source → Deploy from a branch** を選ぶ。
5. branchを **main**、folderを **/(root)** にし、Saveする。独自ビルドやnpmの設定は不要。
6. GitHub側の公開処理後、上記3 URL、CSS、ページ間リンク、メールリンクを確認する。HTTPSで表示されることも確認する。
7. 確認後にApp Store ConnectへURLを登録する。以後`main`へpushするとサイトが更新されるため、変更は公開前に確認する。

GitHub公式：[静的サイトの作成](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)、[公開元branchの設定](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。今回これらのリモート操作は行いません。

## Privacy文言の基準

- v1.0の端末内保存・Local AI方針に合わせ、運営者独自サーバーへ記録本文・写真を保存せず、クラウドAIへ送信して処理しないと説明する。
- AIは対応端末上の提案であり、ユーザー確認後の保存・適用を必要とする。未公開の画像AIを利用可能な機能として宣伝しない。
- Webオンライン取得・バックグラウンド常時監視・自動収集はv1.0で公開しない。
- 購入確認、配布・更新、iOS/iCloud等の通信と、運営者によるユーザーデータ収集を区別する。「完全に通信しない」「一切外部通信しない」と保証しない。
- backupは本文・写真を含み、暗号化されない。共有先はユーザーが選ぶ。アプリ削除・OS backup・独自backupの違いを説明する。
- 問い合わせメールには必要最小限の情報だけを求める。バックアップや写真の提出を前提にしない。
- GitHub Pagesには配信に伴う通信・セキュリティ目的のIP記録がある。サイト独自のtrackingを置かないことと区別し、Policy内で説明する。[GitHub公式の説明](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection)

## 公開前checklist

- [x] 問い合わせメールを`oshicanvas@gmail.com`に確定した
- [x] 仮の問い合わせメールをすべて解消し、Support・Privacyの表示とメールリンクを更新した
- [x] 開発者名・運営者名のplaceholderは不要と決定し、全ページとREADMEから削除した
- [ ] 公開用GitHub repository `sengoku-souroku/oshicanvas-site`を作成し、追跡ファイルと公開Git履歴を確認して通常pushする
- [ ] GitHub Pagesを`main` / `/(root)`から有効化する
- [ ] 公開後、Top/Privacy/Supportの予定URLとページ間リンクがHTTPSでログインなしに開けることを確認する
- [ ] iPhone Safariで文字サイズ変更、縦横表示、リンク、横はみ出し、読み上げ・focusを確認する
- [ ] **Production/TestFlight buildの実際の機能・通信・権限と、Privacy Policy・Support・アプリ内Helpを最終照合した**
- [ ] **App Store ConnectのApp Privacy回答と、実装・第三者SDKのデータの扱い・本Policyを最終照合した**

Production/TestFlightとの照合には、Pro購入・購入の復元、AIの対応条件、backup/restoreの画面名、未公開機能を宣伝していないこと、Privacyの最終更新日（現原稿：2026年11月1日）を含めます。公開URL確認を終えるまでApp Store ConnectへURLを登録しません。

この原稿のローカル検証は、Production/TestFlight実機受入、公開URLの到達性、App Privacy回答の承認を意味しません。実装・SDK・課金・データ処理が変わるときは、文章と最終更新日も見直してください。
