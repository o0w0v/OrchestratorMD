> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/router-shadow-pilot-v2.2.4-fresh-001.md). This report alone does not establish a task result.

# bounded 2.2.4 Fresh-Process Full Shadow Pilot Retry 結果

判定: **NEEDS_PROTOCOL_REVISION**。fresh process gateはPASSし、Gemma26のHTTP応答は正常だった。P224-001の生成候補にRust構文誤りがあり、固定runtimeがrustfmt事前checkのexit 101を`HOST_FORMAT_ERROR`へ分類したため、最初のTaskでcohort STOPとなった。途中で分類・修復policyを変更せず停止した。

CUDA/INFRA_ERRORは0。Local 13件中1件のみterminal、残り12件はNOT_RUN。連続運用安定性や全protocolの品質は今回確認できていない。旧Pilot、旧STOP、過去のCUDA失敗、アプリケーション、Router/Worker/profileは保全した。

## 1. Fresh process gate

ユーザーのtray Quit後、frontend/backend不在、11434接続拒否、`/api/version`・`/api/ps`接続拒否、Ollama GPU process不在、nvidia-smi応答を確認した。同じinstalled Ollamaを起動し、frontend PID **43836**、`models=[]`、backendなし、API正常、両model digest一致を確認。強制kill、OS reboot、generation probeは実施していない。

証跡: Quit（元資料: infrastructure/quit-001.json）、fresh start（元資料: infrastructure/fresh-start-001.json）。準備時の`MANUAL_ACTION_REQUIRED`は過去時点の記録として保持し、このgate通過後に新runを開始した。

## 2. Environment

| 項目 | 値 |
| --- | --- |
| GPU / driver | NVIDIA GeForce RTX 3080 10GB / 591.86 |
| Ollama | 0.35.0、binary hash不変 |
| Windows boot | 2026-10-01 09:57:56.205910 UTC（18:57:56 JST） |
| frontend start | 2026-10-02 18:38:42.597004 UTC（10月3日03:38:42 JST） |
| rustfmt | 1.9.0-stable (48a229ceae 2026-09-01)、binary/config固定 |
| bounded profile | 2.2.4、Router v2.1 policy不変 |

Gemma26 digest: `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。CoderNext digest: `ca06e9e4087c714d44355bf954099187890e63084b4a632b8e9956c4b9492074`。Gemma12 quarantine維持、Qwen14/fallback使用なし。詳細はenvironment（元資料: environment/freeze.json）。

## 3. Cohort / Task一覧

新cohortは`router-shadow-pilot-v2.2.4-fresh-001`。旧14 Taskのbusiness identityと仕様・acceptance・Coverage Matrix・ReferencePlan・validation・routeを維持し、独立workspaceへ325入力ファイルを複製した。再利用検証（元資料: reuse-verification.json）に対応表を保存。run IDは`新cohort/P224-xxx/run-001`、未実行IDは予約のみで実行済みとは扱わない。

| Task | Business Task | 集計group | Model | 結果 |
| --- | --- | --- | --- | --- |
| P224-001 | CLI telemetryを改行しないescaped一行として表示 | fixed_slot | Gemma26 | ESCALATE / REJECT |
| P224-002 | memory evidenceにused KiBを独立した第2要素として追加 | stateful | Gemma26 | NOT_RUN |
| P224-003 | TCP inventoryが非data行の01を誤countする不具合 | debugging | CoderNext | NOT_RUN |
| P224-004 | CLIのused memory量を妥当性検査付きで表示 | fixed_slot | Gemma26 | NOT_RUN |
| P224-005 | MockObserverのnested snapshot値をtyped抽出 | reasoning | Gemma26 | NOT_RUN |
| P224-006 | 正常系auditへprocess sampleのcomplete/bounded区別を追加 | stateful | Gemma26 | NOT_RUN |
| P224-007 | VmRSSの値parse失敗へ診断prefixを付与 | fixed_slot | Gemma26 | NOT_RUN |
| P224-008 | HighLoad evidenceへ観測timestampを第2要素で追加 | stateful | Gemma26 | NOT_RUN |
| P224-009 | mock report reasonへ安定したevent kind labelを表示 | fixed_slot | Gemma26 | NOT_RUN |
| P224-010 | skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示 | stateful | Gemma26 | NOT_RUN |
| P224-011 | CLI warning overviewのstable unique preview | fixed_slot | Gemma26 | NOT_RUN |
| P224-012 | meminfo重複診断へMemTotal/MemAvailableの名前を付加 | stateful | Gemma26 | NOT_RUN |
| P224-013 | Telemetry欠測を説明するUIの表示方針を決定 | boundary | Codex | CODEX_ONLY |
| P224-014 | CLI per-CPU loadの欠測/非有限値と小数表示 | fixed_slot | Gemma26 | NOT_RUN |

全14件のroute、run状態、実測metrics、静的reference計画はall-task-outcomes.json（元資料: analysis/all-task-outcomes.json）。P224-013はCODEX_ONLY境界確認であり、Local inferenceやapplication実装の完了数には含めない。

## 4. Execution order

固定順: 001 → 002 → 003 → 004 → 005 → 006 → 007 → 008 → 009 → 010 → 011 → 012 → 014。実行は001のみ。P224-013は独立した境界確認。結果を見た並替え、同Task retry、Task間restart/unloadはない。

## 5. Completion

| 指標 | 結果 |
| --- | --- |
| planned total / Local | 14 / 13 |
| Local dispatched / terminal | 1 / 1 |
| Local terminal coverage | 1/13 = 7.69% |
| boundaryを含むterminal coverage | 2/14 = 14.29% |
| 未実行Local | 12 |
| cohort completion | false（STOP） |
| cohort wall / Worker time | 32.469秒 / 29.625秒 |

terminalは成功を意味しない。STOP（元資料: STOP.json）とrun history（元資料: run-history.json）を保持。

## 6. ACCEPT_NO_CHANGE

**0/1（0%）**。分母は実dispatchしたLocal Task、未実行12件とCODEX_ONLYを含めない。Codex reviewはREJECT 1、minor/major fix 0、FALSE_GREEN 0。これは1件の結果であり、未実行Taskの品質や一般的成功率を示さない。

## 7. First / final PASS

Local final PASSは0/1。固定集計ではHost-domain結果を能力評価から除くため、First PASSとcapability PASSは**N/A（0/0）**。構文誤り自体は観測済みだが、mandatory validation未到達のため意味的正しさは未検証。既存Local classificationを事後に書き換えていない。

## 8. fixed_slot

Gemma26 fixed_slotは計画6件中1件実行。bounded slot applyは成功し、model diffは追加11/削除1 LOC。formatter stagingの事前checkで停止、applicationへの採用なし。ACCEPT_NO_CHANGE 0/1。CoderNext fixed_slotは次のdebugging群として別集計。

## 9. Stateful

計画5件、実行0。DISCOVERY/EDIT、valid apply、reference completeness、repair、ACCEPT_NO_CHANGEのlive値はN/A。静的preflight成功をlive成功として計上しない。

## 10. Debugging

P224-003 / CoderNextは未実行。model load・生成・reviewともN/A。

## 11. Reasoning

P224-005 / Gemma26は未実行。typed extractionの品質・token/timeはN/A。

## 12. Semantic repair

使用0、回復率N/A。Host-domain STOPのためrepairに進まなかった。構文誤りに対しCodexがretry promptを書いたり、修正したりしていない。global code repair上限1は維持。

## 13. Lint repair

Clippyへ未到達。lint occurrence/eligible/invoked/recoveredの観測件数はすべて0、回復率はN/A。`clippy::useless_conversion`限定policyの有効性は今回評価できない。

## 14. Formatter

P224-001候補のbackslash用character literalが不正。pinned rustfmt事前checkは**exit 101 / E0762: unterminated character literal**を返した。現行`bounded_formatting.py`はpre-check exit 0/1以外を`HOST_FORMAT_ERROR`へ分類する。結果は`ESCALATE / failure_domain=host / stop_cohort=true`。

formatter binary/versionは確認済み。normalization実行前に停止し、Host formatting LOC 0、mandatory validation NOT_RUN。`skip_children`のstable-channel warningもraw stderrへ保存したが、直接の失敗はE0762。source/scope/file/freeze破損は観測せず、`FORMAT_INTEGRITY_FAILURE`は0。記録上のHost failure 1と、実際の共有integrity破損を区別する。

formatter record（元資料: workspace/records/router-v2.2/P224-001/format-1/record.json）、candidate diff（元資料: workspace/records/router-v2.2/P224-001/final.diff）、別枠の失敗分析（元資料: analysis/P224-001-failure.json）。

## 15. Task-local unsupported

`FORMAT_UNSUPPORTED_NORMALIZATION`は0。method-chain / std vec trailing comma / closure blockのnormalization経路はいずれも未観測。今回の停止はunsupported変換の誤分類ではなく、normalization前のparse error経路。Task-local rejection policyを弱めて続行していない。

## 16. References

P224-001はexternal reference不要でcount 0、binding等を含むpacket 246 bytes。静的direct-helper completenessはPASS（必要0/供給0）。全Taskの予定refs/bytesとlive有無をHost workload（元資料: analysis/host-workload.json）に分離保存した。未実行Taskのreference有効性は未評価。

## 17. Context / transport

| 項目 | 実測 |
| --- | --- |
| num_ctx / num_predict / chars gate | 8192 / 2048 / 24000（固定） |
| temperature / seed | 0 / 20260926 |
| serialized message chars / request bytes | 3024 / 3312 |
| HTTP / done / done_reason | 200 / true / stop |
| prompt_eval_count / cached / eval_count | 877 / 0 / 135 |
| total / load / prompt eval / eval duration | 18.6064 / 14.7116 / 1.3477 / 2.5416秒 |
| truncation | NO_TRUNCATION_EVIDENCE、server truncated=0 |
| repair transport | N/A（repairなし） |

request SHA256: `4acf201e8e85ccb1bc69d6891bd4375643a7f3075c315e3cd4147d64eb8af9eb`。旧P224-001および前回infra replayと同一。heuristic token推定値を実測値として使用しない。raw request/responseへの索引（元資料: metrics/request-index.json）。

## 18. Infrastructure / frontend lifetime

frontend PID43836、cohort開始時age **30.557757秒**、終了時 **64.674002秒**。このfrontendのinference index **1**、backend launch **1**（PID38188）、model switch **0**。backendはSTOP後も同じPIDで存在し、API応答正常。途中restart/unloadなし、sleep/resumeイベントなし。

Task境界のnvidia-smi GPU使用量はbefore **1677 MiB**、after **9884 MiB**。Ollama `/api/ps` VRAM報告はbefore 0、after **990348573 bytes**。両指標は別保存し、同一尺度の実使用量と見なさない。既存residency mismatch detectorはfalseだが、API residency量の正確さを立証するものではない。境界samplingのみなのでpeak GPUはnull。

frontend lifetime/backend command（元資料: analysis/frontend-lifetime.json）、GPU/API snapshots（元資料: metrics/gpu-health.json）、post-STOP（元資料: infrastructure/post-stop.json）、server log（元資料: diagnostics/P224-001/server.log）。Windows関連イベントqueryは取得可能で、対象時間窓の該当イベント0、Display resetなし。

## 19. CUDA

CUDA 0、INFRA_ERROR 0、backend crash 0、nvidia-smi timeout 0。今回は短い1 callで打ち切りになったため、fresh processによる恒久解決・長期安定・model切替安定性は主張しない。追加generationや再restartによる救済はない。

## 20. Codex intervention / LOC

通常review結果はREJECT。code repair count 0、filesなし、追加0/削除0 LOC。Local candidateを修正して採用していない。失敗原因調査とinfra/protocol分析は実施しており、code-fix intervention 0を「Codexの作業ゼロ」と解釈しない。

## 21. Host workload

全14 Taskで予定Coverage criteria 112、validation定義86。今回の候補に対するmandatory validation実行は0件/0秒。formatter stagingでversion確認とpre-checkの2 command、合計約3.031秒。Host formatting 0 LOC、unsupported normalization 0。

準備段階の既存Worker suiteとRust fmt/clippy/test/check/buildはすべてPASS、fresh gate offline test 4/4。これらはruntime/preparationのregressionであり、今回candidateのvalidation PASSではない。新cohort入力463ファイルと既存保護14,190ファイルをhash検証し不変。最終integrity（元資料: analysis/final-integrity.json）。

## 22. Review burden

通常reviewはtask/route/diff/check/summaryからなるcompact packet **6826 bytes**を使用。全Local会話を通常reviewに投入していない。別の失敗分析ではformatter診断・該当runtime分岐・候補・raw response比較を参照し、workload supplement（元資料: analysis/workload-supplement.json）にpath/hash/bytesを記録した。

normal-review annotationのwall interval 79.471177秒は経過時間であり、失敗分析との重なりを含み得る。純粋なreview active timeへ換算しない。planning / normal review / failure analysis / code repair / infra-protocol analysisの正確なtokens・active timeはnull。Local tokens 877+135はCodex節約量ではなく、net efficiencyは未算定。

## 23. 旧infra-blocked cohortとの比較

| 指標 | 旧v2.2.4 | 今回fresh-001 |
| --- | --- | --- |
| 最初のTask | P224-001 | 同じP224-001 |
| request | 同一SHA256 | 同一SHA256 |
| API | HTTP500 / CUDA illegal memory access | HTTP200 / done=stop |
| Local結果 | INFRA_ERROR | ESCALATE / HOST_FORMAT_ERROR |
| CUDA / INFRA | 1 / 1 | 0 / 0 |
| 実dispatch / Local terminal | 1 / 1 | 1 / 1 |
| 残りLocal | 12未実行 | 12未実行 |
| ACN（all dispatched） | 0/1 | 0/1 |
| 停止stage | inference | formatter pre-check |

前回Infrastructure Revalidationのfresh 5/5正常応答はtransportの成功であり、コード品質評価ではない。保存済み5 responseの`message.content`は今回候補と同一だった。この比較は別分析で記録し、過去infra PASSや旧Pilot結果を書き換えていない。

## 24. Expansion judgement

**NEEDS_PROTOCOL_REVISION**。ACN基準、cohort完走、全protocol実測を満たさない。今回のblockerはmodel候補の構文誤りがformatter pre-checkでHost/cohort STOPに分類される経路。CUDAは観測しなかったため、このrunを新たなinfra失敗とは扱わない。

次の候補は、保存候補を用いたoffline分類レビューで、model syntax errorとformatter/共有integrity異常を安全に区別できるか確認すること。既存の最大1回repairとの整合、安全なstaging、scope/freeze guardを検証する必要がある。今回classification・repair policyは変更せず、次の改修・実験・Pilot拡大を自動開始していない。

## 25. 結論

fresh-start前提は満たし、元CUDA失敗と同一requestで正常生成まで進んだ。しかしP224-001の構文誤りにより固定Host policyがSTOPしたため、実用品質とcohort完走性の評価は未完了。新しい成功Taskへの差替え、分類変更、追加repairによる救済を行わず、その結果と未実行状態を保存した。

実測集計はmetrics/summary.json（元資料: metrics/summary.json）、旧結果保全・freeze検証はanalysis/final-integrity.json（元資料: analysis/final-integrity.json）。通常コード採用と本番変更はない。
