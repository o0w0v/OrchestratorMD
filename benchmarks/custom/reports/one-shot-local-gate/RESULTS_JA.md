> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/one-shot-local-gate.md). This report alone does not establish a task result.

# Router Economic Policy Experiment — One-Shot Local Gate

実施日: 2026-10-04。判定: **ONE_SHOT_ROUTER_PROMISING**。

新規8 Taskのpaired比較を完了した。実測Codex CLI usageはA（One-Shot Local）807,622 tokens、B（Codex-only）938,417 tokensで、**130,795 tokens / 13.94%減**。一方、計測した工程時間の合計はAが**163.09秒 / 15.28%増**だった。

Local First PASSはOSL-002の1件だけで、そのTaskではCodexコード変更0、tokens 73.68%減。First FAILの7件では、失敗candidateを読ませないclean direct実装のtokensがBより集計で5.07%少なかった。ただしTask別には増減があり、この差をclean handoffによる因果的削減とはみなさない。小標本、特にFirst PASSが1件のためCONFIRMEDにはしない。

## 1. 目的と比較方法

モデルの一般能力やProtocol改善ではなく、Localの初回試行をfilterとして使うworkflow costを測った。

- A: Localの最初のcode candidateだけを評価。PASSなら独立Codex compact review。非PASSならLocal repairを使わず、clean initial sourceから独立Codex direct implementation。
- B: 同じ契約・初期source・allowed scope・acceptance・validationでCodexが直接実装し、独立final review。
- First PASS reviewでfindingが出た場合のcandidate-seeded fallbackも、Local開始前に用意した。今回の呼び出しは0回。
- B全8件を完了・freezeした後、Local全8件、続いてA側のreview/directを順に実施。途中でTaskや条件を最適化していない。

今回の`LOCAL_FIRST_FAIL`は、インフラ異常・cohort STOPを除く初回非PASSのworkflow分類。formatter未対応によるsemantic validation未実施も含む。元resultの`first_pass=null`やfailure domainをFalseやcoding FAILに書き換えてはいない。

## 2. Freeze・変更範囲

Productionのbounded profile **2.2.6**、Router v2.1、Operational Policy、model registry、prompts、Coverage Gate、ReferencePlan、formatter、failure classification、通常repair eligibility/budgetを維持した。Gemma12 quarantineも維持。今回の8件は既存routingでGemma26が選択され、モデルのoverride追加や自動fallbackはない。

Local条件は全10 `/api/chat` callsで確認済み:

|項目|固定値|
|---|---|
|model|gemma4:26b|
|temperature / seed|0 / 20260926|
|num_ctx / num_predict|8192 / 2048|
|max_context_chars|24000|
|stream / think|false / false|
|code generation|各Task 1回、合計8回|
|read-only DISCOVERY|合計2回|
|Local repair generation|0回|

実験専用gateが通常runtimeのrepair scheduling境界でrepairを辞退する。第二code dispatchを送信前に拒否する防御もある。productionファイルやrepair定義は変更せず、通常経路でrepairが引き続き動くことをofflineで確認した。Taskの`max_attempts=2`も維持している。

freeze.json（元資料: freeze.json）、DESIGN.md（元資料: DESIGN.md）、request audit（元資料: summaries/request-audit.json）、One-Shot gate（元資料: economic_gate.py）に定義とSHA256を保存。Task goal/interface/scope/acceptance/source hashesは両経路の開始前に固定。追加したのは本実験ディレクトリのharnessとartifactだけで、applicationへ候補を採用していない。

## 3. 新規TaskとLocal結果

既存CVB/P224/Fresh-Taskのbusiness Taskは再実行していない。同じRust型・repositoryの土台は使用した。差分はnovelty記録（元資料: summaries/task-novelty.json）を参照。fixed_slot 6件、stateful 2件。すべてlow riskでdependency/schema変更なし。

|Task|business挙動|Local初回結果|Local input/output|Worker秒|
|---|---|---|---:|---:|
|OSL-001|AuditRecordのevent kind別件数|compile E0433|1,624 / 235|69.47|
|OSL-002|記録済みbudget/usageから残量を飽和減算|PASS|1,285 / 81|54.24|
|OSL-003|warningをUnicode scalar数でclip|Clippy `explicit_counter_loop`|713 / 194|56.05|
|OSL-004|event targetのstable unique JSON一覧|FORMAT_UNSUPPORTED_NORMALIZATION|1,362 / 195|10.00|
|OSL-005|sourceごとの最大u128 elapsed値|FORMAT_UNSUPPORTED_NORMALIZATION|1,377 / 213|9.99|
|OSL-006|process RSSの3区分件数|acceptance FAIL|994 / 128|52.16|
|OSL-007|MemoryPressureへsampled root-row evidence追加|acceptance FAIL|3,663 / 181|51.97|
|OSL-008|HighLoadへmemory sample状態evidence追加|acceptance FAIL|3,415 / 205|56.95|

Local First PASS **1/8**、First FAIL **7/8**。通常ならsemantic repair対象となる001/006/007/008の4件でgateがrepairを辞退。003は既存allowlist外lint、004/005は既存formatter未対応の分類で終了した。004/005のsemantic品質は未判定のまま保存した。これらを理由にformatterやlint policyを拡張していない。

Local input **14,433**、output **1,432**、reported cache **1,286**。Ollama reported duration合計**61.985秒**、Worker wall合計**360.813秒**。Local token値はAPI報告値であり、Codex tokenへの換算はしていない。

Local outcomes（元資料: summaries/local-outcomes.json）、run-history（元資料: run-history.json）、Local evidence seal（元資料: LOCAL_FROZEN.json）から各raw request/response、candidate、diff、checks、GPU/logへ辿れる。旧CVB結果だけでなく、今回の7件のLocal非PASSも後からPASSへ変更していない。

## 4. Blinding・Codex条件・usage取得

Codex CLI **0.160.0 / gpt-6-astra / xhigh**を両経路で固定。独立sessionは**31件**（B実装8＋B review8＋A direct7＋A review8）。resume/forkによる文脈継承なし。全phaseでraw `turn.completed.usage`を取得し、input/cached input/output/totalを保存した。

A-directの7件はBと同じ初期source hash、契約、AGENTS、最初のimplementation promptを使用。Local candidate/diff/診断/summary/失敗statusは供給していない。A-directは自分のclean directoryのみを読み、reviewは専用packetのみを読んだ。31 sessionのmodel/effort・入力・tool traceを監査し、他Task/他arm参照を示すflagは0。これはtool trace上の監査であり、完全なOS read isolationの証明ではない。

Local PASS reviewには契約・検証済みdiff・check結果・短いsummaryのみを渡し、全会話を渡していない。未呼出しphaseのusageはnull、呼出し回数は0として区別した。

session audit（元資料: summaries/session-audit.json）、review packets（元資料: summaries/review-inputs/）、B_FROZEN.json（元資料: B_FROZEN.json）、A_FROZEN.json（元資料: A_FROZEN.json）を参照。各phaseの`codex/<arm>/<task>/<phase>/END.json`に実usageとraw usageがある。

## 5. Task別A/B

tokensは各workflowの実装＋独立review＋実施したfallbackの合計。削減率は`(B−A)/B`で、負はAの方が多い。LOCはコードの追加＋削除行数（最終正規化後のscope内diff）。

|Task|group|A tokens|B tokens|削減率|A Codex LOC|B LOC|
|---|---|---:|---:|---:|---:|---:|
|OSL-001|FIRST_FAIL|141,757|141,744|−0.01%|20|23|
|OSL-002|FIRST_PASS|31,929|121,291|73.68%|0|7|
|OSL-003|FIRST_FAIL|99,508|98,577|−0.94%|8|8|
|OSL-004|FIRST_FAIL|100,609|120,362|16.41%|11|10|
|OSL-005|FIRST_FAIL|100,722|119,573|15.77%|11|11|
|OSL-006|FIRST_FAIL|100,033|100,185|0.15%|13|11|
|OSL-007|FIRST_FAIL|116,426|100,630|−15.70%|18|18|
|OSL-008|FIRST_FAIL|116,638|136,055|14.27%|20|20|
|合計|8 pairs|**807,622**|**938,417**|**13.94%**|**101**|**108**|

First FAIL群のLOCはA/Bとも101。個別token差には独立Codex sessionの読み方・tool使用量などのばらつきが含まれる。特に007ではAが15.70%多い。集計5.07%減を「失敗後も必ず節約できる」という主張には使わない。

## 6. Group・phase集計

|group|件数|A tokens|B tokens|差 B−A|削減率|
|---|---:|---:|---:|---:|---:|
|LOCAL_FIRST_PASS|1|31,929|121,291|89,362|73.68%|
|LOCAL_FIRST_FAIL|7|775,693|817,126|41,433|5.07%|
|ALL_PAIRED|8|807,622|938,417|130,795|13.94%|

|phase|A tokens|B tokens|
|---|---:|---:|
|implementation / clean direct|550,850|681,913|
|independent review|256,772|256,504|
|review finding後のfallback|未呼出し / null|未呼出し / null|

実測totalはinput＋outputで、cached inputを二重加算しない。

|usage|A|B|
|---|---:|---:|
|input|798,907|927,531|
|cached input（input内数）|506,368|616,960|
|output|8,715|10,886|
|input − cached input|292,539|310,571|

cache構成が異なるため、13.94%というtotal token差を同率の料金差とは扱わない。金額換算は行っていない。

## 7. Coding avoidance・品質・介入

- `CODEX_CODING_AVOIDED`: **1/8 = 12.5%**。OSL-002のみ。
- A: code implementation session 7件、review 8件。B: implementation 8件、review 8件。両経路のCodex追加implementation retryは0回。
- Local PASSに対する`ACCEPT_NO_CHANGE`: **1/1**。全8 Taskを分母にするLocal由来code-free acceptanceは**1/8**。
- A/Bの最終候補はそれぞれ**8/8**で同じmandatory validationをPASSし、独立final reviewもACCEPT_NO_CHANGE。
- First FAILのLocal candidate再利用は**0件（policyによるclean handoff）**。Local candidateを評価して破棄すべきと判断したという意味ではない。
- Local PASS reviewのfinding、Codex review後fallback、FALSE_GREENは0。FALSE_GREENの対象となるLocal PASSは1件だけ。
- Host integrity/scope STOP 0、INFRA/CUDA 0。formatter未対応2件は別記録。

品質条件はacceptance、targeted regression、fmt、Clippy、workspace test/check/build、scope/hash/freeze guard。どちらの最終経路でも緩めていない。

## 8. Wall timeとHost validation

以下は**計測済みの直列工程の合計**（Local Worker wall＋Codex CLI phase wall＋Codex Host validation interval）。実験全体のcalendar elapsedや人間/Codexのactive timeではない。Task間の待機、集計、準備、未測定orchestrationは除く。Bを先に全件実行したbatch schedulingの待ち時間も含めない。

|group|A 秒|B 秒|A−B 秒|
|---|---:|---:|---:|
|FIRST_PASS|69.52|137.66|−68.14|
|FIRST_FAIL|1,160.88|929.64|+231.24|
|全体|**1,230.39**|**1,067.30**|**+163.09**|

First FAIL群には合計**306.578秒**の先行Local Worker時間が追加された。個別A−BにはCodex session時間のばらつきも含まれ、全Taskが同じだけ遅くなるという測定ではない。token削減とlatencyを別評価する。

同じ固定validation commandについて、Aは**91回 / 505.893秒**、Bは**56回 / 339.930秒**。失敗したLocal側の実行も数える。formatter normalization、copy/hash、scope guardの処理時間はこのcommand-only値には含めないが、上のworkflow工程時間にはLocal WorkerまたはCodex Host validation intervalの一部として含まれる。

host-validation-cost.json（元資料: summaries/host-validation-cost.json）が比較可能なcommand-only指標。`metrics.json`の`A_host_validation_seconds`はLocal command時間とCodex Host intervalを足した混合の下限値なので、対等なcommand比較にはこの専用集計を用いる。Localのvalidation全体の独立intervalは取得しておらずnull。

## 9. Preparationと未計測コスト

共通scaffold/wiring/acceptance差分は**357 LOC**。Local専用scope markerは**20 LOC**、runner/Coverage Matrix等のmetadataは**53,841 bytes**。byte数をtokensや作成工数に換算していない。

同じ契約・tests・初期sourceの準備はSHARED_PREP。Local用protocol metadata・markersはLOCAL_ONLY_PREP。blind copy/CLI metrologyはBとA-directで共通。実験harnessの作成・監督・調査・本レポートなど親Codexのphase別tokens/active timeは取得できていない。

したがって、**実測CLI差130,795 tokensと、準備・監督込みのNET_CODEX_TOKENS_SAVEDは別物**。後者はnull。Host preparationを含む全作業が13.94%減ったとは主張しない。preparation.json（元資料: summaries/preparation.json）に内訳を保存した。

## 10. Infrastructure・回帰・保全

Windowsは直前recoveryでユーザーがrebootした環境を継続。今回追加のfresh-process条件を導入せず、健康な既存frontend PID 29348から開始。RTX 3080 10GB、driver 591.86、Ollama 0.35.1、Gemma26 digestはenvironment.json（元資料: environment.json）に保存。再起動・強制unload・download・generation health probeは行っていない。

Task前後のGPU/API/process/residencyを保存し、全8件のpost healthは正常。CUDA/backend fault、display reset、cohort STOP 0。これは今回の短いcohortの観測であり、過去のCUDA障害の解決宣言ではない。

実行前にOne-Shot offline tests **6件PASS**、既存Worker suite PASS、Rust fmt/clippy/test/check/build PASS。通常repair経路、first request/check同等性、syntax/semantic/lint失敗のrepair非dispatch、第二code dispatch拒否を検証した。実際の全10 chat payloadの固定optionsも監査済み。

production/runtimeおよび既存tracked artifactは保存済みhashと一致。旧STOP/CUDA/旧結果は保全。B・Local・Aの結果を別々にsealし、再実行・成功への上書きはしていない。Gitの改行変換でraw証跡が変わらないよう、本ディレクトリだけ`-text`属性にしている。

Git whitespace checkはraw CRLF、unified diffの空行context、terminal出力の末尾改行等を検出した。証跡を整形し直さず保持し、診断一覧（元資料: summaries/git-whitespace-check.json）に記録した。harness/docsだけのwhitespace checkはPASS。Rust候補のfmt品質は上記の固定validationで別途確認済み。

## 11. 判定と限界

**ONE_SHOT_ROUTER_PROMISING**。First PASSをcompact reviewだけで済ませる経路のtoken差は大きく、First FAILをclean directへ回した7件は集計でCodex-onlyに近かった。固定条件のまま8件を終え、両経路で同じ最終品質条件を満たした。

ただし、First PASS群は**1件**であり再現性は未確認。First FAIL群の−15.70%〜+16.41%というTask別削減率の幅、1 Task/armあたり1試行、B先行の固定順序、copyの保存先、cache/API時間の変動がある。統計的な同等性検定ではない。単一repositoryの小さいTaskに限定され、一般的なモデルランキングでもない。

今回はrepairあり・failed-candidate再利用ありの同時対照を置いていないため、**「Local repairに価値がない」「candidateを読まないことが差の原因」までは検証できない**。過去5-pair結果は背景であり、今回の母集団に混ぜていない。

Local First PASS率12.5%では、全体token削減13.94%に対して工程時間は15.28%増となった。待ち時間を重視する用途で常に有利とは言えず、準備・監督込みの経済価値も未確定。production Routerへの採用や追加experimentは行わず、ここで結果報告として停止する。

## Artifact index

- metrics.json（元資料: summaries/metrics.json）: Task/phase別実測tokens、LOC、wall、group集計。
- task-comparison.csv（元資料: summaries/task-comparison.csv）: 8 paired Taskの比較表。
- session-audit.json（元資料: summaries/session-audit.json）: 全31 CLI session、raw usage、blinding、tool calls。
- request-audit.json（元資料: summaries/request-audit.json）: 全Local chat requestのpath、bytes、SHA256、options。
- infrastructure-safety.json（元資料: summaries/infrastructure-safety.json）: GPU/API/Event Logへの参照。
- decision.json（元資料: summaries/decision.json）: 判定と限界。
- regression/（元資料: regression/）: 実験前のoffline/Worker/Rust checks。
- workspace/records/router-v2.2/（元資料: workspace/records/router-v2.2/）: Localのraw候補・response・diff・validation。
- codex/（元資料: codex/）: 独立Codexのprompt、CLI events、usage、source edits、全validation、review。
