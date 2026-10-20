# 実装・検証手順の比較 / bounded-2.2.8-economic-retry

セットID: `bounded-2.2.8-economic-retry`

課題数: 14。個別記録あり: 14、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](bounded-2.2.8-economic-retry.json) / [結果と根拠のJSON](../results/bounded-2.2.8-economic-retry.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_2_2_8_ECONOMIC_RETRY_JA.md](../reports/bounded-2.2.8-economic-retry/RESULTS_2_2_8_ECONOMIC_RETRY_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "model": "qwen2.5-Coder:14b",
    "model_digest": "9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849",
    "codex_model": "gpt-6-sol",
    "effort": "xhigh",
    "speed": "Standard"
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
| [ECR228-001](#ecr228-001) | Render audit execution presence tally as a fixed three-line receipt | 記録あり |
| [ECR228-002](#ecr228-002) | Render sampled disk and service availability as an exact nullable receipt | 記録あり |
| [ECR228-003](#ecr228-003) | Borrow present audit events paired with their recorded schema versions | 記録あり |
| [ECR228-004](#ecr228-004) | Borrow the first denied policy reason including an empty reason | 記録あり |
| [ECR228-005](#ecr228-005) | Compute per-observation RSS excess above an inclusive allowance | 記録あり |
| [ECR228-006](#ecr228-006) | Mark adjacent audit source transitions without trimming | 記録あり |
| [ECR228-007](#ecr228-007) | Locate the first confirmation policy that also has a recorded proposal | 記録あり |
| [ECR228-008](#ecr228-008) | Extract evidence row counts from HighLoad events without flattening | 記録あり |
| [ECR228-009](#ecr228-009) | Remove audit latency narrowing while keeping inclusive budget equality | 記録あり |
| [ECR228-010](#ecr228-010) | Advance a sampled display cursor without usize addition overflow | 記録あり |
| [ECR228-011](#ecr228-011) | Choose the least valid available-memory sample while rejecting incomplete validity | 記録あり |
| [ECR228-012](#ecr228-012) | Detect nondecreasing recorded risk sequence with ties permitted | 記録あり |
| [ECR228-013](#ecr228-013) | Delegate disk availability caption to the protected optional-count renderer | 記録あり |
| [ECR228-014](#ecr228-014) | Delegate evidence cleanup to the protected trimmed-item selector | 記録あり |

<a id="ecr228-001"></a>
## ECR228-001

Render audit execution presence tally as a fixed three-line receipt

元のtask_id: `ECR228-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return exactly dry_run=N followed by LF, blocked=M followed by LF, missing=K followed by LF. Unsigned decimal row counts, no spaces, quotes or extra text. Classify each row by execution.status: DryRun, Blocked, or absent execution. Ignore changed/detail/proposal/verification. Count duplicates independently. Preserve records. Empty input yields three zeros.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-001 --output work/ECR228-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-8d1422afe9d06b](#r-8d1422afe9d06b) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-4f685566b0d914](#r-4f685566b0d914) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8d1422afe9d06b"></a>
### 根拠 R-8d1422afe9d06b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/0`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-4f685566b0d914"></a>
### 根拠 R-4f685566b0d914

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-001/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `4488a434688ac52d9f425d75a26ab9c43e71ec70c2490268fba61ed829fbd991`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return exactly dry_run=N followed by LF, blocked=M followed by LF, missing=K followed by LF. Unsigned decimal row counts, no spaces, quotes or extra text.",
    "Classify each row by execution.status: DryRun, Blocked, or absent execution. Ignore changed/detail/proposal/verification. Count duplicates independently. Preserve records. Empty input yields three zeros.",
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
      "criterion_text": "Return exactly dry_run=N followed by LF, blocked=M followed by LF, missing=K followed by LF. Unsigned decimal row counts, no spaces, quotes or extra text.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Classify each row by execution.status: DryRun, Blocked, or absent execution. Ignore changed/detail/proposal/verification. Count duplicates independently. Preserve records. Empty input yields three zeros.",
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
      "cwd": "units/ECR228-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_001"
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
        "economic_ecr228_001",
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
      "cwd": "units/ECR228-001",
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
      "cwd": "units/ECR228-001",
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
      "cwd": "units/ECR228-001",
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
      "cwd": "units/ECR228-001",
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
      "cwd": "units/ECR228-001",
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
      "cwd": "units/ECR228-001",
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

<a id="ecr228-002"></a>
## ECR228-002

Render sampled disk and service availability as an exact nullable receipt

元のtask_id: `ECR228-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return exactly disks=VALUE;services=VALUE followed by one LF. Each VALUE is unsigned decimal for Some(count), or the lowercase word unknown for None. No spaces, CR, quotes or extra fields. Some(0) is known zero. Preserve usize::MAX without narrowing. Use disk_count/service_count only; do not infer counts from other state fields. Preserve state.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-002 --output work/ECR228-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-580bdee1a25004](#r-580bdee1a25004) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-5d609607360282](#r-5d609607360282) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-580bdee1a25004"></a>
### 根拠 R-580bdee1a25004

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/1`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-5d609607360282"></a>
### 根拠 R-5d609607360282

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-002/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `18a2886233128005c8498685df5e9083dfb0dc235d9d2097e60b7aa6daad3da4`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return exactly disks=VALUE;services=VALUE followed by one LF. Each VALUE is unsigned decimal for Some(count), or the lowercase word unknown for None. No spaces, CR, quotes or extra fields.",
    "Some(0) is known zero. Preserve usize::MAX without narrowing. Use disk_count/service_count only; do not infer counts from other state fields. Preserve state.",
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
      "criterion_text": "Return exactly disks=VALUE;services=VALUE followed by one LF. Each VALUE is unsigned decimal for Some(count), or the lowercase word unknown for None. No spaces, CR, quotes or extra fields.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Some(0) is known zero. Preserve usize::MAX without narrowing. Use disk_count/service_count only; do not infer counts from other state fields. Preserve state.",
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
      "cwd": "units/ECR228-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_002"
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
        "economic_ecr228_002",
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
      "cwd": "units/ECR228-002",
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
      "cwd": "units/ECR228-002",
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
      "cwd": "units/ECR228-002",
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
      "cwd": "units/ECR228-002",
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
      "cwd": "units/ECR228-002",
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
      "cwd": "units/ECR228-002",
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

<a id="ecr228-003"></a>
## ECR228-003

Borrow present audit events paired with their recorded schema versions

元のtask_id: `ECR228-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. For each row with a present event, return (that row schema_version, borrowed Event reference). Preserve row order, duplicates and schema zero/MAX. Skip absent events. References must point to original event values; no clone or owned Event allocation. Ignore event kind and all other audit fields. Empty input gives empty. Preserve records.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-003 --output work/ECR228-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-3ef7cbf7a52cf9](#r-3ef7cbf7a52cf9) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-b5ee76ecb27f80](#r-b5ee76ecb27f80) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-3ef7cbf7a52cf9"></a>
### 根拠 R-3ef7cbf7a52cf9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/2`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-b5ee76ecb27f80"></a>
### 根拠 R-b5ee76ecb27f80

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-003/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `9653d5a62f9c0cb6c2b8db5ffd20ccb5abb09f6809e315c4b49370714940f5a8`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "For each row with a present event, return (that row schema_version, borrowed Event reference). Preserve row order, duplicates and schema zero/MAX. Skip absent events.",
    "References must point to original event values; no clone or owned Event allocation. Ignore event kind and all other audit fields. Empty input gives empty. Preserve records.",
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
      "criterion_text": "For each row with a present event, return (that row schema_version, borrowed Event reference). Preserve row order, duplicates and schema zero/MAX. Skip absent events.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "References must point to original event values; no clone or owned Event allocation. Ignore event kind and all other audit fields. Empty input gives empty. Preserve records.",
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
      "cwd": "units/ECR228-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_003"
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
        "economic_ecr228_003",
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
      "cwd": "units/ECR228-003",
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
      "cwd": "units/ECR228-003",
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
      "cwd": "units/ECR228-003",
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
      "cwd": "units/ECR228-003",
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
      "cwd": "units/ECR228-003",
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
      "cwd": "units/ECR228-003",
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

<a id="ecr228-004"></a>
## ECR228-004

Borrow the first denied policy reason including an empty reason

元のtask_id: `ECR228-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return a borrowed str slice of the first present policy whose decision is Deny. Return Some(empty str) if that reason is empty. None only when no Deny exists. Skip absent, Allow and RequireConfirmation policies. Preserve row order, Unicode, spaces and records. Do not clone reasons or consult proposal/execution.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-004 --output work/ECR228-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-5bc8f9eeeabcf9](#r-5bc8f9eeeabcf9) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-20e3475cde5620](#r-20e3475cde5620) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5bc8f9eeeabcf9"></a>
### 根拠 R-5bc8f9eeeabcf9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/3`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-20e3475cde5620"></a>
### 根拠 R-20e3475cde5620

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-004/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `a7f445ed8ffc602604a54e5ff9a66eb7e3a0304790dea8b56fffa88eb7f936a0`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return a borrowed str slice of the first present policy whose decision is Deny. Return Some(empty str) if that reason is empty. None only when no Deny exists.",
    "Skip absent, Allow and RequireConfirmation policies. Preserve row order, Unicode, spaces and records. Do not clone reasons or consult proposal/execution.",
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
      "criterion_text": "Return a borrowed str slice of the first present policy whose decision is Deny. Return Some(empty str) if that reason is empty. None only when no Deny exists.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Skip absent, Allow and RequireConfirmation policies. Preserve row order, Unicode, spaces and records. Do not clone reasons or consult proposal/execution.",
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
      "cwd": "units/ECR228-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_004"
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
        "economic_ecr228_004",
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
      "cwd": "units/ECR228-004",
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
      "cwd": "units/ECR228-004",
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
      "cwd": "units/ECR228-004",
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
      "cwd": "units/ECR228-004",
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
      "cwd": "units/ECR228-004",
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
      "cwd": "units/ECR228-004",
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

<a id="ecr228-005"></a>
## ECR228-005

Compute per-observation RSS excess above an inclusive allowance

元のtask_id: `ECR228-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return one u64 per process row: rss_kib minus allowance if strictly above, otherwise zero. Preserve order and duplicates. Do not aggregate, filter, wrap subtraction or narrow. Ignore pid/parent_pid; use full u64 domain and preserve rows. Empty returns empty.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-005 --output work/ECR228-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-f9755218445148](#r-f9755218445148) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-c8455593195fee](#r-c8455593195fee) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-f9755218445148"></a>
### 根拠 R-f9755218445148

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/4`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-c8455593195fee"></a>
### 根拠 R-c8455593195fee

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-005/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `a64ebfb68f231e3a02155826339f8606aacdc82bf85d3db03fd9924c6f1bae34`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return one u64 per process row: rss_kib minus allowance if strictly above, otherwise zero. Preserve order and duplicates. Do not aggregate, filter, wrap subtraction or narrow.",
    "Ignore pid/parent_pid; use full u64 domain and preserve rows. Empty returns empty.",
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
      "criterion_text": "Return one u64 per process row: rss_kib minus allowance if strictly above, otherwise zero. Preserve order and duplicates. Do not aggregate, filter, wrap subtraction or narrow.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Ignore pid/parent_pid; use full u64 domain and preserve rows. Empty returns empty.",
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
      "cwd": "units/ECR228-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_005"
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
        "economic_ecr228_005",
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
      "cwd": "units/ECR228-005",
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
      "cwd": "units/ECR228-005",
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
      "cwd": "units/ECR228-005",
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
      "cwd": "units/ECR228-005",
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
      "cwd": "units/ECR228-005",
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
      "cwd": "units/ECR228-005",
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

<a id="ecr228-006"></a>
## ECR228-006

Mark adjacent audit source transitions without trimming

元のtask_id: `ECR228-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return one bool per row. The first row is true even if its source is empty. Each later row is true iff source differs byte-for-byte from the immediately previous row. Do not compare against first row or global seen sources. Do not trim, normalize case/Unicode, or inspect other fields. Preserve records. Empty returns empty.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-006 --output work/ECR228-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-fb23075c886871](#r-fb23075c886871) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-58f21980db09a8](#r-58f21980db09a8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fb23075c886871"></a>
### 根拠 R-fb23075c886871

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/5`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-58f21980db09a8"></a>
### 根拠 R-58f21980db09a8

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-006/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `6edc4e14ce1a2d5687847c625d73e5aed58a5d0ff40f695168c10386a64cf753`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return one bool per row. The first row is true even if its source is empty. Each later row is true iff source differs byte-for-byte from the immediately previous row.",
    "Do not compare against first row or global seen sources. Do not trim, normalize case/Unicode, or inspect other fields. Preserve records. Empty returns empty.",
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
      "criterion_text": "Return one bool per row. The first row is true even if its source is empty. Each later row is true iff source differs byte-for-byte from the immediately previous row.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not compare against first row or global seen sources. Do not trim, normalize case/Unicode, or inspect other fields. Preserve records. Empty returns empty.",
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
      "cwd": "units/ECR228-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_006"
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
        "economic_ecr228_006",
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
      "cwd": "units/ECR228-006",
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
      "cwd": "units/ECR228-006",
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
      "cwd": "units/ECR228-006",
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
      "cwd": "units/ECR228-006",
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
      "cwd": "units/ECR228-006",
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
      "cwd": "units/ECR228-006",
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

<a id="ecr228-007"></a>
## ECR228-007

Locate the first confirmation policy that also has a recorded proposal

元のtask_id: `ECR228-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Find the first row index with both proposal present and policy present whose decision is RequireConfirmation. A confirmation without proposal and an Allow/Deny with proposal do not qualify. Ignore reason/risk/target/execution/verification. Preserve rows and ecr_sample_control behavior. Empty or no match returns None.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-007 --output work/ECR228-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-9d45b04fb99dc2](#r-9d45b04fb99dc2) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-569d88914c8813](#r-569d88914c8813) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9d45b04fb99dc2"></a>
### 根拠 R-9d45b04fb99dc2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/6`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-569d88914c8813"></a>
### 根拠 R-569d88914c8813

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-007/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `eab28be81d4f1db3b58f7c480f12ca2ba0b6e5e2c37a840a00423a690136342b`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Find the first row index with both proposal present and policy present whose decision is RequireConfirmation. A confirmation without proposal and an Allow/Deny with proposal do not qualify.",
    "Ignore reason/risk/target/execution/verification. Preserve rows and ecr_sample_control behavior. Empty or no match returns None.",
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
      "criterion_text": "Find the first row index with both proposal present and policy present whose decision is RequireConfirmation. A confirmation without proposal and an Allow/Deny with proposal do not qualify.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Ignore reason/risk/target/execution/verification. Preserve rows and ecr_sample_control behavior. Empty or no match returns None.",
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
      "cwd": "units/ECR228-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_007"
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
        "economic_ecr228_007",
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
      "cwd": "units/ECR228-007",
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
      "cwd": "units/ECR228-007",
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
      "cwd": "units/ECR228-007",
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
      "cwd": "units/ECR228-007",
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
      "cwd": "units/ECR228-007",
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
      "cwd": "units/ECR228-007",
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

<a id="ecr228-008"></a>
## ECR228-008

Extract evidence row counts from HighLoad events without flattening

元のtask_id: `ECR228-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return evidence.len() for each HighLoad event only, preserving event order and duplicate events. Include zero-length evidence and count empty/duplicate strings independently. Do not sum or flatten, trim evidence, filter targets or include other EventKind values. Preserve events and ecr_sample_control. Empty returns empty.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-008 --output work/ECR228-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-dbc5854b015437](#r-dbc5854b015437) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-68dfb1614a9427](#r-68dfb1614a9427) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-dbc5854b015437"></a>
### 根拠 R-dbc5854b015437

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/7`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-68dfb1614a9427"></a>
### 根拠 R-68dfb1614a9427

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-008/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `c0a1ccd123912f211816d2dd9318586a33055232990849ed6ef62745d070c1b7`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return evidence.len() for each HighLoad event only, preserving event order and duplicate events. Include zero-length evidence and count empty/duplicate strings independently.",
    "Do not sum or flatten, trim evidence, filter targets or include other EventKind values. Preserve events and ecr_sample_control. Empty returns empty.",
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
      "criterion_text": "Return evidence.len() for each HighLoad event only, preserving event order and duplicate events. Include zero-length evidence and count empty/duplicate strings independently.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not sum or flatten, trim evidence, filter targets or include other EventKind values. Preserve events and ecr_sample_control. Empty returns empty.",
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
      "cwd": "units/ECR228-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_008"
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
        "economic_ecr228_008",
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
      "cwd": "units/ECR228-008",
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
      "cwd": "units/ECR228-008",
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
      "cwd": "units/ECR228-008",
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
      "cwd": "units/ECR228-008",
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
      "cwd": "units/ECR228-008",
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
      "cwd": "units/ECR228-008",
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

<a id="ecr228-009"></a>
## ECR228-009

Remove audit latency narrowing while keeping inclusive budget equality

元のtask_id: `ECR228-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return true iff full u128 usage.elapsed_ms is less than or equal to u64 budget.max_latency_ms converted losslessly. Equality is within the allowance. Do not narrow elapsed_ms, saturate it, or consult token/call/model fields. Preserve both inputs. Values above u64::MAX must return false for any budget.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-009 --output work/ECR228-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-6cbff9dacfea57](#r-6cbff9dacfea57) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-6f5abf541e38f8](#r-6f5abf541e38f8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6cbff9dacfea57"></a>
### 根拠 R-6cbff9dacfea57

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/8`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-6f5abf541e38f8"></a>
### 根拠 R-6f5abf541e38f8

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-009/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `91f949731bd5e4c2b817087bd159adabf3b224bff7a9c58c44488b7060e397f9`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return true iff full u128 usage.elapsed_ms is less than or equal to u64 budget.max_latency_ms converted losslessly. Equality is within the allowance.",
    "Do not narrow elapsed_ms, saturate it, or consult token/call/model fields. Preserve both inputs. Values above u64::MAX must return false for any budget.",
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
      "criterion_text": "Return true iff full u128 usage.elapsed_ms is less than or equal to u64 budget.max_latency_ms converted losslessly. Equality is within the allowance.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not narrow elapsed_ms, saturate it, or consult token/call/model fields. Preserve both inputs. Values above u64::MAX must return false for any budget.",
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
      "cwd": "units/ECR228-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_009"
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
        "economic_ecr228_009",
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
      "cwd": "units/ECR228-009",
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
      "cwd": "units/ECR228-009",
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
      "cwd": "units/ECR228-009",
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
      "cwd": "units/ECR228-009",
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
      "cwd": "units/ECR228-009",
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
      "cwd": "units/ECR228-009",
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

<a id="ecr228-010"></a>
## ECR228-010

Advance a sampled display cursor without usize addition overflow

元のtask_id: `ECR228-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. For length zero return None. Otherwise return the exact mathematical (index + steps) modulo length as Some(usize), even when usize addition would overflow. Index may exceed length; normalize it mathematically. No wrapping or saturating addition before modulo. No panics, allocations or changes outside this body.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-010 --output work/ECR228-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | false | [R-604718fc60c883](#r-604718fc60c883) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-30589928f4df30](#r-30589928f4df30) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-604718fc60c883"></a>
### 根拠 R-604718fc60c883

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/9`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-30589928f4df30"></a>
### 根拠 R-30589928f4df30

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-010/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `cf52262ff8189cb4b5ce56b478d5fe9a9fc3956d93b71a2d138f2fa4265391d8`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "For length zero return None. Otherwise return the exact mathematical (index + steps) modulo length as Some(usize), even when usize addition would overflow.",
    "Index may exceed length; normalize it mathematically. No wrapping or saturating addition before modulo. No panics, allocations or changes outside this body.",
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
      "criterion_text": "For length zero return None. Otherwise return the exact mathematical (index + steps) modulo length as Some(usize), even when usize addition would overflow.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Index may exceed length; normalize it mathematically. No wrapping or saturating addition before modulo. No panics, allocations or changes outside this body.",
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
      "cwd": "units/ECR228-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_010"
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
        "economic_ecr228_010",
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
      "cwd": "units/ECR228-010",
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
      "cwd": "units/ECR228-010",
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
      "cwd": "units/ECR228-010",
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
      "cwd": "units/ECR228-010",
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
      "cwd": "units/ECR228-010",
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
      "cwd": "units/ECR228-010",
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

<a id="ecr228-011"></a>
## ECR228-011

Choose the least valid available-memory sample while rejecting incomplete validity

元のtask_id: `ECR228-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return None for empty samples or if any sample has total_kib zero or available_kib greater than total_kib. Otherwise return Some(minimum available_kib) over all rows. Known available zero is valid. Do not ignore invalid rows, calculate percentages, or narrow u64. Preserve samples.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-011 --output work/ECR228-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | — | false | [R-1d698c8330e121](#r-1d698c8330e121) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-245d50a56cfc95](#r-245d50a56cfc95) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1d698c8330e121"></a>
### 根拠 R-1d698c8330e121

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/10`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-245d50a56cfc95"></a>
### 根拠 R-245d50a56cfc95

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-011/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `3bd5ea1350a7e4cd36442f581b0eeefe6d669dbaa898e4d17d2d80055641b54f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return None for empty samples or if any sample has total_kib zero or available_kib greater than total_kib. Otherwise return Some(minimum available_kib) over all rows.",
    "Known available zero is valid. Do not ignore invalid rows, calculate percentages, or narrow u64. Preserve samples.",
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
      "criterion_text": "Return None for empty samples or if any sample has total_kib zero or available_kib greater than total_kib. Otherwise return Some(minimum available_kib) over all rows.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Known available zero is valid. Do not ignore invalid rows, calculate percentages, or narrow u64. Preserve samples.",
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
      "cwd": "units/ECR228-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_011"
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
        "economic_ecr228_011",
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
      "cwd": "units/ECR228-011",
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
      "cwd": "units/ECR228-011",
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
      "cwd": "units/ECR228-011",
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
      "cwd": "units/ECR228-011",
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
      "cwd": "units/ECR228-011",
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
      "cwd": "units/ECR228-011",
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

<a id="ecr228-012"></a>
## ECR228-012

Detect nondecreasing recorded risk sequence with ties permitted

元のtask_id: `ECR228-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return true iff every adjacent pair respects Low <= Medium <= High. Equal adjacent risks are permitted. Empty and single-item samples return true. Inspect the entire ordered sequence; any later decrease returns false. Do not sort, deduplicate or mutate input.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-012 --output work/ECR228-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-b281aa8e840104](#r-b281aa8e840104) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-b2f722a5495f65](#r-b2f722a5495f65) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b281aa8e840104"></a>
### 根拠 R-b281aa8e840104

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/11`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-b2f722a5495f65"></a>
### 根拠 R-b2f722a5495f65

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-012/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `99c5029b97ba438f20373d1198bcc6b55878d864584d6bb82f0ff912b2c23fe8`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return true iff every adjacent pair respects Low <= Medium <= High. Equal adjacent risks are permitted. Empty and single-item samples return true.",
    "Inspect the entire ordered sequence; any later decrease returns false. Do not sort, deduplicate or mutate input.",
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
      "criterion_text": "Return true iff every adjacent pair respects Low <= Medium <= High. Equal adjacent risks are permitted. Empty and single-item samples return true.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Inspect the entire ordered sequence; any later decrease returns false. Do not sort, deduplicate or mutate input.",
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
      "cwd": "units/ECR228-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_012"
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
        "economic_ecr228_012",
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
      "cwd": "units/ECR228-012",
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
      "cwd": "units/ECR228-012",
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
      "cwd": "units/ECR228-012",
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
      "cwd": "units/ECR228-012",
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
      "cwd": "units/ECR228-012",
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
      "cwd": "units/ECR228-012",
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

<a id="ecr228-013"></a>
## ECR228-013

Delegate disk availability caption to the protected optional-count renderer

元のtask_id: `ECR228-013`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact disks=N or disks=unknown with no newline. Some(0)/usize::MAX render exact unsigned count; None renders unknown. Use state.disk_count only. Refactor by calling existing render_optional_inventory_count(label, count) with label disks and disk_count. Do not duplicate inline formatting or alter helper/signature/tests/state.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-013 --output work/ECR228-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-e057f7a35eefea](#r-e057f7a35eefea) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-2a78a87fd8d242](#r-2a78a87fd8d242) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e057f7a35eefea"></a>
### 根拠 R-e057f7a35eefea

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/12`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-2a78a87fd8d242"></a>
### 根拠 R-2a78a87fd8d242

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-013/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `a22a9bf7c0158e4bb43a24bdf9fc14d5ce519f9e31f46caa39b539a83d2019a0`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact disks=N or disks=unknown with no newline. Some(0)/usize::MAX render exact unsigned count; None renders unknown. Use state.disk_count only.",
    "Refactor by calling existing render_optional_inventory_count(label, count) with label disks and disk_count. Do not duplicate inline formatting or alter helper/signature/tests/state.",
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
      "criterion_text": "Preserve exact disks=N or disks=unknown with no newline. Some(0)/usize::MAX render exact unsigned count; None renders unknown. Use state.disk_count only.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Refactor by calling existing render_optional_inventory_count(label, count) with label disks and disk_count. Do not duplicate inline formatting or alter helper/signature/tests/state.",
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
      "cwd": "units/ECR228-013",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_013"
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
        "economic_ecr228_013",
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
      "cwd": "units/ECR228-013",
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
      "cwd": "units/ECR228-013",
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
      "cwd": "units/ECR228-013",
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
      "cwd": "units/ECR228-013",
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
      "cwd": "units/ECR228-013",
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
      "cwd": "units/ECR228-013",
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

<a id="ecr228-014"></a>
## ECR228-014

Delegate evidence cleanup to the protected trimmed-item selector

元のtask_id: `ECR228-014`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return owned strings for nonempty Unicode-whitespace-trimmed items, preserving order, case and duplicates. Skip empty/whitespace-only items; preserve original input. Refactor by applying existing select_trimmed_evidence_item(text) to each input. Do not inline trim/empty-selection logic or alter helper/signature/tests.

取り出し方:

```sh
python materialize_task.py --set bounded-2.2.8-economic-retry --task ECR228-014 --output work/ECR228-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | — | true | [R-8a35f746b79251](#r-8a35f746b79251) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-cd6dc69cfa83e3](#r-cd6dc69cfa83e3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8a35f746b79251"></a>
### 根拠 R-8a35f746b79251

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/13`
- 出典ファイルのSHA-256: `e7c349ba8f929eda3f9b0dee6b84a279d6e76ac2622e7c775dab71fe8026789f`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<a id="r-cd6dc69cfa83e3"></a>
### 根拠 R-cd6dc69cfa83e3

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-014/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `a04f73c14fc035e0981ac6c982232345eec6b11dc72730e3b5ba4945b41607cc`
- [抽出した測定値・他の工程の記録](../results/bounded-2.2.8-economic-retry.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Return owned strings for nonempty Unicode-whitespace-trimmed items, preserving order, case and duplicates. Skip empty/whitespace-only items; preserve original input.",
    "Refactor by applying existing select_trimmed_evidence_item(text) to each input. Do not inline trim/empty-selection logic or alter helper/signature/tests.",
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
      "criterion_text": "Return owned strings for nonempty Unicode-whitespace-trimmed items, preserving order, case and duplicates. Skip empty/whitespace-only items; preserve original input.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Refactor by applying existing select_trimmed_evidence_item(text) to each input. Do not inline trim/empty-selection logic or alter helper/signature/tests.",
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
      "cwd": "units/ECR228-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "economic_ecr228_014"
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
        "economic_ecr228_014",
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
      "cwd": "units/ECR228-014",
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
      "cwd": "units/ECR228-014",
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
      "cwd": "units/ECR228-014",
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
      "cwd": "units/ECR228-014",
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
      "cwd": "units/ECR228-014",
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
      "cwd": "units/ECR228-014",
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
