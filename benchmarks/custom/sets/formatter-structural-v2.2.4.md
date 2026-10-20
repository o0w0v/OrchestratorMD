# 実装・検証手順の比較 / formatter-structural-v2.2.4

セットID: `formatter-structural-v2.2.4`

課題数: 4。個別記録あり: 4、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](formatter-structural-v2.2.4.json) / [結果と根拠のJSON](../results/formatter-structural-v2.2.4.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/formatter-structural-v2.2.4/RESULTS_JA.md)

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
| [F224-001](#f224-001) | process statusのoverflow診断へ対象fieldを付加 | 記録あり |
| [F224-002](#f224-002) | CLI evidenceの空要素省略表示 | 記録あり |
| [F224-003](#f224-003) | memory evidenceへ観測RSSのsaturating合計 | 記録あり |
| [F224-004](#f224-004) | CLI process inventoryの下限表示 | 記録あり |

<a id="f224-001"></a>
## F224-001

process statusのoverflow診断へ対象fieldを付加

元のtask_id: `F224-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. For the existing u32 parse overflow only, return Pid overflow or PPid overflow according to name. Preserve storing parsed values and error propagation. Do not change ASCII digit rejection, missing/duplicate/zero diagnostics or valid u32::MAX support. No complete parser rewrite.

取り出し方:

```sh
python materialize_task.py --set formatter-structural-v2.2.4 --task F224-001 --output work/F224-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | — | REJECT | — | [R-3c61461ea8246d](#r-3c61461ea8246d) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/F224-001/review.json | — | [R-9403b12b1ed5b5](#r-9403b12b1ed5b5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-3c61461ea8246d"></a>
### 根拠 R-3c61461ea8246d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/0`
- 出典ファイルのSHA-256: `bd5545ae95f523682fdc98e9ef3ca28dd869386030e2f3cbb616e15acf20d57d`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

<a id="r-9403b12b1ed5b5"></a>
### 根拠 R-9403b12b1ed5b5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `00f37c33dad4f55dd2606ee46ca9594d7900e84fa45cd37b9eb5371d89617555`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

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
      "cwd": "units/F224-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_f224_001"
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
        "pilot_f224_001",
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
      "cwd": "units/F224-001",
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
      "cwd": "units/F224-001",
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
      "cwd": "units/F224-001",
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
      "cwd": "units/F224-001",
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
      "cwd": "units/F224-001",
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
      "cwd": "units/F224-001",
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

<a id="f224-002"></a>
## F224-002

CLI evidenceの空要素省略表示

元のtask_id: `F224-002`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement evidence_line(entries: &[String]) -> String. Omit empty or whitespace-only entries, join retained entries with exactly one separator " | ". Preserve order, duplicates and original nonempty strings including surrounding spaces/Unicode; do not mutate input. Empty/all-blank input returns (none).

取り出し方:

```sh
python materialize_task.py --set formatter-structural-v2.2.4 --task F224-002 --output work/F224-002
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-6300d7aa942283](#r-6300d7aa942283) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/F224-002/review.json | — | [R-0c1a235edddf63](#r-0c1a235edddf63) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6300d7aa942283"></a>
### 根拠 R-6300d7aa942283

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/1`
- 出典ファイルのSHA-256: `bd5545ae95f523682fdc98e9ef3ca28dd869386030e2f3cbb616e15acf20d57d`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

<a id="r-0c1a235edddf63"></a>
### 根拠 R-0c1a235edddf63

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `00f37c33dad4f55dd2606ee46ca9594d7900e84fa45cd37b9eb5371d89617555`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

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
      "cwd": "units/F224-002",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_f224_002"
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
        "pilot_f224_002",
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
      "cwd": "units/F224-002",
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
      "cwd": "units/F224-002",
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
      "cwd": "units/F224-002",
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
      "cwd": "units/F224-002",
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
      "cwd": "units/F224-002",
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

<a id="f224-003"></a>
## F224-003

memory evidenceへ観測RSSのsaturating合計

元のtask_id: `F224-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Locate memory pressure evidence. Keep its original first string unchanged; always append a second string observed_rss_kib=N where N is the saturating sum of rss_kib of all current state.processes. Empty processes yields 0. Include every entry, including duplicate PIDs. Saturate at u64::MAX; do not sort/mutate snapshot. Preserve memory threshold and all HighLoad behavior.

取り出し方:

```sh
python materialize_task.py --set formatter-structural-v2.2.4 --task F224-003 --output work/F224-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | ESCALATE | ESCALATE | — | — | REJECT | — | [R-6e12b30453740a](#r-6e12b30453740a) |
| コードの検証 | model=gemma4:26b | ESCALATE | — | — | — | workspace/records/router-v2.2/F224-003/review.json | — | [R-92c197b4970b1d](#r-92c197b4970b1d) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-6e12b30453740a"></a>
### 根拠 R-6e12b30453740a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/2`
- 出典ファイルのSHA-256: `bd5545ae95f523682fdc98e9ef3ca28dd869386030e2f3cbb616e15acf20d57d`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

<a id="r-92c197b4970b1d"></a>
### 根拠 R-92c197b4970b1d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `00f37c33dad4f55dd2606ee46ca9594d7900e84fa45cd37b9eb5371d89617555`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

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
      "cwd": "units/F224-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_f224_003"
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
        "pilot_f224_003",
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
      "cwd": "units/F224-003",
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
      "cwd": "units/F224-003",
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
      "cwd": "units/F224-003",
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
      "cwd": "units/F224-003",
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
      "cwd": "units/F224-003",
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

<a id="f224-004"></a>
## F224-004

CLI process inventoryの下限表示

元のtask_id: `F224-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Implement process_inventory(count: usize, truncated: bool) -> String. Return decimal count followed by + exactly when truncated=true; otherwise decimal count only. This marks a lower bound, not an exact total. Preserve zero and usize::MAX; do not change other CLI output or audit behavior.

取り出し方:

```sh
python materialize_task.py --set formatter-structural-v2.2.4 --task F224-004 --output work/F224-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | 記録に条件の明記なし | PASS | PASS | — | — | ACCEPT_NO_CHANGE | — | [R-3d3913a6aa7717](#r-3d3913a6aa7717) |
| コードの検証 | model=gemma4:26b | PASS | — | — | — | workspace/records/router-v2.2/F224-004/review.json | — | [R-56a19cf3fbfe88](#r-56a19cf3fbfe88) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-3d3913a6aa7717"></a>
### 根拠 R-3d3913a6aa7717

- 対応方法: 同一セット・課題IDによる対応
- 出典: `metrics/task-metrics.json` / 位置: `/3`
- 出典ファイルのSHA-256: `bd5545ae95f523682fdc98e9ef3ca28dd869386030e2f3cbb616e15acf20d57d`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

<a id="r-56a19cf3fbfe88"></a>
### 根拠 R-56a19cf3fbfe88

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `00f37c33dad4f55dd2606ee46ca9594d7900e84fa45cd37b9eb5371d89617555`
- [抽出した測定値・他の工程の記録](../results/formatter-structural-v2.2.4.json)

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
      "cwd": "units/F224-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "pilot_f224_004"
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
        "pilot_f224_004",
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
      "cwd": "units/F224-004",
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
      "cwd": "units/F224-004",
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
      "cwd": "units/F224-004",
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
      "cwd": "units/F224-004",
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
      "cwd": "units/F224-004",
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
