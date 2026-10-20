# OrchestratorMD

「Create repository AGENTS.md」チャットで作成した開発ルールと、製品比較に使う課題・検証結果を収録しています。2026年10月20日の公開スナップショットです。

| 内容 | 場所 |
| --- | --- |
| 最新の開発ルール（原文） | [AGENTS.md](AGENTS.md) |
| 独自生成した課題セット・初期コード・テスト・過去の検証結果 | [独自課題の一覧と配布物](benchmarks/custom/README.md) |
| 独自課題のセット別一覧 | [48セットのINDEX](benchmarks/custom/INDEX.md) |
| 過去の課題別検証記録 | [historical-results.csv](benchmarks/custom/historical-results.csv) |
| 公式データセットから選定した30課題 | [公式課題のINDEX](benchmarks/official-30/INDEX.md) |
| 公式課題の比較手順 | [比較手順](benchmarks/official-30/README.md) |

独自課題は **48セット・619課題エントリ**です。改訂・再実行・部分集合を含み、全件が独立した課題や実行済み・成功済みという意味ではありません。36課題のFamily Router検証、Gemma26向けの64課題・52課題などを含みます。初期コードと元のテストはZIPから課題ごとに取り出せます。過去の検証結果はFAIL・未完了・欠測も区別して収録しています。

公式課題は **MultiPL-E Rust 20件＋Multi-SWE-bench Rust 10件**の固定部分集合です。全体の公式ベンチマークを代替するものではなく、この配布物に公式課題の評価結果は含めていません。

今回のアップロードではモデル評価を再実行していません。独自課題の結果記録と、別製品で再評価するための空のCSVは別のファイルです。

`AGENTS.md` は元のNew-Concept-OSリポジトリ向けの原文です。そこで参照するWorker・設定・運用文書は元のプロジェクトを指します。配布物には課題の初期fixtureとテストを含みますが、Router全体や元の実行環境を構築するパッケージではありません。

ライセンスは [LICENSE](LICENSE)、第三者の公式課題については [出典とライセンス](benchmarks/official-30/THIRD_PARTY_NOTICES.md) を参照してください。公開ファイルのSHA-256は [PACKAGE_MANIFEST.json](PACKAGE_MANIFEST.json) に記録しています。
