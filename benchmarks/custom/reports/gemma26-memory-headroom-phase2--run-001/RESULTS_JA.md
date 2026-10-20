> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/gemma26-memory-headroom-phase2--run-001.md). This report alone does not establish a task result.

# Gemma26 Memory Microbenchmark Phase 2
集計: 2026-10-07T12:19:19.199431+00:00 / 判定: **KEEP_8192_F16**

目的: 4096の実VRAM/headroomと8192 fresh replicate。model ranking/production変更は行わない。旧A/B/Cはread-only、全12 Taskとprotocolは同一。
A2=8192/f16、D=4096/f16、E=4096/q8_0。全Arm FA1、Gemma26同digest/Q4_K_M、bounded2.2.8、num_predict2048、temperature0、seed20260926、one-shot repair0。
事前freezeとHost検証: FREEZE.json / OFFLINE_CHECKS.json / DESIGN_JA.md。各Armのuser boundary・absence・fresh models=[]・実backend設定はarms配下。

|Arm|terminal Task|RAW PASS|LF rescue|Host PASS|quality ACCEPT|CTX_INELIGIBLE|quality regression vs A2|Local validation FG|final pipeline FG|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|A2|12/12|9|1|10|9|0|reference|1|0|
|D|12/12|9|1|10|9|0|0|1|0|
|E|12/12|9|1|10|9|0|0|1|0|

Context: actual prompt_eval_count + output reserve、request interval logをapply前に確認。CTX_INELIGIBLEはquality FAILから除外。count単独でtruncation不存在を断定しない。
Independent review: GPT-6 Sol/xhigh/Standard、current compact packetのみ。5 hash完全一致時だけimmutable historical independent reviewを再利用。Local validation false greenと最終採用false greenを分離。

|Arm|before-load background MiB|loaded idle used/free median MiB|peak used MiB|min free MiB|mean loaded used MiB|CLI CPU/GPU %|main GPU layers|CPU offload warning|
|---|---:|---|---:|---:|---:|---|---|---|
|A2|1939.00|9958.00/94.00|9994.00|58.00|9981.74|24/76|31/31|reference|
|D|1322.00|9775.00/277.00|9897.00|155.00|9844.13|24/76|31/31|False|
|E|1017.00|9761.00/291.00|9821.00|231.00|9815.67|27/73|31/31|True|

|Comparison|idle free delta MiB|min free delta MiB|background used delta MiB|background confound|quality regression|
|---|---:|---:|---:|---|---:|
|A2 vs prior A|-300.00|-277.00|909.00|True|0|
|D vs A2|183.00|97.00|-617.00|True|0|
|E vs A2|197.00|173.00|-922.00|True|0|
|E vs D|14.00|76.00|-305.00|True|0|

Global GPU used/freeにはdesktop等のbackgroundが含まれる。background/order effectを保存し、モデル単体VRAMを差分から逆算しない。1秒samplingは瞬間peakを逃す可能性。draft cacheがmain共有の場合、logical KV sizeを重複加算しない。
CPU/GPU evidence: raw cli_ps、backend command、layers、FA、main/draft KV、batch/context、CUDA/Host buffersをsummary allocation_evidence_linesとraw server.logに保存。working setはshared mapped pagesを含みCPU演算量ではない。CLI split変化のみでweight offloadを断定しない。

|Arm|Local input/output tokens|API mean/median/p95 s|gate mean/median/p95 s|validation mean/median/p95 s|CUDA|backend crash|query timeout|infra|new/reused review|
|---|---:|---|---|---|---:|---:|---:|---:|---:|
|A2|16282/663|3.09/2.95/4.66|48.20/51.30/56.31|35.82/39.49/41.75|0|0|0|0|0/10|
|D|16282/663|3.22/3.06/4.95|48.97/52.52/58.88|35.79/39.96/41.28|0|0|0|0|0/10|
|E|16282/653|2.64/2.50/4.14|46.59/49.90/54.83|34.76/38.38/39.73|0|0|0|0|0/10|

Task別:

|Arm|Task|Host reason|review|prompt tokens|context fit|quality|
|---|---|---|---|---|---|---|
|A2|LS3W228-001|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1349]|True|True|
|A2|LS3W228-003|ESCALATE / FORMAT_UNSUPPORTED_NORMALIZATION|None|[1876]|True|False|
|A2|LS3W228-004|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1034]|True|True|
|A2|LS3W228-007|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1325]|True|True|
|A2|LS3W228-009|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1358]|True|True|
|A2|LS3W228-011|PASS / TARGETED_CHECKS_PASSED|REJECT|[950]|True|False|
|A2|LS3W228-014|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1648]|True|True|
|A2|LS3W228-015|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1633]|True|True|
|A2|LS3W228-017|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1378]|True|True|
|A2|LS3W228-020|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1029]|True|True|
|A2|LS3W228-021|ESCALATE / CODE_FAILURE|None|[1334]|True|False|
|A2|LS3W228-023|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1368]|True|True|
|D|LS3W228-001|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1349]|True|True|
|D|LS3W228-003|ESCALATE / FORMAT_UNSUPPORTED_NORMALIZATION|None|[1876]|True|False|
|D|LS3W228-004|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1034]|True|True|
|D|LS3W228-007|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1325]|True|True|
|D|LS3W228-009|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1358]|True|True|
|D|LS3W228-011|PASS / TARGETED_CHECKS_PASSED|REJECT|[950]|True|False|
|D|LS3W228-014|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1648]|True|True|
|D|LS3W228-015|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1633]|True|True|
|D|LS3W228-017|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1378]|True|True|
|D|LS3W228-020|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1029]|True|True|
|D|LS3W228-021|ESCALATE / CODE_FAILURE|None|[1334]|True|False|
|D|LS3W228-023|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1368]|True|True|
|E|LS3W228-001|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1349]|True|True|
|E|LS3W228-003|ESCALATE / FORMAT_UNSUPPORTED_NORMALIZATION|None|[1876]|True|False|
|E|LS3W228-004|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1034]|True|True|
|E|LS3W228-007|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1325]|True|True|
|E|LS3W228-009|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1358]|True|True|
|E|LS3W228-011|PASS / TARGETED_CHECKS_PASSED|REJECT|[950]|True|False|
|E|LS3W228-014|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1648]|True|True|
|E|LS3W228-015|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1633]|True|True|
|E|LS3W228-017|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1378]|True|True|
|E|LS3W228-020|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1029]|True|True|
|E|LS3W228-021|ESCALATE / CODE_FAILURE|None|[1334]|True|False|
|E|LS3W228-023|PASS / TARGETED_CHECKS_PASSED|ACCEPT_NO_CHANGE|[1368]|True|True|

結論: **KEEP_8192_F16**。4096候補はquality regression0・12/12 fit・infra0・対A2明確headroom改善が必要。q8候補は対D追加改善も必要。
改善不足/background交絡/quality低下ならKEEP_8192_F16。これは8192の一般的優越を意味しない。旧停止やCUDAを成功扱いにしない。
各Arm最大12 Task、sampleが小さく固定順序。一般故障率・長期stability・一般能力・経済価値へ外挿しない。production設定、Router、Pilot、applicationは変更しない。
raw request/response/checks/events/log/telemetryはarms/{A2,D,E}/、run-history.json、TERMINAL_SEAL.jsonから参照可能。未開始ArmはNOT_RUN。自動restart/retry/rebootなし。

補足: backend allocationと保全確認

|Arm|main CUDA KV buffers MiB|main CUDA model buffer MiB|main CUDA_Host model buffer MiB|GPU main/draft layers|
|---|---|---:|---:|---|
|A2|[160.0, 300.0] (sum 460.00)|6075.84|10819.57|[(31, 31), (5, 5)]|
|D|[80.0, 300.0] (sum 380.00)|6075.84|10819.57|[(31, 31), (5, 5)]|
|E|[42.5, 159.38] (sum 201.88)|6355.51|10539.91|[(31, 31), (5, 5)]|

Eのmain KV bufferはDより178.12MiB小さい一方、main CUDA model bufferは279.67MiB大きい。CUDA_Host model bufferはほぼ同量減っている。layer countの一致だけではtensor/buffer placementの一致を保証しない。
これはbackendの明示的bufferログの比較であり、global GPU memoryからmodel単体の物理VRAMを推定した値ではない。背景/orderとbackendのfit/placementが交絡し、変化をKV typeだけの一般的因果へ外挿しない。
EのCLI PROCESSORは27%/73% CPU/GPUで、固定された保守的CPU_OFFLOAD_WARNING=trueをそのまま保持する。一方CUDA model bufferは増加しており、CLI比だけで「CPUへ移した」と断定しない。実際の演算割合/個別tensor placementの全容はUNRESOLVED。
draftの論理cacheにはmainとのsharing記録がある。main KV削減へdraft値を追加して二重計上しない。main/draft model buffer、CPU_Host、fit/placement raw行はanalysis/FINAL_ALLOCATION_REQUEST_PROOF.jsonで照合可能。

Actual request / context / quality:
同じTaskについて3 Arm間のmessages/schema/temperature/seed/output budget等が同一であることを、12 Task×3のactual requestで検証した（Task間のmessages/schemaはそれぞれ異なる）。A2/D/E差はpayloadのnum_ctxとprocess-scoped KV設定のみ。各Task exactly one generation、Local repair0、clean fallback0。
A2/D: candidate body identical 12/12、quality regression 0、CTX_INELIGIBLE 0。
A2/E: candidate body identical 10/12、quality regression 0、CTX_INELIGIBLE 0。
全Armでactual prompt最大1876 + output reserve2048 =3924。4096にも収まった。ただしprompt countのみを元prompt全文処理の証明とせず、request intervalのpositive truncation evidenceなし・schema/apply/validationを合わせて確認した。
独立reviewは30件を5 hash完全一致でimmutable再利用、新規Codex review call0。003はformatter未対応、021はCODE_FAILURE、011はHost PASSでもreview REJECT。Local validation FALSE_GREEN1/Armとfinal pipeline FALSE_GREEN0を区別する。

Windows Event Log: available 36/36 Task windows、関連event合計0、Display reset 0。取得不能はnull/unavailableとしてraw保存し、存在しないイベントを推測しない。
開始前のWorker275とRust fmt/clippy/test/check/buildはregression/RESULT.jsonでPASS。36 Worker boundary /36 native Cohort /3 review positives /36 review negativesはOFFLINE_CHECKS.jsonでPASS。runtime/production/source/frozen inputは最終hash一致。
旧memory artifact20891 files、historical L3W artifact、旧STOP・CUDA・A2/D結果は保全。FINAL_PRESERVATION.json、各arm TERMINAL_SEAL.json、analysis/FINAL_ALLOCATION_REQUEST_PROOF.json、run-history.jsonからraw pathsを参照可能。
準備中のcp932入力read errorとOllama CLI queryによるunexpected auto-startはPREPARATION_*へ保全。再user Quit後のabsenceからA2を実施し、意図しないfrontendはArmへ使用していない。終了確認中のCLIを避けるHost運用補正だけで、business/protocol/production変更なし。

結論: **KEEP_8192_F16**。D/Eは品質・context fitを維持したが、loaded-idle/min-freeの改善が事前256MiB基準未達で、background差も大きい。q8_0のD比追加free改善はidle14MiB/min76MiBに留まる。4096/q8のproduction採用根拠は不足する。
4096が動作不能・q8が無意味・8192が常に省VRAMという結論ではない。この12 fixture/1 attempt/fixed arm orderの観測と保守的運用判断である。追加generation/実験・Router/Pilot自動再開は行わない。
終了時snapshotはEXPERIMENT_EXIT_STATE.json。Ollamaが存続している場合はEのchild-only条件が残る。永続user/machine環境は変更していない。通常運用前にはuser tray Quitによるfresh frontendから通常設定へ戻す必要がある。自動restart/unloadは行っていない。
