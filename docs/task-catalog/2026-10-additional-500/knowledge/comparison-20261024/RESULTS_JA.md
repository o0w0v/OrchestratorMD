# Gemma26の既知失敗を補うLocalモデル比較

集計：2026-10-24T08:50:34.505737+00:00

同じ公開request・生成予算・旧固定採点器を使用。既知失敗20件と成功対照10件を選んだ診断であり、一般的な正答率ではない。旧500件は書き換えず、Gemmaも資源比較用に新runで再測定した。

## 補完結果

|モデル|完了|Gemma既知失敗の合格|成功対照|OUTPUT_LIMIT|infra/CUDA|
|---|---:|---:|---:|---:|---:|
|gemma4:26b|30/30|1/20実行|10/10実行|0|0/0|
|qwen2.5-Coder:14b|30/30|2/20実行|8/10実行|0|0/0|
|qwen3.5:9b|30/30|1/20実行|7/10実行|1|0/0|
|devstral-small-2:latest|30/30|5/20実行|8/10実行|0|0/0|
|gpt-oss:20b|2完了＋1中断|設定非互換|N/A|raw length 2|0/0|

### 当日Gemmaの失敗だけに対する補完

旧失敗20件のうちA500-XLS-016は当日Gemmaでも合格したため、それだけで候補の優位とは数えない。当日Gemmaの不合格は19件。

|候補|有効な比較件数|当日Gemma失敗の補完|
|---|---:|---:|
|qwen2.5-Coder:14b|19/19|1|
|qwen3.5:9b|19/19|0|
|devstral-small-2:latest|19/19|4|
|gpt-oss:20b|0/19|0|

未実行はNOT_RUN。protocol非互換、Host例外、infraは能力のFAILと分離。Office合格は旧typed slots＋native export/renderの固定基準で、GUI能力や実業務全体の合格ではない。

## 実行時間と資源

|モデル|初回API秒|warm平均秒/件|warm中央値秒/件|validation合計秒|GPU peak MiB|GPU最小空きMiB|Ollama RSS peak GiB|Host RAM最小空きGiB|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|gemma4:26b|27.78|6.67|4.98|45.27|9888|164|17.37|23.66|
|qwen2.5-Coder:14b|33.88|10.52|7.17|38.64|9624|428|5.44|35.23|
|qwen3.5:9b|29.33|3.46|1.97|38.23|8166|1886|4.63|36.87|
|devstral-small-2:latest|89.36|34.98|20.95|42.72|9755|297|10.49|31.46|
|gpt-oss:20b|設定非互換|N/A|N/A|N/A|N/A|N/A|N/A|N/A|

時間は同じTask群のAPI wall。初回はloadを含む。warmは固定順の初回Taskを除く。token数や正答率が違うため、時間だけのモデル総合順位にはしない。各armは1回で、background/order/cacheの影響が残る。

### 全30件のwallとメモリ観測

|モデル|API合計 秒|Host validation合計 秒|arm実wall 秒|RAM RSS観測 GiB|private memory観測 GiB|
|---|---:|---:|---:|---:|---:|
|gemma4:26b|221.31|45.27|420.34|17.37|26.29|
|qwen2.5-Coder:14b|338.81|38.64|533.03|5.44|13.63|
|qwen3.5:9b|129.74|38.23|310.05|4.63|12.32|
|devstral-small-2:latest|1103.84|42.72|1296.16|10.49|18.96|

arm実wallは30件の前後health check・sampling待ち・Host検証を含む。API時間と同じ意味ではない。

sampling間に2秒待機する設計だが、snapshot処理の時間も加わる。実際の間隔はモデル別JSONに保存し、約2秒で測れたとは主張しない。GPU peakはHost全体の採取時使用量で、モデル単体や真の最大値ではない。背景GPU、loaded idle、API reported VRAM、private memory、OSのprocess lifetime peak working setもJSONに保存。RSSのprocess合算は共有pageを重複し得る。最小必要RAM/VRAMの保証値は未測定null。

Gemmaの/api/ps reported VRAMは最大約1.18GiBだった一方、nvidia-smiのGPU全体使用量は約9.66GiBだった。定義や計上対象の差を含む原因は未特定。API値を実GPU使用量の代わりには使わず、両方を保全した。CUDA障害の証拠とは扱わない。

## GPU/CPU実行構成

|モデル|ログ中のGPU layer offload|実際の採取間隔中央値 秒|
|---|---|---:|
|gemma4:26b|31/31, 5/5|4.85|
|qwen2.5-Coder:14b|39/49|8.41|
|qwen3.5:9b|33/33|4.11|
|devstral-small-2:latest|19/41|9.83|
|gpt-oss:20b|25/25|7.89|

Gemmaログには複数のlayer記録があり、全てを残した。layer数が全てGPUでも、全重みの物理VRAM常駐やCPU不使用を意味するとは限らない。buffer量・/api/ps・実GPU使用量も併記する。

## 当日Gemmaとの組合せ

|候補|候補だけ合格|Gemmaだけ合格|両方合格|両方不合格|比較不能|
|---|---:|---:|---:|---:|---:|
|qwen14|1|2|9|18|0|
|qwen35_9|0|3|8|19|0|
|devstral24|4|2|9|15|0|
|gptoss20|0|0|0|0|30|

## 補完できたTask

### qwen2.5-Coder:14b

- A500-XLS-016：割引併用順の計算
- A500-XLS-052：2台帳の未一致ID抽出

### qwen3.5:9b

- A500-XLS-016：割引併用順の計算

### devstral-small-2:latest

- A500-COD-030：複数口配送の完了判定
- A500-COD-048：待機者の繰上げ対象選定
- A500-COD-090：重み付き稼働指標の集計
- A500-XLS-016：割引併用順の計算
- A500-XLS-052：2台帳の未一致ID抽出

### gpt-oss:20b

既知失敗の合格なし、またはprotocol非互換で未測定。

## 関数全体出力の補助診断

主評価でBODY_CONTRACT_FAILUREだった文字列だけを対象に、生成済みの関数全体を変更せず同じprivate testsと一緒に隔離compile/testした。初期body-only契約を満たしたことにはせず、主評価のFAILも採用判定も変更しない。追加generation・semantic repairは0。

|候補|signature一致で診断した文字列|同じテスト通過|
|---|---:|---:|
|qwen14|15|8|
|qwen35_9|17|4|
|devstral24|7|3|

一部の失敗は、意味が全て誤っているというより、関数本体だけを返す契約への不適合である。ただしこの診断を現行Workerへの採用率として数えない。正式に対応するなら別の出力契約検証が必要。

## gpt-ossの条件非互換と会計

think=falseのrequestに対して、完了した2応答ともthinkingが非空、2048 output tokensで最終contentなし。raw classifierはOUTPUT_LIMITを先に判定していたため、その結果は保全し、別overlayでPROTOCOL_INCOMPATIBLEを付記した。能力FAIL・CUDA/infra障害として集計しない。開始済みの3件目は意図的に中断し、native usageは取得不能null。2件分の取得済み4096 output tokensは保持するが、全消費は推定しない。追加retryやthinking設定変更はない。

## 保全・限界

- run-001：モデル保存先bindingを引き継げず、送信前STOP。生成0。
- run-002：事前検証の再利用照合で、default parameter表示の順序差を検出。実行開始前STOP、生成0。
- run-003：同じparameterの行集合とmodel digestを照合し、実比較。旧STOPは残す。
- CoderNext 80Bは現在の空きRAM/VRAMと4GiB reserveによる資源gateで除外。Gemma12はquarantine。
- 成功した候補を事後に選ぶ合算はRouter性能ではない。新しいTaskで確認してから採用判断する。
- 画像入力、OCR、Office GUIは今回評価していない。Officeは旧Host補助付きtyped slots方式。
- モデルへの自由なread/shell権限、cross-model fallback、semantic repair、production変更、追加downloadはない。
- Codex provider呼出し0。準備Codex usage/creditsはnull。Local tokenからCodex削減率を作らない。

## Task別

|Task|内容|旧Gemma|gemma26|qwen14|qwen35_9|devstral24|gptoss20|
|---|---|---|---|---|---|---|---|
|A500-COD-006|設備予約の空き枠抽出|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|COMPILE_FAILURE|PROTOCOL_INCOMPATIBLE|
|A500-COD-008|会議出席の共通可能時間|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|OUTPUT_LIMIT|SEMANTIC_FAILURE|PROTOCOL_INCOMPATIBLE|
|A500-COD-009|複数営業日にまたがる対応期限|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|INTENTIONAL_ABORT_PROTOCOL_MISMATCH|
|A500-COD-010|担当者交代を伴う当番空白検出|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|COMPILE_FAILURE|NOT_RUN|
|A500-COD-019|期限優先での分割引当|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-025|同梱不可商品の箱分割|FAIL|SEMANTIC_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-028|時間指定に合う配送便選択|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-030|複数口配送の完了判定|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|PASS|NOT_RUN|
|A500-COD-048|待機者の繰上げ対象選定|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|PASS|NOT_RUN|
|A500-COD-057|交換済み部品の二重計上防止|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|SEMANTIC_FAILURE|NOT_RUN|
|A500-COD-060|代替機切替後の稼働率|FAIL|SEMANTIC_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|COMPILE_FAILURE|NOT_RUN|
|A500-COD-071|公開CSV列の順序変換|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-074|必須項目の欠落一覧|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-083|比率の表示用丸め|FAIL|COMPILE_FAILURE|SEMANTIC_FAILURE|BODY_CONTRACT_FAILURE|SEMANTIC_FAILURE|NOT_RUN|
|A500-COD-090|重み付き稼働指標の集計|FAIL|COMPILE_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|PASS|NOT_RUN|
|A500-WRK-036|対応時間帯別の報告作成|FAIL|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|NOT_RUN|
|A500-WRK-045|棚卸差異の集計と報告|FAIL|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|NOT_RUN|
|A500-WRK-066|候補比較の重み付き集計|FAIL|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|CONTENT_FAILURE|NOT_RUN|
|A500-XLS-016|割引併用順の計算|FAIL|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-XLS-052|2台帳の未一致ID抽出|FAIL|CONTENT_FAILURE|PASS|CONTENT_FAILURE|PASS|NOT_RUN|
|A500-COD-001|会議枠の重複判定|PASS|PASS|SEMANTIC_FAILURE|BODY_CONTRACT_FAILURE|SEMANTIC_FAILURE|NOT_RUN|
|A500-COD-031|問い合わせ優先度の分類|PASS|PASS|PASS|BODY_CONTRACT_FAILURE|PASS|NOT_RUN|
|A500-COD-061|差戻し中申請の抽出|PASS|PASS|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|BODY_CONTRACT_FAILURE|NOT_RUN|
|A500-COD-091|締切ちょうどの受付誤判定修正|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-COD-096|ロット残数のoverflow修正|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-PPT-041|指定テーマ色の適用|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-DOC-011|見出しスタイルの適用|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-XLS-001|名簿の姓と名を指定列へ分離|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-XLS-011|数量と単価から小計追加|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
|A500-WRK-001|週次件数表から報告1枚作成|PASS|PASS|PASS|PASS|PASS|NOT_RUN|
