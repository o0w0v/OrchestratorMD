# 実装・検証手順の比較 / bounded-2.2.6-codex-value

セットID: `bounded-2.2.6-codex-value`

課題数: 5。個別記録あり: 5、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](bounded-2.2.6-codex-value.json) / [結果と根拠のJSON](../results/bounded-2.2.6-codex-value.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_A_COMPLETION_JA.md](../reports/bounded-2.2.6-codex-value/RESULTS_A_COMPLETION_JA.md) / [RESULTS_CODEX_BASELINE_JA.md](../reports/bounded-2.2.6-codex-value/RESULTS_CODEX_BASELINE_JA.md) / [RESULTS_JA.md](../reports/bounded-2.2.6-codex-value/RESULTS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "generation_options": {
      "temperature": 0,
      "seed": 20260926,
      "num_ctx": 8192,
      "num_predict": 2048
    }
  },
  {
    "generation_options": {
      "temperature": 0,
      "seed": 20260926,
      "num_ctx": 8192,
      "num_predict": 2048
    }
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [CVB-001](#cvb-001) | CLIに観測process sampleのPID範囲を表示 | 記録あり |
| [CVB-002](#cvb-002) | CLIにauditのpolicy disposition件数を集約表示 | 記録あり |
| [CVB-003](#cvb-003) | MemoryPressure evidenceにsample内未観測parent件数を追記 | 記録あり |
| [CVB-004](#cvb-004) | provider-rejected auditに保持済みreservationを表示 | 記録あり |
| [CVB-005](#cvb-005) | bounded telemetry readerのUTF-8境界によるsize診断誤分類を修正 | 記録あり |

<a id="cvb-001"></a>
## CVB-001

CLIに観測process sampleのPID範囲を表示

元のtask_id: `CVB-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement pid_range(&[ncos_core::Process]) -> String. Empty returns none; otherwise return min..max in unsigned decimal, including singleton N..N. Use the minimum and maximum pid across the entire possibly unsorted sample. Do not sort/mutate the slice or infer unsampled processes. Ignore parent_pid and rss_kib. Handle duplicates, zero and u32::MAX as supplied numeric snapshot values.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.6-codex-value --task CVB-001 --output work/CVB-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/CVB-001/review.json | — | [R-fb7c07216055e1](#r-fb7c07216055e1) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-cd1fef1e93675e](#r-cd1fef1e93675e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fb7c07216055e1"></a>
### 根拠 R-fb7c07216055e1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `2505adb0f1cff8a8d492f6c17a74183ef3cbb31e7240804da4541793fd8417e2`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<a id="r-cd1fef1e93675e"></a>
### 根拠 R-cd1fef1e93675e

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `workspace/records/router-v2.2/CVB-001/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f918bb344e9061bf09d9d5b260d2278b4a26d21d84982012136f3329f9b40bb7`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement pid_range(&[ncos_core::Process]) -> String. Empty returns none; otherwise return min..max in unsigned decimal, including singleton N..N. Use the minimum and maximum pid across the entire possibly unsorted sample.",
    "Do not sort/mutate the slice or infer unsampled processes. Ignore parent_pid and rss_kib. Handle duplicates, zero and u32::MAX as supplied numeric snapshot values.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Implement pid_range(&[ncos_core::Process]) -> String. Empty returns none; otherwise return min..max in unsigned decimal, including singleton N..N. Use the minimum and maximum pid across the entire possibly unsorted sample.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not sort/mutate the slice or infer unsampled processes. Ignore parent_pid and rss_kib. Handle duplicates, zero and u32::MAX as supplied numeric snapshot values.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "value_cvb_001"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--bin",
        "ncos",
        "value_cvb_001",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--test",
        "cli",
        "demo_audit_and_refusal_to_overwrite",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/CVB-001",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="cvb-002"></a>
## CVB-002

CLIにauditのpolicy disposition件数を集約表示

元のtask_id: `CVB-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement policy_overview(&[ncos_core::AuditRecord]) -> String. Count Some(policy).decision Allow, Deny, RequireConfirmation and absent policy separately. Return exactly allow=A; deny=D; confirm=C; unevaluated=U in that order, including zeros. Count each input record once including duplicate records. Do not derive policy from proposal/execution/verification/source, mutate records, evaluate policy, or change audit serialization.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.6-codex-value --task CVB-002 --output work/CVB-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/CVB-002/review.json | — | [R-51b8a6a31cf956](#r-51b8a6a31cf956) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-baf06b723395c9](#r-baf06b723395c9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-51b8a6a31cf956"></a>
### 根拠 R-51b8a6a31cf956

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `2505adb0f1cff8a8d492f6c17a74183ef3cbb31e7240804da4541793fd8417e2`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<a id="r-baf06b723395c9"></a>
### 根拠 R-baf06b723395c9

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `workspace/records/router-v2.2/CVB-002/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `711ebf6ca9d2f2b249e1cb3db0ba18ebfa89fa3ecd9aa54bdfecbd071bc33e0d`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement policy_overview(&[ncos_core::AuditRecord]) -> String. Count Some(policy).decision Allow, Deny, RequireConfirmation and absent policy separately. Return exactly allow=A; deny=D; confirm=C; unevaluated=U in that order, including zeros.",
    "Count each input record once including duplicate records. Do not derive policy from proposal/execution/verification/source, mutate records, evaluate policy, or change audit serialization.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Implement policy_overview(&[ncos_core::AuditRecord]) -> String. Count Some(policy).decision Allow, Deny, RequireConfirmation and absent policy separately. Return exactly allow=A; deny=D; confirm=C; unevaluated=U in that order, including zeros.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Count each input record once including duplicate records. Do not derive policy from proposal/execution/verification/source, mutate records, evaluate policy, or change audit serialization.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "value_cvb_002"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--bin",
        "ncos",
        "value_cvb_002",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-cli",
        "--test",
        "cli",
        "demo_audit_and_refusal_to_overwrite",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "demo_audit_and_refusal_to_overwrite"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/CVB-002",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="cvb-003"></a>
## CVB-003

MemoryPressure evidenceにsample内未観測parent件数を追記

元のtask_id: `CVB-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate only MemoryPressure evidence. Preserve its first evidence string exactly; append a second string parent_unobserved=N. When processes_truncated is false, N counts process rows whose nonzero parent_pid does not equal any pid in the sample. Count rows, not distinct parents. Ignore parent_pid=0. When processes_truncated is true append parent_unobserved=unknown instead. Do not infer an orphan or failure: this is sample visibility only. Preserve detection thresholds, event identity/target, HighLoad evidence and process order/data.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.6-codex-value --task CVB-003 --output work/CVB-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/CVB-003/review.json | — | [R-b9856ec2488c29](#r-b9856ec2488c29) |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | — | — | [R-ae717759f3757f](#r-ae717759f3757f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b9856ec2488c29"></a>
### 根拠 R-b9856ec2488c29

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `2505adb0f1cff8a8d492f6c17a74183ef3cbb31e7240804da4541793fd8417e2`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<a id="r-ae717759f3757f"></a>
### 根拠 R-ae717759f3757f

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `workspace/records/router-v2.2/CVB-003/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `de2038d3c3fceb47c9f287a9bff0e906f635ec87bfbc9627579d41a3d679b9e3`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate only MemoryPressure evidence. Preserve its first evidence string exactly; append a second string parent_unobserved=N. When processes_truncated is false, N counts process rows whose nonzero parent_pid does not equal any pid in the sample. Count rows, not distinct parents. Ignore parent_pid=0.",
    "When processes_truncated is true append parent_unobserved=unknown instead. Do not infer an orphan or failure: this is sample visibility only. Preserve detection thresholds, event identity/target, HighLoad evidence and process order/data.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate only MemoryPressure evidence. Preserve its first evidence string exactly; append a second string parent_unobserved=N. When processes_truncated is false, N counts process rows whose nonzero parent_pid does not equal any pid in the sample. Count rows, not distinct parents. Ignore parent_pid=0.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "When processes_truncated is true append parent_unobserved=unknown instead. Do not infer an orphan or failure: this is sample visibility only. Preserve detection thresholds, event identity/target, HighLoad evidence and process order/data.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "value_cvb_003"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--lib",
        "value_cvb_003",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-events",
        "--test",
        "acceptance",
        "event_detect",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "event_detect"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/CVB-003",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="cvb-004"></a>
## CVB-004

provider-rejected auditに保持済みreservationを表示

元のtask_id: `CVB-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the provider-rejected audit reason in Runtime::handle. Change exactly its reason argument to Provider failed or exceeded resource contract; charged_calls=C; reserved_tokens=T using self.usage.inference_calls and self.usage.reserved_tokens at rejection time. The record helper takes &str. Preserve charges on provider error or over-budget response, no retries/refund, source/event/time and all other reasons. Do not log provider error text, infer actual tokens or alter authority/eligibility.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.6-codex-value --task CVB-004 --output work/CVB-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| コードの検証 | model=gemma4:26b | INFRA_ERROR | — | — | — | workspace/records/router-v2.2/CVB-004/review.json | — | [R-1767e792d0966b](#r-1767e792d0966b) |
| ローカル実装 | model=gemma4:26b | INFRA_ERROR | INFRA_ERROR | — | — | — | — | [R-4e6dce2e434c62](#r-4e6dce2e434c62) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1767e792d0966b"></a>
### 根拠 R-1767e792d0966b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `2505adb0f1cff8a8d492f6c17a74183ef3cbb31e7240804da4541793fd8417e2`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<a id="r-4e6dce2e434c62"></a>
### 根拠 R-4e6dce2e434c62

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `workspace/records/router-v2.2/CVB-004/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `31898424dc519f8de378f6b25c37034695a12de3de1ffe9ff244426c51dd0611`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the provider-rejected audit reason in Runtime::handle. Change exactly its reason argument to Provider failed or exceeded resource contract; charged_calls=C; reserved_tokens=T using self.usage.inference_calls and self.usage.reserved_tokens at rejection time.",
    "The record helper takes &str. Preserve charges on provider error or over-budget response, no retries/refund, source/event/time and all other reasons. Do not log provider error text, infer actual tokens or alter authority/eligibility.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate the provider-rejected audit reason in Runtime::handle. Change exactly its reason argument to Provider failed or exceeded resource contract; charged_calls=C; reserved_tokens=T using self.usage.inference_calls and self.usage.reserved_tokens at rejection time.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "The record helper takes &str. Preserve charges on provider error or over-budget response, no retries/refund, source/event/time and all other reasons. Do not log provider error text, infer actual tokens or alter authority/eligibility.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "value_cvb_004"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-agent",
        "--lib",
        "value_cvb_004",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-agent",
        "--test",
        "acceptance",
        "healthy_fast_path_never_calls_model",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "healthy_fast_path_never_calls_model"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/CVB-004",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>

<a id="cvb-005"></a>
## CVB-005

bounded telemetry readerのUTF-8境界によるsize診断誤分類を修正

元のtask_id: `CVB-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Debug read_bounded(&Path) -> Result<String,String>. Files over 65536 bytes must return telemetry size limit exceeded, even if the bounded prefix splits a multibyte UTF-8 character. Current read_to_string before size check wrongly reports telemetry unavailable. Read at most 65537 bytes (not the whole file). At size <=65536 return exact valid UTF-8 including empty/NUL; invalid UTF-8 or open/read failure returns telemetry unavailable. No retries, lossy decoding, file writes, dependencies, or changes elsewhere.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.6-codex-value --task CVB-005 --output work/CVB-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-e11bd189f2c11d](#r-e11bd189f2c11d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e11bd189f2c11d"></a>
### 根拠 R-e11bd189f2c11d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/0`
- 出典ファイルのSHA-256: `2505adb0f1cff8a8d492f6c17a74183ef3cbb31e7240804da4541793fd8417e2`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.6-codex-value.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Debug read_bounded(&Path) -> Result<String,String>. Files over 65536 bytes must return telemetry size limit exceeded, even if the bounded prefix splits a multibyte UTF-8 character. Current read_to_string before size check wrongly reports telemetry unavailable.",
    "Read at most 65537 bytes (not the whole file). At size <=65536 return exact valid UTF-8 including empty/NUL; invalid UTF-8 or open/read failure returns telemetry unavailable. No retries, lossy decoding, file writes, dependencies, or changes elsewhere.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "All workspace tests remain valid.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Debug read_bounded(&Path) -> Result<String,String>. Files over 65536 bytes must return telemetry size limit exceeded, even if the bounded prefix splits a multibyte UTF-8 character. Current read_to_string before size check wrongly reports telemetry unavailable.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Read at most 65537 bytes (not the whole file). At size <=65536 return exact valid UTF-8 including empty/NUL; invalid UTF-8 or open/read failure returns telemetry unavailable. No retries, lossy decoding, file writes, dependencies, or changes elsewhere.",
      "category": "functional"
    },
    {
      "criterion_id": "REGRESSION",
      "criterion_text": "Existing workspace behavior remains valid.",
      "category": "quality"
    },
    {
      "criterion_id": "FORMAT",
      "criterion_text": "Rust formatting remains clean.",
      "category": "quality"
    },
    {
      "criterion_id": "CLIPPY",
      "criterion_text": "No clippy warnings.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-TEST",
      "criterion_text": "All workspace tests remain valid.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-CHECK",
      "criterion_text": "Workspace type checking succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "WORKSPACE-BUILD",
      "criterion_text": "Workspace build succeeds.",
      "category": "quality"
    },
    {
      "criterion_id": "SCOPE",
      "criterion_text": "Only declared editable regions change; protected source and tests remain identical.",
      "category": "structural"
    }
  ],
  "checks": [
    {
      "id": "acceptance",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "value_cvb_005"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-observer-linux",
        "--lib",
        "value_cvb_005",
        "--",
        "--exact",
        "--nocapture"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "regression",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--locked",
        "-p",
        "ncos-observer-linux",
        "--test",
        "acceptance",
        "memory_parse",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "fmt",
        "--check"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "clippy",
      "kind": "lint",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "clippy",
        "--offline",
        "--all-targets",
        "--all-features",
        "--",
        "-D",
        "warnings"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-test",
      "kind": "test",
      "parser": "rust",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "memory_parse"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "check",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-build",
      "kind": "build",
      "cwd": "units/CVB-005",
      "timeout_seconds": 330,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "build",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    }
  ]
}
```

</details>
