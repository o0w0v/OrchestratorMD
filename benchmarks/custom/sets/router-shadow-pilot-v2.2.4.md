# 実装委譲の検証 / 手順-v2.2.4

セットID: `router-shadow-pilot-v2.2.4`

課題数: 14。個別記録あり: 14、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](router-shadow-pilot-v2.2.4.json) / [結果と根拠のJSON](../results/router-shadow-pilot-v2.2.4.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/router-shadow-pilot-v2.2.4/RESULTS_JA.md)

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
| [P224-001](#p224-001) | CLI telemetryを改行しないescaped一行として表示 | 記録あり |
| [P224-002](#p224-002) | memory evidenceにused KiBを独立した第2要素として追加 | 記録あり |
| [P224-003](#p224-003) | TCP inventoryが非data行の01を誤countする不具合 | 記録あり |
| [P224-004](#p224-004) | CLIのused memory量を妥当性検査付きで表示 | 記録あり |
| [P224-005](#p224-005) | MockObserverのnested snapshot値をtyped抽出 | 記録あり |
| [P224-006](#p224-006) | 正常系auditへprocess sampleのcomplete/bounded区別を追加 | 記録あり |
| [P224-007](#p224-007) | VmRSSの値parse失敗へ診断prefixを付与 | 記録あり |
| [P224-008](#p224-008) | HighLoad evidenceへ観測timestampを第2要素で追加 | 記録あり |
| [P224-009](#p224-009) | mock report reasonへ安定したevent kind labelを表示 | 記録あり |
| [P224-010](#p224-010) | skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示 | 記録あり |
| [P224-011](#p224-011) | CLI warning overviewのstable unique preview | 記録あり |
| [P224-012](#p224-012) | meminfo重複診断へMemTotal/MemAvailableの名前を付加 | 記録あり |
| [P224-013](#p224-013) | Telemetry欠測を説明するUIの表示方針を決定 | 記録あり |
| [P224-014](#p224-014) | CLI per-CPU loadの欠測/非有限値と小数表示 | 記録あり |

<a id="p224-001"></a>
## P224-001

CLI telemetryを改行しないescaped一行として表示

元のtask_id: `P224-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement telemetry_line(warning: &str) -> String: escape each backslash as two backslashes, LF as literal backslash-n, CR as backslash-r, TAB as backslash-t. Preserve all other Unicode characters and spaces exactly, with no trimming or extra prefix. Empty input returns empty. Process original characters once, without re-escaping newly inserted escape characters. Only individual CLI display changes; audit/source input is unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-001 --output work/P224-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | INFRA_ERROR | INFRA_ERROR | — | — | REJECT_INFRA_NO_CANDIDATE | — | [R-c1441aefe0e78b](#r-c1441aefe0e78b) |
| コードの検証 | model=gemma4:26b | INFRA_ERROR | — | — | — | workspace/records/router-v2.2/P224-001/review.json | — | [R-ba13292e28a306](#r-ba13292e28a306) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c1441aefe0e78b"></a>
### 根拠 R-c1441aefe0e78b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/0`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-ba13292e28a306"></a>
### 根拠 R-ba13292e28a306

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement telemetry_line(warning: &str) -> String: escape each backslash as two backslashes, LF as literal backslash-n, CR as backslash-r, TAB as backslash-t.",
    "Preserve all other Unicode characters and spaces exactly, with no trimming or extra prefix. Empty input returns empty. Process original characters once, without re-escaping newly inserted escape characters. Only individual CLI display changes; audit/source input is unchanged.",
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
      "criterion_text": "Implement telemetry_line(warning: &str) -> String: escape each backslash as two backslashes, LF as literal backslash-n, CR as backslash-r, TAB as backslash-t.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve all other Unicode characters and spaces exactly, with no trimming or extra prefix. Empty input returns empty. Process original characters once, without re-escaping newly inserted escape characters. Only individual CLI display changes; audit/source input is unchanged.",
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
      "cwd": "units/P224-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_001"
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
        "pilot_p224_001",
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
      "cwd": "units/P224-001",
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
      "cwd": "units/P224-001",
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
      "cwd": "units/P224-001",
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
      "cwd": "units/P224-001",
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
      "cwd": "units/P224-001",
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
      "cwd": "units/P224-001",
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

<a id="p224-002"></a>
## P224-002

memory evidenceにused KiBを独立した第2要素として追加

元のtask_id: `P224-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the memory pressure event evidence. Preserve the original first evidence string byte-for-byte; append exactly one second entry used_kib=N, where N is total_kib minus available_kib. Preserve the memory validity/strict threshold guard, event identity/order, all HighLoad behavior and source snapshot. On valid emitted memory events the subtraction cannot underflow.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-002 --output work/P224-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-ba2c0c08f2fdef](#r-ba2c0c08f2fdef) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-03842c6530f393](#r-03842c6530f393) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ba2c0c08f2fdef"></a>
### 根拠 R-ba2c0c08f2fdef

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/1`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-03842c6530f393"></a>
### 根拠 R-03842c6530f393

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/0`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the memory pressure event evidence. Preserve the original first evidence string byte-for-byte; append exactly one second entry used_kib=N, where N is total_kib minus available_kib.",
    "Preserve the memory validity/strict threshold guard, event identity/order, all HighLoad behavior and source snapshot. On valid emitted memory events the subtraction cannot underflow.",
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
      "criterion_text": "Locate the memory pressure event evidence. Preserve the original first evidence string byte-for-byte; append exactly one second entry used_kib=N, where N is total_kib minus available_kib.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve the memory validity/strict threshold guard, event identity/order, all HighLoad behavior and source snapshot. On valid emitted memory events the subtraction cannot underflow.",
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
      "cwd": "units/P224-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_002"
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
        "pilot_p224_002",
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
      "cwd": "units/P224-002",
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
      "cwd": "units/P224-002",
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
      "cwd": "units/P224-002",
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
      "cwd": "units/P224-002",
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
      "cwd": "units/P224-002",
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
      "cwd": "units/P224-002",
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

<a id="p224-003"></a>
## P224-003

TCP inventoryが非data行の01を誤countする不具合

元のtask_id: `P224-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Debug count_established_tcp(text: &str) -> usize. Count a line iff it has at least four whitespace-separated fields, the first is one or more ASCII decimal digits followed by exactly one colon, and the fourth is exactly 01. Do not validate the address fields; IPv4/IPv6 opaque fields and extra columns are accepted. Preserve duplicates, leading whitespace and CRLF. Reject headers, empty slots, signed/non-ASCII/malformed slot numbers and other states. This fixes one data-row predicate, not the observer or a whole network parser.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-003 --output work/P224-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-59dcebf92f2154](#r-59dcebf92f2154) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-4d7b7fb2a8ccdd](#r-4d7b7fb2a8ccdd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-59dcebf92f2154"></a>
### 根拠 R-59dcebf92f2154

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/2`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-4d7b7fb2a8ccdd"></a>
### 根拠 R-4d7b7fb2a8ccdd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/1`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Debug count_established_tcp(text: &str) -> usize. Count a line iff it has at least four whitespace-separated fields, the first is one or more ASCII decimal digits followed by exactly one colon, and the fourth is exactly 01.",
    "Do not validate the address fields; IPv4/IPv6 opaque fields and extra columns are accepted. Preserve duplicates, leading whitespace and CRLF. Reject headers, empty slots, signed/non-ASCII/malformed slot numbers and other states. This fixes one data-row predicate, not the observer or a whole network parser.",
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
      "criterion_text": "Debug count_established_tcp(text: &str) -> usize. Count a line iff it has at least four whitespace-separated fields, the first is one or more ASCII decimal digits followed by exactly one colon, and the fourth is exactly 01.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not validate the address fields; IPv4/IPv6 opaque fields and extra columns are accepted. Preserve duplicates, leading whitespace and CRLF. Reject headers, empty slots, signed/non-ASCII/malformed slot numbers and other states. This fixes one data-row predicate, not the observer or a whole network parser.",
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
      "cwd": "units/P224-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_003"
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
        "pilot_p224_003",
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
      "cwd": "units/P224-003",
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
      "cwd": "units/P224-003",
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
      "cwd": "units/P224-003",
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
      "cwd": "units/P224-003",
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
      "cwd": "units/P224-003",
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
      "cwd": "units/P224-003",
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

<a id="p224-004"></a>
## P224-004

CLIのused memory量を妥当性検査付きで表示

元のtask_id: `P224-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement used_memory(total: u64, available: u64) -> String. If total is zero or available exceeds total, return unavailable. Otherwise return N KiB used, N=total-available in unsigned decimal. Equal nonzero values are valid and yield 0 KiB used. No rounding, percentages, wrapping arithmetic or change to observation/audit.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-004 --output work/P224-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-0cf90f4ac0f10f](#r-0cf90f4ac0f10f) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-e2f0048bc98a2d](#r-e2f0048bc98a2d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0cf90f4ac0f10f"></a>
### 根拠 R-0cf90f4ac0f10f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/3`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-e2f0048bc98a2d"></a>
### 根拠 R-e2f0048bc98a2d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/2`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement used_memory(total: u64, available: u64) -> String. If total is zero or available exceeds total, return unavailable. Otherwise return N KiB used, N=total-available in unsigned decimal.",
    "Equal nonzero values are valid and yield 0 KiB used. No rounding, percentages, wrapping arithmetic or change to observation/audit.",
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
      "criterion_text": "Implement used_memory(total: u64, available: u64) -> String. If total is zero or available exceeds total, return unavailable. Otherwise return N KiB used, N=total-available in unsigned decimal.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Equal nonzero values are valid and yield 0 KiB used. No rounding, percentages, wrapping arithmetic or change to observation/audit.",
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
      "cwd": "units/P224-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_004"
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
        "pilot_p224_004",
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
      "cwd": "units/P224-004",
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
      "cwd": "units/P224-004",
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
      "cwd": "units/P224-004",
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
      "cwd": "units/P224-004",
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
      "cwd": "units/P224-004",
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
      "cwd": "units/P224-004",
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

<a id="p224-005"></a>
## P224-005

MockObserverのnested snapshot値をtyped抽出

元のtask_id: `P224-005`。初期ファイル数: 1。

**課題・インターフェース**

From MockObserver.observe, extract observed_unix_ms, logical_cpus, memory.available_kib as available_kib, number of process entries as process_count, processes_truncated, and whether service_count is Some as service_count_present. Read source facts only.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-005 --output work/P224-005
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-51f7390bf9ec0e](#r-51f7390bf9ec0e) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-579ee522ba9b71](#r-579ee522ba9b71) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-51f7390bf9ec0e"></a>
### 根拠 R-51f7390bf9ec0e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/4`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-579ee522ba9b71"></a>
### 根拠 R-579ee522ba9b71

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/3`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Extract all six nested snapshot facts exactly; distinguish absent Option from observed zero and count process entries.",
    "Only declared editable regions change; protected source and tests remain identical."
  ],
  "acceptance_criteria": [
    {
      "criterion_id": "BEHAVIOR-1",
      "criterion_text": "Extract all six nested snapshot facts exactly; distinguish absent Option from observed zero and count process entries.",
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

<a id="p224-006"></a>
## P224-006

正常系auditへprocess sampleのcomplete/bounded区別を追加

元のtask_id: `P224-006`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate healthy no-anomaly audit construction. Return the original record with short_reason No anomaly candidates; model asleep; sample=complete when processes_truncated=false, or the same prefix with sample=bounded when true. Use the protected record helper contract, borrowing any generated String for its reason argument. Keep source/time/intent/empty event and no-provider fast path, returned SystemState, anomaly and duplicate paths unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-006 --output work/P224-006
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-9f8a2a6373aa08](#r-9f8a2a6373aa08) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-661165aec7a494](#r-661165aec7a494) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9f8a2a6373aa08"></a>
### 根拠 R-9f8a2a6373aa08

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/5`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-661165aec7a494"></a>
### 根拠 R-661165aec7a494

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/4`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate healthy no-anomaly audit construction. Return the original record with short_reason No anomaly candidates; model asleep; sample=complete when processes_truncated=false, or the same prefix with sample=bounded when true.",
    "Use the protected record helper contract, borrowing any generated String for its reason argument. Keep source/time/intent/empty event and no-provider fast path, returned SystemState, anomaly and duplicate paths unchanged.",
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
      "criterion_text": "Locate healthy no-anomaly audit construction. Return the original record with short_reason No anomaly candidates; model asleep; sample=complete when processes_truncated=false, or the same prefix with sample=bounded when true.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Use the protected record helper contract, borrowing any generated String for its reason argument. Keep source/time/intent/empty event and no-provider fast path, returned SystemState, anomaly and duplicate paths unchanged.",
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
      "cwd": "units/P224-006",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_006"
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
        "pilot_p224_006",
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
      "cwd": "units/P224-006",
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
      "cwd": "units/P224-006",
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
      "cwd": "units/P224-006",
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
      "cwd": "units/P224-006",
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
      "cwd": "units/P224-006",
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
      "cwd": "units/P224-006",
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

<a id="p224-007"></a>
## P224-007

VmRSSの値parse失敗へ診断prefixを付与

元のtask_id: `P224-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. At the existing VmRSS value conversion, call protected parse_kib_value(value) and retain its successful u64 result in rss. If it fails, propagate exactly invalid VmRSS: E, where E is its original error string. Preserve duplicate RSS error precedence, missing RSS default 0, PID/PPid rules and parse_memory/parse_kib_value behavior. Only this error wrapping changes.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-007 --output work/P224-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-9a8dda8baac31f](#r-9a8dda8baac31f) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-7eae064f37a62b](#r-7eae064f37a62b) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9a8dda8baac31f"></a>
### 根拠 R-9a8dda8baac31f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/6`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-7eae064f37a62b"></a>
### 根拠 R-7eae064f37a62b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/5`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "At the existing VmRSS value conversion, call protected parse_kib_value(value) and retain its successful u64 result in rss. If it fails, propagate exactly invalid VmRSS: E, where E is its original error string.",
    "Preserve duplicate RSS error precedence, missing RSS default 0, PID/PPid rules and parse_memory/parse_kib_value behavior. Only this error wrapping changes.",
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
      "criterion_text": "At the existing VmRSS value conversion, call protected parse_kib_value(value) and retain its successful u64 result in rss. If it fails, propagate exactly invalid VmRSS: E, where E is its original error string.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve duplicate RSS error precedence, missing RSS default 0, PID/PPid rules and parse_memory/parse_kib_value behavior. Only this error wrapping changes.",
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
      "cwd": "units/P224-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_007"
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
        "pilot_p224_007",
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
      "cwd": "units/P224-007",
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
      "cwd": "units/P224-007",
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
      "cwd": "units/P224-007",
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
      "cwd": "units/P224-007",
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
      "cwd": "units/P224-007",
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
      "cwd": "units/P224-007",
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

<a id="p224-008"></a>
## P224-008

HighLoad evidenceへ観測timestampを第2要素で追加

元のtask_id: `P224-008`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate HighLoad evidence. Preserve the original first evidence string and append exactly one second entry observed_unix_ms=T, T=the snapshot u128 timestamp in decimal. Preserve finite/zero CPU guards, strict load threshold, event kind/id/target/order and all memory evidence. No time reading or snapshot mutation.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-008 --output work/P224-008
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-f89ca1d55f5935](#r-f89ca1d55f5935) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-bb8f3bc561091d](#r-bb8f3bc561091d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-f89ca1d55f5935"></a>
### 根拠 R-f89ca1d55f5935

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/7`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-bb8f3bc561091d"></a>
### 根拠 R-bb8f3bc561091d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/6`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate HighLoad evidence. Preserve the original first evidence string and append exactly one second entry observed_unix_ms=T, T=the snapshot u128 timestamp in decimal.",
    "Preserve finite/zero CPU guards, strict load threshold, event kind/id/target/order and all memory evidence. No time reading or snapshot mutation.",
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
      "criterion_text": "Locate HighLoad evidence. Preserve the original first evidence string and append exactly one second entry observed_unix_ms=T, T=the snapshot u128 timestamp in decimal.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Preserve finite/zero CPU guards, strict load threshold, event kind/id/target/order and all memory evidence. No time reading or snapshot mutation.",
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
      "cwd": "units/P224-008",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_008"
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
        "pilot_p224_008",
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
      "cwd": "units/P224-008",
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
      "cwd": "units/P224-008",
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
      "cwd": "units/P224-008",
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
      "cwd": "units/P224-008",
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
      "cwd": "units/P224-008",
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
      "cwd": "units/P224-008",
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

<a id="p224-009"></a>
## P224-009

mock report reasonへ安定したevent kind labelを表示

元のtask_id: `P224-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. In report_for_event, retain the reason prefix Mock analysis: review the observed resource candidate and append ; kind=L; evidence_items=N. L maps MemoryPressure=>memory, HighLoad=>load, SuspiciousProcess=>process, SuspiciousParentChild=>parent-child, UnusualConnection=>connection. N is event.evidence.len(), including empty/duplicate entries. Preserve all authority-bearing fields and evidence bytes.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-009 --output work/P224-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-258d8e2d537aee](#r-258d8e2d537aee) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-2ad74425d22d9d](#r-2ad74425d22d9d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-258d8e2d537aee"></a>
### 根拠 R-258d8e2d537aee

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/8`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-2ad74425d22d9d"></a>
### 根拠 R-2ad74425d22d9d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/7`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "In report_for_event, retain the reason prefix Mock analysis: review the observed resource candidate and append ; kind=L; evidence_items=N.",
    "L maps MemoryPressure=>memory, HighLoad=>load, SuspiciousProcess=>process, SuspiciousParentChild=>parent-child, UnusualConnection=>connection. N is event.evidence.len(), including empty/duplicate entries. Preserve all authority-bearing fields and evidence bytes.",
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
      "criterion_text": "In report_for_event, retain the reason prefix Mock analysis: review the observed resource candidate and append ; kind=L; evidence_items=N.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "L maps MemoryPressure=>memory, HighLoad=>load, SuspiciousProcess=>process, SuspiciousParentChild=>parent-child, UnusualConnection=>connection. N is event.evidence.len(), including empty/duplicate entries. Preserve all authority-bearing fields and evidence bytes.",
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
      "cwd": "units/P224-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_009"
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
        "pilot_p224_009",
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
      "cwd": "units/P224-009",
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
      "cwd": "units/P224-009",
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
      "cwd": "units/P224-009",
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
      "cwd": "units/P224-009",
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
      "cwd": "units/P224-009",
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
      "cwd": "units/P224-009",
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

<a id="p224-010"></a>
## P224-010

skill templateの診断へ現在evidenceのUTF-8 bytes合計を表示

元のtask_id: `P224-010`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate the verified report template reason. Append ; evidence_bytes=N to Verified report template with current evidence. N is the sum of UTF-8 byte lengths of every current event.evidence string, including duplicates, represented as u128 decimal. Do not count Unicode scalar values or separators. Preserve evidence order/bytes, intent eligibility, all action/capability/risk/target fields, and template cache behavior.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-010 --output work/P224-010
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-6b0b65db642bd1](#r-6b0b65db642bd1) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-81132c9761199e](#r-81132c9761199e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6b0b65db642bd1"></a>
### 根拠 R-6b0b65db642bd1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/9`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-81132c9761199e"></a>
### 根拠 R-81132c9761199e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/8`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate the verified report template reason. Append ; evidence_bytes=N to Verified report template with current evidence. N is the sum of UTF-8 byte lengths of every current event.evidence string, including duplicates, represented as u128 decimal.",
    "Do not count Unicode scalar values or separators. Preserve evidence order/bytes, intent eligibility, all action/capability/risk/target fields, and template cache behavior.",
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
      "criterion_text": "Locate the verified report template reason. Append ; evidence_bytes=N to Verified report template with current evidence. N is the sum of UTF-8 byte lengths of every current event.evidence string, including duplicates, represented as u128 decimal.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Do not count Unicode scalar values or separators. Preserve evidence order/bytes, intent eligibility, all action/capability/risk/target fields, and template cache behavior.",
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
      "cwd": "units/P224-010",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_010"
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
        "pilot_p224_010",
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
      "cwd": "units/P224-010",
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
      "cwd": "units/P224-010",
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
      "cwd": "units/P224-010",
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
      "cwd": "units/P224-010",
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
      "cwd": "units/P224-010",
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
      "cwd": "units/P224-010",
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

<a id="p224-011"></a>
## P224-011

CLI warning overviewのstable unique preview

元のtask_id: `P224-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement warning_overview(warnings: &[String]) -> String. Trim each string, discard empty results, deduplicate exact trimmed strings case-sensitively while preserving first-occurrence order. Display the first three unique strings joined by exactly space-pipe-space. If more remain, append space... space(+N), N=additional unique count. Return (none) when none remain. Preserve input and Unicode; do not sort or case-fold. Existing individual warning lines stay unchanged.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-011 --output work/P224-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-c1e764830763a6](#r-c1e764830763a6) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-3bcc3bd587bf31](#r-3bcc3bd587bf31) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c1e764830763a6"></a>
### 根拠 R-c1e764830763a6

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/10`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-3bcc3bd587bf31"></a>
### 根拠 R-3bcc3bd587bf31

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/9`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement warning_overview(warnings: &[String]) -> String. Trim each string, discard empty results, deduplicate exact trimmed strings case-sensitively while preserving first-occurrence order.",
    "Display the first three unique strings joined by exactly space-pipe-space. If more remain, append space... space(+N), N=additional unique count. Return (none) when none remain. Preserve input and Unicode; do not sort or case-fold. Existing individual warning lines stay unchanged.",
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
      "criterion_text": "Implement warning_overview(warnings: &[String]) -> String. Trim each string, discard empty results, deduplicate exact trimmed strings case-sensitively while preserving first-occurrence order.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Display the first three unique strings joined by exactly space-pipe-space. If more remain, append space... space(+N), N=additional unique count. Return (none) when none remain. Preserve input and Unicode; do not sort or case-fold. Existing individual warning lines stay unchanged.",
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
      "cwd": "units/P224-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_011"
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
        "pilot_p224_011",
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
      "cwd": "units/P224-011",
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
      "cwd": "units/P224-011",
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
      "cwd": "units/P224-011",
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
      "cwd": "units/P224-011",
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
      "cwd": "units/P224-011",
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
      "cwd": "units/P224-011",
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

<a id="p224-012"></a>
## P224-012

meminfo重複診断へMemTotal/MemAvailableの名前を付加

元のtask_id: `P224-012`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate duplicate known memory-field rejection in parse_memory. Return duplicate MemTotal or duplicate MemAvailable using the existing name, before parsing the duplicate value. Unknown memory fields remain ignored, and duplicate process-ID, missing/invalid/range diagnostics and valid Memory output are unchanged. No parser restructuring.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-012 --output work/P224-012
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-8e464d7ecdb044](#r-8e464d7ecdb044) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-3825a11b2fc254](#r-3825a11b2fc254) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8e464d7ecdb044"></a>
### 根拠 R-8e464d7ecdb044

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/11`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-3825a11b2fc254"></a>
### 根拠 R-3825a11b2fc254

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/10`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Locate duplicate known memory-field rejection in parse_memory. Return duplicate MemTotal or duplicate MemAvailable using the existing name, before parsing the duplicate value.",
    "Unknown memory fields remain ignored, and duplicate process-ID, missing/invalid/range diagnostics and valid Memory output are unchanged. No parser restructuring.",
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
      "criterion_text": "Locate duplicate known memory-field rejection in parse_memory. Return duplicate MemTotal or duplicate MemAvailable using the existing name, before parsing the duplicate value.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Unknown memory fields remain ignored, and duplicate process-ID, missing/invalid/range diagnostics and valid Memory output are unchanged. No parser restructuring.",
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
      "cwd": "units/P224-012",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_012"
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
        "pilot_p224_012",
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
      "cwd": "units/P224-012",
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
      "cwd": "units/P224-012",
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
      "cwd": "units/P224-012",
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
      "cwd": "units/P224-012",
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
      "cwd": "units/P224-012",
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
      "cwd": "units/P224-012",
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

<a id="p224-013"></a>
## P224-013

Telemetry欠測を説明するUIの表示方針を決定

元のtask_id: `P224-013`。初期ファイル数: 1。

**課題・インターフェース**

An open product choice, not typed source extraction. Codex must decide how unavailable inventory and observed zero should be explained in the CLI; no implementation or observation/authority policy is delegated.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-013 --output work/P224-013
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | CODEX_ONLY | CODEX_ONLY | — | — | BOUNDARY_CORRECT | — | [R-c142ab3200b989](#r-c142ab3200b989) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-c142ab3200b989"></a>
### 根拠 R-c142ab3200b989

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/12`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

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

<a id="p224-014"></a>
## P224-014

CLI per-CPU loadの欠測/非有限値と小数表示

元のtask_id: `P224-014`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement load_per_cpu(load: f64, cpus: usize) -> String. Return unavailable for zero cpus, negative load, NaN or either infinity. Otherwise format load divided by cpus to exactly two decimal places. Treat both positive and negative zero load as 0.00. Use ordinary Rust fixed-point rounding. Preserve source values and all original load/CPU outputs and audit; this is a supplemental display only.

取り出し方:

```sh
python materialize_task.py --set router-shadow-pilot-v2.2.4 --task P224-014 --output work/P224-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | NOT_RUN | NOT_RUN | — | — | NOT_REVIEWED | — | [R-6e7da011e7bc4a](#r-6e7da011e7bc4a) |
| 実行状態・対照条件 | 記録に条件の明記なし | NOT_RUN | — | — | — | — | — | [R-d98f0180bfc819](#r-d98f0180bfc819) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6e7da011e7bc4a"></a>
### 根拠 R-6e7da011e7bc4a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/all-task-outcomes.json` / 位置: `/13`
- 出典ファイルのSHA-256: `ac7e495a48fd14a89f8c9c8366452a4c1d12ac68213596b707bed3da4a4130ac`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<a id="r-d98f0180bfc819"></a>
### 根拠 R-d98f0180bfc819

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/unstarted/11`
- 出典ファイルのSHA-256: `144b3563d16ab92ea9ed46a7ff49980fbfda370cebde25325cc7a77185526946`
- [抽出した測定値・他の工程の記録](../results/router-shadow-pilot-v2.2.4.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Implement load_per_cpu(load: f64, cpus: usize) -> String. Return unavailable for zero cpus, negative load, NaN or either infinity. Otherwise format load divided by cpus to exactly two decimal places.",
    "Treat both positive and negative zero load as 0.00. Use ordinary Rust fixed-point rounding. Preserve source values and all original load/CPU outputs and audit; this is a supplemental display only.",
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
      "criterion_text": "Implement load_per_cpu(load: f64, cpus: usize) -> String. Return unavailable for zero cpus, negative load, NaN or either infinity. Otherwise format load divided by cpus to exactly two decimal places.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Treat both positive and negative zero load as 0.00. Use ordinary Rust fixed-point rounding. Preserve source values and all original load/CPU outputs and audit; this is a supplemental display only.",
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
      "cwd": "units/P224-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_p224_014"
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
        "pilot_p224_014",
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
      "cwd": "units/P224-014",
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
      "cwd": "units/P224-014",
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
      "cwd": "units/P224-014",
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
      "cwd": "units/P224-014",
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
      "cwd": "units/P224-014",
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
      "cwd": "units/P224-014",
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
