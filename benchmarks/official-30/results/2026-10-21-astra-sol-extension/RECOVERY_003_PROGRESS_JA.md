# 回復run-003の進捗（2026-10-21）

旧STATUS_JA.mdは停止時点の証跡として保持する。ユーザーはその後Ollama再起動を承認した。新しい回復runは完了済み17 armと10 Plannerを再利用し、障害Local呼出しを再試行せず、未実行分だけを測定している。

2026-10-21T11:03:00Z時点では、内部46課題のうち8課題が全4armの終端に達した。旧CUDA INFRAの品質結果はnullのまま残し、能力FAILやPASSへ書き換えない。回復runの追加CUDAはこの時点で記録されていない。46課題全体の勝者や削減率は未確定である。

閉じたCodex呼出しの既知小計は251.85741 Credits、別のtransport準備3.96430を加えた既知小計は255.82171 Credits。実行中・欠測usageを0で補完しない。

外部比較は既存Sol29ペアを再課金せず、新Astra経路を準備した。公開30課題のsource/identity、15 Local・15 directのeligibilityを再照合し、比較overlayとrole adapterの24件offlineテスト、およびnetwork=none隔離checkerのsynthetic Rustテスト1件はPASS。これはActor VM隔離PASSや新公式評価の実測を意味しない。

新Guest認証とVM境界の実測が必要なため、新しい外部Astra model callはまだ0。Gold/private tests/公式scoring/Production Router/bounded2.2.8/旧STOPは変更していない。

旧Solの公式結果と内部46課題の結果を混同せず、新規外部測定が終わるまで4-wayの最終結論は保留する。
