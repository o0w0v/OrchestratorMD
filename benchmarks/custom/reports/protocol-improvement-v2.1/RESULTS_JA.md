> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/protocol-improvement-v2.1.md). This report alone does not establish a task result.

# Protocol Improvement Experiment — 結果

実行日: 2026-09-29 JST。9 Task・10 runを完了。**ACCEPT_NO_CHANGEは1/9（11.1%）で、今回の実験では品質改善を確認できなかった。** 全runでGemma26を使用し、INFRA_ERROR/CUDAは0件。Router v2.1・Operational Policy・application・過去artifactは変更していない。

| 実験 | 判定 | Local final PASS | ACCEPT_NO_CHANGE | 得られた証拠 |
| --- | --- | --- | --- | --- |
| A: repair context | **INCONCLUSIVE** | 0/3 | 0/3 | context超過を解消し全3件でrepair生成。最終回復なし |
| B: Host mandatory validation | **PROMISING（validation ownershipに限定）** | 2/3 | 1/3 | 編集後の全checks実行と実際のformat repair回復を確認。契約違反・patch不一致は残る |
| C: evidence grounding | **NOT_PROMISING** | 0/3 | 0/3 | 正しい引用と誤った回答値が併存。引用必須化だけではfact精度が改善しない |

別枠A1-SAVEDは保存済み失敗candidateのrepairのみ。最終失敗で、上表と主要KPIの分母には含めない。

## 1. 実験目的と比較条件

現在のモデルを維持したまま、repair packet、validationの実行主体、型付き回答と引用の契約を改善すれば、Codexの短い最終レビューだけで完了するTaskが増えるかを検証した。Router v2.2の実装・本番採用・Pilot再開は行っていない。

Gemma26 (`gemma4:26b`) / Ollama 0.34.4 / RTX 3080 10GB / NVIDIA driver 591.86。model digestは`08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68`。全generationでtemperature=0、seed=20260926、num_ctx=8192、num_predict=2048、stream=false、think=falseを確認した。cross-model fallback、generation health probe、強制unload、restartは0回。

plan.json（元資料: plan.json）・freeze.json（元資料: freeze.json）で実行前に255入力ファイルを固定した。実装と事前検証commitは`8dcc5cd`、親commitは`a0e305a`。元リポジトリの4,812 tracked filesと全固定入力が不変であることを実行前後にSHA256で確認した。

各群3 Task。元Taskの契約・sourceはbyte-identicalで再利用し、追加Taskは実repoの小さい単一責務から作成した。新コードTaskは事前にred/greenとmutation検証を行い、golden実装はモデルへ渡していない。

## 2. v2.1のfailure modeとの対応

| 元Task | 旧v2.1 | 新run | 今回の結果 |
| --- | --- | --- | --- |
| PILOT-002 | 初回FIFOテストが誤り。CONTEXT_LIMITでrepair generation 0回。Codex 4 LOC修正 | A1-SAVED / A2-FULL | compact repair生成は実行できたが、同じFIFO検証順序の誤りが残る |
| PILOT-005 | モデルがtargetedのみ要求しTEST_NOT_ALLOWED。Codex 2 LOC修正 | B-001 | Hostが3 checks実行しLocal PASS。ただし引数なしhelpの契約を破壊し最終REJECT |
| PILOT-007 | event_key誤答。repair後も4/5 factsでREJECT | C-001 | 最終3/5 facts。event_key誤答は残り、引用必須化による精度向上なし |

A2の初回HTTP requestは旧PILOT-002と**wire bytesまで一致**する。request SHA256は`b983ba794e981ee45733e1f1283be326611cd0d775e4eae136acf96f0d71f31c`。B-002も旧PILOT-004と契約・sourceが同じ追加controlで、旧初回PASSから今回はformat repair後PASSになった。比較証跡（元資料: metrics/historical-pairs.json）

旧7 Task全体の4/7と今回9 Taskの1/9はTask構成が違うため、改善幅・悪化幅の因果推定には使わない。指定された元の3失敗Taskだけを見ると、今回もACCEPT_NO_CHANGEは0/3だった。

## 3. Experiment Aの設計

初回入力を維持し、repair時だけ会話全体の再送をやめた。immutable contract、applied slot body、必要なsource excerpt、失敗checksの実stdout/stderrを新packetへまとめた。完全一致する診断文字列は一度だけ保存し、参照indexで再利用。失敗診断の要約・省略、acceptance緩和、context/output拡大は行っていない。

送信前に実serialized UTF-8 bytes、message文字数、推定input tokens、8192 contextと2048 generation reserveを記録。token推定は`ceil(bytes/3)+256`というheuristicであり、正確なtokenizer値ではない。Aは推定reserveと従来24,000 message文字の両方をguardとし、超過時はAPI送信前にREPAIR_CONTEXT_TOO_LARGEとなる。オフラインテストで送信阻止を確認した。

## 4. A結果・context削減・repair recovery

| run | 初回bytes | 旧方式repair bytes（再構成） | 新repair bytes | 削減 | 推定input tokens | 実prompt_eval_count | repair回復 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| A1-SAVED（別枠） | N/A | 27,382 | 6,845 | 75.0% | 2,538 | 1,966 | なし |
| A2-FULL | 9,621 | 27,372 | 6,843 | 75.0% | 2,537 | 1,958 | なし |
| A-002 | 9,446 | 31,027 | 11,077 | 64.3% | 3,949 | 3,844 | なし |
| A-003 | 10,432 | 29,672 | 7,506 | 74.7% | 2,758 | 2,611 | なし |

旧方式の欄は保存済み会話・candidate・checksから再構成した送信予定packetで、旧方式を再送した結果ではない。全件で旧方式のmessage文字数は24,000超、新packetはbudget checkを通過。repair generationは主分母3/3、A1を含め4/4実行されたが、最終回復はそれぞれ0/3・0/4。

A2/A1では、Aを再挿入してBを追い出した後に「Bは重複」と検査する誤りが残った。A-002/A-003は既存テスト関数のbody内にさらに`#[test] fn`を生成した。外側テストは空のまま成功するためtargetedだけなら見逃すが、clippyとmutation checkが拒否した。repairはformatを直しても入れ子を直さなかった。

したがって**context問題の解消は確認済み、修正能力・最終品質の改善は未確認**。PROTOCOL_IMPROVEMENT_SUCCESSに該当する最終PASSはない。A1は初回生成を含まない条件付き観測として保存した。

## 5. Experiment Bの設計

モデルに公開するtool schemaからcheck選択を除き、HostがTask Specの全mandatory checksを所有する。1回のpatch適用後、targeted → format → clippyを固定argvで実行する。optional checkは導入していない。

任意shell・argv・check名変更の権限は追加していない。失敗時にはcandidate diffと失敗checksの実stdout/stderrを返し、同じモデルに最大1 repairを許可する。Bでは通常のagentic会話履歴を維持し、Aのcompact packet変更は混ぜていない。B/Cのtoken推定は記録のみとし、従来のmessage文字上限をguardとして維持した。

## 6. B結果・Host-owned validation

| run | モデルのcheck要求 | Host checks実行 | 初回 | repair | 最終レビュー |
| --- | ---: | --- | --- | --- | --- |
| B-001 / PILOT-005 | 0 | 3/3 | Local PASS | 不要 | REJECT |
| B-002 / PILOT-004 | 0 | 初回3/3、repair後3/3 | format失敗 | 回復 | ACCEPT_NO_CHANGE |
| B-003 / PEX-B03 | 0 | 0、patch適用前に停止 | SCOPE_VIOLATION | なし | REJECT |

TEST_NOT_ALLOWEDは0件。**適用できた3編集attemptでは9/9 checksをHostが自動実行**した。B-003は未読sourceに対するold textが許可body内に一致せず、scope guardが拒否した。validation未実行を成功扱いせずN/Aとする。

B-001の固定interfaceには`[] and [--help] continue working`と明記されている。しかしcandidateは`[]`をエラーへ変更した。全固定checksとworkspace testsはPASSしたため、既存validationのcoverage不足も判明した。最終レビューの追加実行では引数なしがexit 1、`--help`がexit 0だった。実証（元資料: reviews/B-001-contract-check.json）

これは明確な契約へのモデル違反とvalidation coverage gapの併存であり、Taskを曖昧・無効として分母から除外していない。WorkerのLocal PASSはそのまま保持し、最終レビューだけREJECTとした。実験途中のtest追加や再repairは行っていない。

Bは実行主体の改善としてPROMISING。ただし「全check実行＝全契約充足」ではなく、主要KPIの改善を確認したという意味ではない。

## 7. Experiment Cの設計

既存の5 typed fieldsに、factごとのfile・symbol/region・8〜500文字のexact source quoteを必須とするwrapperを加えた。Hostはsource/excerpt hash、許可region、引用の存在、型、欠落・重複、固定semantic assertionsを検証する。

repairには失敗fact名と中立な診断だけを返し、expected valueを教えない。全5回答は再検証する。raw payload監査で、失敗fact以外の診断や正解値を含むfeedbackがないことを確認した。source引用の存在と意味の支持は別であり、最終レビューでは両者を区別する。

## 8. C結果・evidence grounding

| run | 正しいfacts 初回→最終 | 引用あり | 機械的に有効な引用 初回→最終 | 初回repair対象facts | 最後に残った誤答 |
| --- | --- | --- | --- | ---: | --- |
| C-001 / PILOT-007 | 2/5 → 3/5 | 5/5 | 4/5 → 5/5 | 4 | event_key、duplicate_refreshes_fifo |
| C-002 / PEX-C02 | 4/5 → 4/5 | 5/5 | 5/5 → 5/5 | 1 | extra_tokens_checked_before_unit |
| C-003 / PEX-C03 | 4/5 → 4/5 | 5/5 | 5/5 → 5/5 | 1 | load_comparison |

合計fact正解は10/15 → 11/15、引用存在検証は14/15 → 15/15。Task全体の回復は0/3。最終的に4 factsが誤りのまま残る。

具体的にはkind/targetのtupleを正確に引用しながら`event_id`と回答し、strict `>`を引用しながら`greater_or_equal`と回答した。C-002では追加token検査がunit検査より先にあるsourceを引用しても、順序のBooleanが誤ったままだった。quote matchingをsemantic groundingと同一視してはいけない。

元PILOT-007は旧4/5に対し今回最終3/5。元Taskを含む3件すべて不合格であり、**現行のevidence wrapperを品質改善策として採用する根拠は得られなかった**。NOT_PROMISINGと判定する。

## 9. Task別結果と主要KPI

| run | 単一責務 | 初回Local PASS | repair生成/回復 | 最終Local | Codex review | input/output tokens | Worker秒 |
| --- | --- | --- | --- | --- | --- | ---: | ---: |
| A2-FULL | 重複eventがFIFO順を更新しない回帰test | × | 有/× | ESCALATE | REJECT | 4,538 / 1,250 | 123.109 |
| A-002 | skill cache重複挿入・FIFO回帰test | × | 有/× | ESCALATE | REJECT | 6,283 / 884 | 68.266 |
| A-003 | KiB字句・u64境界回帰test | × | 有/× | ESCALATE | REJECT | 5,343 / 558 | 61.625 |
| B-001 | inspect --help追加 | ○ | 無 | PASS | REJECT | 2,395 / 258 | 28.266 |
| B-002 | memory evidenceにpercent追加 | × | 有/○ | PASS | ACCEPT_NO_CHANGE | 13,490 / 860 | 54.765 |
| B-003 | load evidenceにCPU当たり比率追加 | 未検証 | 無 | ESCALATE | REJECT | 447 / 179 | 5.469 |
| C-001 | dedup/cacheの5 facts | × | 有/× | ESCALATE | REJECT | 2,668 / 918 | 24.860 |
| C-002 | KiB parserの5 facts | × | 有/× | ESCALATE | REJECT | 1,549 / 987 | 23.594 |
| C-003 | load predicate/orderの5 facts | × | 有/× | ESCALATE | REJECT | 1,442 / 888 | 22.140 |
| A1-SAVED（別枠） | 保存済みPILOT-002 candidateのrepair | N/A | 有/× | ESCALATE | REJECT | 1,966 / 625 | 78.063 |

主分母9件: First PASS **1/9**、Local final PASS **2/9**、ACCEPT_NO_CHANGE **1/9**、REJECT **8/9**、Worker escalation **7/9**。同モデルrepair generationを行った7 Task中、回復は**1/7**。A1を含む条件付き観測では1/8だが、主要回復率には混ぜない。

specが無効で実行不能となるTask design failureは0、明示的に発見したvalidation coverage gapは1、scope failureは1。CONTEXT_LIMIT / REPAIR_CONTEXT_TOO_LARGE / TEST_NOT_ALLOWED / FORBIDDEN_TOOL等の停止codeは0。ただしこれはコード・semantic失敗がないという意味ではない。

各requestのbytes・推定/実token・attempt・HTTP status・SHA・raw pathはrequest-index.json（元資料: metrics/request-index.json）、Task別のchecksと分類はtask-metrics.json（元資料: metrics/task-metrics.json）とCSV（元資料: metrics/task-metrics.csv）に保存した。Ollamaのprompt_eval_count/eval_countを実測値として使用し、推定tokenやcache countと区別した。

## 10. Codex介入・修正LOC・時間

通常repair loopへのCodex参加は0、candidateへのCodex修正は0件・**0 LOC**。ACCEPT_WITH_MINOR_FIX / MAJOR_FIXは0件。修正して採用する方針にはせず、失敗を保持してREJECTしたためである。**0 LOCを「必要な修正作業が減った」とは解釈しない**。主分母8/9は別途修正・再分割・契約検証の改善が必要。

全runの最終レビューを行い、B-001のみdiffで発見した違反を追加のCLI実行で確認した。mandatory final reviewやこの追加診断は、モデルの通常repairやCodexによるコード修正とは別に記録した。正確なCodex planning/review/repair tokensとactive review時間は取得不能のためnull、節約量の推定は行っていない。

主分母Worker合計412.094秒、A1を含め490.157秒。cohortのSTART〜ENDは497.066秒で、設計・事前検証・最終レビュー・結果作成時間は含まない。全20 generation callsのreported inputは40,121、outputは7,407 tokens。主分母のみでは19 calls、38,155 / 6,782 tokens。集計（元資料: metrics/summary.json）

## 11. Infrastructureと検証

10 runすべて完了しSTOPなし。INFRA_ERROR 0、CUDA 0、GPU query timeout 0、residency mismatch 0。22件のbaseline / pre / post / final health snapshotでOllama API、GPU照会、backend/residencyに異常は検出されなかった。snapshot時GPU使用量は1,461〜9,813 MiB。連続telemetryではないため実行中peakや長期安定性は推定しない。監査（元資料: metrics/protocol-audit.json）

Protocolのオフライン11テストと既存Python 77テストがPASS。既存Rustのfmt、clippy、workspace test、locked check/buildもPASS。新コードTaskのscaffold失敗とgoldenでの全checks成功を確認した。Local PASSのB-001/B-002は別途workspace regressionもPASS、candidate source bytesは不変。ただしB-001は上記の契約確認で不合格。既存applicationへは何も反映していない。

## 12. v2.2への採用候補と見送り

**第一候補はBのHost-owned mandatory validation。** check選択をモデル権限から除く設計と、実失敗の同モデルrepair回復は確認できた。ただし採用前にinterfaceの全不変条件とcheck coverageの対応を点検する。特に引数なしhelpを覆う固定checkを、次の独立cohortのfreeze前に追加する必要がある。

Aのcompact packetと送信前budget計測は、repairを評価可能にする基盤として候補に残す。最終品質を改善した機能としての全面採用は保留する。次の別実験ではRust statement/bodyの構造をHostが検証し、入れ子のtest宣言を型・構文の契約違反として実行前に検出する案を検討する。単に「関数bodyだけ書け」と依頼を強める方法にはしない。

Cの現wrapperの一般採用は見送る。引用存在検証は監査に役立つが、回答値との整合性を保証しない。次はsourceの比較演算子・key構成・early return等を構造化して返すinterfaceと、AST等による決定的な整合性検証を別実験で比較する。正解値をrepair diagnosticで教える方式にはしない。

自動fallback、モデル変更、context/output拡大、promptだけの注意喚起、本番Router変更は採用していない。B-003のold-text不一致には、編集前にHostがsource snapshot/region識別子を必ず提供するinterface案があるが、今回のcohortへ後付けしていない。

## 13. 次Pilot案と結論

**現状のProtocolをまとめてv2.2へ採用し、Pilotを拡大する判断は見送る。** 次はB単独の限定cohortを候補とし、coverage gapを事前に閉じて、従来conditionとの同じTaskによる比較を行う。Aの構造検証とCのsemantic整合性はそれぞれ独立した実験で扱う。Task・受入基準・モデル・判定を実行前に固定し、今回の失敗を再実行で置き換えない。

今回確認できたのは、Aでrepair送信を可能にする効果、Bでvalidationを必ず実行する効果、Cで引用が正しくても誤答を残す限界である。**Codexの最終レビューだけで済むTaskを増やしたという証拠は得られていない。** この結論とすべての失敗を保持し、Router・Operational Policyへの反映は別変更とする。

成果物の入口: 計画（元資料: README.md）、Task specs（元資料: tasks/）、raw results（元資料: results/）、diffs（元資料: diffs/）、reviews（元資料: reviews/）、metrics（元資料: metrics/）、旧artifact保全監査（元資料: metrics/integrity.json）。
