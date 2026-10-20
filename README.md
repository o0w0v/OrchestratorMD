# OrchestratorMD

「Create repository AGENTS.md」チャットで作成・更新した開発ルールと、他のコーディング製品との比較に使う30課題を収録しています。2026年10月20日に元ファイルから取り出した公開用スナップショットです。

| 内容 | 場所 |
| --- | --- |
| 元リポジトリの最新の開発ルール（原文） | [AGENTS.md](AGENTS.md) |
| 元の作業ルートのルール（原文） | [originals/workspace/AGENTS.md](originals/workspace/AGENTS.md) |
| Worker・モデル選択・プロトコルの説明 | [docs/LOCAL_WORKER.md](docs/LOCAL_WORKER.md) / [docs/MODEL_ROUTER.md](docs/MODEL_ROUTER.md) / [docs/PROTOCOL_ROUTER.md](docs/PROTOCOL_ROUTER.md) |
| 比較用30課題の一覧 | [benchmarks/official-30/INDEX.md](benchmarks/official-30/INDEX.md) |
| 比較の実施方法・採点の準備 | [benchmarks/official-30/README.md](benchmarks/official-30/README.md) |
| 結果記録用CSV（未実行） | [benchmarks/official-30/results-template.csv](benchmarks/official-30/results-template.csv) |
| コピー元とSHA-256 | [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) |

収録課題は、元のチャットで選定した **MultiPL-E Rust 20件とMulti-SWE-bench Rust 10件**です。公式データセットから選んだ固定の部分集合であり、公式ベンチマーク全体の代わりにはなりません。課題ごとのMarkdownとJSONを用意しています。

この公開物には問題入力・ルール・採点方針を収録しています。公式の非公開採点用入力や解答パッチ、実行済み性能比較の結果は含みません。公式採点には、固定したリビジョンのデータと公式harnessを別のEvaluator環境に用意する必要があります。

`AGENTS.md` と `docs/` は New-Concept-OS 向けの原文です。記載されたRust workspace、Workerスクリプト、設定、過去実験、ローカルパスは元の環境を指しています。このリポジトリだけでCodex＋ローカルLLMの実行系が構築されるものではありません。上位の原文と最新の原文には運用の世代差があるため、最新のモデル運用はルートの `AGENTS.md` と `docs/MODEL_ROUTER.md` を参照してください。

コピーした原文のライセンスは [LICENSE](LICENSE)、課題データ・harness・対象リポジトリの出典とライセンスは [THIRD_PARTY_NOTICES.md](benchmarks/official-30/THIRD_PARTY_NOTICES.md) を参照してください。

収録ファイルの整合性確認:

```sh
python scripts/verify_package.py
```
