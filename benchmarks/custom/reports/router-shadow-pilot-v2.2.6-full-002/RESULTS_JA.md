> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.6-full-002.md). This report alone does not establish a task result.

# bounded 2.2.6 Full Shadow Pilot — Terminal Coverage Run

判定: **CONTINUE_LIMITED_SHADOW**。

最優先KPIの**Local terminal coverage 13/13（100%）**を達成。**未実行0、cohort_completed=true、cohort STOP 0**。
Local First/final PASS・ACCEPT_NO_CHANGEはいずれも**8/13（61.54%）**。残り5件は失敗のままTask-localに隔離された。**FALSE_GREEN 0、Codex repair 0件/0 LOC、Host/scope failure 0、INFRA/CUDA 0**。

旧cohortへ結果を混ぜていない。最初の準備runはOllama自動更新でinference前にSTOPし、その後ユーザーが0.35.1での実行を承認。本報告は別run **`router-shadow-pilot-v2.2.6-full-002`** の実測。初回のpreflight STOP（元資料: ../router-shadow-pilot-v2.2.6-full/STOP.json）と報告（元資料: ../router-shadow-pilot-v2.2.6-full/RESULTS_JA.md）はcommit `e114bfb` で保持した。

## 1. Fresh environment

ユーザーのtray Quit後、frontend/backend不在・11434拒否・API不応答・GPU正常を確認し、同じinstalled Ollamaを起動した。アプリ内蔵updaterが保留済み0.35.1を適用したため、その時点のrunは0/13で停止した。driverやruntimeの手動変更・ダウングレードはしていない。

ユーザーの「バージョン差はあまり気にせず実行してください」という承認後、更新後frontendが**推論未使用・models=[]・backend不在**であることを再確認し、追加Quit/restartなしで利用。承認（元資料: user-environment-authorization.json）、fresh gate（元資料: infrastructure/fresh-start-001.json）。

| 項目 | 今回固定した値 |
| --- | --- |
| Ollama | 0.35.1 |
| frontend PID / 起動 UTC | 50980 / 2026-10-03T15:05:50.5416070Z |
| GPU / driver | NVIDIA GeForce RTX 3080 / 591.86 |
| Gemma26 digest | 08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68 |
| CoderNext digest | ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074 |
| profile | bounded_v2_2 2.2.6 |
| context / output / char gate | 8192 / 2048 / 24000 |
| temperature / seed | 0 / 20260926 |
| formatter | rustfmt 1.9.0-stable (48a229ceae 2026-09-01)、既存SHA/config |

正確な両digest・formatter identity・generation optionsはenvironment freeze（元資料: environment/freeze.json）、runtime/profile/registryとcohort入力463ファイルはexecution freeze（元資料: freeze.json）で固定。Gemma12禁止、Qwen14/fallbackなし。Task間restart/unloadなし。Ollama版が過去runと異なるため、結果差を2.2.6だけの因果とは主張しない。

## 2. Task一覧

元P224-001〜014のTask JSON14件と325 input filesをbyte-identicalに再利用。変更はcohort root/spec保存pathと既に統合済みruntime revisionのbindingのみ。再利用照合（元資料: reuse-verification.json）。

| Task | 業務 | group | Local結果の要点 | Codex review |
| --- | --- | --- | --- | --- |
| P224-001 | CLI telemetryを改行しないescaped一行として表示 | fixed_slot | syntax ×2 → REJECT | REJECT |
| P224-002 | memory evidenceにused KiBを独立した第2要素として追加 | stateful | 初回PASS | ACCEPT_NO_CHANGE |
| P224-003 | TCP inventoryが非data行の01を誤countする不具合 | debugging | LF欠落、apply 0 | REJECT |
| P224-004 | CLIのused memory量を妥当性検査付きで表示 | fixed_slot | 初回PASS | ACCEPT_NO_CHANGE |
| P224-005 | MockObserverのnested snapshot値をtyped抽出 | reasoning | 初回PASS | ACCEPT_NO_CHANGE |
| P224-006 | 正常系auditへprocess sampleのcomplete/bounded区別を追加 | stateful | 初回PASS | ACCEPT_NO_CHANGE |
| P224-007 | VmRSSの値parse失敗へ診断prefixを付与 | fixed_slot | 初回PASS | ACCEPT_NO_CHANGE |
| P224-008 | HighLoad evidenceへ観測timestampを第2要素で追加 | stateful | 初回PASS | ACCEPT_NO_CHANGE |
| P224-009 | mock report reasonへ安定したevent kind labelを表示 | fixed_slot | Clippy spanがeligible外 | REJECT |
| P224-010 | skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示 | stateful | semantic repair後Clippy残存 | REJECT |
| P224-011 | CLI warning overviewのstable unique preview | fixed_slot | 初回PASS | ACCEPT_NO_CHANGE |
| P224-012 | meminfo重複診断へMemTotal/MemAvailableの名前を付加 | stateful | LF欠落、apply 0 | REJECT |
| P224-014 | CLI per-CPU loadの欠測/非有限値と小数表示 | fixed_slot | 初回PASS | ACCEPT_NO_CHANGE |
| P224-013 | Telemetry欠測UIの表示方針 | Codex boundary | CODEX_ONLY | Local分母外 |

## 3. Execution order

**001→002→003→004→005→006→007→008→009→010→011→012→014**。指定順を維持し、001/003も除外しなかった。run history（元資料: run-history.json）。013はRouter判断を再照合したCODEX_ONLY境界（元資料: boundary/P224-013.json）、Local generation0。

## 4. Terminal coverage

**13 / 13 = 100%、未実行0**。Local PASS8、Local ESCALATE5。ESCALATE5件のCodex reviewはREJECT。モデル失敗をPASSへ書き換えてcoverageを得たのではない。
terminal taxonomy（元資料: metrics/terminal-taxonomy.json）に各terminal・後続継続・apply/mutationを保存。

## 5. Cohort completion

**cohort_completed=true**。同一frontend・固定条件の1回のcohortとして完走。cohort STOP/ABORTなし。初回preflight STOPは別runのまま保全し、本runの完走によって消していない。

## 6. ACCEPT_NO_CHANGE

**8 / dispatched13 = 61.54%**。ACCEPT_WITH_MINOR_FIX0、REJECT5、FALSE_GREEN0。
全Taskをbrief diff/固定checks/summaryでreviewし、Local resultを変更していない。モデルとの全会話は通常reviewに使用せず、005のprotected source事実と009の保存済みeligibility metadataを補足確認した。

## 7. First / final PASS

First PASS **8/13**、final PASS **8/13**。いずれもdispatched全件を分母にしてbody契約失敗も含める。初回validation/syntax評価がある11件に限った補助First PASSは8/11（72.73%）だが、主要品質指標の分母とは分ける。
repair実施2件の最終回復は0/2。010にはcompile/acceptanceの部分回復があったがfinal PASSとは数えない。

## 8. Syntax failure

001はRust E0762を初回とrepair後の2回検出。same-model syntax repair1回を消費し、Task-local REJECT。002へ継続。formatter integrityやinfra失敗とは分類していない。syntax failure **1 Task / 2 attempts**。

## 9. Generation contract failure

**003（CoderNext/fixed）と012（Gemma26/stateful）の2件**。自然なrequired final-LF欠落を検出。両方ともapply attempted/succeeded0、candidate source mutation0、final diff0 bytes、Host verification PASS、repair0。before/after content IDも一致。Hostによる改行追加なし。
003→004、012→014へ継続し、body契約不備をcohort-wide STOPへ昇格しなかった。両候補のsemantic品質は未検証。

## 10. Semantic repair

010の初回は`events`を参照してcompile失敗。Hostが実diagnosticsを直接返し、Gemma26が`event.evidence`へ修復した。repair後はacceptance・regression・fmt・workspace test/check/build・scopeがPASSしたが、Clippyだけ残存。final reasonは既存の`VALIDATION_FAILURE`、Task-local REJECT。
semantic repair1、final回復0。Codexがretry promptや正解patchを供給していない。

## 11. Lint repair

自然な `clippy::useless_conversion` は009/010の2件で観測。**eligible0、lint repair invoked0、recovery N/A**。
009は他checks PASSでも、保存assessmentが `noncontiguous primary source span` と判定しfail closed。010はsemantic repairでglobal budget1を使用済み。2回目のlint repairを追加しなかった。
これは今回のpolicy条件下の未回復例であり、以前のallowlisted repair成功率を否定/更新する同一実験ではない。allowlist/renderer/parser/prompt変更なし。

## 12. Formatter unsupported

FORMAT_UNSUPPORTED_NORMALIZATION0、FORMAT_INTEGRITY_FAILURE0、HOST_FORMAT_ERROR0。
method-chain whitespace **3 attempts受理**、限定std vec trailing comma **1 attempt受理**。closure normalizationは今回自然発生0であり、liveで再測定したとは言わない。Host formatting **49 LOC**をモデルapply/Codex repairと分離した。format records（元資料: metrics/format-normalizations.json）。

## 13. Fixed-slot

通常fixed（DEBUGGING除外）: planned/terminal **6/6**、First/final PASS **4/6**、ACCEPT_NO_CHANGE **4/6**、repair1、REJECT2。
DEBUGGINGを含む全fixedはplanned/terminal7/7、PASS/ACN4/7、REJECT3。部門別表で003を重複加算しない。

## 14. Stateful

planned/terminal **5/5**。全5件がDISCOVERYでissued handle取得→EDITへの供給まで到達。初回/final PASS・ACN **3/5**、semantic repair1、REJECT2。
replace呼出し6回に対し、bounded handle apply成功5回。残り1回は012のbody LF違反で未適用。invalid/stale/foreign handle、unsafe fuzzy applyはいずれも0。handle選択の正当性とbody契約成功を混ぜない。

## 15. Debugging

CoderNext003を実モデルで必ず測定し、body契約REJECTを保存した。ACN0/1、apply0、coding品質未評価。後続へ継続した事実は確認できたが、DEBUGGING実装品質が十分とは判断できない。Router/model selectionは変更していない。

## 16. Reasoning

005はGemma26でtyped extractionを初回PASS。observed_unix_ms=1、logical_cpus=4、available_kib=50、process_count=1、processes_truncated=false、service_count_present=falseをprotected MockObserverと照合。JSON成立だけでなく全6semantic assertionsとscopeがPASS。source diffなし。

## 17. References

code12 Taskのfinite ReferencePlan/direct-helper completeness **12/12 PASS**。初回reference countは0〜3、packet bytesは246〜2840、repairを含むpacket総bytes **13907**。packetにはbody等のenvelopeも含む。reference部分だけの入力token数はnull。
010でreferenceがあっても誤った複数形identifierを生成した。completeness gateは生成の正しさを保証するものではない。自由なread/search/path/shell権限は追加していない。

## 18. Context / repair transport

21 actual chat calls、**input36,243 / output2,024 tokens**。全HTTP200、done=true、done_reason=stop。OUTPUT_LIMIT/context gate failure0。Task log13/13はNO_TRUNCATION_EVIDENCE。

| Repair | chars | bytes | prompt_eval | cached | eval | server truncated |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 001 syntax | 9947 | 10235 | 3190 | 872 | 135 | 0 |
| 010 semantic | 21336 | 21941 | 8066 | 2428 | 108 | 0 |

010は大きいrepair requestだが、budgetを変更せず処理した。prompt_eval_countだけで元prompt全量保持を断定せず、server証跡と生成後validationを併記する。最終lint failureはcontext transport失敗へ付け替えない。
exact request SHA、serialized chars/bytes、raw response、cached counts、durationはrequest index（元資料: metrics/request-index.json）、truncation evidence（元資料: metrics/truncation.json）。

## 19. Validation

Host mandatory結果 **82件 / 357.875秒**（001のsyntax preflight2件は別）。PASS全8件で全required check実行・scope/hash/freezeを監査。reasoningはstructured+scope2件、codeは各cycle8件。zero-test guard維持。
開始前の同一runtimeで**Worker233 tests、Rust fmt/clippy/test/check/buildが全PASS**。fresh continuity negative4 testsもPASS。0.35.1承認後もruntime bytes同一のため、同turnのoffline結果を再利用した。regression reuse（元資料: regression/reuse.json）。同じsuiteを再実行したとは報告しない。

## 20. Infrastructure

本runで **INFRA_ERROR0 / CUDA0 / shared Host STOP0**。frontend PID50980と起動時刻、GPU/driver/API版はcohort境界を通して同一。read-only continuity全PASS、GPU query timeout0、residency mismatch0。GPU snapshot使用量は1800〜9866 MiB。
Task境界のfrontend ageは約617〜1333秒。inference index1〜21、model switching2回、観測backend PID3個（8904/50444/51888）。これは境界観測のlaunch下限値で、未観測の短命process数を推測しない。telemetry（元資料: metrics/frontend-inference-telemetry.json）。
cohort期間の関連Windows Event Logは取得可能、該当0。events（元資料: infrastructure/final-events.json）。Task間restart/forced unload/generation probeなし。初回preflightの自動updateは別incidentとして残る。

## 21. Codex intervention / LOC

code repair **0件**、changed files[]、added/deleted LOC **0/0**。5件の失敗は未解決で残し、レビューによる採用可否だけ記録。修正しなかったことを「必要な修正工数がゼロ」とは解釈しない。
planning / normal review / failure analysis / code repair / protocol-infra analysisをworkload（元資料: metrics/codex-workload.json）で分離。exact tokens/active secondsはnull。レビュー開始〜記録のwall timeは他Task実行/待機を含み、active review時間とは異なる。

## 22. Host workload

Coverage criteria:全14 Task112（うちLocal110）。Host mandatory定義は境界込み86、live実行結果82。ReferencePlan設計とred/static証跡は過去の再利用、今回実測と混ぜない。
Host formatting49 LOC、Task-local unsupported0。review packet合計145,058 bytes、中央値11,188 bytes。これは保存packetのサイズでありCodex実入力token数ではない。005 protected source、009 eligibility metadataの補足確認も別記録した。
Worker時間 **715.017秒**、Ollama reported duration合計 **227.696秒**、cohort wall **761.172秒（約12.7分）**。planning/報告作成はcohort wallに含まれない。net Codex節約量はnull。

## 23. Failure taxonomy

| 最終分類 | Task数 | 内容 |
| --- | ---: | --- |
| PASS | 8 | 002/004/005/006/007/008/011/014 |
| MODEL_SYNTAX | 1 | 001、repair後もsyntax failure |
| GENERATION_CONTRACT | 2 | 003/012、LF欠落・apply0 |
| LINT | 2 | 009未eligible、010はrepair後lint残存 |
| MODEL_SEMANTIC | 0 final / 1 initial | 010の初回compile failure、部分回復あり |
| FORMAT_UNSUPPORTED / TASK_DESIGN | 0 / 0 | 該当なし |
| CAPABILITY/SCOPE / HOST_INTEGRITY | 0 / 0 | 該当なし |
| INFRASTRUCTURE / CONTEXT_OUTPUT_BUDGET | 0 / 0 | 本runでは該当なし |

taxonomyは保存resultからの分析view。010のraw reason `VALIDATION_FAILURE` をLINTへ書き換えていない。final分類と途中のfailure episodeを分離する。

## 24. Expansion judgement

**CONTINUE_LIMITED_SHADOW**。
13/13 terminal・cohort completion・全protocol群の実測・安全指標は達成。ACCEPT_NO_CHANGE61.54%は限定運用継続の参考範囲だが、拡大の75%に届かない。20〜30 Taskへ自動拡大しない。
残り5件はTask-local品質/契約失敗であり、今回の証拠からProtocol revisionとは判定しない。特にdebuggingは未適用REJECTで、品質の適用範囲を広げない。Codexが短いreviewで採用できたのは8件で、他5件の後続処理工数は残る。

## 25. 結論

001と003の失敗を含む同じTask集合で、**失敗を残したまま13件すべてを測定できた**。012でもstateful body拒否後に継続できた。今回の主目的であるterminal coverageは完了。
Router/Operational Policy/profile/runtime/formatter/repair/contextは無変更。既存17566 tracked filesのbytesを全照合し、旧CUDA・STOP・分類検証・今回最初のpreflight STOPも保全した。監査（元資料: metrics/audit.json）。
Local生成はここで停止。元applicationへ採用せず、追加micro experimentや次Pilotは開始していない。
