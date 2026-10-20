> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/gemma26-memory-headroom-228--run-004.md). This report alone does not establish a task result.

# Gemma26 Memory Headroom Microbenchmark
集計: 2026-10-07T10:42:36.137474+00:00 / 判定: **TEST_4096_NEXT**

1. Arm configuration: A=8192/f16、B=6144/f16、C=6144/q8_0。全Arm FA=1、Gemma26 Q4_K_M、bounded2.2.8、2048 output、one-shot/repair0。production変更なし。
2. Environment proof: 各Armの ENVIRONMENT_PROOF.json / startup/load raw server.log。requested envだけでなくbackendのcontext、FA、main K/V typeで確認。
3. Task selection: SELECTION.json。過去prompt_eval_countのshort/median/long、各family3件。選択に品質結果を使用しない。
4. Context fit: actual native count + output reserveとrequest intervalのtruncation証跡。未fitはCTX_INELIGIBLE。token count単独をtruncation不存在の証明としない。

|Arm|完了Task|RAW PASS|LF救済|Host PASS|QUALITY ACCEPT|CTX不適格|品質regression vs A|Local FG|Final FG|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|A|12/12|9|1|10|9|0|N/A|1|0|
|B|12/12|9|1|10|9|0|0|1|0|
|C|12/12|9|1|10|9|0|0|1|0|

5. Raw/LF pass、6. Review quality、7. Quality regressionは上表。新規reviewは独立GPT-6 Sol xhigh Standard。旧review再利用は5 hash完全一致のみ。
8. Output identity: Aとのcandidate body hash比較。本文はescaped JSONの決定的encodingでhash、LF差も保持。

|Arm|loaded idle used/free median MiB|peak used MiB|min free MiB|mean loaded used MiB|main GPU layers|backend CPU working set median MiB|CPU shift|
|---|---|---:|---:|---:|---|---:|---|
|A|9658.00/394.00|9717.00|335.00|9714.63|31/31|15952.54|reference|
|B|9847.00/205.00|9983.00|69.00|9882.32|31/31|16351.52|False|
|C|9747.00/305.00|9965.00|87.00|9883.38|31/31|13122.81|False|

9. Loaded idleはempty preload完了後generation前3 samples。10. Peak/min/meanはresidentかつ有効なGPU samplesのみ。
11. CPU/GPU offload: CLI ps split、offload layers、backend command、KV/draft/batch/context、native working-set/private bytesをraw保存。CPU working setはshared mapped pagesを含み、CPU演算量ではない。
12. Local usage / 13. latency（API / Local gate / Host validation、secondsのmean/median/p95）:

|Arm|native input/output tokens|API seconds mean/median/p95|gate seconds mean/median/p95|validation seconds mean/median/p95|
|---|---:|---|---|---|
|A|16282/663|2.97/2.80/4.33|47.53/50.57/54.12|35.39/38.53/40.92|
|B|16282/663|8.19/4.41/23.00|53.70/54.42/74.31|35.44/38.52/41.88|
|C|16282/653|4.12/2.72/15.36|47.54/49.77/68.36|33.84/37.95/39.58|

14. CUDA/infra:

|Arm|CUDA|backend crash|GPU query timeout|residency mismatch samples|INFRA_ERROR|new/reused reviews|
|---|---:|---:|---:|---:|---:|---:|
|A|0|0|0|0|0|0/10|
|B|0|0|0|0|0|0/10|
|C|0|0|0|0|0|1/9|

Task別結果:

|Arm|Task|family|Host|review|prompt tokens|fit|API seconds|candidate SHA|
|---|---|---|---|---|---|---|---:|---|
|A|LS3W228-001|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1349]|True|2.73|fbe0b8869615cd5dfc9e41e32a6a3c9b1e773160741b9c6f85843fc684a3e27c|
|A|LS3W228-003|COLLECTION|ESCALATE (FORMAT_UNSUPPORTED_NORMALIZATION)|None|[1876]|True|4.19|e677719b680be5b6ad541fa78fa8e30ae1eb9879d1c56ddda15da337ef9773d6|
|A|LS3W228-004|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1034]|True|2.07|4c92f8a1a915bdb414fce295f52b6799dc291080831f575ef946544985d59111|
|A|LS3W228-007|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1325]|True|4.33|257a5cf9f891c634de82055fafd7434fd3452eed638e62fe3188b4ec865bd13b|
|A|LS3W228-009|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1358]|True|2.60|1656f054ea8e8cab027f9d3b216eee55b782a52051f5b29818b030294db0f809|
|A|LS3W228-011|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|REJECT|[950]|True|1.97|6a3ff02917ab358c6106ff3e6393d6024567458b9f9d36a06f7da064b347561a|
|A|LS3W228-014|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1648]|True|2.86|0e98c25776930d2f489da11d0268483bc39ff0323ab2128d876a487ef9b3949f|
|A|LS3W228-015|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1633]|True|3.30|6b19259c133443fd0ddc377888a59ec2d621ba67150527a1175aa38673a0bfaf|
|A|LS3W228-017|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1378]|True|2.61|07a4030c2abcf95abebdc63a862901dfa958f21d1c85cf0e72c1c7addac1badb|
|A|LS3W228-020|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1029]|True|2.51|486e31982db7295ae70e534bfdadbb986a8cc436c50881a8e85db91bca32e120|
|A|LS3W228-021|RECEIPT|ESCALATE (CODE_FAILURE)|None|[1334]|True|3.63|56776f5334cf558dfbbffa25b10748179989d7e71eef05e8e2bd9e6d74d0bde4|
|A|LS3W228-023|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1368]|True|2.88|c64f57e8fd857a4a531988de7fa5a12fc9056ab9317ca4ba472d4fcdd81a90e8|
|B|LS3W228-001|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1349]|True|2.87|fbe0b8869615cd5dfc9e41e32a6a3c9b1e773160741b9c6f85843fc684a3e27c|
|B|LS3W228-003|COLLECTION|ESCALATE (FORMAT_UNSUPPORTED_NORMALIZATION)|None|[1876]|True|4.08|e677719b680be5b6ad541fa78fa8e30ae1eb9879d1c56ddda15da337ef9773d6|
|B|LS3W228-004|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1034]|True|2.21|4c92f8a1a915bdb414fce295f52b6799dc291080831f575ef946544985d59111|
|B|LS3W228-007|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1325]|True|4.73|257a5cf9f891c634de82055fafd7434fd3452eed638e62fe3188b4ec865bd13b|
|B|LS3W228-009|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1358]|True|2.99|1656f054ea8e8cab027f9d3b216eee55b782a52051f5b29818b030294db0f809|
|B|LS3W228-011|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|REJECT|[950]|True|9.47|6a3ff02917ab358c6106ff3e6393d6024567458b9f9d36a06f7da064b347561a|
|B|LS3W228-014|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1648]|True|8.45|0e98c25776930d2f489da11d0268483bc39ff0323ab2128d876a487ef9b3949f|
|B|LS3W228-015|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1633]|True|16.83|6b19259c133443fd0ddc377888a59ec2d621ba67150527a1175aa38673a0bfaf|
|B|LS3W228-017|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1378]|True|23.00|07a4030c2abcf95abebdc63a862901dfa958f21d1c85cf0e72c1c7addac1badb|
|B|LS3W228-020|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1029]|True|16.75|486e31982db7295ae70e534bfdadbb986a8cc436c50881a8e85db91bca32e120|
|B|LS3W228-021|RECEIPT|ESCALATE (CODE_FAILURE)|None|[1334]|True|3.95|56776f5334cf558dfbbffa25b10748179989d7e71eef05e8e2bd9e6d74d0bde4|
|B|LS3W228-023|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1368]|True|2.92|c64f57e8fd857a4a531988de7fa5a12fc9056ab9317ca4ba472d4fcdd81a90e8|
|C|LS3W228-001|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1349]|True|6.50|fbe0b8869615cd5dfc9e41e32a6a3c9b1e773160741b9c6f85843fc684a3e27c|
|C|LS3W228-003|COLLECTION|ESCALATE (FORMAT_UNSUPPORTED_NORMALIZATION)|None|[1876]|True|3.55|5ac9ae8b4920c70e9181d2512060965c4462b5c958a8ec19d90e0f833a01164c|
|C|LS3W228-004|COLLECTION|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1034]|True|2.21|4c92f8a1a915bdb414fce295f52b6799dc291080831f575ef946544985d59111|
|C|LS3W228-007|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1325]|True|4.55|f2ca09d8f0e5a3539c4e5fe949af181e6a3d5f5a1d1ab9a9be374f94f57f031a|
|C|LS3W228-009|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1358]|True|15.36|1656f054ea8e8cab027f9d3b216eee55b782a52051f5b29818b030294db0f809|
|C|LS3W228-011|NUMERIC|PASS (TARGETED_CHECKS_PASSED)|REJECT|[950]|True|1.65|6a3ff02917ab358c6106ff3e6393d6024567458b9f9d36a06f7da064b347561a|
|C|LS3W228-014|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1648]|True|2.55|0e98c25776930d2f489da11d0268483bc39ff0323ab2128d876a487ef9b3949f|
|C|LS3W228-015|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1633]|True|2.90|6b19259c133443fd0ddc377888a59ec2d621ba67150527a1175aa38673a0bfaf|
|C|LS3W228-017|ADAPTER|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1378]|True|2.29|07a4030c2abcf95abebdc63a862901dfa958f21d1c85cf0e72c1c7addac1badb|
|C|LS3W228-020|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1029]|True|2.29|486e31982db7295ae70e534bfdadbb986a8cc436c50881a8e85db91bca32e120|
|C|LS3W228-021|RECEIPT|ESCALATE (CODE_FAILURE)|None|[1334]|True|3.09|56776f5334cf558dfbbffa25b10748179989d7e71eef05e8e2bd9e6d74d0bde4|
|C|LS3W228-023|RECEIPT|PASS (TARGETED_CHECKS_PASSED)|ACCEPT_NO_CHANGE|[1368]|True|2.55|c64f57e8fd857a4a531988de7fa5a12fc9056ab9317ca4ba472d4fcdd81a90e8|

15. Arm comparison:
A/B: output identical 12/12、品質regression=[]、A採用context不適格=[]。
A/C: output identical 10/12、品質regression=[]、A採用context不適格=[]。

16. Recommended config: **TEST_4096_NEXT**。全Arm完了前は推薦未確定。production採用なし。
17. Whether 4096 should be tested: **TEST_4096_NEXT**。提案のみ、4096 generation実行なし。
18. Limitations: 12既存business fixtures、1 attempt/Task/config、Arm順序固定、resident全GPU使用量にはdesktop等も含まれる。約1秒samplingは瞬間peakを逃す可能性。p95は小標本nearest rank。
Context logsはrequest interval単位でbackendが独立request SHAを出さないため厳密な帰属はできない。原prompt token countを推定せず、cache fieldはnative値/nullを保持。
過去24 Task 20/24採用・42.72% credits削減はhistoricalのみ。本実験ではclean fallbackやCodex経済workflow再測定なし。設定間差から一般能力ランキングは作らない。
19. Decision: **TEST_4096_NEXT**。未開始ArmはNOT_RUN。自動restart/retry/rebootなし。

raw証跡: arms/{A,B,C}/、全事前freeze: FREEZE.json、詳細集計: summaries/、GPU CSV: このrevision配下。
official mechanisms: Ollama FAQ（元資料: http[LOCAL_PATH]） / Ollama API（元資料: http[LOCAL_PATH]）。

## 追加のprovenanceと安全性注記

本報告のprimary値・判定は事前freezeしたsummarize.pyのままです。allocation/background補足（元資料: analysis/ABC_ENVIRONMENT_ALLOCATION_JA.md）は実測の背景負荷差、CLI CPU/GPU表示割合の低下警告、main/draft cache sharing、12組のexact request比較を記録しています。
CのCLI GPU表示割合低下にはMEMORY_SHIFTED_TO_CPU警告を付けています。backend layers/model buffersは不変のため、CPUへのweight移動の有無はこれだけでは断定できません。
初期memory run-001ではTask generation0のままHost startup capture I/Oとproof-parser表記の問題でSTOPしました。旧STOP/applied=false/元FREEZEは変更せず、run-002に起動前補正をfreezeし、既にfresh・empty preloadのみだった同一A processをhash付きprovenance（元資料: arms/A/FRESH_BOUNDARY_PROVENANCE.json）で引き継ぎました。Host問題をCUDAやmodel能力FAILに数えていません。B/Cはそれぞれ新しいuser tray Quitから独立fresh開始しています。
run-002のCでは4候補目007の新規review送信前に旧family helperのTask ID/path bindingでHost STOPしました。旧STOP/SESSION_EXCEPTION/全rawをimmutable external manifestで保持し、run-003だけでexperiment専用の送信境界を補正しました。review prompt/schema/modelは同一で、007のpacketは旧送信予定packetとexact hash一致です。Cの4候補を再生成せず、残る8件のみ新規生成しています。旧STOPを削除・成功扱いせず、CUDA/model失敗にも含めていません。
run-003の007初回reviewはACCEPT_NO_CHANGEでしたが、009はコピーされたcohort manifestのabsolute root mismatchでAPI前にCOHORT_CHANGED停止（calls=[]、edit_generations=0）しました。旧STOPと誤解を招くLocal_attempted=trueも書き換えず保全しています。run-004ではcohort.root/tasks[].spec_pathだけを新copyへrebind・freezeし、その他のcontract/source hashes/reference/model/options/validation完全一致、実C rootに対するnative Cohort全12件およびstale root拒否を確認しました。007のreviewは再送信・再課金せず、009を含む未生成8件だけを実行しました。
Cは同一user-fresh frontendを維持しましたが、Host補正待ち中にmodel residencyが空になっていた状態を保存し、その後の通常loadを含みます。連続residentを中断なしに12件完走したデータではありません。このpauseとbackground GPUの差を因果的比較の制限として扱います。Host境界のpositive/negative検証（11 reject、CLI/generation 0）と36 Worker no-generation検証を新freeze前に完了しています。
36 API-boundary no-generation checks、Worker275 testsおよびRust fmt/clippy/test/check/buildはPASS。追加inference後もproduction/runtimeと旧全artifact hashesを監査します。production採用・4096 inference・clean fallback・経済再測定は行っていません。

最終監査はFINAL_PRESERVATION.json（元資料: FINAL_PRESERVATION.json）でPASSしました。36 Task/configにそれぞれcandidate generation1回・repair0、旧runと全seals/production hashesの不変を確認しています。Cのpause後の009通常reloadでもcontext6144/FA有効/main q8_0/main31/31・draft5/5をraw logで再確認しました。
現在のOllama frontendは実験Cのprocess-only KV=q8_0環境を保持しています。production profileは8192のままで、OS/user environmentは変更していません。通常運用へ戻す際はユーザーのtray Quit後に通常起動してください。今回自動restartは行いません。詳細はEXPERIMENT_EXIT_STATE.json（元資料: EXPERIMENT_EXIT_STATE.json）です。
