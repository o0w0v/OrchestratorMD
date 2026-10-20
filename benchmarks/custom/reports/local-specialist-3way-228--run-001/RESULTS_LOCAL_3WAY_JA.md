> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/local-specialist-3way-228--run-001.md). This report alone does not establish a task result.

# Local Specialist 3-Way Challenger Benchmark

## 1. model identities

| Arm | Model | Digest | Quantization |
| --- | --- | --- | --- |
| qwen14 | qwen2.5-Coder:14b | 9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849 | Q4_K_M |
| gemma26 | gemma4:26b | 08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68 | Q4_K_M |
| qwen35 | qwen3.5:9b | 56671c2ab9385f9cfcb404638e32cd62d88e3501d44822208363c010179a3c90 | Q4_K_M |

## 2. environment

保存済みenvironment/model inventoryとUSER_QUIT_OBSERVATIONを参照。新fresh frontend未起動、production/driver/runtime/model files変更なし。

## 3. Task/family

COLLECTION・NUMERIC・ADAPTER・RECEIPT各6件、24 fresh frozen Tasks。Goal/category/acceptanceは未変更。

## 4. Codex baseline

23/24 full mandatory PASS + independent ACCEPT_NO_CHANGE。017はprotected Host fixture lintで未完成。詳細はRESULTS_BASELINE_STOP_JA.md。

## 5. Qwen14 results

NOT_RUN / Local generation 0。

## 6. Gemma26 results

NOT_RUN / Local generation 0。過去Host STOPを今回model FAILへ引き継がない。

## 7. Qwen3.5 results

導入確認・identity/license freeze済み。NOT_RUN / Local generation 0。軽さ・新しさで採用しない。

## 8. raw First PASS

N/A。未実行をFAIL/PASSへ変換しない。

## 9. LF rescue

N/A。exact final-LF rule/runtimeは未変更。

## 10. review quality

23 baseline ACCEPT_NO_CHANGE。Local reviewは未実施。

## 11. false greens

Local / final pipeline: N/A（Local未実行）。

## 12. Task-by-Task 3-way

全24件NOT_COMPLETE。3-way outcome/cheapest workflowは未評価。

## 13. family adoption

全model × family N/A。

## 14. family economics

Local未実行のためN/A。missing usageはnull、推定しない。

## 15. total credits

全actual合計は欠測によりnull。測定済みsubtotal=85.82789000000004 credits、sessions=75、missing=1。

## 16. credits saved

N/A。baselineだけからsavingsを推定しない。公式Standard ratesはrates/rate-card.jsonにraw URL/time/SHA付き。

## 17. USD equivalent

Model savingsはN/A。公式token USD rateは別保存し実請求額と呼ばない。JPY=null。

## 18. GPU/VRAM/CUDA

loaded model条件未実行、peak/headroom/CUDA stabilityはN/A。

## 19. latency

baseline wallはbaseline-history/、各role wallはcodex/。Local gate/API/routed wallはN/A。

## 20. infrastructure status

全model INCONCLUSIVE / NOT_RUN。原因はCUDAではなくHost fixture妥当性blocker。

## 21. LF dependency

N/A。RAW_ADOPTED / LF_RESCUED_ADOPTED未取得。

## 22. family winners

未選定。

## 23. proposed mixed Router

提案なし。production未変更。

## 24. limitations

比較未成立。source freeze後のHost helper変更は未採用で確認待ち。23のprovider capacity原usage欠測を成功retry usageで置換しない。Host本chat token/active timeはnull。

## 25. decision

**INCONCLUSIVE / STOPPED_HOST_FIXTURE_ERROR**。017 helper修正案の採用確認後のみ旧runを保持した新freeze/new runへ進む。


停止時の回帰確認: Worker offline 275 tests PASS、Rust fmt / clippy / test / check / build PASS。BASELINE_AUDIT.jsonでruntime/source/role/blinding保全を確認。POST_BASELINE_GPU_SNAPSHOT.jsonではOllama processなし・API応答なし・GPU query正常。017修正案未採用。
