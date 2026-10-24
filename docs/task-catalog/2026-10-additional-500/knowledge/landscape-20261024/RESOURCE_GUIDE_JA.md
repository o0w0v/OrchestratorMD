# 大きいモデルを含めた実行環境の見方

## MoEのactive数だけで選ばない

Qwen3-Coder-Nextは80Bの重みを持ち、activeは3B。Gemma26も25.2Bに対しactive 3.8B。activeは計算量の目安であり、保存する重みが3〜4B相当になるという意味ではない。[Qwen公式](https://huggingface.co/Qwen/Qwen3-Coder-Next)、[Google公式](https://ai.google.dev/gemma/docs/core/model_card_4)

必要な資源には重みだけでなく、KV cache、context、batch、画像encoder、buffer、backendの作業領域が含まれる。CPU offloadは動作可能性を広げるが、遅延とRAM・帯域の負担も測る。

## 4bitを仮定した算術例

以下は**全parameterを均一4bitで保持できたと仮定した重み本体の計算例**。実際の配布サイズ、最低VRAM、動作保証ではない。量子化metadata、混合精度、encoder、KV cache等は含まない。GBは10進でGiBではない。

式：parameter数 × 4 / 8 bytes。

| 仮の総parameter | 重み本体だけの計算値 |
| --- | ---: |
| 9B | 4.5 GB |
| 14B | 7 GB |
| 32B | 16 GB |
| 80B | 40 GB |
| 120B | 60 GB |
| 400B | 200 GB |
| 1T | 500 GB |
| 2.8T | 1,400 GB |

公式がMXFP4/FP4/FP8等を混合するモデルを、この均一4bit表と同一視しない。GLM-5.3やGLM-OCRの未確定総数から必要メモリは計算しない。

## 実行環境を3群に分ける

| 群 | 主な候補 | 調査上の扱い |
| --- | --- | --- |
| RTX3080 10GBを中心に試す | Qwen3.5-9B、Qwen14、gpt-oss-20b、Devstral Small 2、Gemma26 | 小さいものでも全GPU常駐を仮定しない。offload、使用RAM、API latency、peak/free VRAMを実測する |
| 大容量RAM/VRAM機で比較 | Qwen3-Coder-Next 80B、gpt-oss-120b、Qwen122B、Devstral123B、Mistral Small4 | RAMに載るだけで業務的な速度とは限らない。別環境として記録 |
| サーバー・複数GPUを想定 | Qwen397B、DeepSeek大型、GLM大型、Kimi、MiniMax、Mistral Large3 | 個人PCの常用推奨とは分け、大型比較用の候補として残す |

分類は調達仕様や最低要件ではなく、次の試験を計画するための目安。大容量CPU RAMへのoffload等もあり、10GBを超えるモデルが全て実行不能という意味ではない。

OpenAIのOllama案内はgpt-oss-20bについて16GB以上、120bについて60GB以上のVRAMまたは統合メモリを望ましいとしており、CPU offloadでは遅くなる。[公式ローカル実行案内](https://developers.openai.com/cookbook/articles/gpt-oss/run-locally-ollama)

## 今回は実行環境を変更しない

モデルdownload・量子化変更・Ollama/driver変更・GPU試験は0。導入済みという記述は前段のinventoryに基づき、新しい起動確認ではない。RTX3080でのCUDA安定性を新モデルへ引き継がない。

次の比較ではmodel digest、backend version、量子化、context/output、thinking、CPU/GPU offload、worker wall、tokens、GPU空き容量、infra errorを必ず残す。CUDA障害をcoding能力のFAILと混ぜない。
