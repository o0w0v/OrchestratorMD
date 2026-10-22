# Astra / Sol × Gemma26 — 内部46課題の最終集計

2026-10-22、46課題×4経路の全184 terminal dispositionを記録。これは内部課題のHost validation＋独立Reviewerの結果であり、公式MultiPL-E/Multi-SWE解決率ではない。

## 結果

| 経路 | 確認PASS | FAIL | 品質未測定 | 比較Credits | Codex total tokens | Local採用 | clean fallback |
|---|---:|---:|---:|---:|---:|---:|---:|
| S0: GPT-6 Sol単体 | 42 | 4 | 0 | 153.97206 | 8,294,502 | 0 | 0 |
| S1: Sol＋Gemma26 | 44 | 0 | 2 | 88.04747 | 4,259,099 | 37 | 7 |
| A0: GPT-6 Astra単体 | 46 | 0 | 0 | 698.50445 | 7,220,425 | 0 | 0 |
| A1: Astra＋Gemma26 | 44 | 0 | 2 | 454.16090 | 4,109,958 | 38 | 6 |

S1対S0はCredits **42.81594%削減**、Codex tokens **48.65154%削減**。A1対A0はCredits **34.98096%削減**、tokens **43.07872%削減**。全経路に失敗・未測定Taskで発生した実消費を含める。Local tokensを節約量として扱っていない。

S1は確認済みPASSだけで44件とS0の42件を上回った。ただしS1/A1の正確な最終PASS率は未測定を含むためnull。両経路の品質区間は44/46〜46/46（95.65〜100%）。未測定を除いて100%と報告しない。比較可能な品質pairのS1対S0は両方PASS40、S1のみPASS4、S0のみPASS0、未測定2。A1対A0は両方PASS44、未測定2。

観測済みCredits削減率は計算可能だが、未測定Taskを完了するための追加費用は含まれない。このため完全完走時の経済効果とは区別する。

## 解決あたりCredits

| 経路 | 確認PASSあたりCredits | 未測定がすべてPASSとなる場合までの区間 |
|---|---:|---:|
| S0 | 3.66600 | 3.66600 |
| S1 | 2.00108 | 1.91408〜2.00108 |
| A0 | 15.18488 | 15.18488 |
| A1 | 10.32184 | 9.87306〜10.32184 |

Astra単体はSol単体より確認PASSが4件多い一方、Creditsは約4.54倍。これは当該workflow・凍結課題・単価に限る比較であり、一般的なモデルランキングではない。

## 会計

共有Plannerは実支出で1回、比較上は対応する両armへ全額配賦。実測Codex呼出し379件、Local呼出し92件。重複除去後の実支出は **1,130.65392 Credits / 19,812,776 tokens**。比較4経路のCredits合計1,394.68488とは異なる。差264.03096は比較側で追加配賦された共有Planner分。

実支出内訳: input19,549,299（cached14,624,640、uncached4,924,659）、output263,477。cachedはinput内数、reasoningはoutput内数として二重加算しない。測定済みtransport準備3.96430を足した既知小計は1,134.61822 Credits。全準備作業のusageは完全に取得できず、プロジェクト総額とJPYはnull。

LocalはCUDA応答でcounterが欠測するため厳密な全tokens合計をnullに保ち、既知小計と欠測件数をTOKEN_ACCOUNTING.jsonに分離した。CSVの空欄は欠測、直接Codex経路のLocal 0は構造的0。

## 旧STOPと回復run

旧runは一切成功へ書き換えていない。新runは未実行slotのみ進め、完了済みpaid出力を再生成せず、旧raw usageをidentityで一意に統合した。

- R002: GSOAK228-003/S1、CUDA illegal memory access。
- R003: GSOAK228-010/S1、同CUDA。
- R005: GSOAK228-060/A1、同CUDA。
- R006: GSOAK228-059/S0、marker外EOF改行変更。scope guard拒否を既知FAILとして保持。
- R008: GSOAK228-022/A1、Local候補の余分な閉じbrace後にformatterが停止。凍結classifierのHOST_FORMAT_ERRORを保持し、品質はnull。CUDAではない。診断を理由にclassifierやformatterを変更していない。
- R004/R007およびboundary準備の停止はHost集計・metadata等の問題として保全。新しいモデル呼出しがなかった停止とcoding failureを混同しない。
- R009で残る16slotを実行し、184件の終端記録に到達した。

CUDA3件をモデル能力FAILやPASSへ変換しない。Host formatter停止1件も隠さない。Worker旧artifactのexecution_modeにoffline_fixtureという不正確なラベルがあるが、native HTTP response/countersで実推論を確認し、旧ラベルは書き換えていない。

## 固定条件と限界

Gemma4:26b Q4_K_M、ctx8192/predict2048、temperature0、seed20260926、FA1/KVf16、bounded2.2.8、one-shot/repair0。GPT-6 Sol/Astraはいずれもxhigh/Standard。RTX3080 10GB、Ollama0.40.6、同一凍結digest。料金は開始時freezeを使用し、現在料金へ置き換えない。

Localには他経路の実装を渡さずclean fallbackを使用。内部実験では共有Planner出力をGemma promptへ注入していないため、公式workflowの経路と完全同一ではない。clean copyとtrace監査はOS read isolationの証明ではない。

本集計は旧自動closeoutの数表と一致するが、旧文中に残ったR4/81経路等の途中経過説明は最終状態ではない。旧ファイルを修正せず、この新しい報告を最終説明とする。

## 判断

**内部データではSol＋Gemmaの経済価値を支持するが、公式ベンチマークでの目的達成は未確定。** CUDA3件とHost停止1件があり、完全無障害やproduction安全性を証明したとはしない。公式30課題は別runで既存Sol29pairを再利用し、Astra2経路を実行中。公式解決率・Credits削減・Credits/解決課題はその公式結果で別途判断する。

添付: TASK_ARM_RESULTS.csv、CODEX_SESSION_USAGE.csv、LOCAL_MODEL_USAGE.csv、TOKEN_ACCOUNTING.json、FOUR_ARM_AGGREGATE.json、PRESERVATION_AND_CHECKS.json。公開物にはsource、gold、private tests、認証情報、Host raw pathを含めない。
