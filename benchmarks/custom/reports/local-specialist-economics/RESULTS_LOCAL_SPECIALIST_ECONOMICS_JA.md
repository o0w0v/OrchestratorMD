> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/local-specialist-economics.md). This report alone does not establish a task result.

# Local Specialist Economic Router Benchmark

集計UTC: 2026-10-04T17:30:19.376732+00:00

判定: **INCONCLUSIVE**

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

|model|有効coding Task|First PASS|rate|economic pairs|
|---|---|---|---|---|
|gemma26|1|0|0.00%|1|
|qwen14|0|0|N/A|0|


## 6. Failure taxonomy

gemma26: {"HOST_FORMAT_ERROR": 1}; missing pairs=['LSE-002', 'LSE-003', 'LSE-004', 'LSE-005', 'LSE-006', 'LSE-007', 'LSE-008', 'LSE-009', 'LSE-010', 'LSE-011', 'LSE-012', 'LSE-013', 'LSE-014']

qwen14: {}; missing pairs=['LSE-001', 'LSE-002', 'LSE-003', 'LSE-004', 'LSE-005', 'LSE-006', 'LSE-007', 'LSE-008', 'LSE-009', 'LSE-010', 'LSE-011', 'LSE-012', 'LSE-013', 'LSE-014']

repairはsyntax/semantic/lintすべて0。read-only DISCOVERYは別カウント。CUDA/infraはcoding分母へ混ぜず、STOP・未実行・coverageを残す。Local FAIL時はclean initialから新sessionのCodex実装。失敗candidateを与えず、成功したbaseline解を流用しない。

## 7. Model × category

|category|Gemma First PASS|Qwen First PASS|Gemma saved|Qwen saved|highest PASS|highest saved|
|---|---|---|---|---|---|---|
|COMPILE_SENSITIVE|0/0|0/0|N/A|N/A|||
|DEBUGGING|0/0|0/0|N/A|N/A|||
|REASONING|0/0|0/0|N/A|N/A|||
|SEMANTIC_EDIT|0/0|0/0|N/A|N/A|||
|SMALL_REFACTOR|0/0|0/0|N/A|N/A|||
|STATEFUL|0/0|0/0|N/A|N/A|||
|STRICT_OUTPUT|0/1|0/0|1.203|N/A|gemma26||


この全screen比較の最大値は事後の記述統計であり、Router選択には使わない。

## 8. Codex raw usage

{
  "usage": {
    "input_tokens": 3019530,
    "cached_input_tokens": 2493952,
    "uncached_input_tokens": 525578,
    "output_tokens": 48360,
    "total_tokens": 3067890
  },
  "credits": 50.838660000000004,
  "USD_equivalent": 2.0335464,
  "session_wall_seconds": 1899.3599999999933,
  "sessions": 45
}

各phaseのEND.jsonにraw turn.completed usageを保存。cachedをinputから差し引いてuncachedを算出。session-audit.jsonで独立session、実model/effort、最大request inputを検証。欠測を推定しない。

## 9. Codex credits

公式pricing（元資料: http[LOCAL_PATH]）から凍結したStandard rateは uncached=50 / cached=5 / output=250 credits / 1M tokens。式は (input-cached)*50/1M + cached*5/1M + output*250/1M。HTML/Markdown・URL・時刻・SHAはrates/。shared Plannerは両workflowへ同じ実測costを1回ずつ加算し、実支出合計はunique sessionを一度だけ数える。

## 10. Credits saved by Local model

|model|baseline matched|routed matched|saved|reduction|saved/Task|First-PASS saved|failed-gate delta|
|---|---|---|---|---|---|---|---|
|gemma26|4.430|3.227|1.203|27.16%|N/A|0.000|-1.203|
|qwen14|N/A|N/A|N/A|N/A|N/A|0.000|0.000|


FAILED_LOCAL_GATE_CODEX_CREDIT_DELTAはrouted-baseline、正が追加消費。complete=falseのmodelでは未実行を0 costにせず、EXPECTED指標はnull。独立Codex sessionのcache/実装探索差をLocal能力の利益と断定しない。

## 11. USD equivalent saved

公式GPT-6 Sol API rate（元資料: http[LOCAL_PATH]）: $2/$0.2/$10 per 1M uncached/cached/output tokens。実請求額ではない。

|model|USD equivalent saved|
|---|---|
|gemma26|0.04813|
|qwen14|N/A|


## 12. JPY status

JPY_PER_CREDIT=null、JPY_SAVED=null。購入単価を確認できていない。為替やcredit残高から実円料金を逆算しない。

## 13. GPU/VRAM/CUDA

|model|sample数|無効sample|peak used MiB|minimum free MiB|CUDA|infra|Host STOP|FALSE_GREEN|
|---|---|---|---|---|---|---|---|---|
|gemma26|31|0|9996.000|56.000|0|0|1|0|
|qwen14|0|0|N/A|N/A|0|0|0|0|


各cohortのfresh-exit/environment、各Task before/during/after、backend/frontend PID、frontend age、server log、Windows eventsを保存。物理容量外の値はraw保持、派生統計null。Gemma12/CoderNextやgeneration probeは使用しない。

## 14. Wall overhead

|model|Worker秒合計|Ollama API秒|Local input/output tokens|平均routed-baseline wall秒|
|---|---|---|---|---|
|gemma26|32.719|25.066|998/169|19.423|
|qwen14|0.000|N/A|None/None|N/A|


Ollama durationはload/CPU offloadを含む実API計測時間。GPU kernelの実行秒は取得していないためnull。Worker wallをGPU kernel時間と同一視せず、Local tokenをCodex creditsへ換算しない。

active作業時間ではなくwall interval。Planner+モデル/Executor/review session+Host validationを合成し、Local Worker wallにはその内部validationを含めて二重計上しない。fresh start待ち、ユーザーQuit待ち、coordinator待機はTask latencyに含めず別の運用負担。baselineの一部は2 process並行のためwallにCPU/service contentionが混ざる。速度の因果比較ではない。

## 15. Development routing

DEV_ROUTING_FROZEN.jsonがselectionの唯一の根拠。developmentでFirst PASS/accepted/positive credit savings/infra安全を満たす候補だけ選ぶ。選択後にheld-outでモデルを差し替えない。

## 16. Held-out validation

|category|dev selected|held-out Task|saved credits|supported|
|---|---|---|---|---|


## 17. Recommended Router

|category|proposal only|
|---|---|


候補Localはone-shot -> PASSなら6 Sol review、FAILならclean sourceから6 Sol direct。production Routerは変更していない。

## 18. Limitations

各categoryはdevelopment/held-out各1件。多様なproduction workloadの平均効果・一般故障率へ外挿しない。追加モデルは未導入/未測定。共通Task設計・acceptance/scaffold・experiment harness・調査とcoordinatorのCodex costは未計測=nullで、ここでのcreditsは測定したworkflow役割の比較に限る。Host準備を含む全アカウントnet savingsとは呼ばない。Standardは指定config/runtime evidenceでありinvoice tierは未取得。私有copyとtool auditは完全なOS read sandboxの証明ではない。

## 19. Decision

**INCONCLUSIVE**。完了状況とカテゴリ単位のheld-out証拠に限定した判断。小標本の最大値をproductionのoracleにしない。旧artifact/STOP/result、Routerとbounded2.2.6は保全。


---

# Development完了追記 2026-10-04T17:58:20.481804+00:00

前節はcheckpoint-001時点の記録。最新の19項目の報告は development完了報告（元資料: RESULTS_LOCAL_SPECIALIST_ECONOMICS_DEVELOPMENT_JA.md）、raw集計は economics.json（元資料: summaries/development-complete/economics.json） を参照。旧checkpointは保持。

Qwen14 development: First PASS 2/7、独立レビュー込み全7経路品質PASS、CUDA/INFRA/Host STOP/FALSE_GREEN 0。matched baseline 25.68249 → routed 23.98654 credits、削減1.69595 credits（6.60%）。First PASS群の削減4.04237 creditsとFirst FAIL群の追加2.34642 creditsを分離。60独立Codex sessionのusage/料金とblinding監査PASS。

STRICT_OUTPUT/SEMANTIC_EDIT → Qwen14というdevelopment候補をDEV_ROUTING_FROZEN.jsonへ固定。held-outは0件で、Qwen frontendのtray Quit待ち。現時点の判定はINCONCLUSIVE。GemmaのHOST_FORMAT_ERROR/STOPは保持し、停止モデルの再試行やproduction変更は行わない。


---

# 最終追記 2026-10-05T01:17:30.416637+00:00

前節のcheckpoint/development記録は保存。最新は 最終結論（元資料: CONCLUSION_JA.md） と 19項目の最終報告（元資料: RESULTS_LOCAL_SPECIALIST_ECONOMICS_FINAL_JA.md）。

Qwen14は14/14経済pair完了、First PASSは2/14（held-out 0/7）。48.84606 → 48.99985 credits、削減−0.15379（0.31%増）。事前選択2カテゴリでもFirst PASS再現0。Gemma26は元のHost STOPで1/14のまま保全。全74session監査PASS、CUDA/INFRA/FALSE_GREEN 0。総合判定INCONCLUSIVE、production変更0。今回の許可されたcohortの実行と集計は終了し、追加推論・download・retryは行わない。
