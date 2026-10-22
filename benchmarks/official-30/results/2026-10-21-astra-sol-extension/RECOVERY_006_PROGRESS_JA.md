# Astra / Sol × Gemma — 回復run006進捗（最終結果ではありません）

集計時点: 2026-10-21T13:55:19Z。研究目的は、Codex単体に対するGemma委譲workflowの品質維持とCredits削減です。

## 内部46課題

29/46課題について4経路のterminal dispositionが揃いました。CUDA由来の未測定をPASSへ変更していません。

|Arm|完了/46|Host validation＋独立review PASS|Local採用|
|---|---:|---:|---:|
|Sol単体|29|26|0|
|Sol＋Gemma|29|27|24|
|Astra単体|29|29|0|
|Astra＋Gemma|29|28|25|

既知の終了済みCodex call費用は746.74221 Credits、transport準備3.96430を含む既知小計750.70651です。実usage×凍結rateであり、実行中callや欠測を0で補完していません。共有Plannerは実支出で1回、workflow比較では対応する各armへ全額配賦します。途中経過からwinnerや最終削減率は判定しません。

## CUDAと証跡保全

累積Local call #9、#41、#55でCUDA illegal memory accessが発生しました。#55は新しい回復run前の障害です。3件をINFRA_ERRORとして保全し、同じ失敗呼出しは再試行していません。GPU照会の正常応答とprocess identityを確認後、許可済みのfresh Ollamaを使用し、108件の完了armと56件のPlanner出力を再利用して残りを続行しています。CUDAからOOM・driver bug・モデル能力失敗を断定しません。

## 公式30課題比較

既存のSol29ペアは不変・再実行0です。新しいGuest専用ChatGPT認証は正常完了し、非管理者Actorのnative境界検査18件とネットワークACL不変を確認しました。全49件のsource/旧authority/freeze hash照合、coordinatorのoffline negative tests6件もPASSしています。これは旧MXC GateをPASSへ昇格するものではありません。

新規Astraの公式課題生成はまだ0件です。内部run006の完了後に外部cohort用fresh境界を確保して、凍結済みの同じ課題・公式Evaluator・GPT-6 Astra/xhigh/Standard・Gemma設定・既存会計方式で続行します。既存Solの失敗結果も再課金せず保持します。tracing-2897は既存の環境未測定のまま30課題分母に残ります。

Primary KPIは公式workflow resolved rate、Codex Credits削減率、Credits/解決課題です。内部Host checksのPASSを公式解決率と混同しません。品質低下やfalse greenがあれば、Credits削減だけで成功とは判定しません。

## 再現用revision

- ローカル研究commit: b8a6ae8bf
- 内部回復freeze SHA256: f32bd19bf40fee4de10a9ddb1f7f15e9bd8a16449dc1c6f74c14b8f9268da450
- 旧STOP・旧結果・raw usage・CUDA証跡・公式Task identityは保全
- 本文には認証code、credential、gold、private tests、Actor実装diffを含めていません。
