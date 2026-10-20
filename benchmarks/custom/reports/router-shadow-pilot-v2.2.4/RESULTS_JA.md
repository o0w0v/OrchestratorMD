> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.4.md). This report alone does not establish a task result.

# bounded profile 2.2.4 Full Shadow Pilot

拡大判定: **NOT_READY — infrastructure blocked**。

新しい14 Task cohortを準備・freezeし実行したが、最初のP224-001でGemma26が **CUDA illegal memory access** を発生させ、cohortを停止した。候補コードは返っておらず、formatter・semantic validationへ到達していない。これはモデル能力FAIL、Router選択ミス、formatter regressionとは評価しない。実装品質を評価できたLocal Taskは0件である。

旧cohort、旧STOP、旧result、v2.2.4実装は保持。新しいSTOPを解除せず、retry・モデル差し替え・残りTaskへのdispatchも行っていない。

## 1. Cohort / environment / freeze

cohortは `router-shadow-pilot-v2.2.4`。application/sourceのbaseは `df7c479`、実行前freeze commitは **`b26ccd3`**、branchは `experiment/bounded-v2.2.4-full-pilot`。

| 項目 | 固定値 / 観測 |
|---|---|
| bounded profile / formatter guard | 2.2.4 |
| Router / Operational Policy | router-v2.1-shadow-1、変更なし |
| GPU / driver | RTX 3080 10GB / 591.86 |
| Ollama | 0.35.0、今回変更なし |
| Gemma26 digest | `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68` |
| CoderNext digest（未dispatch） | `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074` |
| generation | temperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=false |
| context / repair | 24,000 chars、Task全体のcode repair最大1回 |
| lint allowlist | clippy::useless_conversionのみ |
| formatter | pinned rustfmt 1.9.0-stable、binary/config/version/hash不変 |

Task specs、Coverage Matrix、finite ReferencePlan、source/test hashes、validation argv/order、model digests/options、runtime implementation hashes、実行順を freeze.json（元資料: freeze.json） / cohort.json（元資料: cohort.json） に固定した。実行途中の変更は0。environment/freeze.json（元資料: environment/freeze.json） に開始条件を保存。

## 2–3. Task一覧と実行順

12件のコードTaskは今回の新規business仕様。過去のcandidateや成功resultを再利用せず、実repoの表示・診断・集計と既存TCP predicateの不具合を対象にした。empty/Unicode/overflow/enum/collection/helper参照を含む単一責務で、dependency/schema/authorityは変更しない。無作為な本番Task標本ではない。

| ID | Task | 分類 / planned model | 状態 |
|---|---|---|---|
| P224-001 | CLI telemetryの改行・backslash等を一行escape | fixed_slot / Gemma26 | INFRA_ERROR / CUDA_ERROR |
| P224-002 | memory evidenceへused KiBの第2要素 | stateful / Gemma26 | NOT_RUN |
| P224-003 | TCP非data行の`01`誤count修正 | DEBUGGING（fixed_slot） / CoderNext | NOT_RUN |
| P224-004 | CLI used memory量の妥当性付き表示 | fixed_slot / Gemma26 | NOT_RUN |
| P224-005 | MockObserverのnested snapshotをtyped抽出 | reasoning / Gemma26 | NOT_RUN |
| P224-006 | 正常系auditへsample complete/bounded表示 | stateful / Gemma26 | NOT_RUN |
| P224-007 | VmRSS parse失敗へ診断prefix | fixed_slot / Gemma26 | NOT_RUN |
| P224-008 | HighLoad evidenceへ観測timestamp | stateful / Gemma26 | NOT_RUN |
| P224-009 | mock report reasonへevent kind label | fixed_slot / Gemma26 | NOT_RUN |
| P224-010 | skill reasonへevidence UTF-8 bytes合計 | stateful / Gemma26 | NOT_RUN |
| P224-011 | CLI warningのstable unique preview | fixed_slot / Gemma26 | NOT_RUN |
| P224-012 | meminfo重複診断へfield名 | stateful / Gemma26 | NOT_RUN |
| P224-013 | Telemetry欠測説明の表示方針 | Codex境界 / Localなし | CODEX_ONLY、境界判定PASS |
| P224-014 | CLI per-CPU loadの欠測・小数表示 | fixed_slot / Gemma26 | NOT_RUN |

Local実行順は **001 → 002 → 003 → 004 → 005 → 006 → 007 → 008 → 009 → 010 → 011 → 012 → 014**。fixed/stateful/debugging/reasoningを事前にinterleaveした。境界013はfreeze前にCodex判定し、Local実行順の分母に含めない。実際には001だけがdispatchされたため、予定したGemma26→CoderNext→Gemma26のmodel switchingは発生していない。

task-index.json（元資料: task-index.json）、all-task-outcomes.json（元資料: metrics/all-task-outcomes.json） に未実行も含め全件を保存。未実行TaskにPASS/FAILや推定値を付けていない。

## 4–6. Completion / ACCEPT_NO_CHANGE / First・final PASS

| 指標 | 結果 |
|---|---:|
| planned Tasks | 14（Local 13 + Codex境界1） |
| dispatched Local Tasks | 1 / 13 |
| Local terminal result | 1（INFRA_ERROR） |
| Codex境界terminal | 1 |
| 全terminal / planned | 2 / 14（14.29%） |
| Local terminal / planned Local | 1 / 13（7.69%） |
| cohort completed | **false** |
| 能力評価可能Local Tasks | **0** |
| ACCEPT_NO_CHANGE（全dispatch運用指標） | 0 / 1 |
| Local final PASS（全dispatch運用指標） | 0 / 1 |
| First PASS / coding PASS率 | **N/A（有効分母0）** |
| Codex採用REJECT | 1（infraでcandidateなし。coding REJECTではない） |
| FALSE_GREEN | 0（Local PASS自体が0） |

terminal結果の保存は、成功やcohort完走を意味しない。0/1の運用値からcoding能力が0%と結論しない。旧successful runsやformatter micro cohortを今回の分母に足していない。summary.json（元資料: metrics/summary.json）。

## 7–8. Semantic repair / natural lint repair

code repair budget使用0、semantic repair0、lint repair0、Codex candidate repair0。初回HTTPが失敗したため、natural useless_conversion発生0件という集計は**観測機会0**を意味する。eligible/recoveredとも評価不能であり、lint policyの有効性を再確認したとはしない。

共有repair上限・allowlist・eligibilityは不変。infraをcode repairとして再投入せず、追加retryを行わなかった。

## 9–12・22. Protocol別結果

| 分類 | planned | dispatched / terminal | 有効coding結果 | ACCEPT_NO_CHANGE |
|---|---:|---:|---:|---:|
| fixed_slot（DEBUGGINGを除く） | 6 | 1 / 1 | 0 | 0 / 1（infra込み運用値） |
| stateful | 5 | 0 / 0 | 0 | N/A |
| DEBUGGING / CoderNext | 1 | 0 / 0 | 0 | N/A |
| reasoning | 1 | 0 / 0 | 0 | N/A |

P224-001ではHostのsnapshot/hash-bound slot発行まで到達した。model applyは0。stateful valid apply rate、handle更新、repair recovery、reasoning品質はN/A。P224-013は自由仕様をCodexへ返す既存Router境界が正しく働き、generation0、implementationなし。表示方針案を boundary/design-note.md（元資料: boundary/design-note.md） に保存した。

## 13. References

dispatch前に12 code Taskすべてのfinite ReferencePlanとdirect helper completenessを確認。非empty planは6 Task、参照総数11、そのうちdirect helper signatureは `self.record` と `parse_kib_value` の2件。静的packetは最大2,840 bytes、code Task分合計12,468 bytes（参照なしpacketのslot metadataも含む）。

実dispatchされた001は参照0、packet 246 bytes、completeness PASS。残りTaskの事前検査PASSを、実モデルが型情報を活用できた証拠とは扱わない。reference input tokensは未取得でnull。

## 14–15. Formatter normalization / unsupported Task-local failures

今回のformatter invocationは0。method-chain、vec trailing comma、closure block、unsupportedのobserved/accepted/rejected/validation reachedはすべて0で、実動作は未評価。

`FORMAT_UNSUPPORTED_NORMALIZATION` 0、`FORMAT_INTEGRITY_FAILURE` 0、Host integrity STOP 0。cohort STOP 1の原因はCUDA。未対応変換のTask-local継続や真のintegrity STOPの既存実装・既存testsは保持したが、今回のliveで再検証できたとはしない。format-normalizations.json（元資料: metrics/format-normalizations.json） は空の観測一覧。

## 16–17・21. Validation / context / Host workload

開始前の12 code Taskすべてで、compile可能かつ新acceptanceが期待どおりFAILするred状態を確認。Coverage criteriaは全14 Taskで112、宣言validationは86（別途Host scope guard）。全code Taskでacceptance、targeted regression、fmt、Clippy、workspace test/check/buildを固定した。モデルにcheck選択権はない。

実行前の既存Worker suite **201/201 PASS**。Rust fmt / Clippy all-targets・all-features・warnings拒否 / workspace test / locked check / locked buildはすべてPASS。regression/summary.json（元資料: regression/summary.json）。これは事前のHost/runtime検査で、生成候補の合格とは別。

live candidate validation件数0、validation elapsed 0、Host formatting LOC 0。planningでは12件のscaffold/acceptance作成とred検証を行っており、Codex/Hostの準備負担が0だったわけではない。

| P224-001 initial request | 保存値 |
|---|---:|
| serialized message chars | 3,024 |
| serialized request bytes | 3,312 |
| num_ctx / num_predict / char gate | 8192 / 2048 / 24000 |
| HTTP status | 500 |
| HTTP elapsed | 37.723 s |
| prompt_eval_count / eval_count / done_reason | null / null / null |
| repair request | なし |

request SHA256: `4acf201e8e85ccb1bc69d6891bd4375643a7f3075c315e3cd4147d64eb8af9eb`。

server logには `task.n_tokens = 877` があるが、これは成功responseのprompt_eval_countではない。Ollamaのinput/output tokens、eval/load duration等を0で補完せずnullとして保存した。明示的prompt truncation証拠はないが、CUDAにより正常なcontext処理・生成完了を確認できていない。context増量やprompt短縮は行っていない。request-index.json（元資料: metrics/request-index.json）。

## 18. Infrastructure failure

2026-10-03 **01:27:47.496 JST** にP224-001開始、**01:28:31.149 JST** にCUDA_ERRORのterminal resultとSTOPを保存した。Worker elapsed 43.329 s、cohort wall 44.547 s。

raw error:

```text
HTTP 500
CUDA error: an illegal memory access was encountered
```

Ollama/backend logの観測順序は以下。

1. Task前は `/api/ps models=[]`、backend PIDなし。Ollama/frontend/APIとnvidia-smiは正常応答。
2. Gemma26のbackendを起動。log上のloadは20.09秒で完了、01:28:16.931 JSTにstarted。
3. 最初のrequestでprompt処理を開始。8192 context、prompt 877 tokens、cache/checkpoint 365の記録。
4. `ggml_backend_cuda_synchronize` / `cudaStreamSynchronize(cuda_ctx->stream())` でillegal memory access。
5. 01:28:30の `/api/chat` がHTTP 500。backendは `exit status 0xc0000409` で終了。

生成途中のoutput token数は不明。少なくともmodel load完了後・最初のprompt処理記録の後・候補response返却前に障害が生じた。今回の前Taskやmodel switchingはなく、CoderNextは起動していない。

| Snapshot | GPU used | Ollama reported VRAM | backend PID |
|---|---:|---:|---|
| Task前 01:27:52.201 | 1,855 MiB | 0 | なし |
| Task後 01:28:30.569 | 1,171 MiB | 990,348,573 bytes | 40264 / 19780（終了処理付近のsnapshot） |
| cohort終了 01:28:31.242 | 1,278 MiB | 990,348,573 bytes | 19780 |
| read-only追加確認 01:34:11.821 | 1,471 MiB | 0 | なし |

Task境界snapshotなので、実行中のpeak VRAMは不明。既存のresidency mismatch判定はfalse、nvidia-smi timeoutは観測0。APIは障害後も応答した。backend消失とmetadata解放は確認できたが、追加generationを行っていないためinference安定性の回復は未確認。

backend commandにはcontext8192、batch512/ubatch512、flash-attn auto、draft-mtp（draft n max3）が記録されていた。今回変更していない。これらの設定を原因と断定する比較証拠はない。

Windows Event Log（01:23:30–01:33:30 JST）:

- `nvlddmkm` Event ID153が7件（01:28:20.048–01:28:21.904）。MessageはnullだったためXMLも保存。XML dataは `Error occurred on GPUID: 100`。
- 01:28:28.394にApplication Error ID1000。`llama-server.exe`、PID `0x9D48` = 40264、exception `0xc0000409`、fault module `ucrtbase.dll`。
- 保存窓内にDisplay providerのresetイベントは観測されず、**driver resetの断定はしない**。ucrtbase.dllの記録もVisual C++ Runtimeのroot causeを証明しない。

frontend `ollama.exe` PID2544、tray PID12488は残り、creation timeは2026-10-01 19:01 JST。このcohortはfresh frontend比較試験ではない。長寿命frontendとの因果も今回の1件だけでは判断できない。

failure layerは **Ollama / llama-server CUDA backend周辺**まで。OOM、driver bug、Ollama bug、Gemma固有bug、MTP/flash attention原因はいずれも未確定。GPU errorをcoding capability FAILへ変換しない。

infra-analysis.json（元資料: diagnostics/infra-analysis.json）、server.log（元資料: diagnostics/P224-001/server.log）、Windows events（元資料: diagnostics/post-fault/events-processes-decoded.json）、Windows XML / process detail（元資料: diagnostics/post-fault/events-processes-detail.json）、STOP.json（元資料: STOP.json） に証跡を保存した。driver/Ollama/runtime/clock/OS設定変更、再起動、model download、unload、追加inferenceはいずれも行っていない。

## 19–20. Codex intervention / review burden

通常reviewは5,430 bytesのcompact packetを読み、empty final diff・未実行checks・Worker summaryから不採用を記録。`REJECT`はcandidate不在による採用拒否であり、コード品質のREJECTではない。

Codex candidate code repair count/LOCは0。一方、CUDA後に限定的なHost/infra調査を実施し、通常reviewと分けて workload-supplement.json（元資料: metrics/workload-supplement.json） へ記録した。全Local conversationの通常閲覧は行っていない。正確なCodex planning/review/failure-analysis/code-repair/protocol-infra tokensとactive timeは未取得のためnull。Local tokensも未知なので節約量へ換算しない。

初回CIM詳細queryはaccess deniedだったが、その失敗を保持し、read-only権限で再取得した。これは追加model inferenceや環境修復ではない。

## 23–24. Expansion judgement / conclusion

**NOT_READY**。原因は1件目のCUDA/backend障害による停止で、cohort completion・ACCEPT_NO_CHANGE・protocol別品質の実証が不足しているため。今回の観測から `NEEDS_PROTOCOL_REVISION`、Routerが悪い、Gemma26のcoding品質が低いとは結論しない。

有効Local結果0なので、v2.2.4が「Codexはplanning + compact reviewだけで済むTaskを何割に増やせるか」は**未測定**。READY_TO_EXPANDや20–30 Taskへの拡大を判断する材料は得られていない。

次のPilotより先に、Gemma26も含む別のInfrastructure調査で今回のbackend failureを確認する必要がある。今回のcohortで設定変更やモデル差し替えを試すことはせず、STOPを保持して終了する。新たな再実行は別run/cohortとして証跡を分離する。

実行前から存在した**13,409 filesのSHA256不変**、freezeされたTask/runtime/options不変、request SHA256、review evidence binding、repair budget、Gemma12 inference0を確認した。audit.json（元資料: metrics/audit.json）。未実行12 Taskの仕様も保持しており、旧結果の上書きや成功への書き換えはない。
