> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/local-specialist-economics.md). This report alone does not establish a task result.

# Local Specialist Economic Router Benchmark

集計UTC: 2026-10-05T01:15:01.373059+00:00

判定: **INCONCLUSIVE**

Coverage: gemma26 economic pairs 1/14, qwen14 economic pairs 14/14。未実行を失敗や0-cost成功として補完していない。

## 1. Web research

公式card、Ollama packageと一次community報告を取得。詳細と引用は 研究ノート（元資料: research/RESEARCH_JA.md）、公開tagとinstalled digestの区別（元資料: research/REGISTRY_NOTE_JA.md）。raw HTMLと取得日時/SHA256を同じdirectoryに保存。公開coding/tool benchmarkをこのPCのRust first-pass率へ換算していない。

## 2. Candidate Local models

実測対象は既存Gemma26とQwen2.5-Coder14B。新規第一候補Qwen3.5 9B=6.6GB/Q4_K_M/Apache-2.0、次点DeepSeek-Coder-V2 Lite=8.9GB/Q4_0/DeepSeek weight license。10GB環境のheadroomはweight量からの定性的推論であり、未導入候補の実VRAMはnull。download/install/updateは実施していない。

## 3. Task/category freeze

FREEZE.json（元資料: FREEZE.json）で14新規Task、カテゴリ、split、source、acceptance、runtime、料金をモデル実行前に固定。既存P224/CVB/OSL/RSP/ARE Taskは再利用していない。REASONINGは今回、算術/選択を要するcoding Taskであり、no-edit protocolではない。

|Task|split|category|business goal|
|---|---|---|---|
|LSE-001|development|STRICT_OUTPUT|Escape event identity for pipe-delimited audit export|
|LSE-002|development|COMPILE_SENSITIVE|List recorded blocked proposal targets|
|LSE-003|development|SEMANTIC_EDIT|Summarize sample warnings with stable empty/nonempty groups|
|LSE-004|development|STATEFUL|Replace repeated event keys in their first-seen display positions|
|LSE-005|development|DEBUGGING|Remove overflow in rounded-up audit elapsed seconds|
|LSE-006|development|REASONING|Compute affordable future recorded calls from two independent limits|
|LSE-007|development|SMALL_REFACTOR|Consolidate risk rendering through the existing helper|
|LSE-008|held_out|STRICT_OUTPUT|Serialize a process sample as an exact line manifest|
|LSE-009|held_out|COMPILE_SENSITIVE|Collect dry-run proposals lacking successful verification|
|LSE-010|held_out|SEMANTIC_EDIT|Separate sampled process IDs with self-parent anomalies|
|LSE-011|held_out|STATEFUL|Preview cooldown admissions without refreshing rejected timestamps|
|LSE-012|held_out|DEBUGGING|Preserve signed TCP sample decreases and unknown samples|
|LSE-013|held_out|REASONING|Select an ordered evidence prefix under a byte allowance|
|LSE-014|held_out|SMALL_REFACTOR|Centralize paired action display labels|


## 4. Codex-only baseline

完成 14/14、初回実装成功 13/14。各Taskで別のPlanner / Executor / Reviewer session、全てgpt-6-sol / xhigh / Standard。全mandatory checksとACCEPT_NO_CHANGEが完成条件。詳細はcodex/baseline。

## 5. Local First PASS

|model|infra除外 gate terminal|First PASS|rate|economic pairs|
|---|---|---|---|---|
|gemma26|1|0|0.00%|1|
|qwen14|14|2|14.29%|14|


ここでのFirst PASS率は凍結protocolを含むworkflow gateの通過率。Host停止や出力契約違反を含むため、model単体のcoding capability率とは呼ばない。native failure_domainとfirst_pass=nullも元artifactに保持する。

|model|split|First PASS / gate terminal|economic pairs|remaining|
|---|---|---|---|---|
|gemma26|development|0/1|1|LSE-002,LSE-003,LSE-004,LSE-005,LSE-006,LSE-007|
|gemma26|held_out|0/0|0|LSE-008,LSE-009,LSE-010,LSE-011,LSE-012,LSE-013,LSE-014|
|qwen14|development|2/7|7|none|
|qwen14|held_out|0/7|7|none|


## 6. Failure taxonomy

gemma26: {"HOST_FORMAT_ERROR": 1}; missing pairs=['LSE-002', 'LSE-003', 'LSE-004', 'LSE-005', 'LSE-006', 'LSE-007', 'LSE-008', 'LSE-009', 'LSE-010', 'LSE-011', 'LSE-012', 'LSE-013', 'LSE-014']

qwen14: {"TARGETED_CHECKS_PASSED": 2, "GENERATION_CONTRACT_FAILURE": 7, "CODE_FAILURE": 3, "LINT_REPAIR_NOT_ELIGIBLE": 2}; missing pairs=[]

保存されたcohort STOP: gemma26/development STOP（元資料: local/gemma26/development/STOP.json）。凍結designに従い停止modelの残りとheld-outは再実行していない。

Gemma LSE-001はmodel apply後、Rust char literal内に未escapeの実CR/LFがあり、rustfmt preflightが失敗した。bounded 2.2.6はこのdiagnosticを既知のcandidate failureへ束縛できず、**HOST_FORMAT_ERROR / host / stop_cohort=true**を返した。初回semantic validationはNOT_RUN。元resultのfirst_pass=nullを保持し、economic gate上のみFIRST_FAILへ分類する。CUDAやモデル能力評価のFAILへの再分類ではない。protocol/classifierを修正せず、そのcohortを停止した。詳細はSTOP解釈（元資料: local/gemma26/development/STOP_ADJUDICATION.json）。

別件として、Qwen failure後の**Codex direct** LSE-006は2回目にmethod argument末尾commaのrustfmt追加をguardが拒否した。既存分類はFORMAT_UNSUPPORTED_NORMALIZATION / formatter_unsupported / stop_cohort=false。正規化未採用・candidate/scope/freeze/staging/pinned formatterの保全を確認し、元の4 code episode上限内で同じprompt・実診断・全checksを使う続行driverを追加した。凍結harness/guardやLocal repair条件は変更せず、全失敗costを含める。続行証跡（元資料: codex/qwen14-development/LSE-006/RESUME_ADJUDICATION.json）。当該失敗検証の完全なwallは未取得のため、このTaskのtotal wall比較はnullとする。

repairはsyntax/semantic/lintすべて0。read-only DISCOVERYは別カウント。CUDA/infraはcoding分母へ混ぜず、STOP・未実行・coverageを残す。Local FAIL時はclean initialから新sessionのCodex実装。失敗candidateを与えず、成功したbaseline解を流用しない。

## 7. Model × category

|category|Gemma First PASS|Qwen First PASS|Gemma saved|Qwen saved|highest PASS|highest saved|
|---|---|---|---|---|---|---|
|COMPILE_SENSITIVE|0/0|0/2|N/A|0.362|qwen14|qwen14|
|DEBUGGING|0/0|0/2|N/A|0.154|qwen14|qwen14|
|REASONING|0/0|0/2|N/A|-3.272|qwen14|qwen14|
|SEMANTIC_EDIT|0/0|1/2|N/A|1.422|qwen14|qwen14|
|SMALL_REFACTOR|0/0|0/2|N/A|0.836|qwen14|qwen14|
|STATEFUL|0/0|0/2|N/A|-2.205|qwen14|qwen14|
|STRICT_OUTPUT|0/1|1/2|1.203|2.549|qwen14|qwen14|


この全screen比較の最大値は事後の記述統計であり、Router選択には使わない。

## 8. Codex raw usage

```json
{
  "usage": {
    "input_tokens": 5331250,
    "cached_input_tokens": 4420864,
    "uncached_input_tokens": 910386,
    "output_tokens": 81936,
    "total_tokens": 5413186
  },
  "credits": 88.10762,
  "USD_equivalent": 3.5243048000000003,
  "session_wall_seconds": 3181.2039999999615,
  "sessions": 74
}
```

|role|sessions|input|cached|output|credits|
|---|---|---|---|---|---|
|planner|14|665677|546688|12192|11.731|
|implementation|31|3719169|3243008|60489|55.145|
|review|29|946404|631168|9255|21.231|


各phaseのEND.jsonにraw turn.completed usageを保存。cachedをinputから差し引いてuncachedを算出。session-audit.jsonで独立session、実model/effort、最大request inputを検証。欠測を推定しない。

## 9. Codex credits

公式pricing（元資料: http[LOCAL_PATH]）から凍結したStandard rateは uncached=50 / cached=5 / output=250 credits / 1M tokens。式は (input-cached)*50/1M + cached*5/1M + output*250/1M。HTML/Markdown・URL・時刻・SHAはrates/。shared Plannerは両workflowへ同じ実測costを1回ずつ加算し、実支出合計はunique sessionを一度だけ数える。

## 10. Credits saved by Local model

|model|baseline matched|routed matched|saved|reduction|saved/Task|First-PASS saved|failed-gate delta|
|---|---|---|---|---|---|---|---|
|gemma26|4.430|3.227|1.203|27.16%|N/A|0.000|-1.203|
|qwen14|48.846|49.000|-0.154|-0.31%|-0.011|4.042|4.196|


FAILED_LOCAL_GATE_CODEX_CREDIT_DELTAはrouted-baseline、正が追加消費。complete=falseのmodelでは未実行を0 costにせず、EXPECTED指標はnull。独立Codex sessionのcache/実装探索差をLocal能力の利益と断定しない。

|model|group|pairs|baseline|routed|saved|reduction|
|---|---|---|---|---|---|---|
|gemma26|LOCAL_FIRST_PASS|0|N/A|N/A|N/A|N/A|
|gemma26|LOCAL_FIRST_FAIL|1|4.430|3.227|1.203|27.16%|
|qwen14|LOCAL_FIRST_PASS|2|7.464|3.422|4.042|54.16%|
|qwen14|LOCAL_FIRST_FAIL|12|41.382|45.578|-4.196|-10.14%|


未完成/品質未達でpaired savings対象外となった経路の既測定credits（shared planner込み）は gemma26=0.000, qwen14=0.000。除外した費用を消去せず、unique session総額とTask表に保持する。

Task別matched比較（credits、正のsavedは削減）。未実行/未完成はN/A。FALSE_GREENやreview findingはeconomic winから除外する。

|model|Task|split|Local gate|review|baseline|routed|saved|
|---|---|---|---|---|---|---|---|
|gemma26|LSE-001|development|HOST_FORMAT_ERROR|ACCEPT_NO_CHANGE|4.430|3.227|1.203|
|qwen14|LSE-001|development|TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|4.430|1.748|2.682|
|gemma26|LSE-002|development|NOT_RUN|NOT_RUN|4.100|N/A|N/A|
|qwen14|LSE-002|development|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|4.100|2.945|1.155|
|gemma26|LSE-003|development|NOT_RUN|NOT_RUN|3.034|N/A|N/A|
|qwen14|LSE-003|development|TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|3.034|1.674|1.360|
|gemma26|LSE-004|development|NOT_RUN|NOT_RUN|2.331|N/A|N/A|
|qwen14|LSE-004|development|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|2.331|2.674|-0.344|
|gemma26|LSE-005|development|NOT_RUN|NOT_RUN|3.000|N/A|N/A|
|qwen14|LSE-005|development|CODE_FAILURE|ACCEPT_NO_CHANGE|3.000|2.398|0.601|
|gemma26|LSE-006|development|NOT_RUN|NOT_RUN|5.630|N/A|N/A|
|qwen14|LSE-006|development|CODE_FAILURE|ACCEPT_NO_CHANGE|5.630|9.983|-4.352|
|gemma26|LSE-007|development|NOT_RUN|NOT_RUN|3.157|N/A|N/A|
|qwen14|LSE-007|development|LINT_REPAIR_NOT_ELIGIBLE|ACCEPT_NO_CHANGE|3.157|2.564|0.593|
|gemma26|LSE-008|held_out|NOT_RUN|NOT_RUN|3.352|N/A|N/A|
|qwen14|LSE-008|held_out|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|3.352|3.485|-0.133|
|gemma26|LSE-009|held_out|NOT_RUN|NOT_RUN|3.668|N/A|N/A|
|qwen14|LSE-009|held_out|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|3.668|4.460|-0.793|
|gemma26|LSE-010|held_out|NOT_RUN|NOT_RUN|2.766|N/A|N/A|
|qwen14|LSE-010|held_out|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|2.766|2.705|0.061|
|gemma26|LSE-011|held_out|NOT_RUN|NOT_RUN|2.339|N/A|N/A|
|qwen14|LSE-011|held_out|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|2.339|4.201|-1.862|
|gemma26|LSE-012|held_out|NOT_RUN|NOT_RUN|3.298|N/A|N/A|
|qwen14|LSE-012|held_out|GENERATION_CONTRACT_FAILURE|ACCEPT_NO_CHANGE|3.298|3.745|-0.447|
|gemma26|LSE-013|held_out|NOT_RUN|NOT_RUN|3.790|N/A|N/A|
|qwen14|LSE-013|held_out|CODE_FAILURE|ACCEPT_NO_CHANGE|3.790|2.710|1.081|
|gemma26|LSE-014|held_out|NOT_RUN|NOT_RUN|3.950|N/A|N/A|
|qwen14|LSE-014|held_out|LINT_REPAIR_NOT_ELIGIBLE|ACCEPT_NO_CHANGE|3.950|3.707|0.243|


経済順位は全14件の同条件pairが揃ったmodelだけが対象。部分cohortを少ない分母の平均で上位に置かない。First PASSで消せたimplementationの価値と、First FAIL後の別Codex sessionの偶然の差を分離する。

|rank (complete only)|model|expected saved/Task|saved/First PASS|coverage|
|---|---|---|---|---|
|1|qwen14|-0.011|2.021|14/14|


## 11. USD equivalent saved

公式GPT-6 Sol API rate（元資料: http[LOCAL_PATH]）: $2/$0.2/$10 per 1M uncached/cached/output tokens。実請求額ではない。

|model|USD equivalent saved|
|---|---|
|gemma26|0.04813|
|qwen14|-0.00615|


## 12. JPY status

JPY_PER_CREDIT=null、JPY_SAVED=null。購入単価を確認できていない。為替やcredit残高から実円料金を逆算しない。

## 13. GPU/VRAM/CUDA

|model|sample数|無効sample|peak used MiB|minimum free MiB|CUDA|infra|Host STOP|FALSE_GREEN|
|---|---|---|---|---|---|---|---|---|
|gemma26|31|0|9996.000|56.000|0|0|1|0|
|qwen14|430|0|9926.000|126.000|0|0|0|0|


各cohortのfresh-exit/environment、各Task before/during/after、backend/frontend PID、frontend age、server log、Windows eventsを保存。物理容量外の値はraw保持、派生統計null。Gemma12/CoderNextやgeneration probeは使用しない。

## 14. Wall overhead

|model|Worker秒合計|Ollama API秒|Local input/output tokens|平均routed-baseline wall秒|wall比較可能pairs|
|---|---|---|---|---|---|
|gemma26|32.719|25.066|998/169|19.423|1|
|qwen14|454.139|108.867|18578/1182|10.225|13|


Ollama durationはload/CPU offloadを含む実API計測時間。GPU kernelの実行秒は取得していないためnull。Worker wallをGPU kernel時間と同一視せず、Local tokenをCodex creditsへ換算しない。

active作業時間ではなくwall interval。Planner+モデル/Executor/review session+Host validationを合成し、Local Worker wallにはその内部validationを含めて二重計上しない。fresh start待ち、ユーザーQuit待ち、coordinator待機はTask latencyに含めず別の運用負担。baselineの一部は2 process並行のためwallにCPU/service contentionが混ざる。速度の因果比較ではない。

## 15. Development routing

DEV_ROUTING_FROZEN.jsonがselectionの唯一の根拠。developmentでFirst PASS/accepted/positive credit savings/infra安全を満たす候補だけ選ぶ。選択後にheld-outでモデルを差し替えない。

## 16. Held-out validation

|category|dev selected|held-out Task|saved credits|supported|
|---|---|---|---|---|
|STRICT_OUTPUT|qwen14|LSE-008|-0.133|False|
|COMPILE_SENSITIVE|None|None|N/A|False|
|SEMANTIC_EDIT|qwen14|LSE-010|0.061|False|
|STATEFUL|None|None|N/A|False|
|DEBUGGING|None|None|N/A|False|
|REASONING|None|None|N/A|False|
|SMALL_REFACTOR|None|None|N/A|False|


## 17. Recommended Router

|category|proposal only|
|---|---|
|STRICT_OUTPUT|gpt-6-sol-direct|
|COMPILE_SENSITIVE|gpt-6-sol-direct|
|SEMANTIC_EDIT|gpt-6-sol-direct|
|STATEFUL|gpt-6-sol-direct|
|DEBUGGING|gpt-6-sol-direct|
|REASONING|gpt-6-sol-direct|
|SMALL_REFACTOR|gpt-6-sol-direct|


候補Localはone-shot -> PASSなら6 Sol review、FAILならclean sourceから6 Sol direct。production Routerは変更していない。

## 18. Limitations

各categoryはdevelopment/held-out各1件。多様なproduction workloadの平均効果・一般故障率へ外挿しない。追加モデルは未導入/未測定。共通Task設計・acceptance/scaffold・experiment harness・調査とcoordinatorのCodex costは未計測=nullで、ここでのcreditsは測定したworkflow役割の比較に限る。Host準備を含む全アカウントnet savingsとは呼ばない。Standardは指定config/runtime evidenceでありinvoice tierは未取得。私有copyとtool auditは完全なOS read sandboxの証明ではない。

実行順はbaselineを先に固定した後Local経路で、無作為な交差実験ではない。独立sessionでもproviderのprefix cache状態は統制できず、実測cached token比率やCodexの探索・retry回数に差がある。特にFirst FAIL群のcredits差をLocal gateの因果効果と解釈しない。First PASSでも省略したimplementationとreview費用の変動を区別する。

Repository検証はWorker suite 233 tests、experiment guard/accounting tests 7件、Rust fmt/clippy/test/check/buildを実施し全PASS。保存先はpreparation/worker-suite.json、harness-tests.json、repository-checks/。Worker suite内の模擬CUDA errorはoffline negative fixtureであり、live infrastructure件数へ加算していない。CLI session監査とraw usage再計算の結果はsummaries/final-001/。

## 19. Decision

**INCONCLUSIVE**。完了状況とカテゴリ単位のheld-out証拠に限定した判断。小標本の最大値をproductionのoracleにしない。旧artifact/STOP/result、Routerとbounded2.2.6は保全。


## 最終解釈と凍結routingの評価

判定: **INCONCLUSIVE**。Qwen14の14件を完了したが、事前選択カテゴリでのFirst PASSはheld-outに再現せず、Gemma26は既存Host STOPにより比較未完了。

|指標|結果|
|---|---|
|Codex-only baseline|14/14 全checks・独立review PASS|
|Qwen14 Local First PASS|development 2/7、held-out 0/7、合計2/14|
|Qwen14 workflow最終品質|14/14 全checks・独立review PASS（失敗12件はclean Codex実装）|
|Qwen14 matched credits|baseline 48.84606 → Local routed 48.99985|
|Credits saved|−0.15379（0.31%増）|
|First PASS群のcredits削減|4.04237|
|First FAIL群のcredits増分|4.19616|
|CUDA / INFRA / FALSE_GREEN|0 / 0 / 0|
|Gemma26|LSE-001 HOST_FORMAT_ERRORでSTOP、1/14のみ観測。残りを再実行せず保持|
|独立Codex session監査|74件、全gpt-6-sol / xhigh / Standard指定、usage/料金照合PASS、blinding flags 0|

事前選択はSTRICT_OUTPUT/SEMANTIC_EDIT → Qwen14、その他 → GPT-6 Sol directだった。held-outの選択2件はどちらもLocal First FAIL。凍結ルールを測定済み部品から合成すると、held-out 7件で23.16357 → 23.23551 credits（0.07194増、0.31%増）。これは別のend-to-end pipelineを新規実行した値ではなく、選択2件の実測Local workflowと残る5件の実測baselineの合成。事後に有利なmodel/Taskを選んでいない。

**今回の条件でproduction候補へ昇格できるLocal categoryはない。** 全categoryをGPT-6 Sol direct候補として報告するだけで、production Router/configは変更していない。小差のcredits増減はcache/独立Codex探索/実行順の影響を統制しておらず、一般的な優劣へ外挿しない。Gemma26の未完了を能力FAILや0-cost成功へ変換しない。

held-outのLocal失敗は最終LF不足によるGENERATION_CONTRACT_FAILURE 5件、CODE_FAILURE 1件、lint failure 1件。前者はapply前拒否でsemantic validationは未実行。モデルの一般的coding能力スコアではなく、固定bounded 2.2.6とのworkflow適合を測っている。Local repair、prompt/formatter/reference/context/model policyの変更は0。

共通Task/scaffold/acceptance作成やcoordinatorのCodex費用は未計測で、全アカウントのnet savingsは算出しない。USDはAPI料金相当、実請求額ではない。JPY購入単価は未取得=null。追加候補Qwen3.5 9B等は調査のみで、download/installは実行していない。

- 19項目の詳細報告（元資料: RESULTS_LOCAL_SPECIALIST_ECONOMICS_FINAL_JA.md）
- 料金・Task別・group別のraw集計（元資料: summaries/final-001/economics.json）
- 凍結routingのheld-out合成（元資料: summaries/final-001/frozen-routing-held-out.json）
- session監査（元資料: summaries/final-001/session-audit.json） / raw usageからの料金再計算（元資料: summaries/final-001/accounting-verification.json）
- 最終状態（元資料: STATUS_FINAL.json） / Gemmaの元STOP（元資料: local/gemma26/development/STOP.json）

GPU peakはnvidia-smiによるdevice全体の使用量で、モデル単独のVRAM使用量ではない。Qwen14 peak 9926 MiB / minimum free 126 MiB、CUDA 0。高使用量のみからOOMとは判断しない。
