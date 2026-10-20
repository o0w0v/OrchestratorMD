# 実装委譲の検証 / 手順-v2.2.1

セットID: `router-shadow-pilot-v2.2.1`

課題数: 14。個別記録あり: 14、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.2.1.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.2.1.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.2.1/RESULTS_JA.md)

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
| [P221R-001](#p221r-001) | CLI process inventoryの下限表示 | 記録あり |
| [P221R-002](#p221r-002) | CLI available memory割合の整数表示 | 記録あり |
| [P221R-003](#p221r-003) | meminfo重複診断にfield名を含める | 記録あり |
| [P221R-004](#p221r-004) | process statusのmissing field表記を一致 | 記録あり |
| [P221R-005](#p221r-005) | CLI evidenceの空要素省略表示 | 記録あり |
| [P221R-006](#p221r-006) | mock report reasonへevent kindを追加 | 記録あり |
| [P221R-007](#p221r-007) | anomaly-free auditへprocess数を追加 | 記録あり |
| [P221R-008](#p221r-008) | skill template reasonへ現在のevidence件数 | 記録あり |
| [P221R-009](#p221r-009) | HighLoad evidenceへthreshold超過量を表示 | 記録あり |
| [P221R-010](#p221r-010) | process重複ID診断でPidとPPidを区別 | 記録あり |
| [P221R-011](#p221r-011) | memory evidenceへ観測RSSのsaturating合計 | 記録あり |
| [P221R-012](#p221r-012) | diskstats inventoryで空行とmalformed rowを除外 | 記録あり |
| [P221R-013](#p221r-013) | Observerのbounded inventory limitsをsourceから抽出 | 記録あり |
| [P221R-014](#p221r-014) | Partial process inventoryのユーザー向け表示要件を決定 | 記録あり |

<a id="p221r-001"></a>
## P221R-001

CLI process inventoryの下限表示

元のtask_id: `P221R-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement process_inventory(count: usize, truncated: bool) -> String. Return decimal count followed by + exactly when truncated=true; otherwise decimal count only. This marks a lower bound, not an exact total. Preserve zero and usize::MAX; do not change other CLI output or audit behavior.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-001 --output work/P221R-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-b15831d9c7c5a1](#r-b15831d9c7c5a1) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-001/review.json | — | [R-de3645085026ed](#r-de3645085026ed) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b15831d9c7c5a1"></a>
### 根拠 R-b15831d9c7c5a1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/0`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-de3645085026ed"></a>
### 根拠 R-de3645085026ed

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement process_inventory(count: usize, truncated: bool) -> String. Return decimal count followed by + exactly when truncated=true; otherwise decimal count only.",
    "This marks a lower bound, not an exact total. Preserve zero and usize::MAX; do not change other CLI output or audit behavior.",
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
      "criterion_text": "Implement process_inventory(count: usize, truncated: bool) -> String. Return decimal count followed by + exactly when truncated=true; otherwise decimal count only.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "This marks a lower bound, not an exact total. Preserve zero and usize::MAX; do not change other CLI output or audit behavior.",
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
      "cwd": "units/P221R-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_001"
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
        "pilot_p221r_001",
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
      "cwd": "units/P221R-001",
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
      "cwd": "units/P221R-001",
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
      "cwd": "units/P221R-001",
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
      "cwd": "units/P221R-001",
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
      "cwd": "units/P221R-001",
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

<a id="p221r-002"></a>
## P221R-002

CLI available memory割合の整数表示

元のtask_id: `P221R-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement available_percent(total: u64, available: u64) -> String. For valid total>0 and available<=total, return floor(100*available/total) followed by %. Invalid ranges return unavailable. All valid u64 values including MAX must work without overflow or float rounding. Preserve other CLI/audit behavior.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-002 --output work/P221R-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-a4a93d0ee7d201](#r-a4a93d0ee7d201) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-002/review.json | — | [R-dbcb668f942887](#r-dbcb668f942887) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a4a93d0ee7d201"></a>
### 根拠 R-a4a93d0ee7d201

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/1`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-dbcb668f942887"></a>
### 根拠 R-dbcb668f942887

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement available_percent(total: u64, available: u64) -> String. For valid total>0 and available<=total, return floor(100*available/total) followed by %.",
    "Invalid ranges return unavailable. All valid u64 values including MAX must work without overflow or float rounding. Preserve other CLI/audit behavior.",
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
      "criterion_text": "Implement available_percent(total: u64, available: u64) -> String. For valid total>0 and available<=total, return floor(100*available/total) followed by %.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Invalid ranges return unavailable. All valid u64 values including MAX must work without overflow or float rounding. Preserve other CLI/audit behavior.",
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
      "cwd": "units/P221R-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_002"
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
        "pilot_p221r_002",
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
      "cwd": "units/P221R-002",
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
      "cwd": "units/P221R-002",
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
      "cwd": "units/P221R-002",
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
      "cwd": "units/P221R-002",
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
      "cwd": "units/P221R-002",
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

<a id="p221r-003"></a>
## P221R-003

meminfo重複診断にfield名を含める

元のtask_id: `P221R-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. At duplicate memory field rejection, report duplicate MemTotal or duplicate MemAvailable according to the existing name variable. Retain first-error ordering, rejection and unknown-field behavior; all other parser diagnostics and valid output remain unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-003 --output work/P221R-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-fbcdd36f137e85](#r-fbcdd36f137e85) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-003/review.json | — | [R-669fce61f41e20](#r-669fce61f41e20) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fbcdd36f137e85"></a>
### 根拠 R-fbcdd36f137e85

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/2`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-669fce61f41e20"></a>
### 根拠 R-669fce61f41e20

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "At duplicate memory field rejection, report duplicate MemTotal or duplicate MemAvailable according to the existing name variable.",
    "Retain first-error ordering, rejection and unknown-field behavior; all other parser diagnostics and valid output remain unchanged.",
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
      "criterion_text": "At duplicate memory field rejection, report duplicate MemTotal or duplicate MemAvailable according to the existing name variable.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Retain first-error ordering, rejection and unknown-field behavior; all other parser diagnostics and valid output remain unchanged.",
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
      "cwd": "units/P221R-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_003"
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
        "pilot_p221r_003",
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
      "cwd": "units/P221R-003",
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
      "cwd": "units/P221R-003",
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
      "cwd": "units/P221R-003",
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
      "cwd": "units/P221R-003",
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
      "cwd": "units/P221R-003",
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

<a id="p221r-004"></a>
## P221R-004

process statusのmissing field表記を一致

元のtask_id: `P221R-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In parse_process final result assembly, missing Pid must report missing Pid and missing PPid must report missing PPid. Pid absence still wins when both are absent; zero pid remains zero pid. Keep Process fields, default absent RSS=0, and all preceding validation unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-004 --output work/P221R-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-c8ea969812ab7c](#r-c8ea969812ab7c) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-004/review.json | — | [R-b9235a2f5c0295](#r-b9235a2f5c0295) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c8ea969812ab7c"></a>
### 根拠 R-c8ea969812ab7c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/3`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-b9235a2f5c0295"></a>
### 根拠 R-b9235a2f5c0295

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In parse_process final result assembly, missing Pid must report missing Pid and missing PPid must report missing PPid.",
    "Pid absence still wins when both are absent; zero pid remains zero pid. Keep Process fields, default absent RSS=0, and all preceding validation unchanged.",
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
      "criterion_text": "In parse_process final result assembly, missing Pid must report missing Pid and missing PPid must report missing PPid.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Pid absence still wins when both are absent; zero pid remains zero pid. Keep Process fields, default absent RSS=0, and all preceding validation unchanged.",
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
      "cwd": "units/P221R-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_004"
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
        "pilot_p221r_004",
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
      "cwd": "units/P221R-004",
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
      "cwd": "units/P221R-004",
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
      "cwd": "units/P221R-004",
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
      "cwd": "units/P221R-004",
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
      "cwd": "units/P221R-004",
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

<a id="p221r-005"></a>
## P221R-005

CLI evidenceの空要素省略表示

元のtask_id: `P221R-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement evidence_line(entries: &[String]) -> String. Omit empty or whitespace-only entries, join retained entries with exactly one separator " | ". Preserve order, duplicates and original nonempty strings including surrounding spaces/Unicode; do not mutate input. Empty/all-blank input returns (none).

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-005 --output work/P221R-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-6c90ee4ef404db](#r-6c90ee4ef404db) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-005/review.json | — | [R-8bdf9c007d6139](#r-8bdf9c007d6139) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6c90ee4ef404db"></a>
### 根拠 R-6c90ee4ef404db

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/4`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-8bdf9c007d6139"></a>
### 根拠 R-8bdf9c007d6139

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/4`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement evidence_line(entries: &[String]) -> String. Omit empty or whitespace-only entries, join retained entries with exactly one separator \" | \".",
    "Preserve order, duplicates and original nonempty strings including surrounding spaces/Unicode; do not mutate input. Empty/all-blank input returns (none).",
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
      "criterion_text": "Implement evidence_line(entries: &[String]) -> String. Omit empty or whitespace-only entries, join retained entries with exactly one separator \" | \".",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve order, duplicates and original nonempty strings including surrounding spaces/Unicode; do not mutate input. Empty/all-blank input returns (none).",
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
      "cwd": "units/P221R-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_005"
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
        "pilot_p221r_005",
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
      "cwd": "units/P221R-005",
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
      "cwd": "units/P221R-005",
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
      "cwd": "units/P221R-005",
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
      "cwd": "units/P221R-005",
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
      "cwd": "units/P221R-005",
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

<a id="p221r-006"></a>
## P221R-006

mock report reasonへevent kindを追加

元のtask_id: `P221R-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In report_for_event reason, append ; kind=K to Mock analysis: review the observed resource candidate, using the Debug spelling of event.kind. Retain report action, system target, capability, low risk, reversibility and the exact cloned event evidence. No permission or execution-policy changes.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-006 --output work/P221R-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-61cde0dd4eeb0f](#r-61cde0dd4eeb0f) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-006/review.json | — | [R-eb67de9606b9f4](#r-eb67de9606b9f4) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-61cde0dd4eeb0f"></a>
### 根拠 R-61cde0dd4eeb0f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/5`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-eb67de9606b9f4"></a>
### 根拠 R-eb67de9606b9f4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/5`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In report_for_event reason, append ; kind=K to Mock analysis: review the observed resource candidate, using the Debug spelling of event.kind.",
    "Retain report action, system target, capability, low risk, reversibility and the exact cloned event evidence. No permission or execution-policy changes.",
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
      "criterion_text": "In report_for_event reason, append ; kind=K to Mock analysis: review the observed resource candidate, using the Debug spelling of event.kind.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Retain report action, system target, capability, low risk, reversibility and the exact cloned event evidence. No permission or execution-policy changes.",
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
      "cwd": "units/P221R-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_006"
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
        "pilot_p221r_006",
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
      "cwd": "units/P221R-006",
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
      "cwd": "units/P221R-006",
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
      "cwd": "units/P221R-006",
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
      "cwd": "units/P221R-006",
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
      "cwd": "units/P221R-006",
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

<a id="p221r-007"></a>
## P221R-007

anomaly-free auditへprocess数を追加

元のtask_id: `P221R-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the no-anomaly inspect audit record. Its short_reason must be No anomaly candidates; model asleep; processes=N where N is the observed snapshot process count. Keep source fast-path, timestamp, returned snapshot and exactly one record; do not invoke provider or alter anomaly/invalid-intent paths.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-007 --output work/P221R-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-32d2984a333eff](#r-32d2984a333eff) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-007/review.json | — | [R-b49efc697526e7](#r-b49efc697526e7) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-32d2984a333eff"></a>
### 根拠 R-32d2984a333eff

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/6`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-b49efc697526e7"></a>
### 根拠 R-b49efc697526e7

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/7`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

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
      "cwd": "units/P221R-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_007"
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
        "pilot_p221r_007",
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
      "cwd": "units/P221R-007",
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
      "cwd": "units/P221R-007",
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
      "cwd": "units/P221R-007",
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
      "cwd": "units/P221R-007",
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
      "cwd": "units/P221R-007",
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

<a id="p221r-008"></a>
## P221R-008

skill template reasonへ現在のevidence件数

元のtask_id: `P221R-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate report template construction. Set reason to Verified report template with current evidence; evidence_count=N where N counts current event evidence entries, including duplicate entries. Keep unsupported-intent rejection, report action/system target/low risk/capability/reversibility and exact current evidence unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-008 --output work/P221R-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-0f043625648fcd](#r-0f043625648fcd) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-008/review.json | — | [R-3aea637c51cb8e](#r-3aea637c51cb8e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0f043625648fcd"></a>
### 根拠 R-0f043625648fcd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/7`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-3aea637c51cb8e"></a>
### 根拠 R-3aea637c51cb8e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/8`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

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
      "cwd": "units/P221R-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_008"
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
        "pilot_p221r_008",
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
      "cwd": "units/P221R-008",
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
      "cwd": "units/P221R-008",
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
      "cwd": "units/P221R-008",
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
      "cwd": "units/P221R-008",
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
      "cwd": "units/P221R-008",
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

<a id="p221r-009"></a>
## P221R-009

HighLoad evidenceへthreshold超過量を表示

元のtask_id: `P221R-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Find the HighLoad diagnostic evidence. Append ; excess_load=X to the existing single evidence string, with X=load_one-2*logical_cpus formatted to two decimal places. Keep original load_one and logical_cpus values/formatting, strict threshold and finite/zero guards, event identity/order and memory evidence unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-009 --output work/P221R-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-fb6f0eda99d0a3](#r-fb6f0eda99d0a3) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-009/review.json | — | [R-bd0497372ef0f3](#r-bd0497372ef0f3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fb6f0eda99d0a3"></a>
### 根拠 R-fb6f0eda99d0a3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/8`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-bd0497372ef0f3"></a>
### 根拠 R-bd0497372ef0f3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/9`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Find the HighLoad diagnostic evidence. Append ; excess_load=X to the existing single evidence string, with X=load_one-2*logical_cpus formatted to two decimal places.",
    "Keep original load_one and logical_cpus values/formatting, strict threshold and finite/zero guards, event identity/order and memory evidence unchanged.",
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
      "criterion_text": "Find the HighLoad diagnostic evidence. Append ; excess_load=X to the existing single evidence string, with X=load_one-2*logical_cpus formatted to two decimal places.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep original load_one and logical_cpus values/formatting, strict threshold and finite/zero guards, event identity/order and memory evidence unchanged.",
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
      "cwd": "units/P221R-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_009"
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
        "pilot_p221r_009",
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
      "cwd": "units/P221R-009",
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
      "cwd": "units/P221R-009",
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
      "cwd": "units/P221R-009",
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
      "cwd": "units/P221R-009",
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
      "cwd": "units/P221R-009",
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

<a id="p221r-010"></a>
## P221R-010

process重複ID診断でPidとPPidを区別

元のtask_id: `P221R-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate duplicate process-ID rejection. Report duplicate Pid or duplicate PPid based on the repeated field. Preserve duplicate RSS wording, first-error ordering, validation and returned fields. Unknown repeated fields remain ignored.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-010 --output work/P221R-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-c872ffe0c5c1f0](#r-c872ffe0c5c1f0) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-010/review.json | — | [R-71f1539b5befe2](#r-71f1539b5befe2) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c872ffe0c5c1f0"></a>
### 根拠 R-c872ffe0c5c1f0

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/9`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-71f1539b5befe2"></a>
### 根拠 R-71f1539b5befe2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/10`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate duplicate process-ID rejection. Report duplicate Pid or duplicate PPid based on the repeated field.",
    "Preserve duplicate RSS wording, first-error ordering, validation and returned fields. Unknown repeated fields remain ignored.",
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
      "criterion_text": "Locate duplicate process-ID rejection. Report duplicate Pid or duplicate PPid based on the repeated field.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve duplicate RSS wording, first-error ordering, validation and returned fields. Unknown repeated fields remain ignored.",
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
      "cwd": "units/P221R-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_010"
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
        "pilot_p221r_010",
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
      "cwd": "units/P221R-010",
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
      "cwd": "units/P221R-010",
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
      "cwd": "units/P221R-010",
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
      "cwd": "units/P221R-010",
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
      "cwd": "units/P221R-010",
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

<a id="p221r-011"></a>
## P221R-011

memory evidenceへ観測RSSのsaturating合計

元のtask_id: `P221R-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate memory pressure evidence. Keep its original first string unchanged; always append a second string observed_rss_kib=N where N is the saturating sum of rss_kib of all current state.processes. Empty processes yields 0. Include every entry, including duplicate PIDs. Saturate at u64::MAX; do not sort/mutate snapshot. Preserve memory threshold and all HighLoad behavior.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-011 --output work/P221R-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | REJECT | — | [R-c194efb9319a81](#r-c194efb9319a81) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P221R-011/review.json | — | [R-a85862fc462006](#r-a85862fc462006) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c194efb9319a81"></a>
### 根拠 R-c194efb9319a81

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/10`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-a85862fc462006"></a>
### 根拠 R-a85862fc462006

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/11`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate memory pressure evidence. Keep its original first string unchanged; always append a second string observed_rss_kib=N where N is the saturating sum of rss_kib of all current state.processes.",
    "Empty processes yields 0. Include every entry, including duplicate PIDs. Saturate at u64::MAX; do not sort/mutate snapshot. Preserve memory threshold and all HighLoad behavior.",
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
      "criterion_text": "Locate memory pressure evidence. Keep its original first string unchanged; always append a second string observed_rss_kib=N where N is the saturating sum of rss_kib of all current state.processes.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Empty processes yields 0. Include every entry, including duplicate PIDs. Saturate at u64::MAX; do not sort/mutate snapshot. Preserve memory threshold and all HighLoad behavior.",
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
      "cwd": "units/P221R-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_011"
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
        "pilot_p221r_011",
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
      "cwd": "units/P221R-011",
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
      "cwd": "units/P221R-011",
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
      "cwd": "units/P221R-011",
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
      "cwd": "units/P221R-011",
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
      "cwd": "units/P221R-011",
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

<a id="p221r-012"></a>
## P221R-012

diskstats inventoryで空行とmalformed rowを除外

元のtask_id: `P221R-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Fix disk_inventory_rows(text: &str) -> usize, extracted from the existing .lines().count() disk inventory bug. Count rows with at least three whitespace-delimited tokens: major, minor, device. major and minor must each be nonempty ASCII decimal digits fitting u32. Device is any nonempty token. Ignore blank, missing-field, signed, Unicode-digit or overflowing identifiers. Ignore remaining payload columns; count duplicate valid rows separately. Do not implement a full diskstats parser.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-012 --output work/P221R-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-d84d4fe35ade57](#r-d84d4fe35ade57) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-4b1a7cffaa46db](#r-4b1a7cffaa46db) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d84d4fe35ade57"></a>
### 根拠 R-d84d4fe35ade57

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/11`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-4b1a7cffaa46db"></a>
### 根拠 R-4b1a7cffaa46db

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/0`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Fix disk_inventory_rows(text: &str) -> usize, extracted from the existing .lines().count() disk inventory bug. Count rows with at least three whitespace-delimited tokens: major, minor, device.",
    "major and minor must each be nonempty ASCII decimal digits fitting u32. Device is any nonempty token. Ignore blank, missing-field, signed, Unicode-digit or overflowing identifiers. Ignore remaining payload columns; count duplicate valid rows separately. Do not implement a full diskstats parser.",
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
      "criterion_text": "Fix disk_inventory_rows(text: &str) -> usize, extracted from the existing .lines().count() disk inventory bug. Count rows with at least three whitespace-delimited tokens: major, minor, device.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "major and minor must each be nonempty ASCII decimal digits fitting u32. Device is any nonempty token. Ignore blank, missing-field, signed, Unicode-digit or overflowing identifiers. Ignore remaining payload columns; count duplicate valid rows separately. Do not implement a full diskstats parser.",
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
      "cwd": "units/P221R-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p221r_012"
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
        "pilot_p221r_012",
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
      "cwd": "units/P221R-012",
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
      "cwd": "units/P221R-012",
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
      "cwd": "units/P221R-012",
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
      "cwd": "units/P221R-012",
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
      "cwd": "units/P221R-012",
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

<a id="p221r-013"></a>
## P221R-013

Observerのbounded inventory limitsをsourceから抽出

元のtask_id: `P221R-013`。初期ファイル数: 1。

**課題・インターフェース**

From read_bounded and LinuxObserver::observe, extract read take limit, accepted text byte limit, maximum enumerated directory entries, and maximum collected processes. Distinguish the take limit from the accepted size limit.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-013 --output work/P221R-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-8f0e59ae6d82e9](#r-8f0e59ae6d82e9) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P221R-013/review.json | — | [R-3e4ba11eeb2641](#r-3e4ba11eeb2641) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8f0e59ae6d82e9"></a>
### 根拠 R-8f0e59ae6d82e9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/12`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<a id="r-3e4ba11eeb2641"></a>
### 根拠 R-3e4ba11eeb2641

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/6`
- 出典ファイルのSHA-256: `2b5c530b9185c97d8002ff7abf8153833b8abbd5b8a9b60db4bd048dcf21ccff`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Extract the four bounds from their respective call sites exactly, without confusing read cap, accepted bytes and collection limits.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Extract the four bounds from their respective call sites exactly, without confusing read cap, accepted bytes and collection limits.",
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

<a id="p221r-014"></a>
## P221R-014

Partial process inventoryのユーザー向け表示要件を決定

元のtask_id: `P221R-014`。初期ファイル数: 1。

**課題・インターフェース**

An open product choice, not typed source extraction. Codex must choose acceptance meaning for partial counts and unavailable telemetry; no implementation is delegated.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.1 --task P221R-014 --output work/P221R-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | CODEX_ONLY | — | [R-46af9c5af312d8](#r-46af9c5af312d8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-46af9c5af312d8"></a>
### 根拠 R-46af9c5af312d8

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/13`
- 出典ファイルのSHA-256: `7b14ebd1c00d46bf9c0e8b009881b16b81ce8f205705e4520ef067848edf347a`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.1.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Free specification with normal risk must remain Codex-owned, with zero Local dispatch.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Free specification with normal risk must remain Codex-owned, with zero Local dispatch.",
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
