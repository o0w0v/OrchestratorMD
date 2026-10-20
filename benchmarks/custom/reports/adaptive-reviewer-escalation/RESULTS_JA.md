> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/adaptive-reviewer-escalation.md). This report alone does not establish a task result.

# Adaptive Reviewer Escalation Benchmark

判定: **SOL6_ONLY_SUFFICIENT**。この標本では6 Sol単独が全品質基準を満たし最安で、追加reviewによる品質改善を観測しなかった。

## 1. 目的と固定条件

6 Sol初回reviewから、finding・不確実性等がある場合だけ6.1 Solへ上げる方式の品質とcreditsを比較した。
Planner / Executor / Primaryはgpt-6-sol、Secondaryと単独baselineはgpt-6.1-sol。
全session xhigh / Standard、CLI 0.160.0。production Router、bounded 2.2.6、model policyは変更なし。Local inferenceは0。

## 2. 新規Task

| Task | 新規business contract | mandatory checks | Executor retry |
| --- | --- | --- | --- |
| ARE-001 | Memory occupancy gauge in basis points | PASS | 0 |
| ARE-002 | Consecutive audit source run compression | PASS | 0 |
| ARE-003 | Observed direct-child RSS totals | PASS | 0 |
| ARE-004 | Occurrence-aware shared evidence | PASS | 0 |
| ARE-005 | Nearest-rank recorded latency percentile | PASS | 1 |
| ARE-006 | Stable event grouping with merged exact evidence | PASS | 0 |
| ARE-007 | Latest intent verification projection | PASS | 0 |
| ARE-008 | Observation freshness with explicit future clock state | PASS | 0 |

初回mandatory validationは7/8 PASS、ARE-005だけclippy::manual_div_ceilで1回retryし、最終8/8 PASS。
途中の進捗表示で最終PASSを初回PASSと誤認した点は訂正記録（元資料: preliminary-status-correction.json）に保存。raw結果は変更していない。

既存RSP/P224/CVB/OSLは通常Taskに再利用していない。既存データ型を使う独立copy内の小さな純粋関数であり、実production workload全体を代表する標本ではない。

## 3. Freezeとblinding

実測前にcontract・source・interface・validation・prompt・判定規則・mutations・公式rate・CLI hashをFREEZE.json（元資料: FREEZE.json）へ固定。
Planner結果、全candidate packet、全review結果も段階別sealで固定した。
候補はmandatory validationでのみ1回修正可能とし、測定reviewを見た候補選別や修正は行っていない。
candidate-truth.json（元資料: candidate-truth.json）はreview開始前のcontract/diff確認と固定hidden probeに基づく。
説明誤りを別計上する基準もDESIGN.md（元資料: DESIGN.md）で事前登録し、前回のposthoc判定とは分離した。

A=6.1 Sol単独、B=6 Sol単独、C=Adaptive。A/Bのbase packetはbyte SHA256一致。
C PrimaryはBの同一sessionを再利用し、重複課金なし。Secondaryにはbase packetとPrimaryの全reviewを追加し、独立再評価を指示。
追加内容のあるSecondaryとAは同一requestではないため、AをSecondaryとして使い回していない。
別session・別directory・入力hash・tool traceで確認した。directory分離はOSレベルのread隔離証明ではない。

## 4. Controlled sentinel

ARE-009: nearest roundingをfloorへ変更。total=6, available=5で1667のはずが1666。
ARE-010: multiset intersectionをmembership filterへ変更。left=[a,a], right=[a]で[a]のはずが[a,a]。
ARE-011: 最新row選択前にverification=Noneを捨てる。古いtrueと最新Noneから、Noneのはずがtrueを返す。

3件は事前登録したHost oracleのcontrolled mutationで、自然Executorの失敗ではない。
通常mandatory checksは実際に全PASS、固定hidden probeは全FAIL。対応する自然候補はhidden probeもPASS。
過去のFIFO refresh / traversal depth capとは異なる。sentinelを自然成功率へ混ぜない。

## 5. Quality

| 群 | 方式 | 件数 | 真の欠陥 | 有効検出 | FN | FP | 説明誤り | 厳格品質PASS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| natural | A_SOL61_ALWAYS | 8 | 0 | 0 | 0 | 0 | 0 | 8 |
| natural | B_SOL6_ONLY | 8 | 0 | 0 | 0 | 0 | 0 | 8 |
| natural | C_ADAPTIVE | 8 | 0 | 0 | 0 | 0 | 0 | 8 |
| controlled | A_SOL61_ALWAYS | 3 | 3 | 3 | 0 | 0 | 0 | 3 |
| controlled | B_SOL6_ONLY | 3 | 3 | 3 | 0 | 0 | 0 | 3 |
| controlled | C_ADAPTIVE | 3 | 3 | 3 | 0 | 0 | 0 | 3 |
| combined | A_SOL61_ALWAYS | 11 | 3 | 3 | 0 | 0 | 0 | 11 |
| combined | B_SOL6_ONLY | 11 | 3 | 3 | 0 | 0 | 0 | 11 |
| combined | C_ADAPTIVE | 11 | 3 | 3 | 0 | 0 | 0 | 11 |

有効なcore findingと説明の正しさは独立計数。正しい問題を指摘しても反例の数値や因果が誤っていれば説明誤り。
MISSED_ESCALATIONは0、UNNECESSARY_ESCALATIONは0。
正誤adjudicationは同じHost orchestratorによるため、独立した人間の評価panelではない。

## 6. Task別review・escalation

| case | 群 | Primary | finding数 | 説明正確 | escalated | Secondary | 説明正確 | 最終 | Primary credits | Secondary credits | 計 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ARE-001 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 1.16576 | 0.00000 | 1.16576 |
| ARE-002 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 1.15321 | 0.00000 | 1.15321 |
| ARE-003 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 0.58676 | 0.00000 | 0.58676 |
| ARE-004 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 0.58631 | 0.00000 | 0.58631 |
| ARE-005 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 0.63321 | 0.00000 | 0.63321 |
| ARE-006 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 0.64171 | 0.00000 | 0.64171 |
| ARE-007 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 0.60026 | 0.00000 | 0.60026 |
| ARE-008 | natural | ACCEPT_NO_CHANGE | 0 | True | False | N/A | N/A | ACCEPT_NO_CHANGE | 1.12896 | 0.00000 | 1.12896 |
| ARE-009 | controlled | REJECT | 1 | True | True | REJECT | True | REJECT | 0.82331 | 1.23436 | 2.05767 |
| ARE-010 | controlled | REJECT | 1 | True | True | REJECT | True | REJECT | 0.60431 | 1.21221 | 1.81652 |
| ARE-011 | controlled | REJECT | 1 | True | True | REJECT | True | REJECT | 0.66586 | 0.61174 | 1.27760 |

Secondary未実行のclassification・説明判定はN/A、creditsは0 callに対する0。未取得tokensを0へ変換していない。
詳しいfinding、flags、gate理由、正誤根拠はsummaries/cases.json（元資料: summaries/cases.json）。

## 7. Findingの照合

- ARE-009 / primary: Floor division violates nearest rounding. Counterexamples total=20000, available=19999 (0 vs 1) and 19997 (1 vs 2, when cited) are arithmetically correct. The frozen plan lists these examples and the reported targeted-regression suite passed; these are separate true facts, not evidence that each proposed example ran. raw review（元資料: reviews/ARE-009/primary/answer.json）
- ARE-009 / always61: Floor division violates nearest rounding. Counterexamples total=20000, available=19999 (0 vs 1) and 19997 (1 vs 2, when cited) are arithmetically correct. The frozen plan lists these examples and the reported targeted-regression suite passed; these are separate true facts, not evidence that each proposed example ran. raw review（元資料: reviews/ARE-009/always61/answer.json）
- ARE-009 / secondary: Floor division violates nearest rounding. Counterexamples total=20000, available=19999 (0 vs 1) and 19997 (1 vs 2, when cited) are arithmetically correct. The frozen plan lists these examples and the reported targeted-regression suite passed; these are separate true facts, not evidence that each proposed example ran. raw review（元資料: reviews/ARE-009/secondary/answer.json）
- ARE-010 / primary: contains does not consume occurrences. Both the three-x versus one-x example and xyxx versus xxy example (when cited) correctly distinguish actual membership filtering from required multiset counts/order. raw review（元資料: reviews/ARE-010/primary/answer.json）
- ARE-010 / always61: contains does not consume occurrences. Both the three-x versus one-x example and xyxx versus xxy example (when cited) correctly distinguish actual membership filtering from required multiset counts/order. raw review（元資料: reviews/ARE-010/always61/answer.json）
- ARE-010 / secondary: contains does not consume occurrences. Both the three-x versus one-x example and xyxx versus xxy example (when cited) correctly distinguish actual membership filtering from required multiset counts/order. raw review（元資料: reviews/ARE-010/secondary/answer.json）
- ARE-011 / primary: Filtering verification=None before maximum selection resurrects an older verified row; the 100/200 timestamp example is correct, as is the equal-timestamp last-unverified example when cited. raw review（元資料: reviews/ARE-011/primary/answer.json）
- ARE-011 / always61: Filtering verification=None before maximum selection resurrects an older verified row; the 100/200 timestamp example is correct, as is the equal-timestamp last-unverified example when cited. raw review（元資料: reviews/ARE-011/always61/answer.json）
- ARE-011 / secondary: Filtering verification=None before maximum selection resurrects an older verified row; the 100/200 timestamp example is correct, as is the equal-timestamp last-unverified example when cited. raw review（元資料: reviews/ARE-011/secondary/answer.json）

ARE-009には、planにあるexact-tie例と実行済みtargeted-regressionのPASSを並べる表現がある。
本採点では3 armとも「plan記載」と「suite全体の報告」の2事実への言及として一貫して読んだ。
Hostは、これらの予定例が個別に実行されPASSしたとは認定していない。実行argvは固定suiteであり、planの提案例を自動追加していない。
特にPrimaryの“that check”は個別caseの実行と読める曖昧さが残る。これを断言と読む厳格な評価では説明品質は未確定になるため、
この言い回しの差だけでSecondaryの品質改善を主張しない。raw findingとadjudication.json（元資料: adjudication.json）に解釈を残した。
数値・出現回数・timestampの具体的反例は、explanation-probes（元資料: explanation-probes/）の独立copyで実行確認した。

## 8. 公式rateとcredits

取得元: 公式Codex Pricing（元資料: http[LOCAL_PATH]）。取得日時・raw row・SHAはrates/rate-card.json（元資料: rates/rate-card.json）。
Standard / 100万tokens: 6 Sol=50 / 5 / 250、6.1 Sol=50 / 2.5 / 250（uncached input / cached input / output）。
uncachedとoutputの単価は同じで、6.1 Solのcached単価は低い。モデル名だけから6 Solの1 token単価が安いとは扱わない。
実際の生成量・キャッシュ・tool呼び出し量を含むraw usageから算出したtoken-rate換算creditsであり、請求書額ではない。

| 群 | A 6.1常時 | B 6のみ | C Adaptive | A−C節約 | 削減率 | escalation | missed | unnecessary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| natural | 9.16878 | 6.49618 | 6.49618 | 2.67260 | 29.15% | 0/8 | 0 | 0 |
| controlled | 3.01251 | 2.09348 | 5.15179 | -2.13928 | -71.01% | 3/3 | 0 | 0 |
| combined | 12.18129 | 8.58966 | 11.64797 | 0.53332 | 4.38% | 3/11 | 0 | 0 |

Combinedは人工的に3/11の欠陥率を作った混合。通常運用の欠陥率・escalation率へ外挿しない。
自然Taskとcontrolled Taskのコストを別々に示し、採用判断は品質優先とした。

## 9. 実usage・全実験コスト

| role | unique sessions | input | cached | uncached | output | credits | wall秒合計 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| planner | 8 | 815404 | 665728 | 149676 | 27065 | 17.57869 | 998.7 |
| executor | 9 | 750304 | 614784 | 135520 | 14648 | 13.51192 | 557.3 |
| reviewer-primary | 11 | 377751 | 257792 | 119959 | 5211 | 8.58966 | 270.6 |
| reviewer-always61 | 11 | 389256 | 178816 | 210440 | 4849 | 12.18129 | 312.2 |
| reviewer-secondary | 3 | 106726 | 57984 | 48742 | 1905 | 3.05831 | 106.9 |

全unique session 42件、54.91987 credits。
raw turn.completed usage、input/cached/uncached/output/total、model/effort/runtime照合はsummaries/sessions.json（元資料: summaries/sessions.json）。
BとCの論理比較を足して二重課金した総額ではない。Parentの準備・集計・adjudication tokensはnullで、benchmark role費用とは分離。
wallは並列実行や検証待ちの影響を受ける。単発測定で、cache hitの再現性や長期latencyを保証しない。

## 10. 保全・検証

既存Worker suite、Rust fmt/clippy/workspace test/check/build、escalation predicate tests: PASS。
事前tracked 29940ファイルのhashを確認し、旧結果・productionは変更なし。
全freezeと42 unique CLI sessionの入力・runtimeを監査。詳細はsummaries/integrity-audit.json（元資料: summaries/integrity-audit.json）。
fixture準備時のWSL sandboxアクセス拒否は保存し、許可済みtoolchain実行で準備を完了した。これはモデル品質失敗に含めていない。

## 11. 判定と限界

**SOL6_ONLY_SUFFICIENT**。この標本では6 Sol単独が全品質基準を満たし最安で、追加reviewによる品質改善を観測しなかった。
今回だけでADAPTIVE_REVIEWER_CONFIRMEDとはしない。8自然Task・3controlled defect、各モデル1回の小標本であり、
前回の説明誤りが二度と発生しない保証も、高riskや大きなdiffでの品質保証もない。
controlled defectには露呈する明示contractがあり、より曖昧・複雑な実案件への一般化には独立した確認が必要。
SecondaryがPrimaryを見る条件は実運用に合わせたもので、anchoringの影響を分離した実験ではない。
本結果からproduction Routerへの自動反映は行わない。
