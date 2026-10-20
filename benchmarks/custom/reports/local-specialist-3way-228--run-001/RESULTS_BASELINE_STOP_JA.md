> Historical experiment report. Filesystem paths were removed; links to non-distributed original files are shown as source labels. [Task-to-result correspondence](../../sets/local-specialist-3way-228--run-001.md). This report alone does not establish a task result.

# Local Specialist 3-Way Challenger — baseline停止記録

集計: 2026-10-06T08:51:17.838920+00:00。判定: **INCONCLUSIVE / STOPPED_HOST_FIXTURE_ERROR**。

3モデル比較は未実行。Local inference 0、FULL_4_WAY_ECONOMIC_TASK 0/24。モデル品質・GPU安定性・winnerは未評価。

## 停止原因

私が作成したLS3W228-017の編集禁止helper `ls3_epoch_bucket` が `clippy::manual_checked_ops` に違反している。固定Clippyはsource 86〜89行でFAIL、許可bodyは95〜97行であり、bounded実装側から修正できない。

初期sourceそのものでも、実際の固定argv `cargo clippy --offline --all-targets --all-features -- -D warnings` により再現した。候補bodyはacceptance/regression/fmt/workspace test/check/buildを通過しており、これはモデル能力FAILではない。Host作成fixtureの妥当性を全checkで確認してからfreezeすべきだった。

旧STOPとFREEZEは保持。017の自動修正は採用していない。STOP後は変更不要な018〜024のGPU不要baselineのみ別runnerで完成させ、Localを開始していない。

## Baseline

GPT-6 Sol / xhigh / Standard、独立Planner→clean Executor→固定mandatory validation→独立Reviewer。23/24件がfull PASS + ACCEPT_NO_CHANGE。001〜016・018〜024は各1 implementation。017には4 implementation sessionのraw証拠を保持し、成功扱いしない。

| Task | Family | Review | Measured baseline credits |
| --- | --- | --- | --- |
| LS3W228-001 | COLLECTION | ACCEPT_NO_CHANGE | 3.85823 |
| LS3W228-002 | COLLECTION | ACCEPT_NO_CHANGE | 3.7561999999999998 |
| LS3W228-003 | COLLECTION | ACCEPT_NO_CHANGE | 5.03447 |
| LS3W228-004 | COLLECTION | ACCEPT_NO_CHANGE | 2.86708 |
| LS3W228-005 | COLLECTION | ACCEPT_NO_CHANGE | 3.09579 |
| LS3W228-006 | COLLECTION | ACCEPT_NO_CHANGE | 3.5065299999999997 |
| LS3W228-007 | NUMERIC | ACCEPT_NO_CHANGE | 2.9335 |
| LS3W228-008 | NUMERIC | ACCEPT_NO_CHANGE | 4.43391 |
| LS3W228-009 | NUMERIC | ACCEPT_NO_CHANGE | 3.5620600000000002 |
| LS3W228-010 | NUMERIC | ACCEPT_NO_CHANGE | 2.84773 |
| LS3W228-011 | NUMERIC | ACCEPT_NO_CHANGE | 3.93901 |
| LS3W228-012 | NUMERIC | ACCEPT_NO_CHANGE | 3.8833699999999998 |
| LS3W228-013 | ADAPTER | ACCEPT_NO_CHANGE | 4.612260000000001 |
| LS3W228-014 | ADAPTER | ACCEPT_NO_CHANGE | 4.14501 |
| LS3W228-015 | ADAPTER | ACCEPT_NO_CHANGE | 3.10266 |
| LS3W228-016 | ADAPTER | ACCEPT_NO_CHANGE | 3.30192 |
| LS3W228-018 | ADAPTER | ACCEPT_NO_CHANGE | 2.5870699999999998 |
| LS3W228-019 | RECEIPT | ACCEPT_NO_CHANGE | 2.41752 |
| LS3W228-020 | RECEIPT | ACCEPT_NO_CHANGE | 2.23621 |
| LS3W228-021 | RECEIPT | ACCEPT_NO_CHANGE | 2.49972 |
| LS3W228-022 | RECEIPT | ACCEPT_NO_CHANGE | 3.00953 |
| LS3W228-023 | RECEIPT | ACCEPT_NO_CHANGE | null |
| LS3W228-024 | RECEIPT | ACCEPT_NO_CHANGE | 2.86798 |

有効23件のbaseline credit全合計: null。実際の全CLI支出ledger全合計: null credits / 75 sessions。失敗017の費用も実支出側へ含める。測定usage欠測: 1、unique thread IDs: 75。

欠測を除く測定済みsubtotalはbaseline 74.49776 / actual CLI 85.82789000000004 credits。欠測の請求を0と仮定していない。023の候補生成前provider capacity errorは候補なし同一入力retryで品質回復したが、元usageはnullのままでTask経済合計もnull。

runner停止でEND.json未保存だったsessionは既存events.jsonlの実turn.completedからのみusageを別artifactへ復元した。旧raw/START/ENDを変更していない。復元sessionのwall/exit_codeはnull。準備・本chatのtokenはnullで推定しない。USD equivalentは実請求額ではなく、JPY未取得。

## Freeze / blinding / preservation

全24件のsource・契約・acceptance・reference・checksとruntimeはFREEZE.jsonで保全。独立Codex baselineへLocal result/candidate/diff/diagnosticsを渡していない。Localは0call。raw CLI、pre-send input hashes、sealed-baseline-copiesを保存。コピーはpost-run stateであり、per-turn入力証拠はpre-send hashを参照する。

旧preflight MANUAL_ACTION_REQUIRED、全旧実験・STOP・CUDA証跡、Router、Operational Policy、bounded2.2.8、model files、OS/driver/Ollamaを変更していない。今回のHost fixture問題を過去のGemma Host STOPやmodel coding FAILへ混ぜない。

## 初期source診断

固定argv・各workspaceの独立targetで全24件を確認し、017だけFAIL、他23件PASS。fixture-exact-diagnostics/summary.jsonが有効証拠。

先行のfixture-diagnostics/は共有targetかつargv差のある補助診断で017もPASSとなったため、acceptance証拠に使わない。rawは保持し、取り直し結果で明示的にsupersede。cache差の根本原因はUNRESOLVED。verify_fixture_exact.pyの起動時構文エラーも旧版を残し、構文修正のみのv2で診断した。いずれもlive Protocolや条件を変更していない。

## 未採用修正案

protected helperだけを下記へ変更する案。goal・signature・allowed body・acceptance・model/options・Protocolは同じ。proposalの固定ClippyはPASS。

```rust
fn ls3_epoch_bucket(epoch: u128, width: u128) -> Option<u128> {
    epoch.checked_div(width)
}
```

採用するなら旧runを保持した新runで新freezeを作り、017の全経路に同一初期sourceを供給する。変更のない23 baselineはsource/contract/check hash一致を確認して再利用し、017だけblind baselineを取り直す。修正案はfixture-proposal/PROPOSAL.json。初期source/hash変更への確認待ち。

## Model identities / infrastructure

| Arm | Model | Digest | Quantization |
| --- | --- | --- | --- |
| qwen14 | qwen2.5-Coder:14b | 9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849 | Q4_K_M |
| gemma26 | gemma4:26b | 08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68 | Q4_K_M |
| qwen35 | qwen3.5:9b | 56671c2ab9385f9cfcb404638e32cd62d88e3501d44822208363c010179a3c90 | Q4_K_M |

Qwen3.5導入済み、3モデルのmanifest/identityをfreeze済み。ユーザーtray Quit確認済み。fresh start・loaded-state GPU sampling・model cohortは未実行であり、INFRA_STABLEとは評価しない。CUDA再現なしという主張もしない（inference未実行）。

## 比較・次の作業

adoption・RAW PASS・LF rescue・各モデルcredit savings・VRAM/latency・family winnersは全てN/A。baselineだけからモデル勝敗を決めない。production更新なし。

修正案の採用確認後にのみ新freeze・017 baseline・全24 baseline seal→Qwen14→user Quit→Gemma26→user Quit→Qwen3.5の順に進める。確認がなければLocal inferenceを開始しない。


停止時の回帰確認: Worker offline 275 tests PASS、Rust fmt / clippy / test / check / build PASS。BASELINE_AUDIT.jsonでruntime/source/role/blinding保全を確認。POST_BASELINE_GPU_SNAPSHOT.jsonではOllama processなし・API応答なし・GPU query正常。017修正案未採用。
