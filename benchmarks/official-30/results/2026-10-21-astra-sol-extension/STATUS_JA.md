# Astra / Sol追加比較の進捗（2026-10-21）

**判定：未完了。内部評価はCUDA INFRA_ERRORで停止。新規の外部Astra測定は未開始。**

## 既存の公式Sol A/B結果を再利用

凍結済みMultiPL-E Rust20件＋Multi-SWE-bench Rust10件は維持する。採点済み29ペアはSol-onlyとSol+Gemmaが同じ21課題を解決し、比較Creditsは358.35012から335.19033へ6.46%減、解決課題当たりCreditsは17.0643から15.9614へ減った。総tokens削減は0.60%。残る1課題は環境未測定であり、30課題全体の解決率は欠測のまま保持する。Final pipeline false greenはA3/B4、最終判定はINCONCLUSIVE。

これらの既存Sol結果は失敗も含めてhashで固定し、再生成・再課金しない。新規にAstra-onlyとAstra+Gemmaを追加する。既存Solの実装・plan・診断をAstraへ渡さず、同じ公開問題と初期sourceから独立に開始する。旧Solと新Astraの実行日・cache・順序・runtimeの違いは比較の制約として明示する。

## 内部46課題の今回実測

新しいChatGPT Credits transportでSol/Astraの実usage取得を確認後、凍結した4経路を実行した。4課題は全4armがvalidation＋独立reviewを通過し、次の課題のSol-onlyも通過した。その後、9回目のLocal呼出しでHTTP500と `CUDA error: an illegal memory access was encountered` が発生し、backendが消失した。

|Arm|品質PASS|未測定|
|---|---:|---:|
|Sol-only|5|41|
|Sol+Gemma|4|42|
|Astra-only|4|42|
|Astra+Gemma|4|42|

これは内部のHost validation/review結果であり、公式Benchmarkの解決率ではない。未完了のため、46課題全体の削減率・品質優劣は判定しない。閉じた呼出しのknown Codex費用は129.07257 Credits、transport確認は別途3.96430 Credits。Creditsは実usage×凍結rateによる計算で、アカウント残高の引落し照合ではない。失敗Local呼出しの未取得tokensはnull。

旧STOPとraw証跡は保全し、CUDAをモデル能力FAILへ混ぜない。自動restart・Local retryは行わない。新回復run用に17件の完了armと10件のPlannerをhash固定し、再課金を防ぐ。障害が出たLocal呼出し自体は再試行しない。

## 外部追加測定の準備

既存29ペア再利用・30Task分母維持・欠測分離の12件offlineテスト、Astra専用model-only egressの20件offlineテスト、内部回復の8件offlineテストはPASS。これらはVM実効隔離や本評価実測のPASSを代替しない。

外部VM/checkpoint/network bindingはread-onlyで一致を確認したが、固定proxyは停止中で、旧Guest認証leaseは失効済み。新Guest認証・通信境界再確認とLocalの安全なfresh開始が必要。Production Router、bounded2.2.8、公式Task/tests/scoring、過去の結果は変更していない。

モデルの一般ランキング、公式30課題完走、Production成功はいずれも主張しない。認証、gold、private tests、cache、raw会話、個人の絶対pathは本公開に含めない。
