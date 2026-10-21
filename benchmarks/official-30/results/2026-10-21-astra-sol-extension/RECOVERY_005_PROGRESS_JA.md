# Astra / Sol 拡張比較：回復run005の途中経過

これは未完了の測定状況です。最終winnerや公式品質の維持を判定したものではありません。

旧run002のCUDA障害に加え、run003でもLocal累積41呼出し目（fresh後32呼出し目）にHTTP500 / CUDA illegal memory accessが発生しました。両方のraw response・STOP・GPU/backend証跡を保持し、モデルのcoding FAILとは分離しています。障害を起こしたLocal呼出しは再試行していません。

ユーザーのOllama再起動許可に基づき、同じversion/digest/8192 context/2048 output/FA1/KVf16で新runへ移行しました。run004は再利用metadataのHost処理で新generation0のまま停止し、旧STOPを保持してrun005で辞書mergeを修正しました。完了済み81 armと42 Plannerを再課金せず再利用し、未実行102 armだけを同じ順で測定します。2つのCUDA dispositionはINFRA・quality=nullのままです。

外部公式比較は、既存Sol29対の結果・費用をimmutable baselineとして再利用します。新Astra側はGuest境界とfresh認証の準備中で、本ページ時点でgeneration0です。外部課題・採点・eligibilityは変えず、内部Taskと公式resolvedを混ぜません。

容量に関する新しいユーザー指示により、新VM運用overlayはD:100GiBの作業余裕を維持する設計へ変更しました。旧272GiB STOPは変更していません。現在約270GiBの空きがあり、追加のキャッシュ移動は実施しません。これはモデル・protocol・採点変更ではありません。

# 内部46課題 四arm 本評価 進捗

状態: **RUNNING** / terminal disposition 21/46 課題（infra保持を含む・quality不明はPASSにしない）

|Arm|完了/46|Host validation＋review PASS|Local採用|
|---|---:|---:|---:|
|S0|21|19|0|
|S1|21|19|17|
|A0|21|21|0|
|A1|21|21|19|

確定済みCodex callの既知Credits: 562.98319。transport準備 3.96430 を加えた既知小計: 566.94749。実行中callと欠測は0補完しない。

S0=Sol単体、S1=Sol＋Gemma、A0=Astra単体、A1=Astra＋Gemma。内部TaskのHost validation/reviewの品質であり、公式外部resolved率ではない。

更新UTC: 2026-10-21T12:41:18.615421+00:00。旧run保全、retry0、監視1800 Credits。途中経過からwinnerを判定しない。

過去公式Sol比較の既知結果は21/29対で同じ課題を解決、30件中1件は環境未測定、比較Credits削減6.46%でした。ただしfinal pipeline false greenがA3/B4あり、最終判定はINCONCLUSIVEです。この途中のAstra拡張から新しい成功を主張しません。

API料金への切替なし。Creditsは実turn.completed usageと凍結rateの計算値であり、アカウント残高引落しの監査値ではありません。共有Plannerは実支出1回、workflow比較では各armへ全額です。未測定・実行中usageは0補完しません。準備作業の未測定usageはnullです。
