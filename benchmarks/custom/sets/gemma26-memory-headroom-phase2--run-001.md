# Gemma26のメモリ設定・実行条件の比較 / gemma26-memory-headroom-phase2 / run-001

セットID: `gemma26-memory-headroom-phase2--run-001`

課題数: 12。個別記録あり: 12、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](gemma26-memory-headroom-phase2--run-001.json) / [結果と根拠のJSON](../results/gemma26-memory-headroom-phase2--run-001.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

参考の実験レポート: [RESULTS_JA.md](../reports/gemma26-memory-headroom-phase2--run-001/RESULTS_JA.md)

**実験で固定した設定**（実際の結果・モデル情報は各記録を参照）

```json
[
  {
    "model": "gemma4:26b",
    "digest": "08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68",
    "codex_model": "gpt-6-sol",
    "effort": "xhigh",
    "speed": "Standard",
    "Local_repairs": 0
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
| [LS3W228-001](#ls3w228-001) | Collect direct child process IDs for one selected parent | 記録あり |
| [LS3W228-003](#ls3w228-003) | Collect intent IDs for explicitly denied policies | 記録あり |
| [LS3W228-004](#ls3w228-004) | Project warning UTF-8 byte lengths without filtering | 記録あり |
| [LS3W228-007](#ls3w228-007) | Compute observed process RSS spread in KiB | 記録あり |
| [LS3W228-009](#ls3w228-009) | Accumulate audit inference elapsed milliseconds saturating at u128 | 記録あり |
| [LS3W228-011](#ls3w228-011) | Accumulate byte size of intent constraint strings | 記録あり |
| [LS3W228-014](#ls3w228-014) | Forward wide elapsed milliseconds to protected seconds conversion | 記録あり |
| [LS3W228-015](#ls3w228-015) | Delegate proposal reversibility label to protected boolean helper | 記録あり |
| [LS3W228-017](#ls3w228-017) | Delegate observation epoch bucket to two-argument protected helper | 記録あり |
| [LS3W228-020](#ls3w228-020) | Render empty versus nonempty warning inventory receipt | 記録あり |
| [LS3W228-021](#ls3w228-021) | Render three-state event evidence presence receipt | 記録あり |
| [LS3W228-023](#ls3w228-023) | Render intent identity and requester byte sizes in exact receipt | 記録あり |

<a id="ls3w228-001"></a>
## LS3W228-001

Collect direct child process IDs for one selected parent

元のtask_id: `LS3W228-001`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn child_process_ids(state: &SystemState, parent: u32) -> Vec<u32>. Return pid of every process whose parent_pid equals parent, preserving input order and duplicates. Parent zero is an ordinary matching value; no recursion, sorting or deduplication.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-001 --output work/LS3W228-001
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-e4200e68961648](#r-e4200e68961648) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-722c39d1dca87c](#r-722c39d1dca87c) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-c8ee9cdbb889c6](#r-c8ee9cdbb889c6) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-86905609fd9bb2](#r-86905609fd9bb2) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-e73f6a4deb168f](#r-e73f6a4deb168f) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-2d91dffacd1589](#r-2d91dffacd1589) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-9319e25ea8908b](#r-9319e25ea8908b) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-3536a934c2c2a1](#r-3536a934c2c2a1) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-834c97527c8d8f](#r-834c97527c8d8f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e4200e68961648"></a>
### 根拠 R-e4200e68961648

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/0`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-722c39d1dca87c"></a>
### 根拠 R-722c39d1dca87c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/12`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-c8ee9cdbb889c6"></a>
### 根拠 R-c8ee9cdbb889c6

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/24`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-86905609fd9bb2"></a>
### 根拠 R-86905609fd9bb2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/0/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-e73f6a4deb168f"></a>
### 根拠 R-e73f6a4deb168f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/0/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-2d91dffacd1589"></a>
### 根拠 R-2d91dffacd1589

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/0/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-9319e25ea8908b"></a>
### 根拠 R-9319e25ea8908b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/0/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-3536a934c2c2a1"></a>
### 根拠 R-3536a934c2c2a1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/0/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-834c97527c8d8f"></a>
### 根拠 R-834c97527c8d8f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/0/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn child_process_ids(state: &SystemState, parent: u32) -> Vec<u32>.",
    "Return pid of every process whose parent_pid equals parent, preserving input order and duplicates. Parent zero is an ordinary matching value; no recursion, sorting or deduplication.",
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
      "criterion_text": "Preserve exact signature: pub fn child_process_ids(state: &SystemState, parent: u32) -> Vec<u32>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return pid of every process whose parent_pid equals parent, preserving input order and duplicates. Parent zero is an ordinary matching value; no recursion, sorting or deduplication.",
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
      "cwd": "units/LS3W228-001",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_001"
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
        "challenger_ls3w228_001",
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
      "cwd": "units/LS3W228-001",
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
      "cwd": "units/LS3W228-001",
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
      "cwd": "units/LS3W228-001",
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
      "cwd": "units/LS3W228-001",
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
      "cwd": "units/LS3W228-001",
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
      "cwd": "units/LS3W228-001",
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

<a id="ls3w228-003"></a>
## LS3W228-003

Collect intent IDs for explicitly denied policies

元のtask_id: `LS3W228-003`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn denied_intent_ids(records: &[ncos_core::AuditRecord]) -> Vec<String>. For policy Some with decision Deny, collect intent.id as an owned String. Missing/Allow/RequireConfirmation are excluded; preserve order and duplicates, including blank IDs.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-003 --output work/LS3W228-003
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | ESCALATE | — | — | — | — | [R-998e77f94df270](#r-998e77f94df270) |
| ローカル実装 | arm=D | — | ESCALATE | — | — | — | — | [R-688b30b9b630a1](#r-688b30b9b630a1) |
| ローカル実装 | arm=E | — | ESCALATE | — | — | — | — | [R-bfe2e59e725758](#r-bfe2e59e725758) |
| コードの検証 | arms_condition=A2 | ESCALATE | — | — | — | — | — | [R-cb5cc377003969](#r-cb5cc377003969) |
| コードの検証 | arms_condition=D | ESCALATE | — | — | — | — | — | [R-72dd7b4e970609](#r-72dd7b4e970609) |
| コードの検証 | arms_condition=E | ESCALATE | — | — | — | — | — | [R-8096e044ffef22](#r-8096e044ffef22) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-998e77f94df270"></a>
### 根拠 R-998e77f94df270

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/1`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-688b30b9b630a1"></a>
### 根拠 R-688b30b9b630a1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/13`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-bfe2e59e725758"></a>
### 根拠 R-bfe2e59e725758

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/25`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-cb5cc377003969"></a>
### 根拠 R-cb5cc377003969

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/1/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-72dd7b4e970609"></a>
### 根拠 R-72dd7b4e970609

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/1/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-8096e044ffef22"></a>
### 根拠 R-8096e044ffef22

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/1/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn denied_intent_ids(records: &[ncos_core::AuditRecord]) -> Vec<String>.",
    "For policy Some with decision Deny, collect intent.id as an owned String. Missing/Allow/RequireConfirmation are excluded; preserve order and duplicates, including blank IDs.",
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
      "criterion_text": "Preserve exact signature: pub fn denied_intent_ids(records: &[ncos_core::AuditRecord]) -> Vec<String>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "For policy Some with decision Deny, collect intent.id as an owned String. Missing/Allow/RequireConfirmation are excluded; preserve order and duplicates, including blank IDs.",
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
      "cwd": "units/LS3W228-003",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_003"
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
        "challenger_ls3w228_003",
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
      "cwd": "units/LS3W228-003",
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
      "cwd": "units/LS3W228-003",
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
      "cwd": "units/LS3W228-003",
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
      "cwd": "units/LS3W228-003",
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
      "cwd": "units/LS3W228-003",
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
      "cwd": "units/LS3W228-003",
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

<a id="ls3w228-004"></a>
## LS3W228-004

Project warning UTF-8 byte lengths without filtering

元のtask_id: `LS3W228-004`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn warning_byte_lengths(state: &SystemState) -> Vec<usize>. Return one UTF-8 byte length for every warning, in order. Keep empty/whitespace warnings and duplicates. Never trim or count Unicode scalar values.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-004 --output work/LS3W228-004
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-d5c01d8cd1ff32](#r-d5c01d8cd1ff32) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-acf6e6606e6aed](#r-acf6e6606e6aed) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-4fec7f6c702ac9](#r-4fec7f6c702ac9) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-479e3991a7c9b2](#r-479e3991a7c9b2) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-b609a3909c652a](#r-b609a3909c652a) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-4779860f9bd7bf](#r-4779860f9bd7bf) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-887658c7a78883](#r-887658c7a78883) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-1764cacea13896](#r-1764cacea13896) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-1e4a75cfc65637](#r-1e4a75cfc65637) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d5c01d8cd1ff32"></a>
### 根拠 R-d5c01d8cd1ff32

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/2`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-acf6e6606e6aed"></a>
### 根拠 R-acf6e6606e6aed

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/14`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-4fec7f6c702ac9"></a>
### 根拠 R-4fec7f6c702ac9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/26`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-479e3991a7c9b2"></a>
### 根拠 R-479e3991a7c9b2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/2/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-b609a3909c652a"></a>
### 根拠 R-b609a3909c652a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/2/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-4779860f9bd7bf"></a>
### 根拠 R-4779860f9bd7bf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/2/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-887658c7a78883"></a>
### 根拠 R-887658c7a78883

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/2/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-1764cacea13896"></a>
### 根拠 R-1764cacea13896

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/2/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-1e4a75cfc65637"></a>
### 根拠 R-1e4a75cfc65637

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/2/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn warning_byte_lengths(state: &SystemState) -> Vec<usize>.",
    "Return one UTF-8 byte length for every warning, in order. Keep empty/whitespace warnings and duplicates. Never trim or count Unicode scalar values.",
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
      "criterion_text": "Preserve exact signature: pub fn warning_byte_lengths(state: &SystemState) -> Vec<usize>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return one UTF-8 byte length for every warning, in order. Keep empty/whitespace warnings and duplicates. Never trim or count Unicode scalar values.",
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
      "cwd": "units/LS3W228-004",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_004"
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
        "challenger_ls3w228_004",
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
      "cwd": "units/LS3W228-004",
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
      "cwd": "units/LS3W228-004",
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
      "cwd": "units/LS3W228-004",
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
      "cwd": "units/LS3W228-004",
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
      "cwd": "units/LS3W228-004",
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
      "cwd": "units/LS3W228-004",
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

<a id="ls3w228-007"></a>
## LS3W228-007

Compute observed process RSS spread in KiB

元のtask_id: `LS3W228-007`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn process_rss_spread(state: &SystemState) -> u64. Return maximum minus minimum rss_kib across all processes. Empty or one item returns zero. Do not sum, convert units, or ignore zero-valued samples.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-007 --output work/LS3W228-007
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-f2b66d1e9f2360](#r-f2b66d1e9f2360) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-f9f35b61dc969e](#r-f9f35b61dc969e) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-c390933af79768](#r-c390933af79768) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-151e50dfc69981](#r-151e50dfc69981) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-875579305d1ce5](#r-875579305d1ce5) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-104da7c2394e2b](#r-104da7c2394e2b) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-94ca4592591427](#r-94ca4592591427) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-6d3d62a47d2b1e](#r-6d3d62a47d2b1e) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-fc6b0cc9014572](#r-fc6b0cc9014572) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-f2b66d1e9f2360"></a>
### 根拠 R-f2b66d1e9f2360

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/3`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-f9f35b61dc969e"></a>
### 根拠 R-f9f35b61dc969e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/15`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-c390933af79768"></a>
### 根拠 R-c390933af79768

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/27`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-151e50dfc69981"></a>
### 根拠 R-151e50dfc69981

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/3/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-875579305d1ce5"></a>
### 根拠 R-875579305d1ce5

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/3/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-104da7c2394e2b"></a>
### 根拠 R-104da7c2394e2b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/3/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-94ca4592591427"></a>
### 根拠 R-94ca4592591427

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/3/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-6d3d62a47d2b1e"></a>
### 根拠 R-6d3d62a47d2b1e

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/3/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-fc6b0cc9014572"></a>
### 根拠 R-fc6b0cc9014572

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/3/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn process_rss_spread(state: &SystemState) -> u64.",
    "Return maximum minus minimum rss_kib across all processes. Empty or one item returns zero. Do not sum, convert units, or ignore zero-valued samples.",
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
      "criterion_text": "Preserve exact signature: pub fn process_rss_spread(state: &SystemState) -> u64.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return maximum minus minimum rss_kib across all processes. Empty or one item returns zero. Do not sum, convert units, or ignore zero-valued samples.",
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
      "cwd": "units/LS3W228-007",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_007"
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
        "challenger_ls3w228_007",
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
      "cwd": "units/LS3W228-007",
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
      "cwd": "units/LS3W228-007",
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
      "cwd": "units/LS3W228-007",
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
      "cwd": "units/LS3W228-007",
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
      "cwd": "units/LS3W228-007",
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
      "cwd": "units/LS3W228-007",
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

<a id="ls3w228-009"></a>
## LS3W228-009

Accumulate audit inference elapsed milliseconds saturating at u128

元のtask_id: `LS3W228-009`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn total_audit_elapsed_ms(records: &[ncos_core::AuditRecord]) -> u128. Saturating-sum usage.elapsed_ms over every row, including rows without events/executions. Empty returns zero; never narrow to u64 or wrap.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-009 --output work/LS3W228-009
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-d433823350dccd](#r-d433823350dccd) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-6cb61fcd54ea7a](#r-6cb61fcd54ea7a) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-b0c3df5b32fb55](#r-b0c3df5b32fb55) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-1cfe0d2bd9cf04](#r-1cfe0d2bd9cf04) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-454f4d87d6b36f](#r-454f4d87d6b36f) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-6490cb10964a22](#r-6490cb10964a22) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-69d134f19734eb](#r-69d134f19734eb) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-89948b1a098db1](#r-89948b1a098db1) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-a76534af17cc30](#r-a76534af17cc30) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-d433823350dccd"></a>
### 根拠 R-d433823350dccd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/4`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-6cb61fcd54ea7a"></a>
### 根拠 R-6cb61fcd54ea7a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/16`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-b0c3df5b32fb55"></a>
### 根拠 R-b0c3df5b32fb55

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/28`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-1cfe0d2bd9cf04"></a>
### 根拠 R-1cfe0d2bd9cf04

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/4/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-454f4d87d6b36f"></a>
### 根拠 R-454f4d87d6b36f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/4/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-6490cb10964a22"></a>
### 根拠 R-6490cb10964a22

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/4/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-69d134f19734eb"></a>
### 根拠 R-69d134f19734eb

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/4/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-89948b1a098db1"></a>
### 根拠 R-89948b1a098db1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/4/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-a76534af17cc30"></a>
### 根拠 R-a76534af17cc30

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/4/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn total_audit_elapsed_ms(records: &[ncos_core::AuditRecord]) -> u128.",
    "Saturating-sum usage.elapsed_ms over every row, including rows without events/executions. Empty returns zero; never narrow to u64 or wrap.",
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
      "criterion_text": "Preserve exact signature: pub fn total_audit_elapsed_ms(records: &[ncos_core::AuditRecord]) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Saturating-sum usage.elapsed_ms over every row, including rows without events/executions. Empty returns zero; never narrow to u64 or wrap.",
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
      "cwd": "units/LS3W228-009",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_009"
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
        "challenger_ls3w228_009",
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
      "cwd": "units/LS3W228-009",
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
      "cwd": "units/LS3W228-009",
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
      "cwd": "units/LS3W228-009",
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
      "cwd": "units/LS3W228-009",
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
      "cwd": "units/LS3W228-009",
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
      "cwd": "units/LS3W228-009",
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

<a id="ls3w228-011"></a>
## LS3W228-011

Accumulate byte size of intent constraint strings

元のtask_id: `LS3W228-011`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn constraint_byte_total(intent: &ncos_core::Intent) -> usize. Saturating-sum UTF-8 byte lengths of all constraint strings, including duplicates and whitespace. Do not trim, count characters or use number of constraints.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-011 --output work/LS3W228-011
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-b8199a9d5346aa](#r-b8199a9d5346aa) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-b8ef6bb323dfe9](#r-b8ef6bb323dfe9) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-551ff4eac1a5aa](#r-551ff4eac1a5aa) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-507e18d2086a59](#r-507e18d2086a59) |
| コードの検証 | arms_condition=A2 | — | — | — | — | REJECT | — | [R-9606086982a770](#r-9606086982a770) |
| コードの検証 | arms_condition=D | — | — | — | — | REJECT | — | [R-d581a946367c4b](#r-d581a946367c4b) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-e074bfa46c866a](#r-e074bfa46c866a) |
| コードの検証 | arms_condition=E | — | — | — | — | REJECT | — | [R-2b5e2a3bffe926](#r-2b5e2a3bffe926) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-6c2b7913a3ff1f](#r-6c2b7913a3ff1f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b8199a9d5346aa"></a>
### 根拠 R-b8199a9d5346aa

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/5`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-b8ef6bb323dfe9"></a>
### 根拠 R-b8ef6bb323dfe9

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/17`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-551ff4eac1a5aa"></a>
### 根拠 R-551ff4eac1a5aa

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/29`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-507e18d2086a59"></a>
### 根拠 R-507e18d2086a59

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/5/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-9606086982a770"></a>
### 根拠 R-9606086982a770

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/5/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-d581a946367c4b"></a>
### 根拠 R-d581a946367c4b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/5/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-e074bfa46c866a"></a>
### 根拠 R-e074bfa46c866a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/5/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-2b5e2a3bffe926"></a>
### 根拠 R-2b5e2a3bffe926

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/5/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-6c2b7913a3ff1f"></a>
### 根拠 R-6c2b7913a3ff1f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/5/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn constraint_byte_total(intent: &ncos_core::Intent) -> usize.",
    "Saturating-sum UTF-8 byte lengths of all constraint strings, including duplicates and whitespace. Do not trim, count characters or use number of constraints.",
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
      "criterion_text": "Preserve exact signature: pub fn constraint_byte_total(intent: &ncos_core::Intent) -> usize.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Saturating-sum UTF-8 byte lengths of all constraint strings, including duplicates and whitespace. Do not trim, count characters or use number of constraints.",
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
      "cwd": "units/LS3W228-011",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_011"
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
        "challenger_ls3w228_011",
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
      "cwd": "units/LS3W228-011",
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
      "cwd": "units/LS3W228-011",
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
      "cwd": "units/LS3W228-011",
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
      "cwd": "units/LS3W228-011",
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
      "cwd": "units/LS3W228-011",
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
      "cwd": "units/LS3W228-011",
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

<a id="ls3w228-014"></a>
## LS3W228-014

Forward wide elapsed milliseconds to protected seconds conversion

元のtask_id: `LS3W228-014`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn elapsed_seconds_caption_value(record: &ncos_core::AuditRecord) -> u128. Return ls3_whole_seconds applied to record.usage.elapsed_ms. The helper preserves u128 and floors by 1000; do not duplicate arithmetic or narrow the argument.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-014 --output work/LS3W228-014
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-fb1e3e52ff6820](#r-fb1e3e52ff6820) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-c3cfa35225b4f3](#r-c3cfa35225b4f3) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-489fd000cc91cf](#r-489fd000cc91cf) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-74660c610d1add](#r-74660c610d1add) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-9547002275e621](#r-9547002275e621) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-78078a30978551](#r-78078a30978551) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-8f9c94e59e829f](#r-8f9c94e59e829f) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-5be2346b4ebc84](#r-5be2346b4ebc84) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-d8b28f46959fbd](#r-d8b28f46959fbd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fb1e3e52ff6820"></a>
### 根拠 R-fb1e3e52ff6820

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/6`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-c3cfa35225b4f3"></a>
### 根拠 R-c3cfa35225b4f3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/18`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-489fd000cc91cf"></a>
### 根拠 R-489fd000cc91cf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/30`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-74660c610d1add"></a>
### 根拠 R-74660c610d1add

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/6/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-9547002275e621"></a>
### 根拠 R-9547002275e621

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/6/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-78078a30978551"></a>
### 根拠 R-78078a30978551

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/6/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-8f9c94e59e829f"></a>
### 根拠 R-8f9c94e59e829f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/6/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-5be2346b4ebc84"></a>
### 根拠 R-5be2346b4ebc84

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/6/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-d8b28f46959fbd"></a>
### 根拠 R-d8b28f46959fbd

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/6/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn elapsed_seconds_caption_value(record: &ncos_core::AuditRecord) -> u128.",
    "Return ls3_whole_seconds applied to record.usage.elapsed_ms. The helper preserves u128 and floors by 1000; do not duplicate arithmetic or narrow the argument.",
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
      "criterion_text": "Preserve exact signature: pub fn elapsed_seconds_caption_value(record: &ncos_core::AuditRecord) -> u128.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return ls3_whole_seconds applied to record.usage.elapsed_ms. The helper preserves u128 and floors by 1000; do not duplicate arithmetic or narrow the argument.",
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
      "cwd": "units/LS3W228-014",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_014"
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
        "challenger_ls3w228_014",
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
      "cwd": "units/LS3W228-014",
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
      "cwd": "units/LS3W228-014",
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
      "cwd": "units/LS3W228-014",
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
      "cwd": "units/LS3W228-014",
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
      "cwd": "units/LS3W228-014",
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
      "cwd": "units/LS3W228-014",
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

<a id="ls3w228-015"></a>
## LS3W228-015

Delegate proposal reversibility label to protected boolean helper

元のtask_id: `LS3W228-015`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn proposal_reversibility_caption(record: &ncos_core::AuditRecord) -> String. If proposal None return owned missing. Otherwise return ls3_reversible_caption(proposal.reversible). No inline label match, no policy or risk interpretation.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-015 --output work/LS3W228-015
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-a802c5b97fbcaa](#r-a802c5b97fbcaa) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-9ff36bb3fc6ac2](#r-9ff36bb3fc6ac2) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-9695db457b1f95](#r-9695db457b1f95) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-8e23b34f654857](#r-8e23b34f654857) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-b4c71ac56d6b27](#r-b4c71ac56d6b27) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-5b93764c140085](#r-5b93764c140085) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-6dabeae242d0ea](#r-6dabeae242d0ea) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-092c8f51c34bbb](#r-092c8f51c34bbb) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-166dd6a7d162de](#r-166dd6a7d162de) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-a802c5b97fbcaa"></a>
### 根拠 R-a802c5b97fbcaa

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/7`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-9ff36bb3fc6ac2"></a>
### 根拠 R-9ff36bb3fc6ac2

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/19`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-9695db457b1f95"></a>
### 根拠 R-9695db457b1f95

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/31`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-8e23b34f654857"></a>
### 根拠 R-8e23b34f654857

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/7/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-b4c71ac56d6b27"></a>
### 根拠 R-b4c71ac56d6b27

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/7/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-5b93764c140085"></a>
### 根拠 R-5b93764c140085

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/7/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-6dabeae242d0ea"></a>
### 根拠 R-6dabeae242d0ea

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/7/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-092c8f51c34bbb"></a>
### 根拠 R-092c8f51c34bbb

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/7/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-166dd6a7d162de"></a>
### 根拠 R-166dd6a7d162de

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/7/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn proposal_reversibility_caption(record: &ncos_core::AuditRecord) -> String.",
    "If proposal None return owned missing. Otherwise return ls3_reversible_caption(proposal.reversible). No inline label match, no policy or risk interpretation.",
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
      "criterion_text": "Preserve exact signature: pub fn proposal_reversibility_caption(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "If proposal None return owned missing. Otherwise return ls3_reversible_caption(proposal.reversible). No inline label match, no policy or risk interpretation.",
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
      "cwd": "units/LS3W228-015",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_015"
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
        "challenger_ls3w228_015",
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
      "cwd": "units/LS3W228-015",
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
      "cwd": "units/LS3W228-015",
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
      "cwd": "units/LS3W228-015",
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
      "cwd": "units/LS3W228-015",
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
      "cwd": "units/LS3W228-015",
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
      "cwd": "units/LS3W228-015",
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

<a id="ls3w228-017"></a>
## LS3W228-017

Delegate observation epoch bucket to two-argument protected helper

元のtask_id: `LS3W228-017`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn observation_bucket(state: &SystemState, width: u128) -> Option<u128>. Return ls3_epoch_bucket(state.observed_unix_ms,width). Width zero returns None according to helper. Do not duplicate division or swap arguments.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-017 --output work/LS3W228-017
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-55ac6c9ef2446f](#r-55ac6c9ef2446f) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-0c0f4165f63263](#r-0c0f4165f63263) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-364b547730e030](#r-364b547730e030) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-88b80329c89419](#r-88b80329c89419) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-a27e3603af4db0](#r-a27e3603af4db0) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-2213a573a41453](#r-2213a573a41453) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-b0de389a37d2eb](#r-b0de389a37d2eb) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-26d6232d692613](#r-26d6232d692613) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-e2d24c9bb1a666](#r-e2d24c9bb1a666) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-55ac6c9ef2446f"></a>
### 根拠 R-55ac6c9ef2446f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/8`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-0c0f4165f63263"></a>
### 根拠 R-0c0f4165f63263

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/20`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-364b547730e030"></a>
### 根拠 R-364b547730e030

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/32`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-88b80329c89419"></a>
### 根拠 R-88b80329c89419

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/8/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-a27e3603af4db0"></a>
### 根拠 R-a27e3603af4db0

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/8/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-2213a573a41453"></a>
### 根拠 R-2213a573a41453

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/8/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-b0de389a37d2eb"></a>
### 根拠 R-b0de389a37d2eb

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/8/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-26d6232d692613"></a>
### 根拠 R-26d6232d692613

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/8/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-e2d24c9bb1a666"></a>
### 根拠 R-e2d24c9bb1a666

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/8/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn observation_bucket(state: &SystemState, width: u128) -> Option<u128>.",
    "Return ls3_epoch_bucket(state.observed_unix_ms,width). Width zero returns None according to helper. Do not duplicate division or swap arguments.",
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
      "criterion_text": "Preserve exact signature: pub fn observation_bucket(state: &SystemState, width: u128) -> Option<u128>.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return ls3_epoch_bucket(state.observed_unix_ms,width). Width zero returns None according to helper. Do not duplicate division or swap arguments.",
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
      "cwd": "units/LS3W228-017",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_017"
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
        "challenger_ls3w228_017",
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
      "cwd": "units/LS3W228-017",
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
      "cwd": "units/LS3W228-017",
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
      "cwd": "units/LS3W228-017",
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
      "cwd": "units/LS3W228-017",
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
      "cwd": "units/LS3W228-017",
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
      "cwd": "units/LS3W228-017",
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

<a id="ls3w228-020"></a>
## LS3W228-020

Render empty versus nonempty warning inventory receipt

元のtask_id: `LS3W228-020`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn warning_inventory_presence_receipt(state: &SystemState) -> String. Return warnings=none plus LF if warnings is empty, otherwise warnings=present plus LF. A vector containing one empty String is present. No count or trimming.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-020 --output work/LS3W228-020
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-4bc2f72b937582](#r-4bc2f72b937582) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-426f99dde7bae3](#r-426f99dde7bae3) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-973e2c976c2c14](#r-973e2c976c2c14) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-24313f82ac3e4d](#r-24313f82ac3e4d) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-3f8a11f73595d3](#r-3f8a11f73595d3) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-c5a72dda65e26f](#r-c5a72dda65e26f) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-d7681ad1bf0020](#r-d7681ad1bf0020) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-33e3ebc3739c22](#r-33e3ebc3739c22) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-d52c0ee8562244](#r-d52c0ee8562244) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-4bc2f72b937582"></a>
### 根拠 R-4bc2f72b937582

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/9`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-426f99dde7bae3"></a>
### 根拠 R-426f99dde7bae3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/21`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-973e2c976c2c14"></a>
### 根拠 R-973e2c976c2c14

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/33`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-24313f82ac3e4d"></a>
### 根拠 R-24313f82ac3e4d

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/9/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-3f8a11f73595d3"></a>
### 根拠 R-3f8a11f73595d3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/9/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-c5a72dda65e26f"></a>
### 根拠 R-c5a72dda65e26f

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/9/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-d7681ad1bf0020"></a>
### 根拠 R-d7681ad1bf0020

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/9/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-33e3ebc3739c22"></a>
### 根拠 R-33e3ebc3739c22

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/9/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-d52c0ee8562244"></a>
### 根拠 R-d52c0ee8562244

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/9/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn warning_inventory_presence_receipt(state: &SystemState) -> String.",
    "Return warnings=none plus LF if warnings is empty, otherwise warnings=present plus LF. A vector containing one empty String is present. No count or trimming.",
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
      "criterion_text": "Preserve exact signature: pub fn warning_inventory_presence_receipt(state: &SystemState) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return warnings=none plus LF if warnings is empty, otherwise warnings=present plus LF. A vector containing one empty String is present. No count or trimming.",
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
      "cwd": "units/LS3W228-020",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_020"
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
        "challenger_ls3w228_020",
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
      "cwd": "units/LS3W228-020",
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
      "cwd": "units/LS3W228-020",
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
      "cwd": "units/LS3W228-020",
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
      "cwd": "units/LS3W228-020",
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
      "cwd": "units/LS3W228-020",
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
      "cwd": "units/LS3W228-020",
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

<a id="ls3w228-021"></a>
## LS3W228-021

Render three-state event evidence presence receipt

元のtask_id: `LS3W228-021`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn event_evidence_presence_receipt(record: &ncos_core::AuditRecord) -> String. No event returns evidence=unobserved plus LF. Some event with empty evidence vector returns evidence=none plus LF. Nonempty vector returns evidence=present plus LF even if its strings are empty.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-021 --output work/LS3W228-021
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | ESCALATE | — | — | — | — | [R-5088d945b991b1](#r-5088d945b991b1) |
| ローカル実装 | arm=D | — | ESCALATE | — | — | — | — | [R-fdc11da7e9c752](#r-fdc11da7e9c752) |
| ローカル実装 | arm=E | — | ESCALATE | — | — | — | — | [R-78aedf447e4df4](#r-78aedf447e4df4) |
| コードの検証 | arms_condition=A2 | ESCALATE | — | — | — | — | — | [R-bc6a1b4af4caf1](#r-bc6a1b4af4caf1) |
| コードの検証 | arms_condition=D | ESCALATE | — | — | — | — | — | [R-91800bf834353a](#r-91800bf834353a) |
| コードの検証 | arms_condition=E | ESCALATE | — | — | — | — | — | [R-10167aa97f99e3](#r-10167aa97f99e3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-5088d945b991b1"></a>
### 根拠 R-5088d945b991b1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/10`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-fdc11da7e9c752"></a>
### 根拠 R-fdc11da7e9c752

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/22`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-78aedf447e4df4"></a>
### 根拠 R-78aedf447e4df4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/34`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-bc6a1b4af4caf1"></a>
### 根拠 R-bc6a1b4af4caf1

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/10/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-91800bf834353a"></a>
### 根拠 R-91800bf834353a

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/10/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-10167aa97f99e3"></a>
### 根拠 R-10167aa97f99e3

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/10/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn event_evidence_presence_receipt(record: &ncos_core::AuditRecord) -> String.",
    "No event returns evidence=unobserved plus LF. Some event with empty evidence vector returns evidence=none plus LF. Nonempty vector returns evidence=present plus LF even if its strings are empty.",
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
      "criterion_text": "Preserve exact signature: pub fn event_evidence_presence_receipt(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "No event returns evidence=unobserved plus LF. Some event with empty evidence vector returns evidence=none plus LF. Nonempty vector returns evidence=present plus LF even if its strings are empty.",
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
      "cwd": "units/LS3W228-021",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_021"
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
        "challenger_ls3w228_021",
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
      "cwd": "units/LS3W228-021",
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
      "cwd": "units/LS3W228-021",
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
      "cwd": "units/LS3W228-021",
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
      "cwd": "units/LS3W228-021",
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
      "cwd": "units/LS3W228-021",
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
      "cwd": "units/LS3W228-021",
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

<a id="ls3w228-023"></a>
## LS3W228-023

Render intent identity and requester byte sizes in exact receipt

元のtask_id: `LS3W228-023`。初期ファイル数: 27。

**課題・インターフェース**

Preserve existing signatures, surrounding source and all protected tests. Preserve exact signature: pub fn intent_identity_sizes_receipt(record: &ncos_core::AuditRecord) -> String. Return intent_bytes=N;requester_bytes=M plus one LF using byte lengths of intent.id and intent.requested_by. Do not include text, trim strings, use goal or count characters.

取り出し方:

```sh
python materialize_task.py --set gemma26-memory-headroom-phase2--run-001 --task LS3W228-023 --output work/LS3W228-023
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | arm=A2 | — | PASS | — | — | — | — | [R-e63a2f7f7cf969](#r-e63a2f7f7cf969) |
| ローカル実装 | arm=D | — | PASS | — | — | — | — | [R-4796a0dd9718cc](#r-4796a0dd9718cc) |
| ローカル実装 | arm=E | — | PASS | — | — | — | — | [R-294a6472846bdf](#r-294a6472846bdf) |
| コードの検証 | arms_condition=A2 | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-128c36b917601b](#r-128c36b917601b) |
| コードの検証 | arms_condition=A2 | PASS | — | — | — | — | — | [R-5b6e4763a66701](#r-5b6e4763a66701) |
| コードの検証 | arms_condition=D | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-c94612d14ee51c](#r-c94612d14ee51c) |
| コードの検証 | arms_condition=D | PASS | — | — | — | — | — | [R-ff3d7baf739750](#r-ff3d7baf739750) |
| コードの検証 | arms_condition=E | PASS | — | — | — | — | — | [R-0bcd3a1887a7c4](#r-0bcd3a1887a7c4) |
| コードの検証 | arms_condition=E | — | — | — | — | ACCEPT_NO_CHANGE | — | [R-2ccff39f126496](#r-2ccff39f126496) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e63a2f7f7cf969"></a>
### 根拠 R-e63a2f7f7cf969

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/11`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-4796a0dd9718cc"></a>
### 根拠 R-4796a0dd9718cc

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/23`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-294a6472846bdf"></a>
### 根拠 R-294a6472846bdf

- 対応方法: 同一セット・課題IDによる対応
- 出典: `run-history.json` / 位置: `/runs/35`
- 出典ファイルのSHA-256: `e2f2a7afd1522a900c6d2686ba0b70732e96ff62b389c5d819956a7bf9cce204`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-128c36b917601b"></a>
### 根拠 R-128c36b917601b

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/11/review/result`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-5b6e4763a66701"></a>
### 根拠 R-5b6e4763a66701

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/A2/run-history.json` / 位置: `/runs/11/Local`
- 出典ファイルのSHA-256: `577dbb8cf96af6e8a030d35a4eb08b611b34272a59c3bbde2bb6c80f34a008ef`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-c94612d14ee51c"></a>
### 根拠 R-c94612d14ee51c

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/11/review/result`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-ff3d7baf739750"></a>
### 根拠 R-ff3d7baf739750

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/D/run-history.json` / 位置: `/runs/11/Local`
- 出典ファイルのSHA-256: `e9bdd81394de85edc3e6d711e2dd07f626c4768bcc43126f21c3764486871c24`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-0bcd3a1887a7c4"></a>
### 根拠 R-0bcd3a1887a7c4

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/11/Local`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<a id="r-2ccff39f126496"></a>
### 根拠 R-2ccff39f126496

- 対応方法: 同一セット・課題IDによる対応
- 出典: `arms/E/run-history.json` / 位置: `/runs/11/review/result`
- 出典ファイルのSHA-256: `a3f9637312e78b12fc7bcd36989e0d958d23cb0d2591fd17f35de03cfbfafa5b`
- [抽出した測定値・他の工程の記録](../results/gemma26-memory-headroom-phase2--run-001.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    "Preserve exact signature: pub fn intent_identity_sizes_receipt(record: &ncos_core::AuditRecord) -> String.",
    "Return intent_bytes=N;requester_bytes=M plus one LF using byte lengths of intent.id and intent.requested_by. Do not include text, trim strings, use goal or count characters.",
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
      "criterion_text": "Preserve exact signature: pub fn intent_identity_sizes_receipt(record: &ncos_core::AuditRecord) -> String.",
      "category": "functional"
    },
    {
      "criterion_id": "BEHAVIOR-2",
      "criterion_text": "Return intent_bytes=N;requester_bytes=M plus one LF using byte lengths of intent.id and intent.requested_by. Do not include text, trim strings, use goal or count characters.",
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
      "cwd": "units/LS3W228-023",
      "timeout_seconds": 330,
      "required_test_ids": [
        "challenger_ls3w228_023"
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
        "challenger_ls3w228_023",
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
      "cwd": "units/LS3W228-023",
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
      "cwd": "units/LS3W228-023",
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
      "cwd": "units/LS3W228-023",
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
      "cwd": "units/LS3W228-023",
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
      "cwd": "units/LS3W228-023",
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
      "cwd": "units/LS3W228-023",
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
