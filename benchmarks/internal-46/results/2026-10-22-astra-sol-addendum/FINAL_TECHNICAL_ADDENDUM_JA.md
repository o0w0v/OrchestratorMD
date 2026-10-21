# 内部46課題：最終技術補足

本書は[最終集計](../2026-10-22-astra-sol/RESULTS_JA.md)へ、会計測定方式・全Task paired表・wall欠測を補足する。旧集計値・旧STOP・raw usageは変更していない。

## Creditsの意味

**報告Creditsはnative turn.completed usage×開始時凍結公式Standard rateの換算値であり、請求書やアカウント残高から実引落を読み取った値ではない。実引落Creditsはnull。** ACTUAL_STUDY_SPENDというledger名は実際に発生した一意なcallへの換算額を指し、両armへの比較配賦額とは区別する。API USD料金へ切り替えていない。

料金の取得記録: 2026-10-20T22:03:17.753839+00:00、https://learn.chatgpt.com/docs/pricing.md。raw SHA256: `e3e0a5ac79441fac79cf1e50d31c0bdbd8d27e0f30452a8307f87ab64495bdf3`。Sol input/cached/output=50/5/250、Astra=250/25/1250 Credits/1M tokens（凍結Standard条件）。現在の価格を主張するものではない。

## 必須4比較

| 比較（前者対後者） | Codex tokens削減量 | tokens削減率 | Credits削減率 | 品質 |
|---|---:|---:|---:|---|
| A0 vs S0 | 1,074,077 | 12.94926% | -353.65662% | 確認PASS46対42 |
| S1 vs S0 | 4,035,403 | 48.65154% | 42.81594% | 確認PASS44対42、S1未測定2 |
| A1 vs A0 | 3,110,467 | 43.07872% | 34.98096% | 確認PASS44対46、A1未測定2 |
| A1 vs S1 | 149,141 | 3.50170% | -415.81369% | 双方確認PASS44、未測定Task集合は異なる |

負のCredits削減率は費用増。A0/S0はPlanner・Executor・Reviewerを含むworkflow全体のtokens差であり、Executor単体能力の比較ではない。共有planのモデル間差も含む。各Taskのinput/cached/uncached/output/total/Credits/wall差とBOTH/FIRST_ONLY/SECOND_ONLY/NEITHER/UNMEASUREDはPAIRED_COMPARISONS.csv全184行に保存。

S0の既知FAILはGSOAK228-025/048/042/059。A0は4件ともPASS、S1も4件ともPASS。測定済みpairでRouterのみFAILとなったTaskはないが、未測定を「品質低下なし」と確定しない。UNKNOWNの一覧はQUALITY_DIFFERENCES.jsonに保持。

## Wall

|Arm|wall取得Task|欠測|既知小計秒|取得分中央値秒|
|---|---:|---:|---:|---:|
|S0|44|2|6010.52|134.03|
|S1|42|4|5183.89|104.38|
|A0|43|3|5842.23|137.28|
|A1|42|4|5365.35|111.58|

全46件のstrict wall合計は各armともnull。取得率が異なる既知小計同士から速度優劣や削減率を出さない。exact active timeは未計測。Task wallは共有Planner時間を含み得るworkflow比較値であり、4arm合計を実study elapsedとみなさない。

## 限界と結論

対象は旧raw dispatchに実際に存在した46件で、未送信6件・direct control12件は含めていない。fixture修正candidate-003は開始前にfreezeされ、旧runの結果として上書きしていない。Task選択は無作為ではなく、主にbounded codingの内部課題。過去の群推計43.23%を今回のpaired削減率へ合算していない。

内部結果はSol＋GemmaによるCodex生成tokensとrate換算Creditsの削減を支持する。CUDA3件とHost停止1件を残した限定結果であり、公式評価の成功や無障害運用を証明したとはしない。公式30課題のworkflow resolved rate・Credits・Credits/解決課題は独立に採点する。
