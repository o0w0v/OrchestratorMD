# OrchestratorMD

「Create repository AGENTS.md」チャットで作成・更新した `AGENTS.md` と、他のコーディング製品との比較に使う固定30課題です。2026年10月20日に取り出したスナップショットです。

| 内容 | 場所 |
| --- | --- |
| 最新の開発ルール（原文） | [AGENTS.md](AGENTS.md) |
| 比較用30課題の一覧 | [課題一覧](benchmarks/official-30/INDEX.md) |
| 実施方法と採点の準備 | [比較手順](benchmarks/official-30/README.md) |
| 結果記録用CSV（未実行） | [結果テンプレート](benchmarks/official-30/results-template.csv) |
| データセット・harnessの固定リビジョン | [source-pins.json](benchmarks/official-30/source-pins.json) |

収録課題は、元のチャットで選定した **MultiPL-E Rust 20件とMulti-SWE-bench Rust 10件**です。公式データセットから選んだ固定の部分集合であり、公式ベンチマーク全体の代わりにはなりません。課題ごとのMarkdownとJSONを用意しています。

この公開物には問題入力、実施手順、空の結果CSVを収録しています。今回のアップロードでは性能評価を実行していません。公式採点には、固定したリビジョンの公式データとharnessを別のEvaluator環境に用意する必要があります。解答パッチ・hidden test body・実行済み比較結果は同梱していません。

`AGENTS.md` は元のNew-Concept-OSリポジトリ向けに作成した原文を保持しています。記載されたRust workspace・Worker・設定・参照文書は元のプロジェクトを指し、この配布物には実行系や内部運用資料を含みません。

ライセンスは [LICENSE](LICENSE)、課題の出典・ライセンスは [THIRD_PARTY_NOTICES.md](benchmarks/official-30/THIRD_PARTY_NOTICES.md) を参照してください。[PACKAGE_MANIFEST.json](PACKAGE_MANIFEST.json) に公開ファイルのSHA-256を記録しています。
