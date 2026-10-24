# 思考機能込みのLocal Task委譲ナレッジ

対応モデルではthinkingを有効にし、effortを選べるモデルではその違いも測定した。目的はTaskを渡す際の選択材料を増やすこと。

**対象は追加500件から選んだ既知失敗20件＋成功対照10件。公式MultiPL-E / Multi-SWEの30課題ではない。** Codex Credits削減を測った試験でもない。

## 今回分かった使い分け

|Taskの具体例|実測から残す割当候補|時間・条件|
|---|---|---|
|予約区間の統合と空き枠抽出、期限優先の引当、同梱制約、条件に合う配送便選択|Gemma26 thinking=true|これらの固定テストに合格。出力予算・samplingも含むnative profileで測定|
|共通可能時間、営業日をまたぐ期限、代替機切替後の稼働率|gpt-oss 20B / medium|Gemma26が6144出力上限だった3件を、それぞれ約159秒・67秒・100秒で合格|
|発行済みslotへの単純なPPT/Word/Excel表示設定|Qwen3.5 9B / thinking=trueも候補|成功対照5件を約4〜6秒で合格。複雑なOffice計算全般へは広げない|
|品質と費用を重み付けした選択|Gemma26 thinking、またはgpt-oss highの実測例|Gemmaは約20秒で合格。gpt-ossはlow/medium不合格、highで約72秒・合格|
|関数全体のコード生成|gpt-oss lowは次の検証候補|返した4関数を無変更で補助テストすると4/4合格。ただし現行のbody-only契約では不合格のため、そのまま採用しない|

各行はこの具体的Taskで得た結果。新しい類似Taskへ自動dispatchするruleは作成していない。

## 同じ30課題でのprofile実測

|profile|固定契約・検証PASS|過去失敗20件のPASS|成功対照|出力上限|平均API秒|
|---|---:|---:|---:|---:|---:|
|Gemma26 / thinking|27/30|17/20|10/10|3|66.73|
|Qwen3.5 9B / thinking|9/30|2/20|7/10|10|29.72|
|gpt-oss 20B / medium|22/30|13/20|9/10|0|44.84|

選定済みの失敗課題を多く含む診断であり、一般的な正答率やモデルの総合順位ではない。API平均にはloadと失敗した試行も含む。出力上限は「この予算では未完了」であり、意味テストの誤りと分けた。

Gemmaの先行fast profileは同じ30件で11/30だった。新profileだけ合格16件、fastだけ合格0件。ただしthinking以外にsamplingと出力予算も変更しており、thinking単独の効果量とはしない。旧500件と先行比較は当時の条件の結果として保全した。

## effortはTaskに合わせる

同じ代表6件で比較した。

|gpt-oss effort|現行契約PASS|出力上限|出力tokens（思考込み）|API合計秒|
|---|---:|---:|---:|---:|
|low|0/6|0|2,257|75.92|
|medium|4/6|0|10,899|343.33|
|high|2/6|4|28,804|873.72|

highは重み付き選択を回復した一方、mediumで合格したコード3件も出力上限になった。現在の予算で一律にhighを使う根拠にはならない。

lowのコード4件、mediumのbody契約違反5件は、返された関数全体を変更せず同じテストで隔離実行するとすべて合格した。Qwen3.5も6件中4件がこの補助テストを通った。**内容の正誤と受け渡し形式の適合性は別に保存し、主評価のPASSへ加算しない。**

## このPCでの資源観測

RTX 3080 10GB、RAM約64GiB、driver 610.88、Ollama 0.40.10。

|profile|GPU全体の採取時peak MiB|開始前の背景GPU MiB|最小空きVRAM MiB|Ollama/backend RSS peak GiB|
|---|---:|---:|---:|---:|
|Gemma26 thinking|9,906|1,317|146|19.75|
|Qwen3.5 thinking|7,375|657|2,677|6.88|
|gpt-oss medium|8,914|658|1,138|7.72|

GPUはHost全体、RAMはprocess working set合計。共有pageの重複、採取間のpeak、背景差があるため、モデル単体の消費や最低必要メモリとは扱わない。private memory、offload、native eval durationも詳細JSONに記録した。

## 条件と保全

- native thinking、対応effort、メーカー推奨samplingを使用。gpt-ossはinstalled modelの温度defaultを維持。
- 共通num_ctx=8192、num_predict=6144、seed=20260926、FA1/KVf16。one-shot、semantic repair0。
- 新profile102呼出しを完了。温度0の先行診断2件も別runとして保存し、実消費へ含めた。全104呼出しでinput 40,158 / output 259,508 native tokens。思考分を二重加算していない。
- Qwen14/Devstralには対応するthinking設定がなく、先行30件の結果を再利用。再生成0。Gemma12はquarantine、CoderNextは既存の資源admission不足を保全し未実行。
- CUDA、infra、backend crash、GPU query failureは0。旧入力・結果hash、全102 invocationとusage、固定チェックとの照合PASS。
- 新規benchmark用Codex sessionは0。今回の準備会話のCodex usage/creditsは取得できずnull。Local tokensをCodex削減量へ換算しない。
- Production Router、bounded 2.2.8、旧結果、model filesを変更していない。追加download/installなし。
- OfficeはHost補助付きtyped slotsとnative export/render。GUI操作や見栄えを含む全業務品質は未測定。一部の公開requestに既存の日本語文字化けがあり、英語のExact contract・例を含む元入力をそのまま使用した。

## 保存物

- [評価方針](KNOWLEDGE_EVALUATION_POLICY_JA.md)
- [sampling revision](SAMPLING_REVISION_JA.md)
- [全結果](RESULTS_JA.md)
- [Task別割当ナレッジ](TASK_ASSIGNMENT_KNOWLEDGE.json)
- [使用量・比較JSON](COMPARISON_RESULTS.json)
- [raw照合](EVIDENCE_VALIDATION.json)

raw request/response、思考text、native validation、GPU telemetryはローカルに保全。公開版には回答コードや思考全文を載せず、結果・条件・hashを保存する。
