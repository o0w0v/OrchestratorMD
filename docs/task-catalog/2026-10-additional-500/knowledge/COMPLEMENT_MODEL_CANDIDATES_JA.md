# Gemma26を補えるモデルの候補

狙うのは総合点でGemma26を上回るモデルだけではない。**Gemma26が解けなかった作業を、別モデルが正しく解ける組合せ**を探す。まず導入済みモデルを優先する。以下の候補選びは2026年10月24日時点の既存証跡と公式資料によるもので、新しい500件での補完性能は未測定である。

## すでに確認できる補完例

過去の同一24 Task・3モデル比較を、Local採用の有無で再集計した。

| 指標 | 件数 |
|---|---:|
| Gemma26採用 | 20/24 |
| Qwen2.5-Coder 14B採用 | 14/24 |
| Qwen3.5 9B採用 | 7/24 |
| Gemma26非採用4件をQwen14が採用できた | 1/4 |
| 同じ4件をQwen3.5が採用できた | 0/4 |

該当するのは`LS3W228-021`、証跡の有無を3状態で出し分けるコード。Gemma26の最終品質はclean Codex fallbackで完成していたが、ここではそれをLocal成功へ数えていない。採用基準はmandatory validationと独立したACCEPT_NO_CHANGEである。

両モデルの成功を事後的に選べば21/24になるが、これは**結果を知った後の上限**である。実行前に正しく選べるRouterや、Gemma失敗後のhandoffが実測されたわけではない。切替と再検証の費用を含む経済効果も未測定。小標本1例を一般的な専門性へ拡大しない。[再集計JSON](HISTORICAL_COMPLEMENTARITY.json)に元CSVのSHA256と全該当IDを保存した。

過去Phase 1/2にはCoderNextのDEBUGGING最終3/3、Gemma26の1/3という記録もある。ただしGemma失敗2件は旧protocolでのscope違反であり、純粋な原因解析能力差とは断定しない。現在のbounded経路で検証する候補を選ぶための補助証拠とする。

## 最初に比較する候補

| 候補 | 調べたい補完領域 | 選んだ根拠 | 未確定なこと |
|---|---|---|---|
| Qwen2.5-Coder 14B | 小さい条件分岐・コードの取り違え | 上記の実測補完1例。新規導入不要 | Officeの計算・要約を補えるとは未確認 |
| Qwen3.5 9B | 条件付き計算、文章と表の照合、文書からの抽出 | 公式にreasoning、長文・document理解を評価。導入済みで登録サイズ約6.55GB | 同じ8192/2048、Q4での補完率。過去24件では補完0例 |
| gpt-oss 20B | 多段の条件整理、数値と説明の整合性 | 公式に推論量をlow/medium/highで指定可能なopen-weightモデル。導入済み | このTask集合での実力・JSON契約適合・速度 |
| Devstral Small 2 | Rust型不一致、局所修正・コード理解 | 公式にsoftware engineering向けとして公開。導入済み | boundedな関数body生成へ適合するか。コード探索性能をそのまま転用しない |

Qwen3.5の開発元はreasoning/長文/document関連ベンチマークとthinking/non-thinkingの動作を公開している。これは候補に挙げる根拠であり、今回のGemma26より優れることや、日本語Office業務への適性を証明するものではない。公式の推奨context/output条件は今回の8192/2048より大きいので、公開スコアを本環境の予想点に使わない。[Qwen公式model card](https://huggingface.co/Qwen/Qwen3.5-9B)

gpt-ossはテキスト向けで推論量を指定できる。公式Ollama案内は20Bに16GB以上のVRAM/統合メモリを推奨し、CPU offload時の低速化にも言及する。RTX3080 10GBでは全GPU常駐や低latencyを前提にできない。登録ファイル約13.79GBとruntime VRAMを混同しない。[OpenAI公式model資料](https://developers.openai.com/api/docs/models/gpt-oss-20b)、[公式Ollama実行案内](https://developers.openai.com/cookbook/articles/gpt-oss/run-locally-ollama)

Devstralの公式software engineering実績は、探索・tool・scaffold込みの条件を含む。今回の狭い編集方式での優位や、15.18GBのQ4版のRTX3080上の速度は未証明。[Mistral公式model card](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)

既存のQwen3-Coder-Nextもコード向け比較の参照候補として残す。ただし登録約51.74GBで、80B中3B activatedという仕様だけからメモリ負担が小さいとは扱わない。最初から候補を増やしすぎない。[Qwen公式model card](https://huggingface.co/Qwen/Qwen3-Coder-Next)

## 調べ方の優先順位

1. 計算・資料間の整合性はQwen3.5とgpt-ossで補完性を確認する。
2. コードは、補完実績があるQwen14を対照にし、Devstralを比較する。CoderNextは必要な場合の既存参照とする。
3. 採点器の問題は別の修正queueで扱う。モデル変更で採点の穴を通過することを成功としない。

Gemma12はquarantineを維持し、候補から除外した。自動cross-model fallback、production routing、model/runtime設定は変更していない。今回はモデル生成0・download0。クラウドモデルによる課題分割の精度比較も行っていない。
