# ローカルLLMの得意分野調査：小型から超大型まで

調査日：2026-10-24。9開発元・26モデル。公開された開発元資料を確認し、Gemma4 26Bを補う候補を整理した。

**次は、コード修正・条件推論・文書/画像理解を別々に比較するのがよい。大きいモデルも比較対象に含めるが、今回のPCで動かす候補とは分ける。**

## 分野別の見取り図

| 調べたい仕事 | 手元または比較的小さい候補 | 大きいモデルの候補 | 確認したいこと |
| --- | --- | --- | --- |
| 型・APIをまたぐコード修正 | Devstral Small 2、Qwen3.6-27B、GLM-4.7-Flash | Qwen3-Coder-Next、Devstral 2 | Gemmaが失敗した修正を、余計な変更なく直せるか |
| 数学・複雑な条件判断 | gpt-oss-20b、Phi-4-reasoning-plus | gpt-oss-120b、DeepSeek-V4系 | 条件漏れ・計算間違いを減らせるか |
| 長い資料の照合・要約 | Qwen3.5-9B、Gemma4 31B | Qwen3.5-122B/397B、Kimi、Mistral Large 3 | 資料にない情報を足さず、根拠と例外条件を保てるか |
| 表・図・スライド画像の理解 | Qwen3.5-9B、GLM-OCR | Qwen3.5大型、GLM-5.3-Flash、Kimi | OCR、表の対応、図の読み取りを分けて測る |
| 複数工程の業務・画面操作 | 小さいモデルはまず固定工程で確認 | MiniMax-M3.1-Flash、Kimi系 | モデル以外のtool・操作環境込みで測る必要がある |

この表は**比較する価値がある用途**を示す。新モデルがGemmaより得意、あるいは当方の500件で高得点、とはまだ判定していない。各候補の根拠と注意点は[全26モデルの一覧](MODEL_MATRIX_JA.md)に記載。

## 既に分かっていることは維持する

- Gemma26の500件スクリーニングは既存結果。コード85/100、PPT78/100、Excel60/100、Word67/100、複数アプリ43/100が固定チェックを通過した。ただしOfficeはHostがtyped JSONからファイルを作る方式で、業務全体やGUI操作の成功率ではない。
- 過去の同一24件coding比較では、Gemma非採用4件のうちQwen14が1件を補完し、Qwen3.5は0件だった。これはその条件での結果として扱う。画像・Office・他のTaskへの補完性まで否定も肯定もしない。
- 今回は公開資料の調査。新しいgeneration、download、Router変更は行っていない。Gemma12のquarantineも維持する。

既存結果：[Gemma26 knowledge](https://github.com/o0w0v/OrchestratorMD/blob/docs/additional-500-task-catalog-20261024/docs/task-catalog/2026-10-additional-500/knowledge/GEMMA26_KNOWLEDGE_JA.md)、[過去の補完実測](https://github.com/o0w0v/OrchestratorMD/blob/docs/additional-500-task-catalog-20261024/docs/task-catalog/2026-10-additional-500/knowledge/HISTORICAL_COMPLEMENTARITY.json)。

## Office業務を一括りにしない

1. **読む**：PDF、表画像、スライドから情報を取り出す。
2. **考える・書く**：条件照合、数式、文章、説明の組立。
3. **編集する**：PPTX/XLSX/DOCXの構造、数式、レイアウトを壊さず保存する。
4. **操作する**：GUIや複数アプリをまたいで手順を完了する。

画像理解の点数から3や4の成功率は分からない。GLM-OCRは1の専用候補であり、PowerPoint作成やExcel計算を丸ごと任せる候補ではない。既存のHost補助方式とGUI方式も別集計にする。

## 次に絞る候補

- **コード補完**：既に導入済みのDevstral Small 2とQwen3-Coder-Next。新規候補としてQwen3.6-27B/35B-A3B。
- **条件・数理推論**：導入済みgpt-oss-20b。大容量環境ではgpt-oss-120bやDeepSeek系を対照にする。
- **文書・画像**：導入済みQwen3.5-9Bを画像入力で比較。OCR専用枠はGLM-OCR。
- **大型の参照枠**：122B級を一段目とし、397B〜T級は利用環境と費用が用意できた場合に限る。今回それらの実行はしていない。

まず既知のGemma失敗例と成功controlを使って小さく比較し、補完が見えた分野だけ新しいTaskで確認する。既知失敗例での改善は診断結果、新しいTaskでの改善は汎化の証拠として分ける。task分割精度の比較は今回の対象外。

## 読み方と限界

- [MODEL_MATRIX_JA.md](MODEL_MATRIX_JA.md)：モデル別の分野・大きさ・根拠。
- [RESOURCE_GUIDE_JA.md](RESOURCE_GUIDE_JA.md)：必要メモリと、このPC/大容量環境の違い。
- [EVALUATION_PLAN_JA.md](EVALUATION_PLAN_JA.md)：得意不得意を確かめる比較方法。
- [MODEL_SURVEY.json](MODEL_SURVEY.json)、[SOURCES.json](SOURCES.json)：機械可読の整理。

公開成績の多くは開発元の自己報告で、量子化、context、出力上限、thinking、tool scaffoldが異なる。横並びの総合順位は作らない。特に既存8192 context / 2048 output / one-shot条件での成績とは同一視しない。日本語Officeの適性は別の実測が必要。動くモデルの一覧を網羅した調査でも、利用licenseを一括承認する資料でもない。
