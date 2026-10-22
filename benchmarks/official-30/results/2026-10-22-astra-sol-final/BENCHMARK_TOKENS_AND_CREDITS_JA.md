# 公式Benchmark — Tokens / Credits会計

最重要KPIは公式workflow resolved rate、Codex Credits削減率、Credits/解決課題。FOUR_ARM_RESULTS.jsonに全30分母と測定subsetを分離して保存した。

新Astra ACTUAL_STUDY_SPEND既知小計: 1983.67855 Credits。厳密総額: None。未知残余invocation数: 1。

歴史的Sol実支出: 636.06445 Credits。今回のSol再実行・再課金は0。

Shared PlannerはACTUAL_STUDY_SPENDで1回、COMPARISON_WORKFLOW_COSTでは各armへ全額。比較費用の合計を実支出と呼ばない。

uncached_input_tokens = input_tokens - cached_input_tokens。cachedはinputの内数。reasoning outputがoutputの内数であるnative usageから二重加算しない。失敗・retry・capacityも保存し、欠測はnull。1 invocationの複数失敗eventを複数請求へ変換しない。

Credit単価は測定開始時にfreezeした公式Standard rateを使用。https://learn.chatgpt.com/docs/pricing.md 、取得2026-10-20T22:03:17.753839Z、raw SHA256 e3e0a5ac79441fac79cf1e50d31c0bdbd8d27e0f30452a8307f87ab64495bdf3。1M tokensあたりSol input/cached/output=50/5/250、Astra=250/25/1250。これはnative usageによる単価換算であり、実アカウント請求残高の観測ではない。

CLI usageはCODEX_SESSION_USAGE.csv、Ollama native usageはLOCAL_MODEL_USAGE.csv。旧Solの検証済みSTRUCTURAL_ZERO_PROVENは元rawのnullを変更せず別派生証拠に基づく。Astraの実native欠測を同じ0扱いにはしない。

BENCHMARK_VALIDATIONの新規AI callは構造的0。準備のroot Codex usageは未測定null。Local電力費・JPY換算・プロジェクト全体NET savingsはnull。Local tokensをCodex tokens savedに置換しない。

Raw request/response/turn.completedは各immutable invocationに残し、公開CSVには認証・private path・gold/test・実装回答を含めない。

追加の範囲明確化: validation 0はpure-script child AIの構造的0。Rootの準備・結果検討はnull。role-registry161以外のTLS失敗1件はFAILED_CALL_ACCOUNTING_SUPPLEMENT.jsonに保持し、native usageを0へ書き換えていない。
