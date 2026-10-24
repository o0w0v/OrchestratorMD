# 思考設定を使ったLocal Task委譲評価

集計: 2026-10-24T11:11:12.565406+00:00

総合順位ではなく、Taskごとに使えるprofileと費用を残す。旧結果と新結果は別run。Production Router/bounded 2.2.8の変更なし。

## 実測profile

|profile|完了/予定|過去失敗のPASS|成功対照PASS|出力上限|API平均秒|output tokens（思考込み）|
|---|---:|---:|---:|---:|---:|---:|
|gemma26_think|30/30|17/20|10/10|3|66.73|86089|
|qwen35_think|30/30|2/20|7/10|10|29.72|86059|
|gptoss_medium|30/30|13/20|9/10|0|44.84|44011|
|gptoss_low|6/6|0/6|0/0|0|12.65|2257|
|gptoss_high|6/6|2/6|0/0|4|145.62|28804|
|gemma26_fast|30/30|1/20|10/10|0|7.38|6393|
|qwen14_fast|30/30|2/20|8/10|0|11.29|4438|
|qwen35_9_fast|30/30|1/20|7/10|1|4.32|8610|
|devstral24_fast|30/30|5/20|8/10|0|36.79|4253|

fastは前回のthink=false/2048結果の参照。新profileはthink=trueまたはnative effort/6144。Task/messages/schema/testsは同一だが、出力予算・メーカー推奨sampling・telemetry負荷も異なるため、thinking単独の因果効果とはしない。Qwen14/Devstralは思考設定がなく既存結果を再利用した。

## 時間・メモリ

|profile|warm API平均秒|native eval平均秒|全profile wall秒|GPU peak MiB|GPU最小空きMiB|背景GPU MiB|Ollama RSS GiB|
|---|---:|---:|---:|---:|---:|---:|---:|
|gemma26_think|66.10|65.20|2141.64|9906.00|146.00|1317.00|19.75|
|qwen35_think|28.43|29.07|1017.62|7375.00|2677.00|657.00|6.88|
|gptoss_medium|41.91|43.76|1485.64|8914.00|1138.00|658.00|7.72|
|gptoss_low|9.82|10.63|109.59|8914.00|1138.00|657.00|6.34|
|gptoss_high|136.23|143.58|903.86|8914.00|1138.00|657.00|6.89|
|gemma26_fast|6.67|4.02|420.34|9888.00|164.00|2326.00|17.37|
|qwen14_fast|10.52|10.26|533.03|9624.00|428.00|1162.00|5.44|
|qwen35_9_fast|3.46|3.20|310.05|8166.00|1886.00|1114.00|4.63|
|devstral24_fast|34.98|35.22|1296.16|9755.00|297.00|1133.00|10.49|

GPUはHost全体の採取時の値。RAMはOllama/backend working setの合計で共有pageを重複し得る。真のpeak、モデル単体の消費、最低必要メモリは保証しない。新profileのsamplingはprocess名を先に絞って負荷を減らした。旧profileとのwall比較には測定負荷・背景・順序差が含まれる。native eval durationもJSONに保存した。

## 同一モデルのprofile差

- gemma26_think vs gemma26_fast: {'NATIVE_ONLY': 16, 'FAST_ONLY': 0, 'BOTH': 11, 'NEITHER': 3, 'UNPAIRED': 0}。新profileだけPASS: A500-COD-006, A500-COD-010, A500-COD-019, A500-COD-025, A500-COD-028, A500-COD-030, A500-COD-048, A500-COD-057, A500-COD-071, A500-COD-074, A500-COD-083, A500-COD-090, A500-WRK-036, A500-WRK-045, A500-WRK-066, A500-XLS-052。旧だけPASS: なし。
- qwen35_think vs qwen35_9_fast: {'NATIVE_ONLY': 3, 'FAST_ONLY': 2, 'BOTH': 6, 'NEITHER': 19, 'UNPAIRED': 0}。新profileだけPASS: A500-WRK-045, A500-XLS-052, A500-COD-031。旧だけPASS: A500-XLS-016, A500-COD-096。

## 思考ありGemma26を補えるTask

GemmaのOUTPUT_LIMITを補えた場合は、Gemmaの意味的な能力不足ではなく、このprofileの予算内完了を補ったものとして区別する。

|候補|候補だけPASS|そのうちGemmaが出力上限|GemmaだけPASS|両方PASS|両方不合格|比較未完了|
|---|---|---|---:|---:|---:|---:|
|qwen35_think|||18|9|3|0|
|gptoss_medium|A500-COD-008, A500-COD-009, A500-COD-060|A500-COD-008, A500-COD-009, A500-COD-060|8|19|0|0|
|gptoss_low|||5|0|1|24|
|gptoss_high|||3|2|1|24|
|gemma26_fast|||16|11|3|0|
|qwen14_fast|||17|10|3|0|
|qwen35_9_fast|||19|8|3|0|
|devstral24_fast|||14|13|3|0|

## gpt-oss effortの小規模比較

|Task|low|medium|high|
|---|---|---|---|
|A500-COD-006|BODY_CONTRACT_FAILURE / 26.84秒|COMPILE_FAILURE / 129.91秒|OUTPUT_LIMIT / 192.58秒|
|A500-COD-009|BODY_CONTRACT_FAILURE / 20.09秒|PASS / 66.53秒|OUTPUT_LIMIT / 184.47秒|
|A500-COD-028|BODY_CONTRACT_FAILURE / 7.47秒|PASS / 32.00秒|OUTPUT_LIMIT / 184.84秒|
|A500-COD-090|BODY_CONTRACT_FAILURE / 9.39秒|PASS / 72.03秒|OUTPUT_LIMIT / 184.48秒|
|A500-WRK-036|CONTENT_FAILURE / 6.86秒|PASS / 21.03秒|PASS / 54.89秒|
|A500-WRK-066|CONTENT_FAILURE / 5.27秒|CONTENT_FAILURE / 21.83秒|PASS / 72.45秒|

## Task別の割当証拠

各行は、このTaskで厳密なbody/slot契約と同じ固定checksを通過したprofile。API時間順はこの観測だけの値で、総合ランキングではない。全関数出力をHostで修理して主スコアに含めない。

|Task|内容|契約PASSしたprofile（秒）|
|---|---|---|
|A500-COD-006|設備予約の空き枠抽出|gemma26_think 85.06|
|A500-COD-008|会議出席の共通可能時間|gptoss_medium 159.16|
|A500-COD-009|複数営業日にまたがる対応期限|gptoss_medium 66.53|
|A500-COD-010|担当者交代を伴う当番空白検出|gemma26_think 119.88|
|A500-COD-019|期限優先での分割引当|gptoss_medium 59.86, gemma26_think 123.03|
|A500-COD-025|同梱不可商品の箱分割|gemma26_think 76.53|
|A500-COD-028|時間指定に合う配送便選択|gptoss_medium 32.00, gemma26_think 82.67|
|A500-COD-030|複数口配送の完了判定|gptoss_medium 17.55, devstral24_fast 42.19, gemma26_think 92.11|
|A500-COD-048|待機者の繰上げ対象選定|devstral24_fast 27.30, gemma26_think 50.25, gptoss_medium 54.69|
|A500-COD-057|交換済み部品の二重計上防止|gemma26_think 115.08|
|A500-COD-060|代替機切替後の稼働率|gptoss_medium 99.80|
|A500-COD-071|公開CSV列の順序変換|gemma26_think 122.77|
|A500-COD-074|必須項目の欠落一覧|gptoss_medium 50.44, gemma26_think 62.50|
|A500-COD-083|比率の表示用丸め|gemma26_think 127.74|
|A500-COD-090|重み付き稼働指標の集計|devstral24_fast 36.33, gptoss_medium 72.03, gemma26_think 104.33|
|A500-WRK-036|対応時間帯別の報告作成|gptoss_medium 21.03, gemma26_think 39.72, gptoss_high 54.89|
|A500-WRK-045|棚卸差異の集計と報告|gptoss_medium 19.64, gemma26_think 23.41, qwen35_think 32.33|
|A500-WRK-066|候補比較の重み付き集計|gemma26_think 19.92, gptoss_high 72.45|
|A500-XLS-016|割引併用順の計算|qwen35_9_fast 1.02, gemma26_fast 4.77, qwen14_fast 5.23, devstral24_fast 7.69, gptoss_medium 8.59, gemma26_think 55.76|
|A500-XLS-052|2台帳の未一致ID抽出|qwen14_fast 3.44, devstral24_fast 9.52, gptoss_medium 12.42, gemma26_think 13.28, qwen35_think 25.25|
|A500-COD-001|会議枠の重複判定|gemma26_fast 4.78, gptoss_medium 32.69, gemma26_think 78.25|
|A500-COD-031|問い合わせ優先度の分類|gemma26_fast 4.72, qwen14_fast 7.17, qwen35_think 9.39, devstral24_fast 15.28, gptoss_medium 22.09, gemma26_think 52.34|
|A500-COD-061|差戻し中申請の抽出|gemma26_fast 3.67, gptoss_medium 11.61, gemma26_think 49.41|
|A500-COD-091|締切ちょうどの受付誤判定修正|qwen35_9_fast 0.56, qwen14_fast 1.11, qwen35_think 2.01, devstral24_fast 2.31, gemma26_fast 2.69, gemma26_think 6.02|
|A500-COD-096|ロット残数のoverflow修正|qwen35_9_fast 0.80, qwen14_fast 1.80, gemma26_fast 2.94, devstral24_fast 9.05, gptoss_medium 14.39, gemma26_think 17.77|
|A500-PPT-041|指定テーマ色の適用|qwen35_9_fast 0.97, qwen14_fast 2.78, qwen35_think 6.00, gptoss_medium 6.11, gemma26_fast 6.88, devstral24_fast 7.59, gemma26_think 11.77|
|A500-DOC-011|見出しスタイルの適用|qwen35_9_fast 0.86, qwen14_fast 2.11, qwen35_think 4.44, gptoss_medium 4.55, gemma26_fast 4.97, devstral24_fast 5.64, gemma26_think 8.86|
|A500-XLS-001|名簿の姓と名を指定列へ分離|qwen35_9_fast 0.92, qwen14_fast 3.38, qwen35_think 4.33, gemma26_fast 4.34, gptoss_medium 8.52, devstral24_fast 10.61, gemma26_think 10.86|
|A500-XLS-011|数量と単価から小計追加|qwen35_9_fast 1.02, qwen14_fast 3.11, qwen35_think 4.70, gemma26_fast 6.17, gptoss_medium 9.17, devstral24_fast 10.25, gemma26_think 10.59|
|A500-WRK-001|週次件数表から報告1枚作成|qwen35_9_fast 1.19, qwen14_fast 3.92, gemma26_fast 5.01, qwen35_think 5.55, gptoss_medium 8.52, gemma26_think 12.36, devstral24_fast 12.91|

## 全関数出力の補助診断

主評価でBODY_CONTRACT_FAILUREになった生成済み文字列のみ対象。signatureが元interfaceと一致する場合に、コードを変更せず同じ固定テストを付けて隔離実行した。body契約のPASSや採用へ昇格しない。生成/semantic repairは追加していない。

|profile|診断した全関数文字列|意味テストPASS|
|---|---:|---:|
|gemma26_think|0|0|
|qwen35_think|6|4|
|gptoss_medium|5|5|
|gptoss_low|4|4|
|gptoss_high|0|0|

## 安全性・会計・限界

- 既知失敗20件＋成功対照10件を選んだ診断。一般的な正答率、得意分野の確定、新Taskへの汎化率ではない。
- thinkingは失敗としない。最終contentだけを固定validatorに渡し、思考はraw responseに保全。native eval_countに思考分を二重加算しない。
- strict出力契約違反、compile、意味テスト、Office slot内容、native生成/render、OUTPUT_LIMIT、infraを分離。
- OfficeはHost補助付きtyped slots。Office GUIの操作能力や見栄えを含む全業務品質の合格ではない。
- 一部公開promptに日本語文字化けがある。英語のExact contractと例を含む凍結messagesをそのまま使用。入力品質の制限は残る。
- 新規provider AI sessionは0。現在の準備Codex usage/creditsは取得しておらずnull。Local tokensからCodex削減を推定しない。
- Gemma12はquarantine、CoderNextは既存の資源admission不足を保全し未実行。
- memory/latencyの観測だけから各PCでの最低要件を断定しない。
- no-model preflightで正負のRust検査とOffice生成/renderを確認。generated Rustはnetwork=none等の既存隔離containerのみで実行。

## 今回のLocal消費

温度0の先行run-001も実消費へ含める。品質集計はrun-002と分離し、過去のfast profileを再実行した費用として二重計上しない。

{
  "new_native_main_calls": 102,
  "prior_temperature_zero_diagnostic_calls": 2,
  "total_new_calls_including_stopped_revision": 104,
  "input_tokens": 40158,
  "output_tokens_including_thinking": 259508,
  "prior_diagnostic_output_tokens": 12288,
  "historical_fast_profile_calls_reexecuted": 0,
  "quality_cohorts_not_merged": true
}

## 保存とGate

{
  "planned_102_completed": true,
  "all_native_profiles_terminal": true,
  "historical_inputs_unchanged": true,
  "frozen_harness_unchanged": true,
  "request_business_identity": true,
  "journal_started_matches_results": true,
  "one_shot_no_semantic_repair": true,
  "offline_tests_pass": true,
  "isolated_no_model_preflight_pass": true
}
