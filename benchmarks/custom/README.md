# 課題と検証結果のデータセット

ローカル言語モデルへの実装委譲、モデルの役割分担、検証手順、連続稼働を調べるための課題と実験記録です。**同じ課題の定義・初期コード・テスト・条件別結果を対応付けて閲覧できます。**

## 閲覧する

1. [セット一覧](INDEX.md) で検証内容を選びます。
2. 各セットの「課題・結果」ページで課題IDを選びます。
3. 課題文と受入条件、条件別の結果、根拠となる記録を確認します。

| ファイル | 用途 |
| --- | --- |
| [INDEX.md](INDEX.md) | 48セットの課題・結果への入口 |
| [catalog.json](catalog.json) | 課題ごとの一意のキーと結果IDの対応 |
| [historical-results.csv](historical-results.csv) | 全結果の対応表。entry_keyで課題を、result_idで根拠を特定 |
| [result-coverage.json](result-coverage.json) | 全619エントリの収録状況。未確認の項目も列挙 |
| [synthetic-task-bundle.zip](synthetic-task-bundle.zip) | 課題・初期コード・テスト・対応する過去結果・取り出しツール |
| [results-template.csv](results-template.csv) | 別製品で再評価するための空の記録表 |
| [CORRESPONDENCE_AUDIT.md](CORRESPONDENCE_AUDIT.md) | 対応付けの方法、照合範囲、未確認事項 |

619エントリには改訂・再実行・部分集合を含みます。独立した619問題や、619件の実行・成功を意味しません。607エントリに課題別の結果または実行状態の記録が対応し、12エントリは個別結果未確認です。条件や工程ごとの複数記録は独立した課題として数えません。

## 判定の読み方

| 表記・項目 | 意味 |
| --- | --- |
| Local実装のPASS | その実装が固定のチェックを通過。最終採用とは別の判定 |
| レビューのACCEPT_NO_CHANGE | 変更なしでの採用をレビュー担当が認めたという記録 |
| MANDATORY_PASS_AND_ACCEPT_NO_CHANGE | 必須検証とレビューの両方を通過した最終品質の記録 |
| ESCALATE | ローカル処理から上位の処理へ引き継ぎ。工程全体の失敗とは限らない |
| NOT_RUN | 未実行であると明記された記録 |
| CODEX_ONLY | ローカルモデルへの委譲対象外とされた条件 |
| TASK_DESIGN_FAILURE | 課題やテストの設計上の問題。モデル能力の失敗と区別 |
| 個別結果未確認 / UNCONFIRMED | 対応する課題別記録を確認できない。未実行・失敗・成功と推定しない |
| — | その記録に値がない項目。0やfalseへの置換はしない |

モデル、run、修正上限、役割分担が異なる実験を収録しています。同じtask_idが別のセットで使われていても結果を共有しません。全セットをまとめた成功率や削減率として集計せず、比較対象の条件をそろえてください。

## 課題を取り出して再評価する

ZIPを展開したフォルダーで実行します。Python 3.11以降の標準ライブラリを使用します。

```sh
python verify_bundle.py
python materialize_task.py --list
python materialize_task.py --set family-gated-local-router-228 --task FGR228-001 --output work/FGR228-001
```

`PROMPT.md` と `task.json` が課題、`workspace/` が初期コードと保護されたテストです。`historical-results.json` に、その課題に対応する過去の結果が同時に取り出されます。これを再評価の結果として上書きせず、別のrun_idで記録してください。

`evaluator/evaluation.json` は検証担当用です。Rustの検証では、評価ファイルのCargoコマンドを対象のworkspaceで使用します。環境依存のWSL・toolchainパス・timeoutラッパーを外し、Cargo引数は保持しています。Python/HTMLの初期モデル比較には、同梱の `evaluators/model_routing.py` を使用できます。評価ファイルのmodel_routing_taskをJSONへ保存し、そのJSONとcandidate workspaceを引数に渡します。構造化回答はcandidate側のanswer.jsonを読みます。正解値やmutation用情報を含む評価ファイルは実装担当へ渡さないでください。

取り出しツールと整合性検査はモデルやcandidateコードを実行しません。元のHost guard・Router・mutation runnerを完全に再現する実行系は同梱していません。テスト設計の不備を調べる対照課題も含むため、実験ごとの受入条件とレポートを確認してください。

過去結果は保存された記録から抽出したものです。ローカルファイルパスは除去し、出典の位置とSHA-256を保持しています。認証情報、会話全文、モデル応答全文は含みません。データ整備に伴うモデル評価の再実行は行っていません。
