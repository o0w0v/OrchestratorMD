> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-v2.2.8-candidate-parse.md). This report alone does not establish a task result.

# bounded 2.2.8 Candidate Parse Failure Classification Revision

判定: **READY_FOR_ECONOMIC_RETRY**（分類revisionのreadiness）。次のEconomic cohort/production adoptionは開始していない。

## 目的・変更範囲

旧ECC227-007は候補の式の後に`None`が残り、rustfmtが`expected `;`, found `None``を返した。旧classifierが非対応でHOST_FORMAT_ERROR/Host STOPになった。本revisionはこれを安全にcandidate-localと証明する。Router/registry/Operational Policy、prompt、ReferencePlan、capability、generation/repair budget、formatter binary/config/normalization、validation argv/orderは不変。2.2.7のexact final-LF関数自体もbyte不変。

明示`profile_version=2.2.8`だけで新分類を有効化。旧2.2.7/versionlessは旧classifier。互換名`CANDIDATE_SYNTAX_FAILURE`、corroboration件数のalias`CANDIDATE_PARSE_FAILURE`、domain worker、stop_cohort=false。普通のrepairは既存最大1回のまま。one-shotは実験側veto、repair生成0。

## 決定的証拠とfail closed

authorized schema/apply transaction、source/freeze/reference/Git metadata、protected source、candidate/staging、formatter version/binary/configを検証。pinned installed rustcの直接metadata診断で同じcandidate SHA、message、primary行・列・byte span、changed regionを照合する。Cargo/build script/外部proc macro/生成物実行は使わない。baselineも独立copyで検査する。`--extern`なしによるE0432/E0433は、baselineと同じ保護位置の同じ診断のみ分離し、parse/validation PASSとは数えない。

launch/panic/internal error、I/O、unknown renderer/span、source/staging/pin drift、corroboration不能、semantic/type compile errorは降格しない。private copyはOS sandboxという主張ではない。複数行primaryや別の未対応parse表現も保守的にHost STOPとなり得る。

## ECC227-007 saved replay

`saved-replay/ECC227-007/run-004/`が最終runtimeのreplay。raw response/request、authorized saved handle、候補body、staging source、old stderr/result/STOPとSHAを保持。旧候補bytesを変えず、rustfmt/rustcとも87:127で同じmissing-semicolonを確認。**CANDIDATE_SYNTAX_FAILURE / worker / stop=false**。normalization/mandatory validation/採用なし。

rustc version/baseline/candidateのcommand durationは合計2.265秒。これは今回の1 replay観測で一般的なlatencyの推定ではない。root直下の最初の部分記録はWSL sandbox E_ACCESSDENIED、run-002はcompilerの共通未解決importを初期adapterがfail closedした記録、run-003はauthority証拠追加前のprototype結果。すべて削除せず残す。最終判定にはrun-004のみ使用。

## Regression

Worker **275/275 PASS**（旧255＋新20）。missing formatter、panic、source/staging drift、unrelated span/source、compiler unknown/timeout、semantic type、baseline parse、pin drift、共通dependency区別、LF、budget、append-only safety metricsを確認。root Rust fmt/clippy/test/check/build **5/5 PASS**。既存全Worker suite内のhandle/reference/scope/formatter/repair testsも維持。

LSE-008..012 **5/5期待一致、raw/normalized bytesが2.2.7と同一**。008 semantic FAIL、009 compile FAIL、010/011/012 PASSを保持。正規化bytesはexact LF 1 byteのみ。旧artifactに適用していない。

## Small live verification

未使用4 Taskを事前freeze。前ECCと同じQwen14の明示実験binding、num_ctx8192/num_predict2048/temp0/seed20260926。routing/registryファイル不変。Ollama0.35.1、RTX3080 10GB、driver591.86。開始時models=[]/backendなし、GPU1147MiB。healthy idle frontend16332/server20880を再起動せず使用し、その条件を明記。generation probeなし。

| Task | Local terminal | 分類 | input/output tokens | Worker秒 |
|---|---|---|---:|---:|
| PAR228-001 | PASS | TARGETED_CHECKS_PASSED | 854/31 | 51.625 |
| PAR228-002 | PASS | TARGETED_CHECKS_PASSED | 2698/125 | 57.172 |
| PAR228-003 | ESCALATE | CODE_FAILURE | 618/45 | 32.125 |
| PAR228-004 | PASS | TARGETED_CHECKS_PASSED | 2651/125 | 54.406 |

全4件terminal。003は`Option<usize>`に`u32`を渡すE0308の**semantic/type failure**でありparse failureへ誤分類していない。repairせず、次の004がPASS。合計input 6821、output 326、Worker 195.328秒。これはworkflow economicsやモデル能力rankingではない。

自然発生parse errorは0件。したがってliveそのものからparse分類の再現を主張しない。`controlled/`の別cohortでは実pinned toolchain＋決定的候補を使い、parse failure→Task-local→次Task PASSを確認。missing formatter/panic conditionではHost STOPを保持、次dispatchはCOHORT_STOPPEDで生成0。controlled faultsはモデル失敗/自然発生Host障害/CUDAへ混ぜない。

## 安全指標・Review

LOCAL_VALIDATION_FALSE_GREENとFINAL_PIPELINE_FALSE_GREENを今後のannotationで分離。旧FALSE_GREENは維持し、旧ECC227-002/SAFETY_REGRESSIONは改訂しない。

独立CLI review（PASS 3件＋任意width sentinel）はautomatic approval reviewが外部egress承認不足として拒否した。送信0、実usageはnull。4 packet/39,663 bytesを`review-packets/`へ保存し、ユーザーへ送信承認を依頼済み。coordinatorはcompact diff/contract/checkをreviewしたが、独立sessionの代用とは数えていない。

今回production採用0、FINAL_PIPELINE_FALSE_GREEN=0はその限定的事実。独立review未完了ならLOCAL_VALIDATION_FALSE_GREENはnullであり、0へ補完しない。production候補は独立review acceptance＋FINAL_PIPELINE_FALSE_GREEN=0を要求する。

## Infrastructure・保全

live Host STOP/scope/infra/CUDA **0**。毎Taskのbefore/during/after、API ps、backend PID、Windows events、existing server logを`live/infrastructure/`へ保存。driver reset/query timeout/residency mismatchなし。GPU使用量だけでOOMを断定しない。review外部送信のapproval rejectionはprovider/permission issueでありmodel/Protocol FAILへ計上しない。

`audit.json`: 旧実験/application/registry等 **41,347 filesのSHA不変**、旧STOP保持、live中runtime/input freeze不変、generation/prompt AST不変、LF/repair/reference/handle helperのbytes不変、formatter normalization AST不変。既存未追跡CVB private copiesをstage/削除しない。

## 次段階・限界

分類revisionとしてREADY。micro experimentのliveで自然parse failureは観測しておらず、その機序はsaved/controlled native evidenceで検証した。unknownは今後もfail closed。PASS率改善やcredits節減は今回測定していない。

2.2.8 freeze後の別Economic cohortはsequential 6 Sol Planner/Executor/Reviewer、complete-pair>=90%、Qwen14 one-shot、exact LF、独立review gateを維持。旧cohort/STOPを再開・解除しない。独立CLI reviewの外部送信は承認を得てから行う。
