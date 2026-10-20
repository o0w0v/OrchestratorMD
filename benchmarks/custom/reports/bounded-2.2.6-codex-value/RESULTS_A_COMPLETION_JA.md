> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/bounded-2.2.6-codex-value.md). This report alone does not establish a task result.

# Codex Value Benchmark — Phase A Completion

実施日: 2026-10-04 JST。**CVB-001〜003のLocal-first workflowを完了し、3件とも両側でmandatory validation / contract review PASSとなった。**

判定: **LOCAL_FIRST_VALUE_CONFIRMED_FOR_SAMPLE**。今回の3件と実測CLI coding/review費用に限定した判定。Aは2件をコード変更なしで採用、1件をCodexの1行修正で完了。アカウント全体のcredit削減やHost準備込みの純便益を認定したものではない。

## 1. Local artifact freeze

開始前に旧Task Spec、final candidate、diff、validation、Worker summary、source/hash/freeze証跡を再hashした。Local封印集合を照合し、Task/contract/compact packetを含む335 filesを新しいLocal_FROZEN.json（元資料: phase-a-completion/Local_FROZEN.json）へ保存。final formatter outputとfrozen initial sourceから各candidateを復元して、全source hashが保存済みnormalized_hashesと一致し、tested_content_idとの対応、allowed region/file setを確認した。生成・再実装はしていない。

旧tracked 21,680 filesも開始時に保護。旧Local result、STOP、CUDA artifact、B baselineと旧報告は変更しない。今回のLocal inference、Ollama起動、GPU復旧、OS操作はいずれも0。新review結果は別annotationとして保存した。

## 2. Reviewer blinding

各Taskのreviewは新規独立Codex CLI session。packetはfrozen contract/allowed scope、Local final diff、最終mandatory validation summary、compact Worker summary、scope検証結果だけ。全会話やLocal repair過程のdiagnosticsは渡さず、B実装/diff/reasoning/usage・他Task解答も渡していない。

修正が必要となったCVB-002には、さらに新規fallback sessionと新規final review sessionを使用した。計5 sessionは互いにもB側10 sessionにも重ならず、fork/resumeなし。fallbackだけが自身のLocal candidate sourceを読んだ。reviewerのtool traceは自身のREVIEW_PACKET.json読取りだけで、編集0。親orchestratorはB結果を知っているが、そのconversationをCLIへ渡していない。これは入力/実traceの監査でありOS read隔離の保証ではない。

| Task | A initial review packet bytes |
| --- | --- |
| CVB-001 | 5527 |
| CVB-002 | 5790 |
| CVB-003 | 6508 |

開始前入力（元資料: phase-a-completion/blinding-before.json）、3 reviewのsession監査（元資料: phase-a-completion/session-audit.json）、fallback/追加review監査（元資料: phase-a-completion/fallback-session-audit.json）。A/Bのreview packetは同じcontract/diff/check-summary形式を使用したが、候補内容・summary・classification schemaには差がある。

## 3. Reviewer model / effort

CLI `0.158.0-alpha.2.1` / model `gpt-6-astra` / effort `xhigh`。Bと同じexecutable、`codex exec --json --ignore-user-config`を使い全sessionで固定。version stdout/stderr、binary SHA256はPLAN（元資料: phase-a-completion/PLAN.json）と隣接raw filesへ保存。runtime turn_contextのmodel/effort/cwdも検証した。Protocol、Task、acceptance、Router、Local repair policyは不変。

## 4. CVB-001 review

**ACCEPT_NO_CHANGE**。PIDのempty/unsorted/singleton/duplicate/zero/u32::MAX条件と非破壊性を満たし、diffはallowed region内。保存済みmandatory validation PASSとのhash対応も確認。Codex coding 0 LOC、fallbackなし。

review結果（元資料: codex/A/CVB-001/review-result.json） / raw usage（元資料: codex/A/CVB-001/review/END.json）

## 5. CVB-002 review

初期reviewは**ACCEPT_WITH_MINOR_FIX**。Local candidateのcounter初期値`(0, 0, 0, 0)`はi32に推論されるため、category件数が2,147,483,647を超えるsliceではexact countを満たせないという指摘。既存テストはPASSだったため、**FALSE_GREEN候補1件**として保存した。これは静的contract reviewによる境界指摘であり、数十億件の入力を確保して動的にoverflowを再現したわけではない。

旧Local PASSと既存のsemantic repair履歴はそのまま。新しい独立copyで修正し、全checksと追加reviewを経て最終PASS。

初期review（元資料: codex/A/CVB-002/review-result.json） / fallback最終review（元資料: codex/A-fallback/CVB-002/review-result.json）

## 6. CVB-003 review

**ACCEPT_NO_CHANGE**。MemoryPressureの先頭evidenceを保存し、parent_pid=0を除外した欠落親PIDの行数を追加。truncated時はunknown。その他挙動・scopeを維持。Codex coding 0 LOC、fallbackなし。

review結果（元資料: codex/A/CVB-003/review-result.json） / raw usage（元資料: codex/A/CVB-003/review/END.json）

## 7. Fallback

CVB-002のみ、Local candidateをそのままseedとして別copyへ配置。新規CLIへcontract、candidate/diff、validation summary、reviewer findingを渡し、Codexがcounterを`(0usize, 0usize, 0usize, 0usize)`へ変更した。Hostによる正解patch生成は行っていない。

1 file、追加1/削除1、**2 LOC / TRIVIAL**。生成session 1回、追加code retry 0。Host formatter → acceptance → regression → fmt → clippy → workspace test/check/build → scope/hash/freeze guardを固定条件で全実行しPASS。その後の新規独立reviewはACCEPT_NO_CHANGE。

Local editable regionは13行中12行を保持（**92.31%**）、変更file全体は169行中168行を保持（99.41%）。前者をcandidate reuseの代表値とする。SequenceMatcherによる旧行保持率であり意味的な寄与率ではない。旧candidateを破棄した再実装ではない。

Codex差分（元資料: codex/A-fallback/CVB-002/fallback-01/source-edits.json）、全validation（元資料: codex/A-fallback/CVB-002/validation-01/summary.json）、分類/計測定義（元資料: phase-a-completion/METRIC_DEFINITIONS.json）。

## 8. A Codex usage

| Task | phase | input | cached input（内数） | output | total |
| --- | --- | --- | --- | --- | --- |
| CVB-001 | review | 31,891 | 14,976 | 212 | 32,103 |
| CVB-002 | review | 31,940 | 14,976 | 901 | 32,841 |
| CVB-002 | fallback | 72,905 | 52,352 | 1,157 | 74,062 |
| CVB-002 | fallback_review | 31,980 | 14,976 | 200 | 32,180 |
| CVB-003 | review | 32,362 | 27,520 | 253 | 32,615 |
| 計 | 5 sessions | 201,078 | 124,800 | 2,723 | 203,801 |

全5 sessionでraw `turn.completed` usageを取得。各phaseのevents.jsonlとEND.jsonに保存。total=input+output、cachedはinputの内数で二重加算しない。未実施fallbackのraw usageはnull・status=NOT_INVOKEDで、CLI合計への寄与だけ0とする。Local PASSを根拠にreview usageを0と仮定していない。

## 9. B Codex usage

| Task | phase | input | cached input（内数） | output | total |
| --- | --- | --- | --- | --- | --- |
| CVB-001 | implementation | 99,152 | 64,000 | 1,435 | 100,587 |
| CVB-001 | review | 31,765 | 14,976 | 223 | 31,988 |
| CVB-002 | implementation | 105,856 | 85,376 | 1,069 | 106,925 |
| CVB-002 | review | 31,853 | 14,976 | 259 | 32,112 |
| CVB-003 | implementation | 124,359 | 103,040 | 2,237 | 126,596 |
| CVB-003 | review | 31,944 | 14,976 | 270 | 32,214 |
| 計 | 6 sessions | 424,929 | 297,344 | 5,493 | 430,422 |

前phaseのblind baseline実測をそのまま再利用。Bの実装・review・usageは再生成/上書きしていない。元証跡はbaseline metrics（元資料: codex-baseline-recovery/baseline-metrics.json）と旧B報告（元資料: RESULTS_CODEX_BASELINE_JA.md）。CVB-004/005を分母へ含めない。

## 10. Task別token savings

| Task | A review | A fallback | A追加review | A合計 | B合計 | CLI差 B−A | 削減率 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVB-001 | 32,103 | 0 | 0 | 32,103 | 132,575 | 100,472 | 75.7850% |
| CVB-002 | 32,841 | 74,062 | 32,180 | 139,083 | 139,037 | -46 | -0.0331% |
| CVB-003 | 32,615 | 0 | 0 | 32,615 | 158,810 | 126,195 | 79.4629% |

CVB-002ではfallbackと追加reviewを含めるとAが46 tokens多い。Taskごとに必ずtoken削減するとは言えず、修正と再reviewの費用は小さなコード変更でも発生する。

## 11. Aggregate token savings

`CLI_CODEX_TOKENS_SAVED = 430,422 − 203,801 = 226,621`

`CLI_CODEX_TOKEN_REDUCTION_RATE = 226,621 / 430,422 = 52.6509%`

同じ3 Task、同じCLI version/model/effortで、Aはreview+fallback+追加review、Bはimplementation+reviewを合計。Local modelのinput 14,790 / output 725 tokensは別欄で保持し、Codex tokenから引いていない。

これは**実行されたCLI session群に限定したtoken差**。親orchestration、harness開発、準備のCodex usageは未計測。TOTAL_CODEX_CREDITS_SAVEDとは呼ばず、アカウント全体/Host込み純削減量はnullのまま。

## 12. Coding LOC comparison

| Task | A Codex LOC | B Codex LOC | A coding sessions | B coding sessions | A coding avoided |
| --- | --- | --- | --- | --- | --- |
| CVB-001 | 0 | 12 | 0 | 1 | True |
| CVB-002 | 2 | 12 | 1 | 1 | False |
| CVB-003 | 0 | 28 | 0 | 1 | True |
| 計 | 2 | 52 | 1 | 3 | 2/3 (66.67%) |

LOCは追加+削除。AはLocal candidateからのCodex変更、Bはinitial sourceからのCodex実装量。A review sessionは初期3+追加1、B reviewは3。review自体のコード変更は0。初回ACCEPT_NO_CHANGE率は2/3であり、fallback後の最終完了3/3と混同しない。

## 13. Wall comparison

| Task | Local Worker秒 | A review秒 | A fallback秒 | A再validation秒 | A追加review秒 | A phase和秒 | B phase和秒 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVB-001 | 84.250 | 13.844 | 0.000 | 0.000 | 0.000 | 98.094 | 149.968 |
| CVB-002 | 82.656 | 42.985 | 61.156 | 64.156 | 15.610 | 266.563 | 142.313 |
| CVB-003 | 58.547 | 20.000 | 0.000 | 0.000 | 0.000 | 78.547 | 159.563 |

AはLocal Worker内のvalidationを二重加算せず、今回review/fallback/full validation/追加reviewだけを加算。A計443.204秒。Bは実装231.094 + Host validation 165.500 + review 55.250 = 451.844秒。これは計測phaseのwall和で、親の作業・待機時間や正確なactive timeを表さない。A/Bのfilesystem、cache、CLI実行時刻が異なり、厳密なspeed rankingはしない。CVB-002ではA wallが増加している。

## 14. Quality / FALSE_GREEN

両側とも最終mandatory validation / contract reviewは3/3 PASS。Aの002だけは旧PASSに未検出の境界問題があり、FALSE_GREEN候補1件を残す。旧Local resultをFAILへ改変したり、後の修正でこの発見を消したりしない。fallback後の未解決review指摘は0。

今回の指摘に対するB側のread-only確認では、保存済みB-002は初めからusize counterを使用しており同じ問題はない。この確認結果はA CLIへ渡していない。テストは有限例であり、PASSだけで全境界を証明したとは扱わない。今回の経験からacceptance・Protocolを変更することはしていない。

## 15. Host prep caveat

旧preparation記録（元資料: benchmark-summary.json）をそのまま参照。paired 3件のSHARED_PREPはsource追加116 LOC（acceptance 101 LOC）、LOCAL_ONLY_PREPはmarker 8 LOC、生成metadata 16,320 bytesとreference 6,071 bytes。共有準備をA/Bへ二重加算しない。旧Task generator 124 LOC、benchmark harness 944 LOC、今回のreview/fallback orchestration・監査・集計もBENCHMARK_ONLY_PREPとして別扱いで、無償とはしない。

これらの作業時間/親Codex tokenは正確にphase帰属できずnull。LOCや文字数をtokenへ換算してCLI_CODEX_TOKENS_SAVEDへ加減していない。準備再利用時の償却効果も今回の数値から推定しない。

## 16. Decision

**LOCAL_FIRST_VALUE_CONFIRMED_FOR_SAMPLE**。

この3件では、最終品質条件を両側で揃えた後も、実測CLI tokensが52.65%少なく、Codex coding量は52→2 LOC、coding sessionは3→1。2件がcoding-freeで、1件のfallbackもLocal bodyを92.31%保持した。これが限定判定の根拠。

一方でCVB-002はtoken差がほぼゼロでwall増、FALSE_GREEN候補も1件ある。全Task・一般的model能力・全Codex作業費用について優位と結論しない。

## 17. Limitations / 保存 / 停止

3件の小標本、親/Host preparation費用欠測、実行順序とcache差、review stochasticity、A/B classification schema差、静的な境界指摘を含む。cached inputは報告上のinputの内数であり、token削減率を金額やcredit削減率に読み替えない。

旧cohortはINCONCLUSIVE / STOPPED_INFRA_ERRORのまま。新phaseの判定はこの3件の完了workflowだけに適用する。旧Local、B baseline、STOP、CUDA/Windows eventsを保持し、CVB-004/005は集計に含めない。

全Task metrics / aggregate（元資料: phase-a-completion/workflow-summary.json）、比較CSV（元資料: phase-a-completion/paired-comparison.csv）、A freeze（元資料: phase-a-completion/A_FROZEN.json）、最終保全監査（元資料: phase-a-completion/final-verification.json）。

このphaseはここで完了。Local inference、GPU recovery、Windows rebootは開始も要求もしない。CVB-004/005のLocal recoveryは別phaseとする。
