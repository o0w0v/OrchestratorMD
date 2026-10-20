> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-v2.2.6-body-contract--offline.md). This report alone does not establish a task result.

# bounded profile 2.2.6 Pre-Apply Body Contract / Scope Failure Classification

判定: **READY_FOR_FULL_SHADOW_PILOT_RETRY**。

保存済みP224-003を、source未変更・apply 0を検証して`GENERATION_CONTRACT_FAILURE`へ分類できた。独立liveでもCoderNextの末尾改行欠落が自然発生し、**Task-local REJECT → 次Task継続 → fixed/stateful controlとも初回PASS**を確認した。

liveは**3/3 terminal、cohort STOP 0、ACCEPT_NO_CHANGE 2/3、FALSE_GREEN 0、Host/scope failure 0、INFRA/CUDA 0**。body契約失敗TaskをPASSへ変えたわけではなく、安全に拒否したまま後続を測定できるようにした。Full Shadow Pilot自体は開始していない。

## 1. 目的と変更範囲

旧2.2.5のP224-003はJSON schema valid / HTTP200にもかかわらず、body末尾LF欠落が`GENERATION_FAILED → EDIT_SCHEMA_ERROR → scope → cohort STOP`となった。今回はこの適用前body不備を、capability違反・共有integrity破損から分離した。

変更はbounded profile **2.2.6**の分類、未適用proof、関連metrics。実装commit **46821b2**。
Router/Operational Policy/モデル選択/Gemma12 quarantine、固定slot/stateful authority、Typed References/Coverage、formatter、lint/syntax repair、global repair最大1、generation prompt/response schema、8192/2048/24000 budgetは維持。
制約照合（元資料: constraints-verification.json）ではprompt/payload/schema生成関数のASTと、version以外のprofile設定一致を検証した。

## 2. 分類設計

| 分類 | 意味 | cohort処置 |
| --- | --- | --- |
| GENERATION_CONTRACT_FAILURE | schema/capability/source正常、非空bodyのrequired final LFのみ欠落、commit未実行 | Task-local ESCALATE、追加repairなし |
| GENERATION_SCHEMA_FAILURE | malformed model JSON/text、正しいslot keyの値型不正 | **既存STOP維持**。worker/output domainでありscope破損とは扱わない |
| CAPABILITY_SCHEMA_FAILURE | unknown/wrong slot、追加path/key、phase/schema authority違反 | scope STOP |
| FOREIGN_HANDLE / STALE_EDIT_REGION / SCOPE_VIOLATION_MODEL | 他session/expired ID、source snapshot不一致、path/marker/scope違反 | STOP維持 |
| HOST_SCOPE_ERROR / COHORT_CHANGED等 | Host/Git/protected source/reference/freeze異常 | STOP維持 |

HTTP envelope/transport不良は既存INFRA_ERROR。JSON重複keyは曖昧な権限指定として既存scope STOPを維持。今回新しくTask-local化したのは、証明可能な末尾LF契約違反だけ。malformed JSON等のSTOP解除は別変更としても実施していない。

## 3. 適用前の安全確認

fixed-slotではexact slot keys・body型・Host binding・fresh snapshotを確認。statefulではpublished schema・issued enum・epoch・source/body hashを確認済みの経路だけを対象とする。issued identityの独立snapshotも照合する。

そのうえで全replacementのHost-owned path/region、strict UTF-8/NUL、marker禁止を確認。別targetの違反が混在していたらbody failureへ降格しない。source、protected inputs、references、Git metadata、cohort freezeを再検証し、**commit呼出し前**に拒否する。

before/after content ID一致、apply attempt/success 0、candidate未変更、Host integrity確認、normalization=false、repair_eligible=falseをresultへ保存。health後の最終guardでも異常があればHost STOPへ昇格する。設計（元資料: DESIGN_JA.md）。

既存body契約にはtext型・UTF-8・NUL禁止・required LF・Host marker禁止がある。encoding/type、marker、unknown capabilityをLFだけの不良と混ぜない。fixedの空body既存扱いとstatefulの空body拒否も維持した。HostによるLF自動追加は0。

## 4. Saved P224-003 replay

旧response、parsed JSON、body、slot metadata、source hashes、failure recordをread-only参照し、別copyで新runtimeを実行した。

| 指標 | 旧2.2.5 | 新2.2.6 offline replay |
| --- | --- | --- |
| response/body | 保存済みCoderNext出力 | 同一response/body bytes |
| final reason | EDIT_SCHEMA_ERROR | GENERATION_CONTRACT_FAILURE |
| domain | scope | worker/output |
| cohort STOP | true | false |
| apply attempted / succeeded | 0 / 0 | 0 / 0 |
| candidate mutation / final diff | 0 / 0 bytes | 0 / 0 bytes |
| Host/source verification | PASS | PASS |
| formatter normalization / validation | NOT_RUN | NOT_RUN |
| repair generation | 0 | 0 |

formatter binary/configのHost preflightは実行するが、候補へのformattingは実行しない。
最終実装での証跡: offline-verified/summary（元資料: offline-verified/summary.json）、parsed response（元資料: offline-verified/saved-parsed-response.json）、body（元資料: offline-verified/saved-body.txt）、metadata（元資料: offline-verified/saved-slot-metadata.json）。旧result/STOPを変更していない。注入responseの過去usageを新しいLocal token数へ加算していない。

## 5. Syntax / formatter回帰

旧P224-001の初回とrepair responseもreplayし、実際のpinned rustfmtで両方E0762を確認。`CANDIDATE_SYNTAX_FAILURE`、same-model repair合計1、Task-local terminal、STOPなしを維持した。

既存method-chain whitespace、限定std vec comma、closure normalization、unsupported→Task-local、format integrity/Host formatter failure→STOPのテストを維持。formatter実装・binary/configは今回無変更。

## 6. Negative tests / 必須regression

**既存212 + 追加21 = 233 tests、全PASS**。Rust fmt/clippy/test/check/buildも全PASS。

追加確認は、fixed/stateful LF欠落、wrong slot/path override、foreign handle、source drift、protected source/freeze drift、未知file、Host metadata不一致、marker injection、malformed JSON、値型不正、重複JSON key、拒否後health中のsource変更、正常fixed/stateful、同一cohort後続継続、混在target違反、旧FileScope互換、encoding不正等。
expired capability・reference・formatter・scope・global repair budgetの既存テストも維持した。

開発途中のsuite失敗も`regression/worker-suite-initial.json`と`worker-suite-second.json`へ保存。新reasonへの変更でlint repairの既存schema分類/STOP期待を外してしまった点を修正し、**lint policyを変更せず**最終suiteをPASSさせた。最終判定にはworker-summary（元資料: regression/worker-summary.json）とrust-summary（元資料: regression/rust-summary.json）を使用する。

## 7. 独立live cohort

業務仕様・acceptance・source・checksは保存Taskから再利用し、Task IDとcohortだけ独立化した。末尾改行欠落をpromptへ要求していない。

| Task | 元Task / model / protocol | Local | Review | 後続 |
| --- | --- | --- | --- | --- |
| S226-001 | P224-003 / CoderNext / fixed-slot debugging | GENERATION_CONTRACT_FAILURE / ESCALATE | REJECT | 002へ継続 |
| S226-002 | P224-004 / Gemma26 / fixed-slot | 初回PASS | ACCEPT_NO_CHANGE | 003へ継続 |
| S226-003 | P224-002 / Gemma26 / stateful | 初回PASS | ACCEPT_NO_CHANGE | 計画3件完了 |

run history（元資料: live/run-history.json）、Task map（元資料: live/task-map.json）、Task metrics（元資料: task-metrics.json）。S226-001のbody契約違反は自然発生。repairも正規化もせず未適用で終了した。そのコードのsemantic品質は未検証でありPASSを仮定しない。

## 8. 正常経路とCodex review

S226-002はtotal=0 / available>totalを先に拒否し、安全な差分を正確なKiB文字列で表示。S226-003は元first evidenceとguardを保ったままused_kib entryを1件追加し、typed memory fieldsを正しく利用した。

両Taskともapply → Host formatter → acceptance/regression/fmt/clippy/workspace test/check/build → Host scopeがPASS。各8 checks、合計**16 results / 78.299秒**。Host formatting **20 LOC**、reference packetは002が246 bytes、003が2157 bytes。
通常reviewはcompact packets（元資料: reviews/）のTask・diff・checks・短いsummaryのみ。全Local会話は通常reviewで読んでいない。ACCEPT_NO_CHANGE **2/3（66.67%）**、REJECT **1/3**、Codex repair LOC **0**、FALSE_GREEN **0**。未修正REJECTを工数削減成功へ換算していない。

## 9. 指定metrics

| Metric | live結果 |
| --- | ---: |
| GENERATION_CONTRACT_FAILURE | 1 |
| GENERATION_SCHEMA_FAILURE / EDIT_SCHEMA_ERROR | 0 / 0 |
| capability / scope failures | 0 / 0 |
| Task-local terminal | 3/3 |
| cohort STOP / Host failure | 0 / 0 |
| apply attempted / succeeded | 2 / 2 |
| body rejection Taskのapply / mutation | 0 / 0 |
| 正常Taskのauthorized candidate mutation | 2 Task |
| 元application/source変更 | 0 |
| body rejection後のnext Task continued | true |
| First PASS / Local final PASS | 2/3 / 2/3 |
| repair budget used | 0 |
| ACCEPT_NO_CHANGE / FALSE_GREEN | 2 / 0 |
| INFRA_ERROR / CUDA_ERROR | 0 / 0 |

source_mutationは許可されたcandidate editを数えるmetricでありscope破損ではない。formatter commitはmodel apply件数から分離した。

## 10. Context / tokens / time

8192 context、2048 output、24000 chars、temperature0、seed20260926を維持。**4 actual chat calls、input5390 / output417 tokens、Worker186.562秒、cohort207.125秒**。

| Task / call | message chars | request bytes | prompt_eval_count | eval_count |
| --- | ---: | ---: | ---: | ---: |
| 001 | 3279 | 3564 | 880 | 169 |
| 002 | 2836 | 3124 | 837 | 56 |
| 003 DISCOVERY | 2777 | 3779 | 662 | 40 |
| 003 EDIT | 7663 | 8268 | 3011 | 152 |

すべてHTTP200 / done=true / done_reason=stop / response schema valid。server logのtruncated flagsは0、NO_TRUNCATION_EVIDENCE。OUTPUT_LIMITなし。
exact request SHA256・raw payload/response・duration等はrequest index（元資料: request-index.json）。Codex exact tokens/active seconds/net savingsはnull。

## 11. Infrastructureと診断helperの記録

installed Ollama **0.35.0**、driver **591.86**、RTX3080。Gemma12 inferenceなし、fallbackなし。live前後およびTask境界のGPU/API/backend/residencyをread-only保存した。GPU telemetry（元資料: gpu-telemetry.json）。

live境界のGPU使用量は1873〜9857 MiB、backend PIDはCoderNext: 50624 → Gemma26: 17616。frontend PID51240を利用。Task間restart/forced unloadなし。GPU query timeout、residency mismatch、CUDA/backend crashはlive中0。これらは短い検証での観測であり、長期安定性の証明ではない。

cohort開始前、診断helperが`ollama ps`実行中に待機した。近接時刻に`ollama app.exe --hide --fast-startup`とfrontendが出現しており、CLI自動起動と継承pipe待機に整合するが、stack traceによる原因確定ではない。**自分が起動した診断用Pythonだけ**をPID/command/parentで照合して終了し、Ollama/backendは強制終了していない。
最初のsnapshotは未保存のため、その旨を明記し、改めてAPI正常・models=[]・GPU正常を保存してからliveを開始した。これはlive inference failure/CUDAではない。詳細は診断incident（元資料: pre-live-diagnostic-incident.json）、pre-live baseline（元資料: environment-pre-live.json）。恒久設定変更なし。

## 12. 保全と判定

基準16190 tracked filesのうち、意図した既存実装/doc/profile7ファイルだけ変更。旧実験artifact・raw response・STOP、Router/model/operational policy、application、formatter、lint/syntax実装は保全。live中はruntime/hash/cohort条件不変。execution freeze（元資料: execution-freeze.json）、runtime byte snapshots（元資料: runtime-snapshot/index.json）。

**READY_FOR_FULL_SHADOW_PILOT_RETRY**。saved003の分類・未適用proof、live自然発生時の後続継続、actual capability/integrity違反のSTOP維持、saved001 syntax回帰、通常fixed/stateful経路、FALSE_GREEN/Host/scope/infra/CUDAゼロを確認した。

これは限定した分類revisionの検証結果である。malformed JSONや別のcapability違反の既存STOPは残り、次のFull Pilotが必ず完走すること、CoderNextのコードが修復されたこと、一般的成功率が改善したことは主張しない。旧STOPは解除せず、Full Shadow Pilotの自動再開も行わず、この報告で停止する。
