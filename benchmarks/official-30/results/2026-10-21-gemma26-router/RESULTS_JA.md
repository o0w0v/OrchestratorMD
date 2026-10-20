# 公式30課題 A/B workflow 最終報告

集計: 2026-10-20T21:36:08.133352+00:00

**判定: INCONCLUSIVE。** 採点できた29ペアでは、A/Bとも同じ21課題を解決し、Bの比較CreditsとCredits/解決課題は6.46%低かった。ただしTracing 1課題は環境未測定であり、全30課題での達成は未確定。公式採点でHost/Reviewerのfalse greenも検出したため、Production成功や拡大は宣言しない。

A = GPT-6 Sol Planner → Executor → Host validation → 独立Reviewer。B = 同じPlanner → frozen eligibility → Gemma26 one-shot（repair0）またはclean Sol Executor → 同じvalidation/Reviewer。Shared Plannerは実支出1回、比較では各Armへ全額。

## Primary KPI

|対象|公式解決 A / B|採点済 / 元分母|A Credits|B Credits|削減率|A Credits/解決|B Credits/解決|
|---|---:|---:|---:|---:|---:|---:|---:|
|MultiPL-E|18 / 18|20 / 20|102.18|96.52|5.54%|5.68|5.36|
|Multi-SWE-bench|3 / 3|9 / 10|256.17|238.67|6.83%|85.39|79.56|
|overall|21 / 21|29 / 30|358.35|335.19|6.46%|17.06|15.96|

費用表は両Armの公式結果・実usageが揃った同じペア集合で計算し、不合格Taskの消費も含む。元の20/10/30分母は保持。MultiPL-Eの確定公式解決率は両Arm 18/20 = 90%。SWEは3解決・6不解決・1環境未測定、全体は21解決・8不解決・1環境未測定。全30の確定解決率はnullで、21/30 = 70%は下限値。29採点分だけなら両Arm 21/29 = 72.41%。

A_ONLY 0、B_ONLY 0、BOTH 21、NEITHER 8、ENV 1。成功集合まで一致した。全30の未測定を失敗・成功・0 tokenへ置換していない。全TaskはTASK_AB_RESULTS.csvに記載。

## Tokensと会計

比較総tokensはA 25,807,856 → B 25,652,929、154,927 tokens（0.60%）減。**Credits削減6.46%と総tokens削減0.60%は別指標。** cached inputはinput内数、reasoningはoutput内数として二重加算していない。Local 9,489 input / 1,381 output tokensをCodex節約量へ換算していない。

ACTUAL_STUDY_SPEND（実行phase、共有Planner1回）は636.06445 Credits。COMPARISON_WORKFLOW_COSTはA 358.35012、B 335.19033 Credits。比較2列の合計から重複する共有Planner 57.47600 Creditsを1回分引くと実支出に一致する。実支出は凍結した700 Credits停止目安内。

Creditsは実turn.completed usageと凍結Standard単価（uncached/cached/output = 50/5/250 credits per 1M tokens）から算出した値で、アカウント残高の引落しとの直接照合ではない。価格原本・timestamp・SHA256はlive-capture-037/RATE_FREEZE.json等に保全。[公式料金](https://learn.chatgpt.com/docs/pricing)。JPY換算はnull。

既知の準備CLI支出1.9866 Credits、主会話のnative token部分snapshot、過去準備の未測定部分は別記録。Desktopの料金tierとphase配賦が未確定のため、研究全体のCreditsとNET_PROJECT_SAVINGSはnull。準備・監督・Host修復を含むプロジェクト全体の純削減を主張しない。


### Planner出力の実際の供給条件

共通Plannerの実行と両Armへの費用配賦は維持した。Sol Executor/Reviewerは同じShared Planを使用する。一方、Gemmaへの実入力は15件すべてLOCAL_FREEZE.jsonに明記したnative bounded Task packetのままで、Shared Planを追加注入していない。これはfrozen promptを維持した結果であり、Gemmaが同じPlanを直接読んだ実験とは主張しない。実条件とruntime moduleのpostcheckはローカル保全の実行条件証跡を参照。

## Gemma委譲の内訳と帰属限界

Local 15 attempts、code generation各1、repair0、Qwen等へのcross-model retry0。Host PASS 8、Local採用6、clean Codex fallback 9。採用6件はすべて公式PASS（採用Localの公式false green 0）。Local採用率はeligible分母で6/15 = 40%、元30分母では6/30 = 20%。

旧集計127のfallback directory globはB_RESOURCE8_067_EXECUTOR_001を見落として8件と表示した。新しい送信・fallback照合記録は実ledgerのrole=EXECUTORで9件を確認。旧集計・raw・Task結果は書き換えていない。

Local eligible 15課題ではA/Bとも13解決、75.49859 → 68.16259 Credits（9.72%減）。一方、Local対象外の14採点ペアでも282.85153 → 267.02774 Credits（5.59%減）であり、ここにはGemmaが参加していない。SWE全10課題はfrozen direct対象。**全体の23.15979 Credits削減をすべてGemmaの因果効果とは扱わない。** 独立CLIの試行・出力量・cache・固定実行順の差を含む観測値であり、一般モデルランキングや統計的非劣性の証明ではない。

## 品質とHost側の制約

Host validation＋Reviewer採用後に公式不合格だったFINAL_PIPELINE_FALSE_GREENはA 3 / B 4（合計7）。これはProductionのfalse green 0条件を満たさない。

MultiPL-Eの両Arm共通不合格はmean_absolute_deviation（compile成功後のassertion失敗）とclosest_integer（公式compile E0599/TryFrom未スコープ）。後者はActor Cargo edition2021環境と、edition指定なしの公式rustc argvとの互換性差を確認。Host検証PASSを公式PASSへ読み替えていない。数値assertionの詳細なprivate期待値やtest sourceは開示せず、修正・再生成・再採点はしない。

SWEではripgrep両Arm、nushell Bの採用候補が公式未解決。rayon/serde/bytes/tokio等の採用未達もworkflow失敗として残した。rayonでは編集ファイルの未解決Clippy診断10件が先頭24件の簡約projectionに含まれない制約を確認（direct-diagnostic-observation-132）。途中でprojectionやvalidationを変更せず、その影響を費用・結果に含めた。これをモデル一般のcoding能力の低さと断定しない。

Localの3件のsyntax/Host-format停止は個別quarantineし、旧STOPを保全してclean fallbackへ移った。Direct Cargo.lock検証のHost修正に伴う有料7試行等も費用から除外していない。SWE source symlinkのpre-start wrapper 1件はNative開始前と固定証跡で確認し、raw nullを残した別会計projectionだけで構造的0とした。正常Vendor callのusage欠測を0補完していない。自律運用・Host介入0とは報告しない。

## 保全・Infrastructure・認証

元30 Task、公式prompt/tests/scoring、Router eligibility 15 Local/15 Direct、bounded2.2.8、Gemma26 digest・8192/2048・temperature0・seed20260926・FA1/KVf16は変更していない。旧freeze/capture/CLI/STOP等61件のhash postcheckは全件一致。Production Router/Applicationは変更していない。Worker 275 testsとRust fmt/clippy/test/check/buildの保存済み回帰結果はregression-no-model-121を参照。

Local inference結果にCUDA障害は0、repair/自動restart/追加model生成は0。旧CUDA障害・旧runは保全。報告処理で検出したprojectionのLF/CRLF hash差は、旧ファイルを残したaccounting-byte-freeze-134で実バイトhashを固定し、検証条件やusageを緩和せずに解消。known-environment-closeout-plan-133は未実行（通常controllerでTracing ENVが確定）。

Guest live認証ファイル3件は削除済み。stock CLI logoutは実行しておらず、アカウント側失効は未確認の利用者作業として残る。旧checkpoint内の暗号化状態は再利用しない。旧MXC隔離GateをPASSへ変更せず、承認済み研究VM overlayの範囲で実施した。

## 結論

今回の29採点ペアでは「解決集合を維持し、workflow CreditsとCredits/解決課題を6.46%削減」を観測した。Local eligible部分では同等の13解決で9.72%低い費用だった。ただし1環境未測定、公式false green、Host/公式compiler互換性と診断visibility制約、Direct部分の費用差がある。**全30課題での完成証明・Production成功・全削減のGemma因果帰属は未確定（INCONCLUSIVE）。** 本結果を保全し、未解決環境とHost互換性を別revisionで解消する前に自動拡大しない。

## 公開証跡

[TASK_AB_RESULTS.csv](TASK_AB_RESULTS.csv)、[FINAL_BENCHMARK_RESULT.json](FINAL_BENCHMARK_RESULT.json)、[ACCOUNTING_RECONCILIATION.json](ACCOUNTING_RECONCILIATION.json)、[SAFE_FAILURE_PROJECTION.json](SAFE_FAILURE_PROJECTION.json)を収録。raw会話・認証・gold・private tests・Evaluator cacheは非公開。公開用編集ではローカル証跡への参照だけを整理し、計測値・失敗・制約を保持した。
