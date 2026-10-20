# 比較用30課題

[課題一覧](INDEX.md) から個別の入力を開けます。MultiPL-EのRust問題20件とMulti-SWE-benchのRust問題10件です。`official-30` はこの選定集合の名前であり、提供元による認定や全問題の実施を意味しません。

`prompts/` は製品に渡せるMarkdown、`tasks/` は同じ公開入力の構造化JSONです。問題文とMulti-SWEのbase commitは固定した課題定義に基づきます。Markdownには共通の実施指示を追加しています。`results-template.csv` は新たな比較試験用の記録表で、初期状態はすべて `NOT_RUN` です。入力データと分離して、[A/B workflow実測結果](results/2026-10-21-gemma26-router/README.md)を収録しています（29採点/30、判定INCONCLUSIVE）。

## 実施方法

1. 製品・モデル・バージョン・設定・試行上限・時間上限・ネットワーク条件を実行前に記録します。既定設定の比較と、同じAGENTSを与える比較は別の `configuration` にします。
2. 課題ごとに新しいセッションとcleanな作業領域を使い、該当する `prompts/<task_id>.md` と必要な公開base sourceを与えます。AGENTSなしの条件では、ルートのAGENTSが自動適用されない別の領域に課題ファイルだけをコピーします。片方だけに追加の設計や他製品の出力を与えないでください。
3. MultiPL-Eでは関数シグネチャを維持した完成関数を保存します。JSONの `prompt` は関数の閉じ括弧前までの原文prefix、`stop_tokens` は元データのメタデータです。Multi-SWEでは指定base commitから開始し、公開issueを解決したGit diffを保存します。
4. 実装担当には解答PR・後続履歴・gold patch・hidden tests・他製品のcandidateを渡さず、候補確定後に隔離したEvaluatorで同じ固定リビジョンの公式harnessを使って採点します。自己採点をofficial PASSとして記録しないでください。
5. `results-template.csv` を製品・設定・試行ごとにコピーし、PASS、失敗の種類、実測tokens、料金と通貨、経過時間、試行数、candidateと採点・usage証拠の場所を記録します。取得できない値は空欄のままにし、0へ変換しません。ローカルLLMのtokensは別列です。

結果はMultiPL-Eの20件とMulti-SWEの10件を分けて報告し、未実施・環境エラー・会計欠測の件数も示します。料金体系の違う製品のcreditsを直接加減せず、通貨換算する場合はレートと日時を記録してください。各製品の追加設計・review・repair・fallbackを含む範囲も同じ条件にそろえます。

## 公式採点の準備

[source-pins.json](source-pins.json) の固定したharnessとデータセットをEvaluator専用の領域へ取得し、対象30 ID、問題文、Multi-SWEのbase commitを照合します。セットアップと実行方法は各固定commitのREADMEを参照してください。

- [MultiPL-E harness](https://github.com/nuprl/MultiPL-E/tree/3025a531af7450e7df8b96fe0440e9804480bbad)
- [Multi-SWE-bench harness](https://github.com/multi-swe-bench/multi-swe-bench/tree/24f493f8a103e72312ded4f6b9c89f081d69cb09)

公式hidden test body、gold patch、Docker imageや対象リポジトリのソース全体は同梱していません。この公開物の整合性確認は元の固定入力との一致を確認したもので、公式データ全体のrevision照合・実行環境の準備完了・公式採点成功を証明するものではありません。元チャットのCodex＋ローカルLLM実行系を再現するパッケージではなく、共通の課題入力を配布するものです。
