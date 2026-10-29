# モデル別一覧

調査日：2026-10-24。**分野欄は開発元資料から分かる重点領域。今回の追加実測による「得意」の確定ではない。**
Bは10億parameter、Tは1兆parameter。activeはMoEの一度の推論で使う部分で、必要メモリではない。denseのactive欄は省略した。

| モデル | 重みの規模 | 公開資料の重点領域 | 当方で確かめたい用途 | 主な注意点 |
| --- | --- | --- | --- | --- |
| [Gemma 4 26B A4B](https://ai.google.dev/gemma/docs/core/model_card_4) | 25.2B / active 3.8B | コード、推論、画像理解 | 既存の明確な変更規則を持つTaskの基準モデル | 今回の500件はHost補助付き。一般業務成功率や他モデルとの優劣へ拡張しない。 |
| [Gemma 4 31B](https://ai.google.dev/gemma/docs/core/model_card_4) | 30.7B dense | 推論、多言語、画像・文書理解 | 同系列dense化で複雑な条件判断・文書理解が改善するか | 26B MoEの上位互換とは限らない。速度とメモリも別測定。 |
| [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | 9B dense | 画像・文書理解、推論、多言語 | 図表やスライドからの事実抽出、短い条件推論 | 過去24件codingではGemma非採用4件を救済しなかった。視覚・Office能力はその結果から判断しない。 |
| [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) | 27B dense | repository coding、frontend、agentic coding | 型・APIの組合せが必要な小さな修正、UI実装 | 公開agent評価はツールと長い推論込み。既存bounded 8192/2048での優位は未測定。 |
| [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 35B / active 3B | coding、agentic task、画像理解 | Qwen dense版との速度・正確性比較、構造化出力 | active 3Bでも35B全体の重みを保持する必要がある。 |
| [Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 122B / active 10B | 推論、長文・画像理解、instruction following | 複数資料の条件照合、長文から根拠付き抽出 | 長いcontext上限は正確な参照能力の保証ではない。別の大容量環境候補。 |
| [Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | 397B / active 17B | 総合推論、文書・画像理解、coding | 大型マルチモーダルの比較基準 | 個人GPUでの日常利用候補とは分ける。量子化・backend・運用費未検証。 |
| [gpt-oss-20b](https://developers.openai.com/api/docs/models/gpt-oss-20b) | 21B / active 3.6B | 推論、数学、tool use | 複雑な条件分岐や計算、短い根拠付き判断 | 画像入力なし。Harmony等の公式templateが必要。thinkingを含む出力予算不足に注意。 |
| [gpt-oss-120b](https://developers.openai.com/api/docs/models/gpt-oss-120b) | 117B / active 5.1B | 推論、coding、tool use | gpt-oss-20bで不十分な条件推論の大型対照 | 公式Ollama案内は60GB以上のVRAM/統合メモリが望ましい。画像入力なし。 |
| [Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | 14B dense | code generation、code repair | Gemmaが落とした既知coding例の対照 | 過去同一24件ではGemma非採用4件のうち1件で採用。一般的な補完率ではない。 |
| [Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next) | 80B / active 3B | 長いcoding task、tool use、失敗からの回復 | debugging、複数工程を持つrepository修正の参照モデル | non-thinkingモデル。active 3Bを必要RAM/VRAMと混同しない。短いbounded Taskへの効果は別検証。 |
| [Devstral Small 2 24B](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | 24B dense | repository探索、複数file修正、software engineering | helper/interfaceをまたぐ修正、既存コードの局所debug | 公開成績はagent scaffold込み。自由な探索を与えない現行方式では差が変わり得る。 |
| [Devstral 2 123B](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512) | 123B dense | software engineering、repository coding | Devstral Smallで残る複雑な修正の大型対照 | モデルカードは独自license。利用条件確認と大容量環境が必要。 |
| [Mistral Small 4](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | 119B / active 6.5B | 推論、coding、多言語・画像 | 日本語を含む文書・コード横断Task | 名称のSmallは軽量GPU向けを意味しない。reasoning設定も比較条件に含める。 |
| [Mistral Large 3](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) | 675B / active 41B | 多言語、長文・検索併用、総合知識 | 大型の長文・文書理解対照 | 検索やtool scaffoldの寄与をモデル単体能力と分離する。 |
| [DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | 284B / active 13B | 推論、coding、長文 | 数理・ロジック・長いコードの比較基準 | 混合精度の公式重みと任意のQ4を同一視しない。小型Flashではない。 |
| [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 1.6T / active 49B | 高度な推論、coding、長文 | 超大型推論の参照候補 | サーバー/複数GPU級。今回のPCで動作確認したわけではない。 |
| [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 552B backbone / active count unresolved | 画像とテキストの推論、長文 | 文書画像と長文を組み合わせた大型対照 | cardに8B/16Bのactive表記があるが単一値へ集約しない。backbone値は全構成の実メモリではない。 |
| [GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) | 30B / active 3B | coding、推論、tool use | 小さなcode修正と条件推論の別系列対照 | 公開評価は課題別に大きな生成予算を使用。2048 outputで同じ結果とは限らない。 |
| [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | 320B / active 18B | coding agent、推論、長文・画像 | 大型のコード・視覚横断Task | Flashという名称から消費メモリを推定しない。 |
| [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | 大型 / canonical total not verified | 長時間coding、agent task、推論 | 大型software engineeringの参考候補 | HF表示753Bをcanonical parameter数として採用しない。GLM5.2由来の構成詳細とlicenseは別確認。 |
| [Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) | 1T / active 32B | coding、knowledge work、画像理解 | 複数資料とコードの横断Task | 256K等のcontext仕様と当方8192条件を混同しない。 |
| [Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) | 2.8T / active 104B | 長時間coding、knowledge work、視覚推論 | 超大型の文書・コード横断比較 | 公式の低精度構成でも巨大。通常の個人PC向け推奨ではない。独自license。 |
| [MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | 428B / active 23B | coding、agentic task、computer use | 業務手順や画面操作の大型参考候補 | computer-use scoreはagent環境込み。Officeファイル編集や日本語業務の保証ではない。HF UIの220B表示を本文428Bより優先しない。 |
| [Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus) | 14B dense | 数学、科学、code reasoning | 英語での計算・ロジック対照 | 主に英語向けで多言語用途を想定しないと公式に記載。日本語Officeの第一候補にはしない。 |
| [GLM-OCR](https://huggingface.co/zai-org/GLM-OCR) | 0.5B decoder + vision; total not verified | 文書OCR、表・数式認識、情報抽出 | PDF・表画像からの構造化抽出 | layout処理を含む二段pipeline。汎用推論やOffice編集モデルではない。全体parameterは未確定。 |

## 比較の前提

- 総parameterはモデルカードの定義に依存する。GLM-5.3、GLM-OCRの総数は確定できずJSONではnull。DeepSeek-V4.1-Flashの552Bはbackboneの値。HF画面の丸め表示や混合精度による表示を無条件に採用しない。
- Qwen、DeepSeek、GLM、Kimi、MiniMaxの大型モデルにも重み公開版がある。ただし「自己ホスト可能」と「RTX3080で実用速度」は別。
- gpt-ossはtextモデル。画像を含む仕事へ使うには別の画像認識工程が必要。
- Phi-4-reasoning-plusは主に英語向け。英語の数理成績を日本語業務適性へ転用しない。
- OCR/文書解析モデルは専用pipelineを含むことがある。認識器単体とシステム全体の費用を分ける。
- licenseはApache/MIT等だけでなく独自条件もある。導入する版・量子化配布元ごとに確認する。今回は導入していない。

参照した仕様は可変URLで、モデルのcommit/digestを実験用にfreezeしたものではない。実行する候補が決まった時点で、重み・template・backend・license・設定を改めて固定する。
