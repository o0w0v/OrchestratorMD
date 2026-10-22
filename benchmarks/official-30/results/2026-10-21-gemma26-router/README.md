# 公式30課題 A/B workflow実測結果

**判定: INCONCLUSIVE。** 採点済み29ペアは両Armが同じ21課題を解決。Routerの比較Creditsは6.46%減、総tokensは0.60%減。元30課題のうち1件は環境未測定。最終pipeline false greenはA3件/B4件。全30完了・Production成功の証明ではない。

[日本語報告](RESULTS_JA.md) / [30課題の全行](TASK_AB_RESULTS.csv) / [集計JSON](FINAL_BENCHMARK_RESULT.json)

AはGPT-6 Sol直接実装、Bはfrozen eligibilityによるGemma26 one-shot＋clean Sol fallback。15 eligible課題では両Arm13解決、Credits9.72%減。Direct課題でも費用差があり、全削減をGemmaの因果効果とはしない。Shared Plannerは実支出で1回、比較費用では各Armへ全額配賦。認証、private tests、gold、raw会話は収録しない。
