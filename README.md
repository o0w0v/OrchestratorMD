# OrchestratorMD — 開発ルール・実験記録

**Orchestrator Localのアプリ本体・導入手順は、[専用リポジトリ](https://github.com/o0w0v/orchestrator-local)へ分離しました。** アプリを使いたい方は、そちらを参照してください。

このリポジトリは、ローカルLLMへの作業分担を調べた開発ルール、課題、比較結果、説明資料の保管先です。アプリのソースを更新する場所とは分けて扱います。

## 資料を探す

|資料|入口|
|---|---|
|100件比較の説明|[通常SolとGemma＋Sol確認の比較](docs/presentations/2026-11-practical-review-100.md)|
|100件の課題・結果・詳細設計・再検証|[実験一式](benchmarks/practical-review-100/2026-11-05/README.md)|
|100件比較の解釈・会計・品質の範囲|[完了レビュー](benchmarks/practical-review-100/2026-11-05/COMPLETION_REVIEW_JA.md)|
|その他の実験・課題|[ベンチマークの案内](benchmarks/README.md)|
|説明資料・図|[説明資料の一覧](docs/presentations/README.md)|
|従来の開発用ルールと背景|[AGENTS.md](AGENTS.md) / [背景の案内](DEVELOPMENT_RULES_OVERVIEW_JA.md)|
|従来の開発用実行系の配布範囲|[配布状況の記録](PORTABLE_EXECUTION_READINESS_JA.md)|

過去の課題・結果・実行記録は保持しています。これらは個別の条件下での検証であり、Orchestrator Localの全利用場面での品質・費用を保証するものではありません。

## アプリの移転について

- 新しい公開先：[o0w0v/orchestrator-local](https://github.com/o0w0v/orchestrator-local)
- 新リポジトリでは本体をルートに置き、導入・使い方・内部設計・サンプル・テストをまとめています。
- 以前の`apps/orchestrator-local`には移転案内を残します。
- [分離前のアプリとトップREADME](https://github.com/o0w0v/OrchestratorMD/tree/d95881af188056933886d148f0bc0a5ea7c2e664)はGitの履歴から確認できます。

## ライセンス

[MIT License](LICENSE)。第三者の公式課題は[出典とライセンス](benchmarks/official-30/THIRD_PARTY_NOTICES.md)を参照してください。公開ファイルのSHA-256は[PACKAGE_MANIFEST.json](PACKAGE_MANIFEST.json)に記録しています。
