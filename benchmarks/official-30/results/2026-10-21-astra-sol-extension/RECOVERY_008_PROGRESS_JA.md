# Astra / Sol × Gemma — 回復run008進捗（最終結果ではありません）

以下は取得時点の固定snapshotです。全46課題の最終比較ではありません。


状態: **RUNNING** / terminal disposition 40/46 課題（infra保持を含む・quality不明はPASSにしない）

|Arm|完了/46|Host validation＋review PASS|Local採用|
|---|---:|---:|---:|
|S0|40|36|0|
|S1|40|38|33|
|A0|40|40|0|
|A1|40|39|34|

確定済みCodex callの既知Credits: 1002.97780。transport準備 3.96430 を加えた既知小計: 1006.94210。実行中callと欠測は0補完しない。

S0=Sol単体、S1=Sol＋Gemma、A0=Astra単体、A1=Astra＋Gemma。内部TaskのHost validation/reviewの品質であり、公式外部resolved率ではない。

更新UTC: 2026-10-21T15:29:54.109191+00:00。旧run保全、retry0、監視1800 Credits。途中経過からwinnerを判定しない。


## 追加の停止・回復の扱い

- CUDA illegal memory access 3件はINFRA_ERROR、品質は未測定のまま保持しています。失敗したLocal呼出しは再試行していません。
- GSOAK228-059 / Sol単体でprotected領域のファイル末尾に空行を追加した候補を検出しました。FileScope guardの拒否は正しく、formatter・semantic validationは未実行です。候補をHostで直さず、SCOPE_VIOLATION / REJECTとして保持しています。
- 回復run007は、再利用したCUDA記録にwall-time欄がないことによるHost metadata KeyErrorで、追加AI呼出し前に停止しました。旧STOPを残し、欠測をnullとして扱う新run008へ移行しました。guard、Task、モデル、prompt、採点条件は変更していません。
- 現在のrunは125件の完了経路と64件のPlanner出力を再利用して開始しました。旧raw usageをinvocation IDで重複排除し、失敗callの消費も保持しています。

## 公式比較

既存のSol29ペアは不変・再実行0です。公式Astra生成はまだ0件で、内部run008の完了後に新しいGemma cohort境界を確認して開始します。同じ30課題・公式Evaluator・A/B workflowを維持します。Local対象は15件、directは15件で、tracing-2897の既存未測定も30課題分母に残します。Gemma単体評価を代替にしません。

Guest認証は正常完了済みです。native access checks18件、固定ネットワークACL、config exact hash、およびweb_search=disabledの静的一致を確認しました。これは旧MXC GateのPASS昇格ではありません。Guest利用の既存UTC期限は延長せず、model gatewayの既存cutoffと固定cleanup停止markerを維持します。

最終KPIは公式workflow resolved rate、Codex Credits削減率、Credits/解決課題です。品質低下やfalse greenをCredits削減だけで成功と判定しません。Host準備側の総usage/creditsは安全に配賦できない部分をnullのまま保ち、測定対象CLIのturn.completed usageと混合しません。

研究用source commit: ef97c765b。raw auth、credential、gold、private tests、Actor実装diffは本文に含めていません。
