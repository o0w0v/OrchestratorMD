# 公式4経路比較の途中状況 — 2026-10-22

公式30課題でCodex-onlyとGemma Routerの品質・Creditsを比較する目的は維持しています。新しい公式4経路比較の結論は、まだ確定していません。

内部46課題の184 terminal dispositionは完了し、[最終集計](../../../internal-46/results/2026-10-22-astra-sol/RESULTS_JA.md)と[技術補足](../../../internal-46/results/2026-10-22-astra-sol-addendum/FINAL_TECHNICAL_ADDENDUM_JA.md)を公開済みです。内部結果を公式ベンチマークの解決率として扱いません。

外部評価では既存Sol29 pairをimmutable baselineとして再利用し、再生成・再課金していません。Astraの最初のTLS失敗は旧CA bindingのHost修正を新copyに限定して実施し、完了済みPlanner/Executorを再利用しました。

その後、Local候補のunexpected closing delimiterが、凍結2.2.8 classifierでHOST_FORMAT_ERRORとなる停止が2課題で発生しました。旧STOPとraw candidate/usageを保持し、coding PASS/FAILへ書き換えていません。停止時までのLocal生成は9回、Host unknown2件、採用2件。失敗Localの再生成は0です。

残るLocal6件は未試行のまま保留しています。classification不変という元条件との衝突があるため、別revisionの分類修正を行うかをユーザーへ確認中です。現行Worker/Router/formatter/scoringは変更していません。回答待ちも、未完了Codex-onlyおよび元からLocal不適格だったdirect経路は、同じTask契約・モデル・validationで進めています。LocalをCodexへ先回りしてrerouteしてはいません。

新Astraの40 native invocationまでの凍結停止snapshotではusage欠測0、換算支出253.64190 Creditsです。これは実usage×凍結公式Standard単価であり、アカウント実引落の読み取りではありません。現在のDirect継続分は別途追加されます。準備usageは欠測をnullとし、0推定しません。

Tracing-2897は別のpublic pristine trybuild不一致で未測定のままです。公式testやstderrを修理して通してはいません。全30 Taskの分母と旧証跡を維持しています。

公式採点は新しい全候補の固定後に行います。途中のHost PASSをOfficial resolvedとして数えず、現時点の3-way/4-way winnerや公式目標達成を宣言しません。
