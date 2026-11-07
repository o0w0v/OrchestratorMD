# 同じ100件比較の再開

ユーザーの明示回答「残り6件の設計を終えて100件比較を再開」に基づく。先に開始した95〜99の5件をそのまま回収し、100件目の相談・設計を完了した後、元計画どおり全100件×2方式の比較とHost採点・会計監査・報告へ進む。新しい課題や別実験は始めない。

旧188回と5件の10回、計198回の完了応答を再生成しない。元の容量失敗1回も物理履歴と不明消費として保存する。次の新規生成はPR100-100。全100設計をsealしてからA/B実作業、全200採否をsealしてからprivate採点、追加の採点モデル呼出し0。モデル・low/medium/high・prompt・成果物・修正上限・元の600/Task12予算guardは維持する。旧失敗とraw/freeze/通知は上書きしない。

内部再送や容量失敗の未知費用はnull。報告usage既知小計に、不明callごと12Creditsの予算予備額を加えて次call前600を監視する。予備額は実支出や保証上限ではない。単独比較への共有費配賦とstudyの重複しない小計を分け、実支出総額と厳密な削減率はnullのまま。Cloud外側自動retry0、再発capacity/usage欠測/不正tool等はSTOP。

既存runは保存し別revisionで続行。通常の100件の実験手順は次の原計画を維持する。

# 再開revisionについて

ユーザーの再開依頼により、RECOVERY_PLAN_JA.mdの限定的な完了応答回収・会計不明分の分離を適用する。課題、モデル、推論割当、確認方針、採点、修正回数、予算閾値は元のまま。旧STOPとrawは不変。

# 新100件：必要十分な確認と部分修正の比較

2026-11-04。ユーザーの「それでまた100件採点してみて」に基づく実行。

新100件は既知10業務型×設計難易度5×2例。旧2回の100件とは添付データが非重複。合成JSON＋短いreport_mdの机上処理で、実人間の要件対話やOffice GUIは対象外。

同じ元のSol相談・固定owner補足・Sol方針・実施承認を2方式へ渡す。追加の専用PlannerやLuna/Terraへの依頼書生成は置かない。元の方針で必要情報が揃っているため、任意の引継ぎ段を全件省く。

- A SOL_CONTINUE：同じSol sessionで通常続行。余分な独立業務Reviewerは加えない。
- B PRACTICAL：小仕事はAと同じ直接Sol処理なので物理callを共有し、再生成しない。それ以外は新Gemma全作業→fresh Solが短い方針で1回確認。ACCEPTなら原物採用、PATCHなら変更前後を照合して必要箇所だけ適用。REWORK等は同じSolへ対象限定の修正を最大1回。修正後の別AI監査は置かない。未解決は未解決として残す。

profileは公開の業務型・入力構造から実行前に決める。small=low、normal=medium、complex=high。両方式のSolに同じprofileを使い、旧xhighを比較基準にして削減を水増ししない。smallの共有実作業も単独方式の比較には各全額、study実支出には一度だけ。

最初に全100相談を公開対話として固定し、それから2方式を交互先行で実行する。smallは同じ物理callなのでA先行。全200最終採否をROUTING_COMPLETEへ固定してからprivate正解を採点にだけ使う。private正解、他方式回答、前の実験結果をモデルへ渡さず、採点結果で経路や採否を変えない。

運用の確認文は共通88文字＋元資料＋出力形式の例のみ。四観点の逐一採点、optional改善案、遵守報告は出力させない。CLIの複雑なunion schemaに依存せず、確認は短いJSON形式例で指示しHostで判定別の形式を検査する。作業成果物には元のJSON schemaを使う。形式失敗の候補しかない場合は元の公開対話だけからSolが最大1回実作業し、この費用も全額計上する。

採点は全件のデータ完全一致、誤採用、修正前後、採用区分、未解決、型/profile別、対応差、全工程実Credits・tokens・時間・資源。文章は成果物と一緒に読む実務基準を運用Solへ適用するが、別のSolによる全件独立文章監査は今回は追加しない。文章の同等性を独立に証明したとは報告しない。完了時に修正・失敗・代表例のrawを読み、必要な追加解釈を別ファイルへ保存する。

Cloud最大500回、Local初回最大100・物理最大200。見込み200～400 Credits、次Cloud前600 Creditsで監視STOP、Taskごと12 Creditsでも次call停止。これは呼出し途中のhard capではない。準備chat・手作業実時間・電力は未測定null。Cloud retry0。Local infraのみ固定runnerが所有serverを回復し同payload最大1retry、初回も保存。繰返しinfra、GPU不能、Cloud capacity/reconnect、usage欠測、cache_write非0、未知tool、保存異常はSTOP。自動resume/restartなし。

Gemma4 26B digest、native thinking、ctx65536/output32768、seed/sampling、FA1/KVf16は旧試験から維持。既存ChatGPT Credits、verified capture、installed CLI、agents disabled、Standardを使う。会話継続のturn.completed累積usageは前回counterを引いた増分だけ計上し、persistent rolloutのusage metadataと照合する。非公開の思考内容は転記しない。

RAM6GiB/disk5GiB。未所有process停止、モデルdownload/install、課題・予算・promptの実行中変更、旧成果の上書き、GitHub公開、Production変更は行わない。完了後はHost分析・会計監査・報告まで自動実行。後処理だけの不具合はraw/freeze/STOPを残した別revisionで修理し、完了済みmodel callを再実行しない。

旧結果とは入力も設定も異なり、率をpoolしない。今回の比較は推論設定・呼出し削減・部分修正を合わせた運用全体の効果であり、Reviewer単独の差ではない。全相談先行、cache、時刻、背景負荷の留保を記す。少ない誤りを人手で直して使える場合も、修正箇所と手間を明示して評価する。
