# 実装委譲の検証 / 手順-v2.2

セットID: `router-shadow-pilot-v2.2`

課題数: 12。個別記録あり: 12、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.2.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.2.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.2/RESULTS_JA.md)

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
  }
]
```

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [P22-001](#p22-001) | MemoryPressure evidenceにused_kibを追加 | 記録あり |
| [P22-002](#p22-002) | CLI optional inventoryの表示を統一 | 記録あり |
| [P22-003](#p22-003) | meminfo欠落fieldの診断を明示 | 記録あり |
| [P22-004](#p22-004) | VmRSS parse errorへfield contextを追加 | 記録あり |
| [P22-005](#p22-005) | CLI警告表示のstable dedup | 記録あり |
| [P22-006](#p22-006) | HighLoad evidenceへCPUあたりloadを追加 | 記録あり |
| [P22-007](#p22-007) | anomaly-free auditへprocess数を追加 | 記録あり |
| [P22-008](#p22-008) | skill template reasonへ現在のevidence件数 | 記録あり |
| [P22-009](#p22-009) | MemoryPressure evidenceへ最大RSS processを付記 | 記録あり |
| [P22-010](#p22-010) | CPU inventory labelの過剰countを修正 | 記録あり |
| [P22-011](#p22-011) | Extract the default mock ResourceBudget from the supplied Rust source. | 記録あり |
| [P22-012](#p22-012) | Boundary case: redesign dry-run execution into privileged automatic execution. | 記録あり |

<a id="p22-001"></a>
## P22-001

MemoryPressure evidenceにused_kibを追加

元のtask_id: `P22-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In memory_event, keep exactly one evidence string: available_kib=A; total_kib=T; used_kib=U, with U=T-A. Preserve the predicate, event id/kind/target and invalid-range rejection; use integer arithmetic including u64::MAX.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-001 --output work/P22-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-001.json | — | [R-d87d702493ba10](#r-d87d702493ba10) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-001/review.json | — | [R-4c7088252585e7](#r-4c7088252585e7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d87d702493ba10"></a>
### 根拠 R-d87d702493ba10

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-4c7088252585e7"></a>
### 根拠 R-4c7088252585e7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In memory_event, keep exactly one evidence string: available_kib=A; total_kib=T; used_kib=U, with U=T-A.",
    "Preserve the predicate, event id/kind/target and invalid-range rejection; use integer arithmetic including u64::MAX.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "In memory_event, keep exactly one evidence string: available_kib=A; total_kib=T; used_kib=U, with U=T-A.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the predicate, event id/kind/target and invalid-range rejection; use integer arithmetic including u64::MAX.",
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
      "cwd": "units/P22-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_001"
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
        "pilot_p22_001",
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
      "cwd": "units/P22-001",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-001",
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
      "cwd": "units/P22-001",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-001",
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
      "cwd": "units/P22-001",
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

<a id="p22-002"></a>
## P22-002

CLI optional inventoryの表示を統一

元のtask_id: `P22-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement inventory_count(value: Option<usize>) -> String: None returns unavailable; Some(n) returns only the decimal n. Preserve zero and usize::MAX without a Some wrapper; the CLI already calls this helper for disks/services/TCP.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-002 --output work/P22-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-002.json | — | [R-01f4ee4aebb428](#r-01f4ee4aebb428) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-002/review.json | — | [R-99d49ec39a690e](#r-99d49ec39a690e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-01f4ee4aebb428"></a>
### 根拠 R-01f4ee4aebb428

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-99d49ec39a690e"></a>
### 根拠 R-99d49ec39a690e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement inventory_count(value: Option<usize>) -> String: None returns unavailable; Some(n) returns only the decimal n.",
    "Preserve zero and usize::MAX without a Some wrapper; the CLI already calls this helper for disks/services/TCP.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Implement inventory_count(value: Option<usize>) -> String: None returns unavailable; Some(n) returns only the decimal n.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve zero and usize::MAX without a Some wrapper; the CLI already calls this helper for disks/services/TCP.",
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
      "cwd": "units/P22-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_002"
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
        "pilot_p22_002",
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
      "cwd": "units/P22-002",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-002",
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
      "cwd": "units/P22-002",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-002",
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
      "cwd": "units/P22-002",
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

<a id="p22-003"></a>
## P22-003

meminfo欠落fieldの診断を明示

元のtask_id: `P22-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In the final parse_memory result block, total and available are Option<u64>. Report missing MemTotal and missing MemAvailable respectively. When both are missing, report missing MemTotal first. Preserve invalid memory range for zero total or available>total, and valid Memory fields.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-003 --output work/P22-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-003.json | — | [R-d5b6a599f89f9b](#r-d5b6a599f89f9b) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-003/review.json | — | [R-32ea45ac42f4da](#r-32ea45ac42f4da) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d5b6a599f89f9b"></a>
### 根拠 R-d5b6a599f89f9b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-32ea45ac42f4da"></a>
### 根拠 R-32ea45ac42f4da

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In the final parse_memory result block, total and available are Option<u64>. Report missing MemTotal and missing MemAvailable respectively.",
    "When both are missing, report missing MemTotal first. Preserve invalid memory range for zero total or available>total, and valid Memory fields.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "In the final parse_memory result block, total and available are Option<u64>. Report missing MemTotal and missing MemAvailable respectively.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "When both are missing, report missing MemTotal first. Preserve invalid memory range for zero total or available>total, and valid Memory fields.",
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
      "cwd": "units/P22-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_003"
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
        "pilot_p22_003",
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
      "cwd": "units/P22-003",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-003",
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
      "cwd": "units/P22-003",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-003",
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
      "cwd": "units/P22-003",
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

<a id="p22-004"></a>
## P22-004

VmRSS parse errorへfield contextを追加

元のtask_id: `P22-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In the VmRSS assignment, retain parse_kib_value(value) -> Result<u64, String>, but prefix its error with VmRSS: followed by one space. Preserve original helper error text, valid RSS, default zero when absent, and duplicate RSS handling. Do not change PID errors.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-004 --output work/P22-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-004.json | — | [R-e21e6293f29557](#r-e21e6293f29557) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-004/review.json | — | [R-2e2f381b84df8f](#r-2e2f381b84df8f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e21e6293f29557"></a>
### 根拠 R-e21e6293f29557

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/3`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-2e2f381b84df8f"></a>
### 根拠 R-2e2f381b84df8f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In the VmRSS assignment, retain parse_kib_value(value) -> Result<u64, String>, but prefix its error with VmRSS: followed by one space.",
    "Preserve original helper error text, valid RSS, default zero when absent, and duplicate RSS handling. Do not change PID errors.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "In the VmRSS assignment, retain parse_kib_value(value) -> Result<u64, String>, but prefix its error with VmRSS: followed by one space.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve original helper error text, valid RSS, default zero when absent, and duplicate RSS handling. Do not change PID errors.",
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
      "cwd": "units/P22-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_004"
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
        "pilot_p22_004",
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
      "cwd": "units/P22-004",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-004",
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
      "cwd": "units/P22-004",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-004",
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
      "cwd": "units/P22-004",
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

<a id="p22-005"></a>
## P22-005

CLI警告表示のstable dedup

元のtask_id: `P22-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement unique_warnings(warnings: &[String]) -> Vec<&str>: omit empty or whitespace-only strings; remove exact duplicate strings, retaining first occurrence order. Do not trim or otherwise change retained strings; differently spaced nonempty strings are distinct. Do not mutate input.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-005 --output work/P22-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-005.json | — | [R-309294312c1e19](#r-309294312c1e19) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-005/review.json | — | [R-4f1ae8a10583ee](#r-4f1ae8a10583ee) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-309294312c1e19"></a>
### 根拠 R-309294312c1e19

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/4`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-4f1ae8a10583ee"></a>
### 根拠 R-4f1ae8a10583ee

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/4`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement unique_warnings(warnings: &[String]) -> Vec<&str>: omit empty or whitespace-only strings; remove exact duplicate strings, retaining first occurrence order.",
    "Do not trim or otherwise change retained strings; differently spaced nonempty strings are distinct. Do not mutate input.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Implement unique_warnings(warnings: &[String]) -> Vec<&str>: omit empty or whitespace-only strings; remove exact duplicate strings, retaining first occurrence order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not trim or otherwise change retained strings; differently spaced nonempty strings are distinct. Do not mutate input.",
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
      "cwd": "units/P22-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_005"
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
        "pilot_p22_005",
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
      "cwd": "units/P22-005",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-005",
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
      "cwd": "units/P22-005",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-005",
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
      "cwd": "units/P22-005",
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

<a id="p22-006"></a>
## P22-006

HighLoad evidenceへCPUあたりloadを追加

元のtask_id: `P22-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate HighLoad event construction. Its single evidence string must be load_one=L; logical_cpus=C; load_per_cpu=R, with L and R formatted to two decimal places, R=load_one/logical_cpus. Keep event identity, strict >2*CPU threshold, zero/non-finite guards and memory-first ordering unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-006 --output work/P22-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | PASS | PASS | — | — | reviews/P22-006.json | — | [R-dde80280ea1068](#r-dde80280ea1068) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P22-006/review.json | — | [R-53f34e210418f2](#r-53f34e210418f2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-dde80280ea1068"></a>
### 根拠 R-dde80280ea1068

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/5`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-53f34e210418f2"></a>
### 根拠 R-53f34e210418f2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/5`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate HighLoad event construction. Its single evidence string must be load_one=L; logical_cpus=C; load_per_cpu=R, with L and R formatted to two decimal places, R=load_one/logical_cpus.",
    "Keep event identity, strict >2*CPU threshold, zero/non-finite guards and memory-first ordering unchanged.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate HighLoad event construction. Its single evidence string must be load_one=L; logical_cpus=C; load_per_cpu=R, with L and R formatted to two decimal places, R=load_one/logical_cpus.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep event identity, strict >2*CPU threshold, zero/non-finite guards and memory-first ordering unchanged.",
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
      "cwd": "units/P22-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_006"
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
        "pilot_p22_006",
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
      "cwd": "units/P22-006",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-006",
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
      "cwd": "units/P22-006",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-006",
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
      "cwd": "units/P22-006",
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

<a id="p22-007"></a>
## P22-007

anomaly-free auditへprocess数を追加

元のtask_id: `P22-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the no-anomaly inspect audit record. Its short_reason must be No anomaly candidates; model asleep; processes=N where N is the observed snapshot process count. Keep source fast-path, timestamp, returned snapshot and exactly one record; do not invoke provider or alter anomaly/invalid-intent paths.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-007 --output work/P22-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | — | reviews/P22-007.json | — | [R-ec2101117e5b23](#r-ec2101117e5b23) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P22-007/review.json | — | [R-2ad53c3084ce78](#r-2ad53c3084ce78) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ec2101117e5b23"></a>
### 根拠 R-ec2101117e5b23

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/6`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-2ad53c3084ce78"></a>
### 根拠 R-2ad53c3084ce78

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/6`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the no-anomaly inspect audit record. Its short_reason must be No anomaly candidates; model asleep; processes=N where N is the observed snapshot process count.",
    "Keep source fast-path, timestamp, returned snapshot and exactly one record; do not invoke provider or alter anomaly/invalid-intent paths.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate the no-anomaly inspect audit record. Its short_reason must be No anomaly candidates; model asleep; processes=N where N is the observed snapshot process count.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep source fast-path, timestamp, returned snapshot and exactly one record; do not invoke provider or alter anomaly/invalid-intent paths.",
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
      "cwd": "units/P22-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_007"
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
        "pilot_p22_007",
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
      "cwd": "units/P22-007",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-007",
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
      "cwd": "units/P22-007",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-007",
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
      "cwd": "units/P22-007",
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

<a id="p22-008"></a>
## P22-008

skill template reasonへ現在のevidence件数

元のtask_id: `P22-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate report template construction. Set reason to Verified report template with current evidence; evidence_count=N where N counts current event evidence entries, including duplicate entries. Keep unsupported-intent rejection, report action/system target/low risk/capability/reversibility and exact current evidence unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-008 --output work/P22-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | ESCALATE | ESCALATE | — | — | reviews/P22-008.json | — | [R-a6586decdb5bd5](#r-a6586decdb5bd5) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P22-008/review.json | — | [R-f5b2a3c057dfcd](#r-f5b2a3c057dfcd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a6586decdb5bd5"></a>
### 根拠 R-a6586decdb5bd5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/7`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<a id="r-f5b2a3c057dfcd"></a>
### 根拠 R-f5b2a3c057dfcd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/7`
- 出典ファイルのSHA-256: `688dd00ca5e78995c0558e25ce16ab3c8da3961eeae9a8566cf18ec80b324518`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate report template construction. Set reason to Verified report template with current evidence; evidence_count=N where N counts current event evidence entries, including duplicate entries.",
    "Keep unsupported-intent rejection, report action/system target/low risk/capability/reversibility and exact current evidence unchanged.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate report template construction. Set reason to Verified report template with current evidence; evidence_count=N where N counts current event evidence entries, including duplicate entries.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep unsupported-intent rejection, report action/system target/low risk/capability/reversibility and exact current evidence unchanged.",
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
      "cwd": "units/P22-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_008"
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
        "ncos-skills",
        "--lib",
        "pilot_p22_008",
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
      "cwd": "units/P22-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "skill_cache"
      ],
      "min_test_count": 1,
      "argv": [
        "cargo",
        "timeout",
        "300",
        "/mnt/d/Codex-Ollama/.toolchain/cargo/bin/cargo",
        "test",
        "--offline",
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-008",
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
      "cwd": "units/P22-008",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-008",
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
      "cwd": "units/P22-008",
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

<a id="p22-009"></a>
## P22-009

MemoryPressure evidenceへ最大RSS processを付記

元のtask_id: `P22-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate memory pressure event creation. Keep its original first evidence string exactly. Append one second string largest_rss_pid=P; largest_rss_kib=R if the observed processes list is nonempty. Select the maximum rss_kib; ties use the smallest pid. Empty list has no second evidence. Do not sort or mutate the snapshot. Keep memory threshold, id/kind/target, and all other event/dedup behavior unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-009 --output work/P22-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | NOT_RUN | NOT_RUN | — | — | — | — | [R-5be3e2bbce51d1](#r-5be3e2bbce51d1) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5be3e2bbce51d1"></a>
### 根拠 R-5be3e2bbce51d1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/8`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate memory pressure event creation. Keep its original first evidence string exactly. Append one second string largest_rss_pid=P; largest_rss_kib=R if the observed processes list is nonempty.",
    "Select the maximum rss_kib; ties use the smallest pid. Empty list has no second evidence. Do not sort or mutate the snapshot.",
    "Keep memory threshold, id/kind/target, and all other event/dedup behavior unchanged.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Locate memory pressure event creation. Keep its original first evidence string exactly. Append one second string largest_rss_pid=P; largest_rss_kib=R if the observed processes list is nonempty.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Select the maximum rss_kib; ties use the smallest pid. Empty list has no second evidence. Do not sort or mutate the snapshot.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-3",
      "criterion_text": "Keep memory threshold, id/kind/target, and all other event/dedup behavior unchanged.",
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
      "cwd": "units/P22-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_009"
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
        "pilot_p22_009",
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
      "cwd": "units/P22-009",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-009",
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
      "cwd": "units/P22-009",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-009",
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
      "cwd": "units/P22-009",
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

<a id="p22-010"></a>
## P22-010

CPU inventory labelの過剰countを修正

元のtask_id: `P22-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Fix logical_cpu_count(stat: &str) -> usize. Count lines whose first whitespace-delimited token is cpu followed by one or more ASCII decimal digits and nothing else. Current starts_with-digit logic incorrectly accepts cpu1x and cpu2.5. Ignore aggregate cpu and unrelated/malformed tokens; allow surrounding whitespace. Return max(count,1). No CPU payload parsing.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-010 --output work/P22-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=qwen3-coder-next:latest | NOT_RUN | NOT_RUN | — | — | — | — | [R-6ddbd0eebf1d4c](#r-6ddbd0eebf1d4c) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6ddbd0eebf1d4c"></a>
### 根拠 R-6ddbd0eebf1d4c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/9`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Fix logical_cpu_count(stat: &str) -> usize. Count lines whose first whitespace-delimited token is cpu followed by one or more ASCII decimal digits and nothing else.",
    "Current starts_with-digit logic incorrectly accepts cpu1x and cpu2.5. Ignore aggregate cpu and unrelated/malformed tokens; allow surrounding whitespace. Return max(count,1). No CPU payload parsing.",
    "Existing workspace behavior remains valid.",
    "Rust formatting remains clean.",
    "No clippy warnings.",
    "Workspace type checking succeeds.",
    "Workspace build succeeds.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Fix logical_cpu_count(stat: &str) -> usize. Count lines whose first whitespace-delimited token is cpu followed by one or more ASCII decimal digits and nothing else.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Current starts_with-digit logic incorrectly accepts cpu1x and cpu2.5. Ignore aggregate cpu and unrelated/malformed tokens; allow surrounding whitespace. Return max(count,1). No CPU payload parsing.",
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
      "cwd": "units/P22-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p22_010"
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
        "pilot_p22_010",
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
      "cwd": "units/P22-010",
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
        "--workspace",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P22-010",
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
      "cwd": "units/P22-010",
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
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P22-010",
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
      "cwd": "units/P22-010",
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

<a id="p22-011"></a>
## P22-011

Extract the default mock ResourceBudget from the supplied Rust source.

元のtask_id: `P22-011`。初期ファイル数: 1。

**課題・インターフェース**

Return only max_tokens, max_inference_calls, max_latency_ms, preferred_model_class from impl Default for ResourceBudget.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-011 --output work/P22-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | model=gemma4:26b | NOT_RUN | NOT_RUN | — | — | — | — | [R-d9fa66c4e4de60](#r-d9fa66c4e4de60) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d9fa66c4e4de60"></a>
### 根拠 R-d9fa66c4e4de60

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/10`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Extract the four Default ResourceBudget values exactly; distinguish defaults from fields in ResourceUsage.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Extract the four Default ResourceBudget values exactly; distinguish defaults from fields in ResourceUsage.",
      "category": "functional"
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
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>

<a id="p22-012"></a>
## P22-012

Boundary case: redesign dry-run execution into privileged automatic execution.

元のtask_id: `P22-012`。初期ファイル数: 1。

**課題・インターフェース**

This is a routing boundary only. No implementation or model dispatch is authorized.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2 --task P22-012 --output work/P22-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | CODEX_ONLY | CODEX_ONLY | — | — | — | — | [R-8f9bbe12def0f5](#r-8f9bbe12def0f5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8f9bbe12def0f5"></a>
### 根拠 R-8f9bbe12def0f5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/11`
- 出典ファイルのSHA-256: `87ffa9fb197027df5fcbd743a3b87e666d2552d8c025a9ce64e49887173f8a3c`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Routing must retain this high-risk architecture/authorization request with Codex and send zero Local generation calls.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Routing must retain this high-risk architecture/authorization request with Codex and send zero Local generation calls.",
      "category": "functional"
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
      "kind": "structured",
      "argv": null,
      "portability_note": "Original adapter-specific check; use the declared acceptance contract and fixture tests."
    }
  ]
}
```

</details>
