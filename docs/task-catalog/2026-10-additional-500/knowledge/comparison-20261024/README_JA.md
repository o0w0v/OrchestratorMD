# このPCでGemma26を補えるモデルはあるか

2026-10-24。**同じ入力・生成設定・採点基準では、Devstral Small 2がGemmaの失敗19件を4件補完した。Qwen14は1件、Qwen3.5 9Bは0件だった。**

まず比較候補として残すのはDevstral。ただし平均API時間はGemmaの約5倍で、成功対照も2件落とした。限定されたTaskでの補完として扱う。

## 同条件の結果

既存500件から、以前の失敗20件と成功対照10件を選んだ。Gemmaも同じ30件を再測定し、以前の失敗のうちExcel1件は今回は通過。以下の補完数は、**当日もGemmaが失敗した19件**に対するもの。

| モデル | Gemma失敗の補完 | 成功対照 | 平均API秒/件 | Ollama RAM観測 GiB | GPU全体観測 GiB |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gemma4 26B：基準 | — | 10/10 | 7.4 | 17.4 | 9.7 |
| Devstral Small 2 24B | 4/19 | 8/10 | 36.8 | 10.5 | 9.5 |
| Qwen2.5-Coder 14B | 1/19 | 8/10 | 11.3 | 5.4 | 9.4 |
| Qwen3.5 9B | 0/19 | 7/10 | 4.3 | 4.6 | 8.0 |

各モデル30件・初回1回、repair0。requestはmodel名だけ変更し、8192 context / 2048 output / temperature0 / seed20260926 / think=falseを維持。PCはRAM約64GB、RTX3080 10GB、Ollama0.40.10、driver610.88。

API平均は初回loadを含む30件の平均。warm平均はGemma6.7秒、Devstral35.0秒、Qwen14 10.5秒、Qwen3.5 3.5秒。Host validationや前後health check込みの30件arm wallは、Gemma約7.0分、Devstral約21.6分、Qwen14約8.9分、Qwen3.5約5.2分だった。

RAMはOllama/backendのworking set合算の採取最大値。GPUはdesktop等も含むPC全体で、背景使用量はarm間で異なる。どちらも最低必要メモリの保証値ではない。private memory、background/idle、min free、実際のsampling間隔は[詳細結果](RESULTS_JA.md)と[JSON](COMPARISON_RESULTS.json)に保存した。

## 補完できたTask

Devstralが新たに通した4件：

- 複数口配送の完了判定：キャンセル・重複・不明IDの扱い。
- 待機者の繰上げ対象選定：キャンセル除外、申込順とIDでの並べ替え。
- 欠測を除いた稼働率加重平均：有効weightの再正規化と欠測IDの保持。
- 2台帳の未一致ID抽出：追加・削除・継続の分類。

Qwen14の補完は最後の台帳比較1件で、Devstralも合格した。今回Qwen14だけが補完したTaskはない。これは上記の具体的な失敗例について得られた結果であり、全ての条件処理・集計に一般化しない。

## 実行環境による違い

- DevstralはGPUへ19/41層、Qwen14は39/49層、Qwen3.5は33/33層をoffloadしたというログがある。DevstralにはCPU側model bufferもあり、待ち時間の判断にこの構成を含める。
- GemmaのGPU層ログは31/31と補助側5/5。層数だけで全weightのVRAM常駐を判定せず、Host bufferと実使用量も記録した。
- gpt-oss 20Bは、think=falseでもthinkingを返した。2応答は2048 tokensまでthinkingのみで最終回答なし。設定非互換として停止し、開始済み3件目は中断した。能力FAILや自然なinfra failureへ含めない。取得済み4096 output tokensは保全し、中断分のusageはnull。
- CoderNext 80Bは現在の空きRAM＋空きGPUと4GiB reserveの資源gateで除外。常にこのPCで実行不能という意味ではない。Gemma12はquarantineを維持した。
- 同条件の120件とgpt-ossの完了2件で、自然発生のCUDA、backend crash、GPU query timeout、API infra failureは0。意図的なgpt-oss停止は別記録。

## コード能力と出力形式の区別

Qwen14は15件、Qwen3.5は17件、Devstralは7件で、関数本体のみの指示に対して関数全体を返した。主評価では契約違反として不合格。

追加生成をせず、保存された関数全体を変更せず同じRust testsへ渡す補助診断では、Qwen14は8/15、Qwen3.5は4/17、Devstralは3/7が通過した。**この診断を主評価の合格や採用数には加えない。** 一部には意味の正しいコードが含まれるため、形式不適合だけを根拠にコード能力全体が低いとも判定しない。

## 次の使い方

1. Devstralを上記4種の補完候補として残す。新しい同種Taskで再確認し、時間の負担も評価する。
2. Qwen3.5は小さいメモリと短い応答時間が利点。Officeの成功対照5件は全て合格したが、Gemmaの失敗を新たには救っていない。固定slot業務の高速化は別の確認対象にする。
3. Qwen系のコードについては、出力契約への適合性を別途調べる。主評価を事後的に書き換えたり、現行Workerのscope guardを緩めたりしない。

今回は既知失敗を集めた診断。一般成功率、production採用率、Codex Credits削減率は測っていない。Production Router・bounded 2.2.8・旧500件を変更せず、モデル追加downloadや新しいprovider AI呼出しも行っていない。準備Codex usageは欠測null。

Raw request/response、検証、telemetry、旧STOPはローカルの新実験directoryに保全。公開資料は集計とhash等で、rawを含む完全な再実行bundleではない。
