> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/role-separated-codex-routing.md). This report alone does not establish a task result.

# Role-Separated Codex Routing Benchmark

集計日時: 2026-10-04T15:08:43.693724+00:00

Phase 1: **PLANNER_6_SOL_DEFAULT**

Phase 2: **REVIEWER_6_1_SOL_DEFAULT**

## 1. Rate freeze

取得: 2026-10-04T13:52:41.047286+00:00。raw公式文書、URL、SHA256をrates/rate-card.json（元資料: rates/rate-card.json）へ保存。
全roleはxhigh / Standard設定。CLIは--ignore-user-config、fast_mode=false、service tier overrideなし。runtime model/effortもsessionログで照合。

| Model | uncached input | cached input | output（credits / 1M） |
| --- | --- | --- | --- |
| gpt-6-astra | 250.0000 | 25.0000 | 1250.0000 |
| gpt-6.1-sol | 50.0000 | 2.5000 | 250.0000 |
| gpt-6-sol | 50.0000 | 5.0000 | 250.0000 |

公式Codex pricing（元資料: http[LOCAL_PATH]）を使用。uncached=input−cached、credits=(uncached×input rate+cached×cached rate+output×output rate)/1M。
USDは公式Astra（元資料: http[LOCAL_PATH]）、6.1 Sol（元資料: http[LOCAL_PATH]）、6 Sol（元資料: http[LOCAL_PATH]）のtoken単価によるequivalentであり、実請求額ではない。JPY=null。実際の個別credit購入価格・accountの請求tier・cache-write別課金は推定しない。

## 2. Task一覧

| Task | 新規business task | 分類 | risk |
| --- | --- | --- | --- |
| RSP-001 | Clamped sample-page bounds | simple bounded edit | low |
| RSP-002 | Inventory presence mask | simple bounded edit | low |
| RSP-003 | Conservative process sample change list | semantic multi-step edit | normal |
| RSP-004 | Filtered chronological audit page | semantic multi-step edit | normal |
| RSP-005 | Top-RSS sample ranking regression | debugging | normal |
| RSP-006 | Preview session dedup decisions from repository contract | repo evidence interpretation | normal |
| RSP-007 | Shared optional-inventory label formatter | interface-preserving refactor | normal |
| RSP-008 | Bounded ancestry projection with ambiguous rows | Codex boundary candidate | normal |

実repoの型・trait・既存docsに基づくisolated Rust fixture。P224/CVB/OSLのbusiness contractは再利用していない。
初期source、依頼、allowed files、interface、同一acceptance、validation、global constraintsをFREEZE.json（元資料: FREEZE.json）で全Planner開始前に固定した。
初期stub/bugは失敗、非公開Host参考実装は同じchecksでPASSを確認。RSP-007は初期behaviorがPASSだが指定の共通helper構造が欠けるrefactor。

## 3. Planner outputs

24 planはruns/（元資料: runs/）の各Task/arm/planner/answer.json。arm a=Astra、b=6.1 Sol、c=6 Sol。全planをPLANNERS_FROZEN.json（元資料: PLANNERS_FROZEN.json）で固定してからExecutorを開始。

| Task | Astra boundary | 6.1 Sol boundary | 6 Sol boundary |
| --- | --- | --- | --- |
| RSP-001 | LOCAL | LOCAL | LOCAL |
| RSP-002 | LOCAL | LOCAL | LOCAL |
| RSP-003 | LOCAL | LOCAL | CODEX |
| RSP-004 | LOCAL | LOCAL | CODEX |
| RSP-005 | LOCAL | LOCAL | CODEX |
| RSP-006 | LOCAL | LOCAL | CODEX |
| RSP-007 | LOCAL | LOCAL | LOCAL |
| RSP-008 | SPLIT_THEN_LOCAL | SPLIT_THEN_LOCAL | SPLIT_THEN_LOCAL |

Plannerには共通依頼と初期source、Executorには自armのplanと初期sourceのみを渡した。独立sessionでfork/resumeなし。他armのplan/diff/診断は渡していない。

## 4. Planner quality defects

6 SolのRSP-006でconstructor signatureがReferencePlanに含まれず、Executorも不足を申告した。PLANNER_MISSING_REFERENCE（minor）1件とadjudicateしたが、正しいconstructorを使用できておりcompile failure・retry・quality REJECTは起こしていない。その他のHost検証コマンド・source hash・Git metadataの不足申告は、意図したHost/Executor分離に由来し、Planner欠陥に数えていない。PLANNER_NO_DEFECTは下流で欠陥を観測しなかった意味である。

| Planner | 観測defect数 / 8 | rate |
| --- | --- | --- |
| gpt-6-astra | 0 | 0.0000 |
| gpt-6.1-sol | 0 | 0.0000 |
| gpt-6-sol | 1 | 0.1250 |
| Task | arm | adjudicated categories | 根拠 |
| --- | --- | --- | --- |
| RSP-006 | c | PLANNER_MISSING_REFERENCE | All final diffs are identical wrappers over a new Deduplicator per call, preserving current key/FIFO/zero-capacity semantics and input order; all checks/reviews pass. The frozen c ReferencePlan omits Deduplicator::new(capacity: usize) -> Self, unlike a/b. Executor explicitly reports this missing constructor signature and assumes it; its tool trace does not read lib.rs. Classify a concrete nonfatal Planner reference-packet omission. No compile failure, retry or measured downstream penalty resulted, and source was available for inspection. This is not a quality rejection. |

全24 armの確認はphase1-adjudication.json（元資料: phase1-adjudication.json）。Reviewer claimsとExecutor自己申告を保存し、実装FAILだけでPlanner欠陥と判定していない。

## 5. Executor結果

| Planner arm | Final quality PASS / 8 | First validation PASS / 8 | retry | LOC |
| --- | --- | --- | --- | --- |
| gpt-6-astra | 8 | 8 | 0 | 181 |
| gpt-6.1-sol | 8 | 8 | 0 | 203 |
| gpt-6-sol | 8 | 7 | 1 | 179 |

Executorは全arm 6 Sol/xhigh。First PASSは初回mandatory validationのPASS。最終qualityには独立6 Sol ReviewerのACCEPT_NO_CHANGEも必要。
初回+再実装1回が上限。検証failureまたはreview findingは同じ残り1回の予算を使用し、Planner packetは変更していない。
唯一の初回FAILはRSP-004 / 6 Sol plan経路のclippy::manual_contains。意味・acceptanceはPASSし、Executorが選んだiter().any()だけがlintで拒否された。frozen planはこの書き方を要求していないため、Executor lint failureに分類した。実diagnosticsを受けた独立6 Sol retry 1回でcontainsへ変更し、全mandatory checksを再実行してPASS。通常bounded Workerのlint eligibilityは変更していない。

## 6. Reviewer結果

Phase 1の最終reviewは24/24 ACCEPT_NO_CHANGE。自然candidateの契約違反・scope違反・FALSE_GREENはadjudicationで観測されなかった。First validation FAILを成功に書き換えず、RSP-004/cの初回失敗とretryを保持した。

Phase 1 Reviewerは全arm 6 Sol。original request / frozen plan / final diff / mandatory checks / concise Executor summaryのみ。
Phase 2はPhase 1の推奨Plannerと固定6 Sol Executorが作った同一candidate packetを比較。自然candidateの6 Sol reviewは同一のPhase 1 sessionを再利用し、二重課金していない。

## 7. Model別usage

| model | role | sessions | input | cached | uncached | output |
| --- | --- | --- | --- | --- | --- | --- |
| gpt-6-astra | planner | 8 | 535981 | 348800 | 187181 | 23777 |
| gpt-6-astra | reviewer | 10 | 350559 | 149760 | 200799 | 3659 |
| gpt-6.1-sol | planner | 8 | 540980 | 349824 | 191156 | 31421 |
| gpt-6.1-sol | reviewer | 10 | 351505 | 176384 | 175121 | 4555 |
| gpt-6-sol | planner | 8 | 926411 | 766848 | 159563 | 29701 |
| gpt-6-sol | executor | 24 | 2115531 | 1807744 | 307787 | 43168 |
| gpt-6-sol | retry | 1 | 115935 | 90880 | 25055 | 896 |
| gpt-6-sol | reviewer | 26 | 899127 | 629888 | 269239 | 8599 |

全usageはraw turn.completedから取得。cachedはinputの内数。文字数推定なし。raw response、session ID、CLI/runtime照合はphase1-sessions（元資料: summaries/phase1-sessions.json）、phase2-sessions（元資料: summaries/phase2-sessions.json）。

## 8. Model別credits

| model | role | credits | USD equivalent |
| --- | --- | --- | --- |
| gpt-6-astra | planner | 85.2365 | 3.4095 |
| gpt-6-astra | reviewer | 58.5175 | 2.3407 |
| gpt-6.1-sol | planner | 18.2876 | 0.7315 |
| gpt-6.1-sol | reviewer | 10.3358 | 0.4134 |
| gpt-6-sol | planner | 19.2376 | 0.7695 |
| gpt-6-sol | executor | 35.2201 | 1.4088 |
| gpt-6-sol | retry | 1.9311 | 0.0772 |
| gpt-6-sol | reviewer | 18.7611 | 0.7504 |

実行した独立sessionは95件。重複を除いた合計 247.5274 credits / $9.9011 equivalent。親chatの準備・集計・Host oracleは含まない（token=null）。

## 9. Pipeline credits

| Planner | Planner | Executor初回 | Reviewer全回 | Executor retry | Total |
| --- | --- | --- | --- | --- | --- |
| gpt-6-astra | 85.2365 | 12.1810 | 5.4692 | 0 | 102.8866 |
| gpt-6.1-sol | 18.2876 | 13.4418 | 7.2419 | 0 | 38.9714 |
| gpt-6-sol | 19.2376 | 9.5973 | 4.6848 | 1.9311 | 35.4509 |
| Task | Astra pipeline | 6.1 Sol pipeline | 6 Sol pipeline |
| --- | --- | --- | --- |
| RSP-001 | 11.8697 | 5.0397 | 4.6597 |
| RSP-002 | 10.9946 | 4.7442 | 3.1973 |
| RSP-003 | 15.6990 | 5.1755 | 4.6151 |
| RSP-004 | 12.0762 | 4.5353 | 7.6366 |
| RSP-005 | 12.3034 | 3.9459 | 4.2222 |
| RSP-006 | 12.8594 | 4.9516 | 3.3464 |
| RSP-007 | 11.0655 | 5.0353 | 3.2114 |
| RSP-008 | 16.0188 | 5.5439 | 4.5623 |

失敗armも消費費用は残すがcheapest passingから除外。Reviewer再実行はReviewer列、Executor再実装はRetry列にのみ計上。

## 10. Planner net benefit

| Task | Planner | extra Planner credits | downstream avoided | net benefit |
| --- | --- | --- | --- | --- |
| RSP-001 | gpt-6-astra | 7.0159 | -0.1942 | -7.2101 |
| RSP-001 | gpt-6.1-sol | -0.4566 | -0.8367 | -0.3801 |
| RSP-002 | gpt-6-astra | 7.3777 | -0.4196 | -7.7973 |
| RSP-002 | gpt-6.1-sol | 0.3534 | -1.1936 | -1.5469 |
| RSP-003 | gpt-6-astra | 9.7552 | -1.3287 | -11.0838 |
| RSP-003 | gpt-6.1-sol | -0.0063 | -0.5667 | -0.5604 |
| RSP-004 | gpt-6-astra | 6.2326 | 1.7930 | -4.4396 |
| RSP-004 | gpt-6.1-sol | -1.8687 | 1.2326 | 3.1013 |
| RSP-005 | gpt-6-astra | 7.7328 | -0.3484 | -8.0812 |
| RSP-005 | gpt-6.1-sol | -0.6358 | -0.3594 | 0.2763 |
| RSP-006 | gpt-6-astra | 9.4017 | -0.1113 | -9.5130 |
| RSP-006 | gpt-6.1-sol | 0.8105 | -0.7948 | -1.6052 |
| RSP-007 | gpt-6-astra | 7.5678 | -0.2863 | -7.8542 |
| RSP-007 | gpt-6.1-sol | 0.1617 | -1.6622 | -1.8239 |
| RSP-008 | gpt-6-astra | 10.9152 | -0.5413 | -11.4565 |
| RSP-008 | gpt-6.1-sol | 0.6919 | -0.2897 | -0.9817 |

比較基準は6 Sol Planner。両pipelineがquality PASSの場合のみ算出し、非比較可能pairはnull。
AggregateでAstraは6 SolよりPlanner費用が65.99886 credits高く、downstream削減は−1.43689 credits、net benefitは−67.43575 credits。Astraだけが防いだfailureは0件で、defaultにする経済根拠はこの標本では得られない。6.1 SolはPlanner単体で0.95003 credits安く、First PASS 8/8かつ参照欠落0だったが、downstreamは4.47050 credits多く、net benefitは−3.52047 credits。6.1 Solが最安だったRSP-004/005は記録するが、Task IDから後付けのproduction routing ruleは作らない。cache比率・sessionのtool usage差も含む実測値であり、1回のlint回避だけをPlannerの因果効果と断定しない。

## 11. Cheapest passing Planner

| Task | cheapest passing Planner |
| --- | --- |
| RSP-001 | gpt-6-sol |
| RSP-002 | gpt-6-sol |
| RSP-003 | gpt-6-sol |
| RSP-004 | gpt-6.1-sol |
| RSP-005 | gpt-6.1-sol |
| RSP-006 | gpt-6-sol |
| RSP-007 | gpt-6-sol |
| RSP-008 | gpt-6-sol |
| Planner | cheapest count | aggregate net benefit |
| --- | --- | --- |
| gpt-6-astra | 0 | -67.4357 |
| gpt-6.1-sol | 2 | -3.5205 |
| gpt-6-sol | 6 | 0.0000 |

Phase 1判定: **PLANNER_6_SOL_DEFAULT**。詳細選択はphase1-selection.json（元資料: summaries/phase1-selection.json）。

## 12. Reviewer comparison

| Reviewer | core検出同等 / cases | 根拠まで同等 / cases | natural defects | sentinel defects | false positive | 説明誤り | credits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gpt-6-astra | 10/10 | 10/10 | 0 | 2 | 0 | 0 | 58.5175 |
| gpt-6.1-sol | 10/10 | 10/10 | 0 | 2 | 0 | 0 | 10.3358 |
| gpt-6-sol | 10/10 | 9/10 | 0 | 2 | 0 | 1 | 6.0500 |
| Case | Reviewer | classification | finding count | valid defects | false positives | 説明誤り | credits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RV-001 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.5354 |
| RV-001 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.1169 |
| RV-001 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5316 |
| RV-002 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.6251 |
| RV-002 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.0898 |
| RV-002 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5623 |
| RV-003 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.8772 |
| RV-003 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.1882 |
| RV-003 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.6048 |
| RV-004 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.7739 |
| RV-004 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5299 |
| RV-004 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5825 |
| RV-005 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.6634 |
| RV-005 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.0991 |
| RV-005 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.6572 |
| RV-006 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.7421 |
| RV-006 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.1256 |
| RV-006 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5659 |
| RV-007 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.7747 |
| RV-007 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 1.1478 |
| RV-007 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5407 |
| RV-008 | gpt-6-astra | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 5.9836 |
| RV-008 | gpt-6.1-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.5881 |
| RV-008 | gpt-6-sol | ACCEPT_NO_CHANGE | 0 | 0 | 0 | 0 | 0.6400 |
| RV-009 | gpt-6-astra | REJECT | 1 | 1 | 0 | 0 | 6.3154 |
| RV-009 | gpt-6.1-sol | REJECT | 1 | 1 | 0 | 0 | 1.2175 |
| RV-009 | gpt-6-sol | REJECT | 1 | 1 | 0 | 1 | 0.6737 |
| RV-010 | gpt-6-astra | REJECT | 1 | 1 | 0 | 0 | 6.2267 |
| RV-010 | gpt-6.1-sol | REJECT | 1 | 1 | 0 | 0 | 1.2330 |
| RV-010 | gpt-6-sol | REJECT | 1 | 1 | 0 | 0 | 0.6916 |

valid/false-positiveの個別根拠はphase2-adjudication.json（元資料: phase2-adjudication.json）。known defect未検出と不要なREJECTをquality不一致として扱う。

## 13. Quality sentinel findings

RV-009はduplicate hitをFIFO末尾へ移動する改変、RV-010はmax_nodes.min(8)による隠れたdepth cap。両方とも3 Reviewerが実在するcontract defectを検出しREJECTした。Astraだけの有効findingは0件。RV-009/cの反例はA,B,A,C,B / capacity=2についてexpectedとcandidateを逆に記載していた。追加のadjudication probeで、実際はclean=[0,1,3]、mutant=[0,1,3,4]と確認した。指摘箇所・不具合検出は正しいのでfalse positiveにはしないが、説明誤り1件として別記録する。この補助probeはreview freeze後の根拠検証だけに使用し、元のacceptance・candidate・reviewを変更していない。

事前freezeした2件のcontrolled mutationを自然candidateと分離。共通mandatory checksが実際にPASSすることを確認した後、3 Reviewerへ同一packetを投入した。
全review固定後のheld-out probeでmutant FAIL / clean PASSを確認。sentinel-probe-results.json（元資料: sentinel-probe-results.json）。追加probeは元のacceptanceやPhase 1結果を書き換えていない。

## 14. Cheapest equivalent Reviewer

| Case | 根拠まで同等の最安Reviewer | 検出結果だけの最安Reviewer |
| --- | --- | --- |
| RV-001 | gpt-6-sol | gpt-6-sol |
| RV-002 | gpt-6-sol | gpt-6-sol |
| RV-003 | gpt-6-sol | gpt-6-sol |
| RV-004 | gpt-6.1-sol | gpt-6.1-sol |
| RV-005 | gpt-6-sol | gpt-6-sol |
| RV-006 | gpt-6-sol | gpt-6-sol |
| RV-007 | gpt-6-sol | gpt-6-sol |
| RV-008 | gpt-6.1-sol | gpt-6.1-sol |
| RV-009 | gpt-6.1-sol | gpt-6-sol |
| RV-010 | gpt-6-sol | gpt-6-sol |

Phase 2判定: **REVIEWER_6_1_SOL_DEFAULT**。

10 packetのreview費用は6 Sol 6.05004、6.1 Sol 10.33576、Astra 58.51750 credits。coreの検出集合・正しいACCEPT/REJECT・false positive 0だけなら全モデル同等で、6 Solが最安となる。一方、確認済みの反例誤りを含むreviewを「根拠まで同等」とは採用しない保守的な判断では6.1 Solを暫定推奨する。この説明正確性の区別は観測後のadjudicationで追加したため、事前に固定された統計検定であるとは扱わない。元のcore指標と6 Sol最安の別結果を併記し、raw findingを改変していない。6.1 Solは6 Solより4.28572 credits高いが、この標本では反例誤り0。Astraは同じ有効findingに48.18174 credits追加となり、必要性は示されなかった。

## 15. LOC

| Task | arm | changed LOC | retry | final quality |
| --- | --- | --- | --- | --- |
| RSP-001 | a | 6 | 0 | PASS |
| RSP-001 | b | 5 | 0 | PASS |
| RSP-001 | c | 6 | 0 | PASS |
| RSP-002 | a | 13 | 0 | PASS |
| RSP-002 | b | 13 | 0 | PASS |
| RSP-002 | c | 5 | 0 | PASS |
| RSP-003 | a | 62 | 0 | PASS |
| RSP-003 | b | 64 | 0 | PASS |
| RSP-003 | c | 62 | 0 | PASS |
| RSP-004 | a | 20 | 0 | PASS |
| RSP-004 | b | 21 | 0 | PASS |
| RSP-004 | c | 25 | 1 | PASS |
| RSP-005 | a | 2 | 0 | PASS |
| RSP-005 | b | 2 | 0 | PASS |
| RSP-005 | c | 2 | 0 | PASS |
| RSP-006 | a | 10 | 0 | PASS |
| RSP-006 | b | 10 | 0 | PASS |
| RSP-006 | c | 10 | 0 | PASS |
| RSP-007 | a | 16 | 0 | PASS |
| RSP-007 | b | 17 | 0 | PASS |
| RSP-007 | c | 17 | 0 | PASS |
| RSP-008 | a | 52 | 0 | PASS |
| RSP-008 | b | 71 | 0 | PASS |
| RSP-008 | c | 52 | 0 | PASS |

LOC=最終candidateと同一初期sourceのadded+deleted。Host rustfmtを含むsource diffであり、思考量や生成tokenの代用ではない。

## 16. Wall

| Phase | session開始〜終了の実経過 s | 結果freezeまで s |
| --- | --- | --- |
| Phase 1 | 2746.8217 | 2779.2437 |
| Phase 2 | 300.8344 | 302.7462 |
| Planner arm | role+validation component seconds |
| --- | --- |
| gpt-6-astra | 1990.3450 |
| gpt-6.1-sol | 2551.0310 |
| gpt-6-sol | 2203.7690 |
| Task | arm | Planner s | Executor s | review s | retry s | Host validation s |
| --- | --- | --- | --- | --- | --- | --- |
| RSP-001 | a | 91.8910 | 42.8120 | 15.0940 | 0 | 49.0150 |
| RSP-001 | b | 98.4850 | 39.9220 | 20.9850 | 0 | 50.7180 |
| RSP-001 | c | 105.9070 | 57.9680 | 16.4220 | 0 | 53.7030 |
| RSP-002 | a | 80.4220 | 49.5150 | 22.7500 | 0 | 52.4840 |
| RSP-002 | b | 119.4690 | 44.3900 | 17.5000 | 0 | 54.8910 |
| RSP-002 | c | 99.4380 | 53.1870 | 18.8440 | 0 | 51.3590 |
| RSP-003 | a | 143.3130 | 102.1570 | 19.5000 | 0 | 51.1880 |
| RSP-003 | b | 237.0940 | 89.1250 | 17.1570 | 0 | 53.7810 |
| RSP-003 | c | 139.3440 | 76.4690 | 17.9220 | 0 | 46.9530 |
| RSP-004 | a | 107.8600 | 53.7820 | 20.0150 | 0 | 50.7650 |
| RSP-004 | b | 138.9690 | 89.9370 | 22.1400 | 0 | 54.3750 |
| RSP-004 | c | 198.9850 | 53.3130 | 17.4850 | 44.0630 | 79.2960 |
| RSP-005 | a | 97.0310 | 54.1090 | 17.0160 | 0 | 52.4060 |
| RSP-005 | b | 142.2030 | 61.7340 | 18.0940 | 0 | 53.4220 |
| RSP-005 | c | 138.9850 | 42.2500 | 15.9850 | 0 | 49.5780 |
| RSP-006 | a | 109.9370 | 57.9850 | 18.8910 | 0 | 55.7030 |
| RSP-006 | b | 176.2650 | 63.0470 | 17.8280 | 0 | 59.0780 |
| RSP-006 | c | 89.7970 | 59.7660 | 16.7810 | 0 | 53.9220 |
| RSP-007 | a | 84.3910 | 63.2500 | 19.2030 | 0 | 47.8900 |
| RSP-007 | b | 114.1250 | 151.6720 | 23.9370 | 0 | 43.8750 |
| RSP-007 | c | 107.6560 | 59.7810 | 15.9530 | 0 | 51.3750 |
| RSP-008 | a | 164.9850 | 113.5630 | 26.5310 | 0 | 54.8910 |
| RSP-008 | b | 309.3750 | 102.2350 | 17.9060 | 0 | 47.2970 |
| RSP-008 | c | 196.8290 | 96.3440 | 25.7500 | 0 | 52.3590 |

wallは各session/validationの実区間。armを3並列実行しているため合計は実経過時間でもactive reasoning時間でもない。CPU/IO競合・cache・通信待ちを含み、speed rankingには使わない。

## 17. Allowance snapshot

同じweekly window（10,080分、resetsAt=1791613304）でusedPercentは48%→56%（+8ポイント）。5h/secondaryは取得値null。購入credit balanceは11.8295395000のまま。これは本benchmarkだけの消費量ではなく、計算credits 247.52737と直接対応付けない。reset・追加購入は実行していない。

before（元資料: allowance-before.json） / after（元資料: allowance-after.json）を保存。親chat・同時利用を含むaccount-wide値。5h/weekly windowを同一視せず、Task creditsへの因果配賦はnull。

## 18. Recommended role-separated Router

Planner: **gpt-6-sol** / Executor: **gpt-6-sol** / Reviewer: **gpt-6.1-sol**。全て今回測定したxhigh / Standard。

通常codingのPlanner/Executor候補は6 Sol→6 Sol。Reviewerは説明根拠の正確性を優先する暫定案として6.1 Solを選ぶ。8 natural Taskの実測roleをこの組合せで再構成すると38.65131 credits（Planner 19.23764 + Executor 9.59728 + Retry 1.93115 + Reviewer 7.88524）。これは実施済みroleの費用組替えであり、新たなproduction runではない。検出結果だけを求めるコスト下限案6 Sol→6 Sol→6 Solは35.45089 creditsで、今回も同じ2 defectを検出した。ただし反例説明1件の誤りを留保する。hard/high-riskやAstra Executorは測っておらず、そのroutingは提案しない。

これは次の検証候補。production Router / bounded profile / model policyには反映していない。Local inferenceは0回。

## 19. Limitations

Hostが先にinterface・scaffold・acceptanceを作っており、Plannerが曖昧な大規模依頼から仕様を作る価値は測れていない。6 Solの安価さにはcache hitの違いも含まれる。Reviewer説明精度のstrict判定は1件の観測後adjudicationに基づくため、6.1 Sol一般優位の根拠にはしない。準備段階のRSP-003 oracle検証でformat前の署名比較がfalse positiveとなり、測定開始前に共通Host処理を修正・再検証した。元記録はpreparation配下に保持し、FREEZE後の条件変更はない。CLI versionは0.160.0でbinary SHAを固定。95 sessionのruntime model/effortと新規sessionを監査した。

- 各Task/armは1試行。8件のpure in-memory fixtureなので、一般的な大規模変更・high-risk・security/dependency作業へ外挿しない。
- cache共有、モデル内部揺らぎ、並列CPU/IO、task順序を完全統制した因果実験ではない。
- Reviewer 6 Solの自然candidate結果はPhase 1から再利用。各レビューは独立だが、3モデルの実行時刻は一致しない。
- controlled sentinelは2種の既知defect。自然発生不具合の分布・見逃し率とは別。
- shared scaffold/acceptance/oracle作成と親chatの集計tokenはnull。pipeline creditsは実装準備込みの全事業費ではない。
- CLI使用量と公式単価からのcredits計算であり、account実請求・included allowanceのTask配賦ではない。
- input inventoryとtool traceを監査したprivate copyであり、OSによる完全なread隔離を証明したものではない。

## 20. Conclusion

この8 TaskではPlannerをAstraへ上げても追加creditsを回収できず、Plannerは6 Solが暫定default。Reviewerは不具合検出だけなら6 Solで十分だったが、反例の正確性まで品質条件に含める保守的な採用案は6.1 Sol。Astraをいずれかのdefault roleにする実測根拠は得られなかった。Local specialist integrationやproduction Router更新には進まず、本結果を保存して停止する。

既存Worker/Rust regressionは全PASS。integrity-audit（元資料: summaries/integrity-audit.json）で既存27637ファイルと全freeze hashを再確認。旧実験・productionを変更していない。
