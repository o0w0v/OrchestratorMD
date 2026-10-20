# 実装・検証手順の比較 / economic-accounting-recovery-228

セットID: `economic-accounting-recovery-228`

課題数: 3。個別記録あり: 3、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](economic-accounting-recovery-228.json) / [結果と根拠のJSON](../results/economic-accounting-recovery-228.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_ACCOUNTING_RECOVERY_JA.md](../reports/economic-accounting-recovery-228/RESULTS_ACCOUNTING_RECOVERY_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "model": "gpt-6-sol",
    "effort": "xhigh",
    "speed": "Standard"
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [ECR228-002](#ecr228-002) | Render sampled disk and service availability as an exact nullable receipt | 記録あり |
| [ECR228-005](#ecr228-005) | Compute per-observation RSS excess above an inclusive allowance | 記録あり |
| [ECR228-009](#ecr228-009) | Remove audit latency narrowing while keeping inclusive budget equality | 記録あり |

<a id="ecr228-002"></a>
## ECR228-002

Render sampled disk and service availability as an exact nullable receipt

元のtask_id: `ECR228-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return exactly disks=VALUE;services=VALUE followed by one LF. Each VALUE is unsigned decimal for Some(count), or the lowercase word unknown for None. No spaces, CR, quotes or extra fields. Some(0) is known zero. Preserve usize::MAX without narrowing. Use disk_count/service_count only; do not infer counts from other state fields. Preserve state.

取り出し方:

```sh
python materialize_task.py --set economic-accounting-recovery-228 --task ECR228-002 --output work/ECR228-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | recovery_arm=A | — | — | true | — | — | — | [R-ba69b2bc0bd896](#r-ba69b2bc0bd896) |
| 実装・検証・レビューの工程 | recovery_arm=B | — | — | true | — | — | — | [R-912ce82eb99ae3](#r-912ce82eb99ae3) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-5e13ce0aabac94](#r-5e13ce0aabac94) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ba69b2bc0bd896"></a>
### 根拠 R-ba69b2bc0bd896

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/0/A_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-912ce82eb99ae3"></a>
### 根拠 R-912ce82eb99ae3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/0/B_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-5e13ce0aabac94"></a>
### 根拠 R-5e13ce0aabac94

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-002/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `33bb7441b1fc7b46f4e424218b48408cc8446cb12bcf6384bcc6b14731bd3583`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

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

<a id="ecr228-005"></a>
## ECR228-005

Compute per-observation RSS excess above an inclusive allowance

元のtask_id: `ECR228-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return one u64 per process row: rss_kib minus allowance if strictly above, otherwise zero. Preserve order and duplicates. Do not aggregate, filter, wrap subtraction or narrow. Ignore pid/parent_pid; use full u64 domain and preserve rows. Empty returns empty.

取り出し方:

```sh
python materialize_task.py --set economic-accounting-recovery-228 --task ECR228-005 --output work/ECR228-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | recovery_arm=A | — | — | true | — | — | — | [R-a6004c2d6ae4e0](#r-a6004c2d6ae4e0) |
| 実装・検証・レビューの工程 | recovery_arm=B | — | — | true | — | — | — | [R-1d3f574fec5bc4](#r-1d3f574fec5bc4) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-e435d2be7c02be](#r-e435d2be7c02be) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a6004c2d6ae4e0"></a>
### 根拠 R-a6004c2d6ae4e0

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/1/A_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-1d3f574fec5bc4"></a>
### 根拠 R-1d3f574fec5bc4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/1/B_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-e435d2be7c02be"></a>
### 根拠 R-e435d2be7c02be

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-005/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `b07d75d44a59f22ef5fcfa5aac820be89dc4ba3324d6db9b76ffd55cffccbebd`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

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

<a id="ecr228-009"></a>
## ECR228-009

Remove audit latency narrowing while keeping inclusive budget equality

元のtask_id: `ECR228-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Return true iff full u128 usage.elapsed_ms is less than or equal to u64 budget.max_latency_ms converted losslessly. Equality is within the allowance. Do not narrow elapsed_ms, saturate it, or consult token/call/model fields. Preserve both inputs. Values above u64::MAX must return false for any budget.

取り出し方:

```sh
python materialize_task.py --set economic-accounting-recovery-228 --task ECR228-009 --output work/ECR228-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 実装・検証・レビューの工程 | recovery_arm=A | — | — | true | — | — | — | [R-73ba3d3100ccda](#r-73ba3d3100ccda) |
| 実装・検証・レビューの工程 | recovery_arm=B | — | — | true | — | — | — | [R-b82704d9e2b4c9](#r-b82704d9e2b4c9) |
| コードの検証 | 記録に条件の明記なし | — | — | — | true | ACCEPT_NO_CHANGE | — | [R-20df81ac6072ac](#r-20df81ac6072ac) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-73ba3d3100ccda"></a>
### 根拠 R-73ba3d3100ccda

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/2/A_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-b82704d9e2b4c9"></a>
### 根拠 R-b82704d9e2b4c9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `task-results.json` / 位置: `/2/B_quality_PASS`
- 出典ファイルのSHA-256: `8c0e3d3c6ae53a8a8a9c637e1d03e9f8e945f8ce295dad77790687c97103b5b0`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

<a id="r-20df81ac6072ac"></a>
### 根拠 R-20df81ac6072ac

- 対応方法: 同一実験内の課題ディレクトリによる対応
- 出典: `codex/B/ECR228-009/RESULT.json` / 位置: `/`
- 出典ファイルのSHA-256: `606f4d75ffcd04b67eabec0cdef70fb16d94eae629d9565c316780caa91b90bc`
- [抽出した測定値・他の工程の記録](../results/economic-accounting-recovery-228.json)

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
