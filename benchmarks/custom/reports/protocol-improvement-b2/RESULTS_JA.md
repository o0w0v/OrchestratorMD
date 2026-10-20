> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/protocol-improvement-b2.md). This report alone does not establish a task result.

# Protocol Improvement Experiment B2 — 結果

2026-09-29 JST。**採用判定はINCONCLUSIVE。** 5 Taskを実行し、ACCEPT_NO_CHANGEは2/5、FALSE_GREENは0件だった。Coverage Gateと既知位置のfixed_slotは有望だが、region-bound agenticは3件とも未発行IDで停止し、実モデルによるread → handle → applyの成功を確認できなかった。

Router v2.1、Operational Policy、model routing、Gemma12 quarantine、CoderNext/Qwen14 status、application、過去artifactは不変。全generationはGemma26のみ。今回の結果を受けたAPI修正、再実行、v2.2への反映、Pilot再開は行っていない。

## 1. 目的

Hostがcheckを全実行することに加え、Taskの各受入条件をdeterministic checkへ対応付け、coverage不足をdispatch前に止める。また、探索が必要な編集ではモデルによるold text再入力をなくし、Hostが発行・検証するregion handleで編集先を特定する。

plan.json（元資料: plan.json）・freeze.json（元資料: freeze.json）に5 Task、40受入条件、source、check順、harness、model/options、採用基準を実行前に固定した。固定commitは`8981159`、親commitは`d9c485c`。実行中に条件は変更していない。

## 2. 前回Bの問題

前回B-001は、全mandatory checksとworkspace testsがPASSしても、明示された「引数なしのhelpを維持する」という契約を破壊していた。Local PASSを最終レビューが拒否したFALSE_GREENだった。B-003はモデルが送るold textが編集bodyに一致せず停止した。

今回、前回B-001の保存済みcandidateを新しい検証用コピーで再検査した。`--help`と新helpはPASSする一方、独立したno-args checkはFAILし、以前のcoverage gapを検出できた。新しいinferenceや旧artifactの修正は行っていない。証跡（元資料: preflight/historical-false-green-recheck.json）

## 3. Coverage Gate

各criterionについて、ID、本文、check IDs、check type、positive/negative、利用可能なmutationをcoverage（元資料: coverage/）に保存した。gateはcriterionの完全一致、非空mapping、check存在/type、機能条件へのtest対応、Rust test宣言とsource hash、必須のsource/Git guardを確認する。

coverage不足は`TASK_DESIGN_FAILURE / VALIDATION_COVERAGE_INCOMPLETE`。オフラインcanaryでcriterion未対応・行欠落・機能条件をlintだけへ対応・test binding欠落を拒否した。実際のruntime入口を使った不足canaryでは**全API呼び出し0回**を確認した。canaryは5 live Tasksの分母に含めていない。

5 Taskすべて、40/40条件のmapping gateを通過。goldenで全固定checksがPASSし、19/19の意図的な誤変更を対応するassertionが検出した。ただしmappingが完全でも、semanticなテスト網羅性を数学的に保証するものではない。最終レビューは維持する。

## 4. Region-bound editing

APIは`replace_region(region_id, replacement)`。path、old text、marker、check名、argvをモデルから受け取らない。read/search時にHostがsource/body hash、file、start/end identity、行範囲、current contentと周辺contextを返す。handleは発行時snapshotへ結び付け、apply時にdisk/file/body一致を確認する。fuzzy applyは行わない。

オフラインでは有効handleによる編集、編集後の古いhandle拒否、disk変更の検出、未知ID、marker注入、schema違反、Host側I/O障害を区別できた。固定slotもrequestごとのsnapshotとapply対応を保存する。

**liveではagenticの3件ともread/searchを行わず、最初にreplace_regionを選択した。** Hostは未発行IDを拒否し、sourceは変更されなかった。安全境界は維持できたが、live region reads=0、region applies=0のため、実モデルでの成功経路は未確認である。

## 5. Task一覧とProtocol

| run | 単一責務 | Protocol | 過去との対応 |
| --- | --- | --- | --- |
| B2-001 | inspect --help追加と既存CLI挙動維持 | fixed_slot | PILOT-005 / 前回B-001 |
| B2-002 | memory evidenceにavailable_percent追加 | fixed_slot | PILOT-004 / 前回B-002 |
| B2-003 | HighLoad evidenceにCPU当たり比率追加 | region-bound agentic | 前回B-003 |
| B2-004 | anomaly-free audit summaryにprocess件数追加 | region-bound agentic | 新規repo Task |
| B2-005 | reusable skill reasonに現在のevent target追加 | region-bound agentic | 新規repo Task |

既に場所が確定した元2 Taskはfixed_slotへ変更した。残りは候補component内のsource探索をモデルに残した。元3 Taskはgoal/interfaceと旧source filesがbyte-identicalで、checksを追加・明示した。同一request・単一変数だけの比較とは扱わない。

## 6. Taskごとのcoverage

| run | 独立した機能check | その他の必須check | 条件数 | preflight mutant |
| --- | --- | --- | ---: | ---: |
| B2-001 | no args、--help、新help、不正/重複引数、既存demo-repeat | regression、format、clippy、host_scope | 9 | 5/5検出 |
| B2-002 | percent表示、event identity、閾値/zero/u64境界、既存HighLoad | 同上 | 8 | 3/3検出 |
| B2-003 | load比率、event identity、閾値/非有限値、memory event順序 | 同上 | 8 | 4/4検出 |
| B2-004 | reasonの件数、snapshot/record保持、既存anomaly経路、不正intent | 同上 | 8 | 4/4検出 |
| B2-005 | reasonのtarget、proposal/evidence保持、非対応intent | 同上 | 7 | 3/3検出 |

実行順はacceptance-specific → targeted regression → format → clippy。source/Git guardは各check前後で検証し、成功cycleでは`host_scope`として記録した。binding先のtest ID、source hash、polarity、mutation名は各coverage JSON（元資料: coverage/）から確認できる。

## 7. Local結果

| run | 初回 | 最終Local | final review | configured checks実行 | input/output tokens | Worker秒 |
| --- | --- | --- | --- | --- | ---: | ---: |
| B2-001 | PASS | PASS | ACCEPT_NO_CHANGE | 9/9 | 585 / 85 | 59.313 |
| B2-002 | PASS | PASS | ACCEPT_NO_CHANGE | 8/8 | 670 / 222 | 36.829 |
| B2-003 | 編集前停止 | ESCALATE / INVALID_REGION_ID | REJECT | 未実行 | 570 / 105 | 3.953 |
| B2-004 | 編集前停止 | ESCALATE / INVALID_REGION_ID | REJECT | 未実行 | 575 / 325 | 9.859 |
| B2-005 | 編集前停止 | ESCALATE / INVALID_REGION_ID | REJECT | 未実行 | 543 / 108 | 4.125 |

全5 Taskを完了しcohort STOPはなし。編集が適用された2 Taskでは合計17/17 checksが実行され、PASSした。残り3件を「validation成功」とは扱わない。コードが適用・評価されていないため、coding能力の失敗と断定せずProtocol interaction失敗として記録する。Task完了率の分母には含める。

## 8. Repair

live repairは0件。2候補は初回で全checksを通過し、3件は編集前のID拒否で終了した。したがってrepair recoveryは**N/A（分母0）**であり、改善・悪化の証拠はない。

オフラインruntimeテストでは、failed criterion/check・診断・diff・fresh regionを返し、Bの会話履歴を保持したまま1回だけrepairし、Hostが再度全checksを実行することを確認した。Aのfresh compact packetは使用していない。num_ctx=8192、num_predict=2048、24,000 message文字上限は維持し、context/output limitは今回0件だった。

## 9. ACCEPT_NO_CHANGE

First PASS、Local final PASS、ACCEPT_NO_CHANGEはいずれも**2/5（40%）**。既知位置のfixed_slotでは2/2、region-bound agenticでは0/3だった。ACCEPT_WITH_MINOR_FIX / MAJOR_FIXは0、REJECTとWorker escalationは3件。

B2-001はif条件への最小追加で引数なし/global helpを維持。B2-002は閾値とevent identityを保ったpercent追加で、冗長なzero-total fallbackはあるが修正が必要な挙動差はなかった。両候補とも別途workspace regressionを通過し、candidate source bytesが不変であることを確認した。

## 10. FALSE_GREEN

定義は「Local PASS + 全configured validation PASS + 明示契約違反による最終REJECT」。今回は**0件、Local PASSを分母にすると0/2**。前回FALSE_GREENだった同じCLI Taskは今回ACCEPT_NO_CHANGEとなった。

これは小標本の観測であり、今後もFALSE_GREENが発生しない保証ではない。coverage gateの完全mappingとsemanticな妥当性を区別し、全Taskで最終レビューを続ける。

## 11. TEST_NOT_ALLOWED

**0件。** モデルにcheck選択operationを公開せず、必須checksはHostが固定argvと順序で実行した。model-requested checksも0件。optional checksや任意shellは追加していない。

## 12. Scope failuresとAPIの課題

| 分類 | live件数 |
| --- | ---: |
| SCOPE_VIOLATION_MODEL | 0 |
| STALE_EDIT_REGION | 0 |
| INVALID_REGION_ID | **3** |
| PATCH_SCHEMA_ERROR | 0 |
| HOST_SCOPE_ERROR | 0 |

送信されたIDはB2-003で`load_evidence`、B2-004で`crates/ncos-agent/src/lib.rs:audit_summary`、B2-005で`skill_reason`。いずれも発行済みcapabilityではない。通常のcandidate reviewとは別に、保存済みtool名とIDだけを抽出して確認した。診断（元資料: metrics/region-interaction-diagnostic.json）

**今回のHost APIにも設計上の不足がある。** 初回schemaで未発行でもreplace_regionを選べ、region_idが自由文字列だった。また初回のlegacy contextには内部region名が残っていた。モデルがその名前をIDとして使ったことは観測できるが、名前の提示だけが原因とは断定しない。

Hostは誤った編集を拒否したものの、「readしてから正しいIDを送る」という手順をモデルの選択に残している。次の独立実験では、未発行時は編集toolを公開せず、発行後はIDを発行済みhandleのenumに制限する、またはHostが先に必要snapshotを供給する設計を候補とする。内部marker名をhandleと混同させるcontextも除く。今回のfrozen harnessには後付けしていない。

## 13. Codex介入・token・時間

通常のrepair loopへのCodex参加0、candidateの手動修正0件・**0 LOC**。ただし3 Taskは未完了のままREJECTしているため、0 LOCを修正作業の削減量と解釈しない。最終レビューではTask Spec、Coverage Matrix、diff、validation、short summaryを読み、全Local会話は読んでいない。

5 generation calls合計のOllama reported inputは2,943、outputは845 tokens。Worker合計114.079秒、START〜ENDは117.982秒。設計・preflight・最終レビュー・報告作成時間は含まない。正確なCodex planning/review/repair tokensとactive review時間は取得不能のためnull。節約token数を推定していない。

## 14. Infrastructure・事前検証・保全

モデルは`gemma4:26b`のみ。digest `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`、temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=false。Ollama 0.34.4、RTX 3080 10GB、driver 591.86。

INFRA_ERROR / CUDA / GPU query timeout / residency mismatchはすべて0。12件のbaseline・Task前後・final snapshotを保存した。snapshot時GPU使用量は1,720〜9,844 MiBで、実行中peakや長期故障率は推定しない。generation probe、強制unload、restart、download、version/driver/runtime変更は0。

最終オフライン境界テスト10件、既存Python 77件、Rust fmt/clippy/workspace test/locked check/buildはPASS。preflightのmutation定義がsourceに一致しなかった準備エラー1件は、実sourceのu128比較に合わせてfreeze前に修正し証跡を残した。live Taskやモデルの失敗数へは含めない。

164固定入力と元5,586 tracked filesのSHA256を実行前後に検証。過去結果、A compact packet、C evidence wrapper、Router、registry、applicationは変更していない。保全監査（元資料: metrics/integrity.json）

## 15. Paired historical comparison

| 同じbusiness Task | 旧Router v2.1 | 前回Protocol B | 今回B2 |
| --- | --- | --- | --- |
| PILOT-005 / inspect help | TEST_NOT_ALLOWED → Codex 2 LOC修正、ACCEPT_WITH_MINOR_FIX | Local PASSだが空引数契約違反、FALSE_GREEN / REJECT | fixed_slot初回PASS、ACCEPT_NO_CHANGE、0 LOC |
| PILOT-004 / memory percent | agentic初回PASS、ACCEPT_NO_CHANGE | format repair後PASS、ACCEPT_NO_CHANGE | fixed_slot初回PASS、ACCEPT_NO_CHANGE |
| load ratio / 前回B-003 | 該当なし | old-text不一致、SCOPE_VIOLATION | 未発行ID、INVALID_REGION_ID |

対応する旧source files、goal、interfaceの一致を確認した。比較JSON（元資料: metrics/historical-comparison.json）。ただし元2 Taskはfixed_slotへ変更し、coverage checksも拡充しているため、CLI改善をCoverage Gate単独の効果とは主張できない。新規2 Taskを過去の分母に混ぜた成功率比較もしない。

## 16. v2.2採用可否

**INCONCLUSIVE。B2全体の採用は保留する。** FALSE_GREEN=0、TEST_NOT_ALLOWED=0、coverage gateのdispatch前拒否、安全なID拒否は確認できた。しかし実モデルによるregion handle取得・適用の成功が0件で、必要な経路の安定運用を示せていない。

Coverage GateとHost mandatory validationは有望な構成要素であり、既知位置のfixed_slotを対象とした限定的な追試候補とする。region APIは上記の状態に応じたtool公開・ID制約を別cohortで検証してから判断する。採用判定（元資料: metrics/adoption-decision.json）

## 17. 次の課題

次の実験ではHostが「現在利用可能な操作」と「発行済みの編集先」をschemaで制限し、readの省略や任意ID生成を選べないinterfaceを検証する。編集成功後のcriterion失敗→same-model repairも実測し、今回未測定だった回復経路を確認する。

semanticなcoverage不足を見逃さないよう、対応表だけでなく保存済み失敗candidate・golden・mutationで検証する運用は残す。モデル変更、Aのcompact reset、Cのfact extractionを混ぜず、今回の成功・失敗を上書きせずに別cohortを固定する。今回からRouter/Pilotを自動変更・再開することはない。

成果物: Task specs（元資料: tasks/）、Coverage（元資料: coverage/）、Raw results（元資料: results/）、Diffs（元資料: diffs/）、Reviews（元資料: reviews/）、Task metrics（元資料: metrics/task-metrics.json）、CSV（元資料: metrics/task-metrics.csv）、Request/response index（元資料: metrics/request-index.json）、集計（元資料: metrics/summary.json）。
