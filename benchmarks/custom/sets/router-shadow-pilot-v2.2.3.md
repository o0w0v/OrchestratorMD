# 実装委譲の検証 / 手順-v2.2.3

セットID: `router-shadow-pilot-v2.2.3`

課題数: 14。個別記録あり: 14、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.2.3.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.2.3.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.2.3/RESULTS_JA.md)

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
| [P223-001](#p223-001) | CLI optional inventoryの不明値と実測ゼロを区別して表示 | 記録あり |
| [P223-002](#p223-002) | CLI telemetry warningの空要素除外と単複表示 | 記録あり |
| [P223-003](#p223-003) | meminfo重複診断にfield名を含める | 記録あり |
| [P223-004](#p223-004) | meminfo invalid-range診断へ観測値を記載 | 記録あり |
| [P223-005](#p223-005) | process statusのoverflow診断へ対象fieldを付加 | 記録あり |
| [P223-006](#p223-006) | mock report reasonへ観測対象名を追加 | 記録あり |
| [P223-007](#p223-007) | memory pressure evidenceへprocess sample完全性を表示 | 記録あり |
| [P223-008](#p223-008) | skill template reasonへ現在のevidence件数 | 記録あり |
| [P223-009](#p223-009) | HighLoad evidenceへlogical CPU当たりloadを追加 | 記録あり |
| [P223-010](#p223-010) | process IDの字句不正診断でPidとPPidを区別 | 記録あり |
| [P223-011](#p223-011) | anomaly-free auditへtelemetry warning件数を追加 | 記録あり |
| [P223-012](#p223-012) | diskstats inventoryで空行とmalformed rowを除外 | 記録あり |
| [P223-013](#p223-013) | ResourceBudgetのdefault数値をsourceから抽出 | 記録あり |
| [P223-014](#p223-014) | Telemetry warning集約のユーザー向け表示要件を決定 | 記録あり |

<a id="p223-001"></a>
## P223-001

CLI optional inventoryの不明値と実測ゼロを区別して表示

元のtask_id: `P223-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement inventory_count(Option<usize>) -> String for disk/service/TCP display: None => unavailable; Some(n) => unsigned decimal n without wrappers or separators. Some(0) is an observed zero, not unavailable. Preserve maximum usize, other CLI output and audit behavior.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-001 --output work/P223-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-805e95b2f49906](#r-805e95b2f49906) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P223-001/review.json | — | [R-45a39455a79d2a](#r-45a39455a79d2a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-805e95b2f49906"></a>
### 根拠 R-805e95b2f49906

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/0`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-45a39455a79d2a"></a>
### 根拠 R-45a39455a79d2a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement inventory_count(Option<usize>) -> String for disk/service/TCP display: None => unavailable; Some(n) => unsigned decimal n without wrappers or separators.",
    "Some(0) is an observed zero, not unavailable. Preserve maximum usize, other CLI output and audit behavior.",
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
      "criterion_text": "Implement inventory_count(Option<usize>) -> String for disk/service/TCP display: None => unavailable; Some(n) => unsigned decimal n without wrappers or separators.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Some(0) is an observed zero, not unavailable. Preserve maximum usize, other CLI output and audit behavior.",
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
      "cwd": "units/P223-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_001"
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
        "pilot_p223_001",
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
      "cwd": "units/P223-001",
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
      "cwd": "units/P223-001",
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
      "cwd": "units/P223-001",
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
      "cwd": "units/P223-001",
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
      "cwd": "units/P223-001",
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
      "cwd": "units/P223-001",
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

<a id="p223-002"></a>
## P223-002

CLI telemetry warningの空要素除外と単複表示

元のtask_id: `P223-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Count only warnings whose trim() is nonempty, without mutating input. Return no warnings for 0, 1 warning for 1, N warnings for larger counts. Preserve duplicates and Unicode warnings as separate entries. This is summary presentation only; existing individual warning lines stay unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-002 --output work/P223-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-4e152ba1bfc993](#r-4e152ba1bfc993) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P223-002/review.json | — | [R-8ccbb4d5d7f163](#r-8ccbb4d5d7f163) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4e152ba1bfc993"></a>
### 根拠 R-4e152ba1bfc993

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/1`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-8ccbb4d5d7f163"></a>
### 根拠 R-8ccbb4d5d7f163

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Count only warnings whose trim() is nonempty, without mutating input. Return no warnings for 0, 1 warning for 1, N warnings for larger counts.",
    "Preserve duplicates and Unicode warnings as separate entries. This is summary presentation only; existing individual warning lines stay unchanged.",
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
      "criterion_text": "Count only warnings whose trim() is nonempty, without mutating input. Return no warnings for 0, 1 warning for 1, N warnings for larger counts.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve duplicates and Unicode warnings as separate entries. This is summary presentation only; existing individual warning lines stay unchanged.",
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
      "cwd": "units/P223-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_002"
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
        "pilot_p223_002",
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
      "cwd": "units/P223-002",
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
      "cwd": "units/P223-002",
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
      "cwd": "units/P223-002",
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
      "cwd": "units/P223-002",
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
      "cwd": "units/P223-002",
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
      "cwd": "units/P223-002",
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

<a id="p223-003"></a>
## P223-003

meminfo重複診断にfield名を含める

元のtask_id: `P223-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. At duplicate memory field rejection, report duplicate MemTotal or duplicate MemAvailable according to the existing name variable. Retain first-error ordering, rejection and unknown-field behavior; all other parser diagnostics and valid output remain unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-003 --output work/P223-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-de11c8a25fa65c](#r-de11c8a25fa65c) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/P223-003/review.json | — | [R-de90b0a5b48a8e](#r-de90b0a5b48a8e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-de11c8a25fa65c"></a>
### 根拠 R-de11c8a25fa65c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/2`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-de90b0a5b48a8e"></a>
### 根拠 R-de90b0a5b48a8e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

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
    "All workspace tests remain valid.",
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
      "cwd": "units/P223-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_003"
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
        "pilot_p223_003",
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
      "cwd": "units/P223-003",
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
      "cwd": "units/P223-003",
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
      "cwd": "units/P223-003",
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
      "cwd": "units/P223-003",
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
      "cwd": "units/P223-003",
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
      "cwd": "units/P223-003",
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

<a id="p223-004"></a>
## P223-004

meminfo invalid-range診断へ観測値を記載

元のtask_id: `P223-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. At the existing invalid memory range branch, return exactly invalid memory range: total=T; available=A using the parsed u64 values. Retain total==0 and available>total rejection, error precedence, duplicate/missing/value errors and valid Memory output. Do not alter parsing.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-004 --output work/P223-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | ACCEPT_WITH_MINOR_FIX | — | [R-0e6855ac10a9af](#r-0e6855ac10a9af) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P223-004/review.json | — | [R-6b5df96d845982](#r-6b5df96d845982) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0e6855ac10a9af"></a>
### 根拠 R-0e6855ac10a9af

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/3`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-6b5df96d845982"></a>
### 根拠 R-6b5df96d845982

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/4`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "At the existing invalid memory range branch, return exactly invalid memory range: total=T; available=A using the parsed u64 values.",
    "Retain total==0 and available>total rejection, error precedence, duplicate/missing/value errors and valid Memory output. Do not alter parsing.",
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
      "criterion_text": "At the existing invalid memory range branch, return exactly invalid memory range: total=T; available=A using the parsed u64 values.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Retain total==0 and available>total rejection, error precedence, duplicate/missing/value errors and valid Memory output. Do not alter parsing.",
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
      "cwd": "units/P223-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_004"
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
        "pilot_p223_004",
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
      "cwd": "units/P223-004",
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
      "cwd": "units/P223-004",
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
      "cwd": "units/P223-004",
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
      "cwd": "units/P223-004",
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
      "cwd": "units/P223-004",
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
      "cwd": "units/P223-004",
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

<a id="p223-005"></a>
## P223-005

process statusのoverflow診断へ対象fieldを付加

元のtask_id: `P223-005`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. For the existing u32 parse overflow only, return Pid overflow or PPid overflow according to name. Preserve storing parsed values and error propagation. Do not change ASCII digit rejection, missing/duplicate/zero diagnostics or valid u32::MAX support. No complete parser rewrite.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-005 --output work/P223-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | ESCALATE | — | — | REJECT | — | [R-cb517560274b83](#r-cb517560274b83) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/P223-005/review.json | — | [R-601b9813c758a5](#r-601b9813c758a5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-cb517560274b83"></a>
### 根拠 R-cb517560274b83

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/4`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-601b9813c758a5"></a>
### 根拠 R-601b9813c758a5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/5`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "For the existing u32 parse overflow only, return Pid overflow or PPid overflow according to name. Preserve storing parsed values and error propagation.",
    "Do not change ASCII digit rejection, missing/duplicate/zero diagnostics or valid u32::MAX support. No complete parser rewrite.",
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
      "criterion_text": "For the existing u32 parse overflow only, return Pid overflow or PPid overflow according to name. Preserve storing parsed values and error propagation.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not change ASCII digit rejection, missing/duplicate/zero diagnostics or valid u32::MAX support. No complete parser rewrite.",
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
      "cwd": "units/P223-005",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_005"
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
        "pilot_p223_005",
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
      "cwd": "units/P223-005",
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
      "cwd": "units/P223-005",
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
      "cwd": "units/P223-005",
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
      "cwd": "units/P223-005",
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
      "cwd": "units/P223-005",
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
      "cwd": "units/P223-005",
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

<a id="p223-006"></a>
## P223-006

mock report reasonへ観測対象名を追加

元のtask_id: `P223-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In report_for_event reason, append ; observed_target=T to Mock analysis: review the observed resource candidate, where T is event.target verbatim. The proposal target must remain system. Keep action/capability/risk/reversibility and cloned evidence unchanged; this adds human-readable context only.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-006 --output work/P223-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-eb26406d8b8abd](#r-eb26406d8b8abd) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-3e785891a0ed08](#r-3e785891a0ed08) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-eb26406d8b8abd"></a>
### 根拠 R-eb26406d8b8abd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/5`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-3e785891a0ed08"></a>
### 根拠 R-3e785891a0ed08

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/0`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In report_for_event reason, append ; observed_target=T to Mock analysis: review the observed resource candidate, where T is event.target verbatim.",
    "The proposal target must remain system. Keep action/capability/risk/reversibility and cloned evidence unchanged; this adds human-readable context only.",
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
      "criterion_text": "In report_for_event reason, append ; observed_target=T to Mock analysis: review the observed resource candidate, where T is event.target verbatim.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "The proposal target must remain system. Keep action/capability/risk/reversibility and cloned evidence unchanged; this adds human-readable context only.",
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
      "cwd": "units/P223-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_006"
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
        "pilot_p223_006",
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
      "cwd": "units/P223-006",
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
      "cwd": "units/P223-006",
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
      "cwd": "units/P223-006",
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
      "cwd": "units/P223-006",
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
      "cwd": "units/P223-006",
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
      "cwd": "units/P223-006",
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

<a id="p223-007"></a>
## P223-007

memory pressure evidenceへprocess sample完全性を表示

元のtask_id: `P223-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate memory pressure evidence. Keep its single string prefix, appending ; sampled_processes=N; truncated=B using processes.len() and processes_truncated (lowercase bool). Do not change memory threshold, event identity/order, snapshot or HighLoad evidence. Count every current entry, including duplicates.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-007 --output work/P223-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-4f298449d44297](#r-4f298449d44297) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-c845f10ba943a0](#r-c845f10ba943a0) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4f298449d44297"></a>
### 根拠 R-4f298449d44297

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/6`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-c845f10ba943a0"></a>
### 根拠 R-c845f10ba943a0

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/2`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate memory pressure evidence. Keep its single string prefix, appending ; sampled_processes=N; truncated=B using processes.len() and processes_truncated (lowercase bool).",
    "Do not change memory threshold, event identity/order, snapshot or HighLoad evidence. Count every current entry, including duplicates.",
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
      "criterion_text": "Locate memory pressure evidence. Keep its single string prefix, appending ; sampled_processes=N; truncated=B using processes.len() and processes_truncated (lowercase bool).",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not change memory threshold, event identity/order, snapshot or HighLoad evidence. Count every current entry, including duplicates.",
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
      "cwd": "units/P223-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_007"
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
        "pilot_p223_007",
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
      "cwd": "units/P223-007",
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
      "cwd": "units/P223-007",
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
      "cwd": "units/P223-007",
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
      "cwd": "units/P223-007",
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
      "cwd": "units/P223-007",
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
      "cwd": "units/P223-007",
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

<a id="p223-008"></a>
## P223-008

skill template reasonへ現在のevidence件数

元のtask_id: `P223-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate report template construction. Set reason to Verified report template with current evidence; evidence_count=N where N counts current event evidence entries, including duplicate entries. Keep unsupported-intent rejection, report action/system target/low risk/capability/reversibility and exact current evidence unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-008 --output work/P223-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-829f6811e0c019](#r-829f6811e0c019) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-fc4b2effda8202](#r-fc4b2effda8202) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-829f6811e0c019"></a>
### 根拠 R-829f6811e0c019

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/7`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-fc4b2effda8202"></a>
### 根拠 R-fc4b2effda8202

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/3`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

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
    "All workspace tests remain valid.",
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
      "cwd": "units/P223-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_008"
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
        "pilot_p223_008",
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
      "cwd": "units/P223-008",
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
        "--locked",
        "-p",
        "ncos-skills",
        "--test",
        "acceptance",
        "skill_cache",
        "--",
        "--exact"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "format",
      "kind": "lint",
      "cwd": "units/P223-008",
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
      "cwd": "units/P223-008",
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
      "cwd": "units/P223-008",
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
        "--workspace",
        "--offline",
        "--locked"
      ],
      "portability_note": "Host WSL, environment and external timeout wrappers removed; Cargo arguments preserved."
    },
    {
      "id": "workspace-check",
      "kind": "typecheck",
      "cwd": "units/P223-008",
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
      "cwd": "units/P223-008",
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

<a id="p223-009"></a>
## P223-009

HighLoad evidenceへlogical CPU当たりloadを追加

元のtask_id: `P223-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate HighLoad diagnostic evidence. Append ; load_per_cpu=X to the existing single string, X=load_one/logical_cpus with two decimal places. Keep strict threshold, finite/zero guards, original prefix, event identity/order and memory evidence unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-009 --output work/P223-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-56595ea3117cbf](#r-56595ea3117cbf) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-5c964c8e283f3f](#r-5c964c8e283f3f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-56595ea3117cbf"></a>
### 根拠 R-56595ea3117cbf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/8`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-5c964c8e283f3f"></a>
### 根拠 R-5c964c8e283f3f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/4`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate HighLoad diagnostic evidence. Append ; load_per_cpu=X to the existing single string, X=load_one/logical_cpus with two decimal places.",
    "Keep strict threshold, finite/zero guards, original prefix, event identity/order and memory evidence unchanged.",
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
      "criterion_text": "Locate HighLoad diagnostic evidence. Append ; load_per_cpu=X to the existing single string, X=load_one/logical_cpus with two decimal places.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Keep strict threshold, finite/zero guards, original prefix, event identity/order and memory evidence unchanged.",
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
      "cwd": "units/P223-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_009"
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
        "pilot_p223_009",
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
      "cwd": "units/P223-009",
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
      "cwd": "units/P223-009",
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
      "cwd": "units/P223-009",
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
      "cwd": "units/P223-009",
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
      "cwd": "units/P223-009",
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
      "cwd": "units/P223-009",
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

<a id="p223-010"></a>
## P223-010

process IDの字句不正診断でPidとPPidを区別

元のtask_id: `P223-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the empty/non-ASCII-digit process-ID rejection. Replace invalid process id with invalid Pid or invalid PPid using name. Duplicate, overflow, zero and missing diagnostics must remain unchanged; valid Process results are unchanged. Do not change accepted syntax.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-010 --output work/P223-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-0717931a0fd3f4](#r-0717931a0fd3f4) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-04d06ddf854b47](#r-04d06ddf854b47) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0717931a0fd3f4"></a>
### 根拠 R-0717931a0fd3f4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/9`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-04d06ddf854b47"></a>
### 根拠 R-04d06ddf854b47

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/5`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the empty/non-ASCII-digit process-ID rejection. Replace invalid process id with invalid Pid or invalid PPid using name.",
    "Duplicate, overflow, zero and missing diagnostics must remain unchanged; valid Process results are unchanged. Do not change accepted syntax.",
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
      "criterion_text": "Locate the empty/non-ASCII-digit process-ID rejection. Replace invalid process id with invalid Pid or invalid PPid using name.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Duplicate, overflow, zero and missing diagnostics must remain unchanged; valid Process results are unchanged. Do not change accepted syntax.",
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
      "cwd": "units/P223-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_010"
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
        "pilot_p223_010",
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
      "cwd": "units/P223-010",
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
      "cwd": "units/P223-010",
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
      "cwd": "units/P223-010",
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
      "cwd": "units/P223-010",
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
      "cwd": "units/P223-010",
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
      "cwd": "units/P223-010",
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

<a id="p223-011"></a>
## P223-011

anomaly-free auditへtelemetry warning件数を追加

元のtask_id: `P223-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Find the healthy no-anomaly audit record construction. Its short_reason must be No anomaly candidates; model asleep; warnings=N, N=state.warnings.len(), including empty strings and duplicates. Borrow the constructed string for the existing record helper. Preserve no-model fast path, returned snapshot, record timestamp/source and all anomalous paths. Non-target regions must remain unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-011 --output work/P223-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-e63391d211af5d](#r-e63391d211af5d) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-27f329afd7f65a](#r-27f329afd7f65a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e63391d211af5d"></a>
### 根拠 R-e63391d211af5d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/10`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-27f329afd7f65a"></a>
### 根拠 R-27f329afd7f65a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/6`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Find the healthy no-anomaly audit record construction. Its short_reason must be No anomaly candidates; model asleep; warnings=N, N=state.warnings.len(), including empty strings and duplicates.",
    "Borrow the constructed string for the existing record helper. Preserve no-model fast path, returned snapshot, record timestamp/source and all anomalous paths. Non-target regions must remain unchanged.",
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
      "criterion_text": "Find the healthy no-anomaly audit record construction. Its short_reason must be No anomaly candidates; model asleep; warnings=N, N=state.warnings.len(), including empty strings and duplicates.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Borrow the constructed string for the existing record helper. Preserve no-model fast path, returned snapshot, record timestamp/source and all anomalous paths. Non-target regions must remain unchanged.",
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
      "cwd": "units/P223-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_011"
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
        "pilot_p223_011",
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
      "cwd": "units/P223-011",
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
      "cwd": "units/P223-011",
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
      "cwd": "units/P223-011",
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
      "cwd": "units/P223-011",
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
      "cwd": "units/P223-011",
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
      "cwd": "units/P223-011",
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

<a id="p223-012"></a>
## P223-012

diskstats inventoryで空行とmalformed rowを除外

元のtask_id: `P223-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Fix disk_inventory_rows(text: &str) -> usize, extracted from the existing .lines().count() disk inventory bug. Count rows with at least three whitespace-delimited tokens: major, minor, device. major and minor must each be nonempty ASCII decimal digits fitting u32. Device is any nonempty token. Ignore blank, missing-field, signed, Unicode-digit or overflowing identifiers. Ignore remaining payload columns; count duplicate valid rows separately. Do not implement a full diskstats parser.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-012 --output work/P223-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-4b40782078630f](#r-4b40782078630f) |
| コードの検証 | model=qwen3-coder-next:latest | PASS | — | — | — | workspace/records/router-v2.2/P223-012/review.json | — | [R-a2c6af5baecb3f](#r-a2c6af5baecb3f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4b40782078630f"></a>
### 根拠 R-4b40782078630f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/11`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-a2c6af5baecb3f"></a>
### 根拠 R-a2c6af5baecb3f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

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
    "All workspace tests remain valid.",
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
      "cwd": "units/P223-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p223_012"
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
        "pilot_p223_012",
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
      "cwd": "units/P223-012",
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
      "cwd": "units/P223-012",
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
      "cwd": "units/P223-012",
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
      "cwd": "units/P223-012",
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
      "cwd": "units/P223-012",
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
      "cwd": "units/P223-012",
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

<a id="p223-013"></a>
## P223-013

ResourceBudgetのdefault数値をsourceから抽出

元のtask_id: `P223-013`。初期ファイル数: 1。

**課題・インターフェース**

From impl Default for ResourceBudget, extract max_tokens, max_inference_calls, max_latency_ms exactly. These are application default budgets, not Worker/Ollama settings.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-013 --output work/P223-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | — | — | [R-7bc607befcf25d](#r-7bc607befcf25d) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-bc1b04c9e2e880](#r-bc1b04c9e2e880) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-7bc607befcf25d"></a>
### 根拠 R-7bc607befcf25d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/12`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<a id="r-bc1b04c9e2e880"></a>
### 根拠 R-bc1b04c9e2e880

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/1`
- 出典ファイルのSHA-256: `349c1a481de7370be9f5cf690430107220b33c04f592aa8afdf6690e5aab4c41`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Extract the three numeric application defaults exactly; do not substitute Worker generation budgets.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Extract the three numeric application defaults exactly; do not substitute Worker generation budgets.",
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

<a id="p223-014"></a>
## P223-014

Telemetry warning集約のユーザー向け表示要件を決定

元のtask_id: `P223-014`。初期ファイル数: 1。

**課題・インターフェース**

An open product choice, not typed source extraction. Codex must choose acceptance meaning for warning aggregation and duplicate telemetry; no implementation is delegated.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.3 --task P223-014 --output work/P223-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | — | — | — | — | CODEX_ONLY | — | [R-226a4502631999](#r-226a4502631999) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-226a4502631999"></a>
### 根拠 R-226a4502631999

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/13`
- 出典ファイルのSHA-256: `2bfae4ed3ce0507b9ed2b27998ec80308019d6639df68b59d4bc71e6bcaf35a8`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.3.json)

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
