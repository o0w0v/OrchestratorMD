> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.6-codex-value.md). This report alone does not establish a task result.

# Codex Value Benchmark — Blind Codex Baseline Recovery

実施日: 2026-10-04 JST。**Codex-only 5/5完了、全件validation PASS / ACCEPT_NO_CHANGE。実装・validationのpaired比較はCVB-001〜003の3件成立。暫定価値判定はINCONCLUSIVE。**

旧cohortは`INCONCLUSIVE / STOPPED_INFRA_ERROR`のまま保存。今回のLocal inferenceは0回。GPU復旧、Ollama起動・再起動、Local fallback、Protocol変更は実施していない。

## 1. Blind baseline確認

既存5つの独立B copyを使用。開始前にinitial sourceとfreeze済みhash、plain Task contract、scope metadataの一致を確認した。CLIに渡したのはbusiness goal・interface・allowed scope・acceptance・validation contract・initial sourceのみ。実装用内部handle/ReferencePlanは強制していない。

Taskごとに新規CLI実装session、さらに完成後のreviewにも別sessionを使用（計10 session）。fork/resumeは0。自動投入されたAGENTSは各copy自身のものだけであり、正確な入力promptとsession metadataを保存した。Local candidate/diff/response/diagnostics/summary/fallbackの投入、他Taskの実装の読取りは観測されなかった。reviewerはB側のcontract/diff/check結果/短いauthor summaryだけを読んだ。

指示と実tool traceに基づくblind監査であり、OSによるread隔離を主張しない。親の集計担当は旧経緯を知っているが、CLIへ親conversationは渡していない。

証跡: 開始前（元資料: codex-baseline-recovery/blinding-before.json）、session監査（元資料: codex-baseline-recovery/session-audit.json）、入力・tool trace最終監査（元資料: codex-baseline-recovery/blinding-final.json）。

5件のB freeze: `2026-10-03T19:12:15.514728+00:00`。A/B開封: `2026-10-03T19:13:00.630074+00:00`。順序はfreeze（元資料: codex-baseline-recovery/B_FROZEN.json）と開封記録（元資料: codex-baseline-recovery/comparison-opened.json）に保存。開封後にBコード・Task Spec・checksを変更していない。

## 2. Codex version / model / effort

CLI `0.158.0-alpha.2.1`、`gpt-6-astra`、`xhigh`を全sessionで固定。`codex exec --json --ignore-user-config`を使用し、model/effortを明示した。各START.jsonに完全argv、cwd、prompt SHA256、END.jsonにthread IDを保存。runtime rolloutのturn_contextでもmodel/effort/cwdを照合済み。

本番Router、model policy、bounded 2.2.6、formatter、budgets、repair policyは変更していない。Gemma12を含めLocal modelへのdispatchは0。

## 3. Usage capture可否

実usage取得は10/10成功。各sessionの`events.jsonl`にraw `turn.completed`、`END.json`にraw usageとinput/cached_input/output/totalを保存した。totalは報告input+outputの厳密な加算。cached_inputはinputの内数として表示し、二重加算しない。rawのreasoning/cache-write等の追加fieldも保持する。

Task内のplanningは実装turn内に含まれ、独立計測値はnull。親Codexの準備・harness整備・集計・報告のtokenはこの測定範囲外でnull。Local-firstのCodex実装/review/fallbackは未実施なので、そのusageもnull。文字数・Local tokensからの推定はしない。

## 4. CVB-001 result — PID範囲表示

空sampleはnone、非空は全要素の最小・最大PIDを1回の走査で取得。sliceは変更しない。

実装1回・code retry 0回。全mandatory checksとscope/hash/freeze guardはPASS、独立reviewはACCEPT_NO_CHANGE。変更は1 file、+10/−2（合計12 LOC）。 formatter作業ディレクトリ衝突によるHost setup失敗を1件保持し、実装再生成なしで別stageにて検証した。

実装diff（元資料: codex/B/CVB-001/implementation-01/source-edits.json） / validation（元資料: codex/B/CVB-001/validation-02/summary.json） / review（元資料: codex/B/CVB-001/review-result.json）

## 5. CVB-002 result — Policy判定集計

各AuditRecordのpolicyの有無とDecisionだけを参照し、allow/deny/confirm/unevaluatedを集計。

実装1回・code retry 0回。全mandatory checksとscope/hash/freeze guardはPASS、独立reviewはACCEPT_NO_CHANGE。変更は1 file、+10/−2（合計12 LOC）。

実装diff（元資料: codex/B/CVB-002/implementation-01/source-edits.json） / validation（元資料: codex/B/CVB-002/validation-01/summary.json） / review（元資料: codex/B/CVB-002/review-result.json）

## 6. CVB-003 result — MemoryPressure補足情報

既存evidenceを維持し、非zero親PIDが観測sample内にない行数を追加。truncatedはunknown。

実装1回・code retry 0回。全mandatory checksとscope/hash/freeze guardはPASS、独立reviewはACCEPT_NO_CHANGE。変更は1 file、+24/−4（合計28 LOC）。

実装diff（元資料: codex/B/CVB-003/implementation-01/source-edits.json） / validation（元資料: codex/B/CVB-003/validation-01/summary.json） / review（元資料: codex/B/CVB-003/review-result.json）

## 7. CVB-004 result — Provider拒否理由

provider-rejectedの理由だけに既存usageのcharged_calls/reserved_tokensを追加。

実装1回・code retry 0回。全mandatory checksとscope/hash/freeze guardはPASS、独立reviewはACCEPT_NO_CHANGE。変更は1 file、+4/−1（合計5 LOC）。

実装diff（元資料: codex/B/CVB-004/implementation-01/source-edits.json） / validation（元資料: codex/B/CVB-004/validation-01/summary.json） / review（元資料: codex/B/CVB-004/review-result.json）

## 8. CVB-005 result — 上限境界のUTF-8読取

最大65537 bytesを読み、size判定をUTF-8変換より先に行う。上限以下のinvalid UTF-8は既存の一般error。

実装1回・code retry 0回。全mandatory checksとscope/hash/freeze guardはPASS、独立reviewはACCEPT_NO_CHANGE。変更は1 file、+4/−4（合計8 LOC）。

実装diff（元資料: codex/B/CVB-005/implementation-01/source-edits.json） / validation（元資料: codex/B/CVB-005/validation-01/summary.json） / review（元資料: codex/B/CVB-005/review-result.json）

## 9. LOCとintervention

| Task | 追加 | 削除 | 合計 | 実装session | 追加code retry | review session |
| --- | --- | --- | --- | --- | --- | --- |
| CVB-001 | 10 | 2 | 12 | 1 | 0 | 1 |
| CVB-002 | 10 | 2 | 12 | 1 | 0 | 1 |
| CVB-003 | 24 | 4 | 28 | 1 | 0 | 1 |
| CVB-004 | 4 | 1 | 5 | 1 | 0 | 1 |
| CVB-005 | 4 | 4 | 8 | 1 | 0 | 1 |
| 全5件 | 52 | 13 | 65 | 5 | 0 | 5 |

LOCはfrozen initial sourceから最終sourceまでの追加+削除。全件Host formatterによる追加diffは0で、今回の値はCodex自身のコード変更量と一致する。interventionは実装sessionとreview sessionを別記録し、総数は各Task 2。code再修正の介入は0。CLI tool内の失敗（CVB-001の相対path read 2回、CVB-003のpython未検出1回）はusage/wallに含め、business candidateの再試行とは分けた。

## 10. Tokens

| Task | phase | input | cached input（内数） | output | total |
| --- | --- | --- | --- | --- | --- |
| CVB-001 | implementation | 99,152 | 64,000 | 1,435 | 100,587 |
| CVB-001 | review | 31,765 | 14,976 | 223 | 31,988 |
| CVB-002 | implementation | 105,856 | 85,376 | 1,069 | 106,925 |
| CVB-002 | review | 31,853 | 14,976 | 259 | 32,112 |
| CVB-003 | implementation | 124,359 | 103,040 | 2,237 | 126,596 |
| CVB-003 | review | 31,944 | 14,976 | 270 | 32,214 |
| CVB-004 | implementation | 87,929 | 67,840 | 617 | 88,546 |
| CVB-004 | review | 31,737 | 14,976 | 204 | 31,941 |
| CVB-005 | implementation | 69,171 | 48,896 | 1,178 | 70,349 |
| CVB-005 | review | 31,886 | 14,976 | 272 | 32,158 |
| 全5件 | 両phase計 | 645,652 | 444,032 | 7,764 | 653,416 |

これらは実行したCLI workflowの実usageであり、モデル一般能力や最小実装コストのランキングではない。raw token fieldの出典は各Taskのimplementation-01/END.jsonとreview/END.json。集約はbaseline-metrics.json（元資料: codex-baseline-recovery/baseline-metrics.json）。

## 11. Validation

全5件でacceptance、targeted regression、fmt、clippy、workspace test/check/build、Host scope/hash/freeze guardを実行しPASS。元のRust toolchain・formatter binary/config・固定check引数・テストを使用した。CVB-001〜003はLocal側の最終成功checkとB側を照合し、隔離rootの違いを除きargv一致、成功test ID一致を確認した。照合記録（元資料: codex-baseline-recovery/validation-equivalence.json）

validation起動は6回、全checkを実行したcycleは5回。CVB-001の初回Host validationは、準備時smokeが残した`.format-stage-CVB-001-1`へのmkdir衝突でcheck前に停止した。既存directoryと失敗artifactを残し、benchmark wrapperだけでstage識別子を`1000 + validation index`にした。HostFormatterの実装・挙動・binary・scope/token検証・check contractは変更していない。保存先識別子の修正であり、Codexコード不良・Local CUDA failureとは別の**benchmark Host setup failure 1件**。その失敗wallは正確に分離できずnull。validation-01の失敗とvalidation-02の成功を併存させ、実装は1回のまま。

Worker/applicationの既存sourceは不変で、旧regression証跡も保持した。このphaseでGPUは検査も使用もしておらず、現在のGPU健全性を新たに認定しない。

## 12. Wall / Host preparation workload

| Task | B実装秒 | B validation全体秒 | 内check process秒 | B review秒 | 計測phase和秒 | 開始〜review終了秒 |
| --- | --- | --- | --- | --- | --- | --- |
| CVB-001 | 89.453 | 44.093 | 23.842 | 16.422 | 149.968 | 366.489 |
| CVB-002 | 63.344 | 60.719 | 42.095 | 18.250 | 142.313 | 150.595 |
| CVB-003 | 78.297 | 60.688 | 42.391 | 20.578 | 159.563 | 167.974 |
| CVB-004 | 47.657 | 67.328 | 48.705 | 15.781 | 130.766 | 139.230 |
| CVB-005 | 63.485 | 60.985 | 42.547 | 13.797 | 138.267 | 146.610 |

全5件の実装wall 342.236秒、Host validation 293.813秒、review 84.828秒、計測phase和 720.877秒。monotonic wallでありCodexのactive reasoning timeではない。絶対時刻intervalにはorchestration・監査・Host問題対応の待ち時間が含まれる。CVB-001は準備smoke済みtarget cache、A/Bは[LOCAL_PATH]

旧準備記録はshared source追加205/削除1 LOC（acceptance 187 LOC）、Local専用marker 14 LOCとmetadata/reference packet、Task generator 124 LOC、旧benchmark harness 944 LOC。これは無償ではない。共有準備を両側へ二重計上せず、Local専用metadataを分けた旧記録をそのまま参照する。今回のbaseline回復・監査・報告scriptもbenchmark計測のためのHost作業で、実装65 LOCや純削減量に含めない。準備のactive time・phase別token・再利用時の償却量はnullのまま。旧準備記録を含む新集計（元資料: codex-baseline-recovery/paired-comparison.json）

## 13. Paired CVB-001〜003比較

| Task | A Local結果 | A Worker秒 | B実装秒 | A check秒 | B check秒 | B LOC | B total tokens |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVB-001 | First PASS | 84.250 | 89.453 | 44.422 | 23.842 | 12 | 132,575 |
| CVB-002 | PASS（repair 1） | 82.656 | 63.344 | 54.485 | 42.095 | 12 | 139,037 |
| CVB-003 | First PASS | 58.547 | 78.297 | 39.798 | 42.391 | 28 | 158,810 |

3件でA Local validation PASS、B full validation+review PASS。Aにはsame-model repairが1件、B code retryは0件。Bの実装量は合計52 LOC、実装usageは334,108 tokens、review込み430,422 tokens。A Localのinput/outputは14,790 / 725 tokensであり、Codex tokensとは換算・相殺しない。

A Worker wall計225.453秒はHost checks等を内包する。B実装wall計231.094秒はCLI実装だけなので、両値をそのまま「速い/遅い」と判断しない。Bのvalidation+review込み計測phase和は451.844秒。A側の旧host_validation_secondsはcheck processだけを合計した138.705秒であり、Bのformatter/guards込み165.500秒とは範囲が異なる。共通部分のB check process和は108.328秒。

A側の`LOCAL_FIRST_CODEX_LOC / INTERVENTIONS / TOKENS / TOTAL_WALL`は全件null。実装・fallback・reviewの**観測call数は0**だが、review未実施のため最終coding-free率、ACCEPT_NO_CHANGE、FALSE_GREEN、CODEX_CODING_AVOIDEDも未確定。0 tokensを実測した扱いにはしない。candidate reuseはfallbackなしのためN/A（jsonはnull）。`NET_CODEX_TOKENS_SAVED=null`。

これは同一frozen business contractの実装・validationを比較できる3対であり、Local-first最終reviewまで含む完了workflowの3対ではない。機械可読の全metricとnullはJSON（元資料: codex-baseline-recovery/paired-comparison.json）、短い比較表はCSV（元資料: codex-baseline-recovery/paired-comparison.csv）。

## 14. Unpaired CVB-004 / 005

CVB-004: BはPASS、5 LOC。旧AはINFRA_ERROR/CUDAのまま。CVB-005: BはPASS、8 LOC。旧AはNOT_RUNのまま。この2件は3件のpaired aggregateから完全に除外し、後続Fresh-OS Local recoveryのbaselineとして保持する。B成功で旧A failureを上書きしない。

## 15. Interim judgement

**INCONCLUSIVE**。blindなB全5件とA成功3件のpaired implementation/validationデータを取得できた。一方、Aの独立final review・実Codex usage、shared/Local-only Host準備工数の帰属が未計測で、net workflow savingsを確定できない。Local-firstが不利と認定した意味ではない。3件の低/normal risk Taskから一般化せず、Gemma26対Codexの能力順位も作らない。

## 16. Limitations / 保全 / 次の前提

旧tracked 21,401 files、封印済みLocal 326 files、B freeze 294 filesのSHA256不変を確認。旧STOP、ABORT、CUDA/raw logs、Windows events、Local 001〜003、004 failure、005 NOT_RUN、旧RESULTS_JA.md/benchmark-summary.jsonは変更しない。保全検証（元資料: codex-baseline-recovery/preservation-check.json）

主な限界は3件の小標本、A final review欠測、親Host作業のtoken/time欠測、異なるfilesystem/cache、CLI起動・tool環境失敗のoverhead。Host setup failureも隠さず残した。active timeとwall、未実施と実測0、Local tokensとCodex tokensを分けている。

このphaseはここで完了し停止する。**Local inferenceは自動再開しない。次のLocal recoveryはユーザーによるWindows rebootが必要条件**であり、新runとして旧failureを保全する。今回GPU状態の復旧・検証は実施していない。
