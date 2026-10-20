# 小規模なPython・HTML・構造化回答のモデル比較

セットID: `model-routing`

課題数: 30。個別記録あり: 30、個別記録未確認: 0。

[全セット一覧](../INDEX.md) / [課題定義JSON](model-routing.json) / [結果と根拠のJSON](../results/model-routing.json) / [判定の読み方](../README.md#判定の読み方)

各結果はこのセットの保存記録に対応します。収録外の別runの結果を新たに代入していません。SHA-256が記録されている結果は課題定義と照合し、それ以外は実行キー・ディレクトリ・同一セット内の一意のIDによる対応として表示しています。元の記録が過去の工程を再利用している場合、独立した再実行の結果とは扱わないでください。

| 課題ID | 内容 | 個別記録 |
| --- | --- | --- |
| [AGENTIC_CODING-01](#agentic_coding-01) | Batch report loses trailing items. Include full and final partial batches; size <=0 raises ValueError even if input empty. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [AGENTIC_CODING-02](#agentic_coding-02) | Report picks lowest score, ties use earliest input occurrence; empty input returns None; no mutation. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [AGENTIC_CODING-03](#agentic_coding-03) | Report histogram uses mathematical floor buckets, supports negative/large integers, width>0; invalid width raises even for empty input. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [BOUNDED_LOGIC-01](#bounded_logic-01) | Convert a money string to cents: trim outer whitespace; ASCII digits with optional leading minus and 1 or 2 decimal digits. Reject plus, exponent, comma, missing integer, trailing dot, >2 decimals or empty. No floating point. | 記録あり |
| [BOUNDED_LOGIC-02](#bounded_logic-02) | Normalize tags by strip then casefold, discard empty strings, deduplicate preserving first occurrence. Never mutate input. | 記録あり |
| [BOUNDED_LOGIC-03](#bounded_logic-03) | Parse exactly ASCII YYYY-MM-DD into canonical ISO date. Calendar dates must exist; reject whitespace, unpadded digits and non-ASCII digits with ValueError. | 記録あり |
| [DEBUGGING-01](#debugging-01) | Mean incorrectly truncates fractions and does not implement empty-input ValueError. Identify cause briefly in summary and add a regression unittest that fails on original implementation. | 記録あり |
| [DEBUGGING-02](#debugging-02) | Window should return count items from start, truncating at the list end; negative arguments raise ValueError. Identify cause briefly in summary and add a regression unittest that fails on original implementation. | 記録あり |
| [DEBUGGING-03](#debugging-03) | First present means first value which is not None; false/zero/empty string are present. Identify cause briefly in summary and add a regression unittest that fails on original implementation. | 記録あり |
| [ERROR_ANALYSIS-01](#error_analysis-01) | Analyze this synthetic evidence only: pytest: test_retry_limit failed: assert attempts == 3; got 4. Trace: client.py:51 while attempts <= max_attempts; max_attempts=3, attempts initially0, increment after request. Transport succeeded each time. | 記録あり |
| [ERROR_ANALYSIS-02](#error_analysis-02) | Analyze this synthetic evidence only: test_import FAILED before collection: ModuleNotFoundError: No module named 'widgetlib'. pip show widgetlib: Package(s) not found. requirements.txt lists widgetlib==1.2.0. No application function executed. | 記録あり |
| [ERROR_ANALYSIS-03](#error_analysis-03) | Analyze this synthetic evidence only: pytest test_price: expected 1230 cents, actual 1200. Trace price.py: return int(float(text))*100; input '12.30'. No network or DB activity. The public contract requires exact decimal cents. | 記録あり |
| [MECHANICAL_CODE-01](#mechanical_code-01) | Format nonnegative integer seconds as unbounded hours:MM:SS (hours at least two digits). Reject negative values with ValueError. | 記録あり |
| [MECHANICAL_CODE-02](#mechanical_code-02) | Map input rows to dictionaries with id and name only, preserving order; missing/None name becomes empty string. Never mutate input. | 記録あり |
| [MECHANICAL_CODE-03](#mechanical_code-03) | Return compact JSON of a mapping, with lexically sorted keys, Unicode preserved, and no whitespace outside strings. | 記録あり |
| [REPO_EDIT-01](#repo_edit-01) | Count distinct exact strings in report; preserve case distinctions. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [REPO_EDIT-02](#repo_edit-02) | Report keeps rows at or after cutoff, including equality; no mutation. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [REPO_EDIT-03](#repo_edit-03) | Report uses unknown for absent, None or empty name. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair. | 記録あり |
| [SPECIFICATION-01](#specification-01) | For normalize_tags(tags), strip then casefold, remove blanks and duplicates preserving first occurrence. No input mutation, dependencies or network. Implement only subject.py, <=80 changed LOC. Write acceptance cases for [], [' A ', 'a', 'B'], ['Straße', 'STRASSE']. | 記録あり |
| [SPECIFICATION-02](#specification-02) | For page(items, index, size), index is ZERO based. Slice starting at index*size, truncate at end; index<0 or size<=0 raises ValueError, including empty inputs. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases: [[1,2,3],0,2], [[1,2,3],1,2], [[],0,2], [[],0,0]. | 記録あり |
| [SPECIFICATION-03](#specification-03) | For expires(now, deadline), expiration begins at equality (now>=deadline). Integers only by contract; no runtime type validation. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases [9,10], [10,10], [11,10], [-2,-1]. | 記録あり |
| [SPECIFICATION-04](#specification-04) | For normalize_tags(tags), strip then casefold, remove blanks and duplicates preserving first occurrence. No input mutation, dependencies or network. Implement only subject.py, <=80 changed LOC. Write acceptance cases for [], [' A ', 'a', 'B'], ['Straße', 'STRASSE']. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels. | 記録あり |
| [SPECIFICATION-05](#specification-05) | For page(items, index, size), index is ZERO based. Slice starting at index*size, truncate at end; index<0 or size<=0 raises ValueError, including empty inputs. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases: [[1,2,3],0,2], [[1,2,3],1,2], [[],0,2], [[],0,0]. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels. | 記録あり |
| [SPECIFICATION-06](#specification-06) | For expires(now, deadline), expiration begins at equality (now>=deadline). Integers only by contract; no runtime type validation. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases [9,10], [10,10], [11,10], [-2,-1]. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels. | 記録あり |
| [TEMPLATE_UI-01](#template_ui-01) | Render a form with POST method; label for=email, required input id=email name=email type=email, submit button text Subscribe. No scripts/external resources. | 記録あり |
| [TEMPLATE_UI-02](#template_ui-02) | Render semantic table with caption Inventory, headers Item and Qty using th scope=col; body row Pen / 3; no scripts/external resources. | 記録あり |
| [TEMPLATE_UI-03](#template_ui-03) | Render pagination nav aria-label=Pagination with span aria-current=page text 2, link href=?page=1 text Previous, link href=?page=3 text Next. No scripts/external resources. | 記録あり |
| [UNIT_TEST_GENERATION-01](#unit_test_generation-01) | Write unittest methods covering ALL supplied acceptance cases for clamp. Tests must pass on correct implementation and detect behavior regressions. | 記録あり |
| [UNIT_TEST_GENERATION-02](#unit_test_generation-02) | Write unittest methods covering ALL supplied acceptance cases for unique. Tests must pass on correct implementation and detect behavior regressions. | 記録あり |
| [UNIT_TEST_GENERATION-03](#unit_test_generation-03) | Write unittest methods covering ALL supplied acceptance cases for divide. Tests must pass on correct implementation and detect behavior regressions. | 記録あり |

<a id="agentic_coding-01"></a>
## AGENTIC_CODING-01

Batch report loses trailing items. Include full and final partial batches; size <=0 raises ValueError even if input empty. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `AGENTIC_CODING-01`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def split_batches(items: list[int], size: int) -> list[list[int]]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task AGENTIC_CODING-01 --output work/AGENTIC_CODING-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-8252131bc3e82c](#r-8252131bc3e82c) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-319441cb1b6024](#r-319441cb1b6024) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-cff808c9faf023](#r-cff808c9faf023) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8252131bc3e82c"></a>
### 根拠 R-8252131bc3e82c

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/AGENTIC_CODING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `83a1c9e7cdc8720c4aa513212a2016a54dd9a3e1844bc5270d2a10afff4558be`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-319441cb1b6024"></a>
### 根拠 R-319441cb1b6024

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/AGENTIC_CODING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1888e164850388a4d191a35c295844645b9a4985925c9171c8de8ffeb901917a`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-cff808c9faf023"></a>
### 根拠 R-cff808c9faf023

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/AGENTIC_CODING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `74802600d3a53baeccd0c56b04a41c09cd527bf02b1debd23df41b815ebb7e4e`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          1,
          2,
          3,
          4,
          5
        ],
        2
      ],
      "expected": [
        [
          1,
          2
        ],
        [
          3,
          4
        ],
        [
          5
        ]
      ]
    },
    {
      "args": [
        [
          1,
          2
        ],
        2
      ],
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "args": [
        [],
        2
      ],
      "expected": []
    },
    {
      "args": [
        [
          1
        ],
        0
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        [],
        -1
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="agentic_coding-02"></a>
## AGENTIC_CODING-02

Report picks lowest score, ties use earliest input occurrence; empty input returns None; no mutation. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `AGENTIC_CODING-02`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def pick_min(rows: list[dict]) -> dict | None:

取り出し方:

```sh
python materialize_task.py --set model-routing --task AGENTIC_CODING-02 --output work/AGENTIC_CODING-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-0d4469566ccd00](#r-0d4469566ccd00) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-401c3154ab8348](#r-401c3154ab8348) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-3871f173e98d73](#r-3871f173e98d73) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0d4469566ccd00"></a>
### 根拠 R-0d4469566ccd00

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/AGENTIC_CODING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `543bf115e594c909df6cbee607c7a13c676df56bb8f23161cbf24291ca93c81b`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-401c3154ab8348"></a>
### 根拠 R-401c3154ab8348

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/AGENTIC_CODING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `6d2e9d12d1dcb523d804dbcad32a4147289734a36abec7f0153acd135f2a44f2`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-3871f173e98d73"></a>
### 根拠 R-3871f173e98d73

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/AGENTIC_CODING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7e77e960d7465ed387c8184ef79a85c27148658847e2185f4cf50a1a5d63983a`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        []
      ],
      "expected": null
    },
    {
      "args": [
        [
          {
            "id": "z",
            "score": 1
          },
          {
            "id": "a",
            "score": 1
          }
        ]
      ],
      "expected": {
        "id": "z",
        "score": 1
      }
    },
    {
      "args": [
        [
          {
            "id": "a",
            "score": 2
          },
          {
            "id": "b",
            "score": 1
          }
        ]
      ],
      "expected": {
        "id": "b",
        "score": 1
      }
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="agentic_coding-03"></a>
## AGENTIC_CODING-03

Report histogram uses mathematical floor buckets, supports negative/large integers, width>0; invalid width raises even for empty input. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `AGENTIC_CODING-03`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def bucket_counts(values: list[int], width: int) -> dict[int, int]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task AGENTIC_CODING-03 --output work/AGENTIC_CODING-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-0d7a153ee92f8a](#r-0d7a153ee92f8a) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-bd0504d4ee5f4e](#r-bd0504d4ee5f4e) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-1f68ee8266ebb5](#r-1f68ee8266ebb5) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0d7a153ee92f8a"></a>
### 根拠 R-0d7a153ee92f8a

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/AGENTIC_CODING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bea6519c2bd25fdad000607c513326e28b777c7ffe20dbdb2a2320034bdacee3`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-bd0504d4ee5f4e"></a>
### 根拠 R-bd0504d4ee5f4e

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/AGENTIC_CODING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `591ce5ad3ed9f22a4d5618436b01ef6a6e0a91684139fe3c2a974abb76e744cd`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-1f68ee8266ebb5"></a>
### 根拠 R-1f68ee8266ebb5

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/AGENTIC_CODING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4d4e58b0937b27e3cfdd60247cbac5d05a22cdf91f834b6bb9af7e62a922894b`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          -1,
          0,
          9,
          10
        ],
        10
      ],
      "expected": {
        "-1": 1,
        "0": 2,
        "1": 1
      }
    },
    {
      "args": [
        [],
        2
      ],
      "expected": {}
    },
    {
      "args": [
        [],
        0
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        [
          100000000000000000001
        ],
        10
      ],
      "expected": {
        "10000000000000000000": 1
      }
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="bounded_logic-01"></a>
## BOUNDED_LOGIC-01

Convert a money string to cents: trim outer whitespace; ASCII digits with optional leading minus and 1 or 2 decimal digits. Reject plus, exponent, comma, missing integer, trailing dot, >2 decimals or empty. No floating point.

元のtask_id: `BOUNDED_LOGIC-01`。初期ファイル数: 1。

**課題・インターフェース**

def cents(text: str) -> int:

取り出し方:

```sh
python materialize_task.py --set model-routing --task BOUNDED_LOGIC-01 --output work/BOUNDED_LOGIC-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-b4c932cced6b92](#r-b4c932cced6b92) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-e2ef092a2453c8](#r-e2ef092a2453c8) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | FAIL | FAIL | — | — | — | — | [R-8b10272702320a](#r-8b10272702320a) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b4c932cced6b92"></a>
### 根拠 R-b4c932cced6b92

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/BOUNDED_LOGIC-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `e94f481922c1a73aace223b72a48fca705dd3f93c9ce55c9d26874aa335c2242`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-e2ef092a2453c8"></a>
### 根拠 R-e2ef092a2453c8

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/BOUNDED_LOGIC-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `22ae9531f49f26598a2ed7d11dff3213bb873e571ac2022a4704cd0d804dd444`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-8b10272702320a"></a>
### 根拠 R-8b10272702320a

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/BOUNDED_LOGIC-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `cae2443cc5c028f5bac8210c2c5b2f1f5f5fcb176d266ab5f2a1d7c90c2d3436`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        " 12.3 "
      ],
      "expected": 1230
    },
    {
      "args": [
        "-0.01"
      ],
      "expected": -1
    },
    {
      "args": [
        "001"
      ],
      "expected": 100
    },
    {
      "args": [
        "0"
      ],
      "expected": 0
    },
    {
      "args": [
        "+1"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "1e2"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "1.234"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "1."
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        ".1"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        ""
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "1,2"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "１２"
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="bounded_logic-02"></a>
## BOUNDED_LOGIC-02

Normalize tags by strip then casefold, discard empty strings, deduplicate preserving first occurrence. Never mutate input.

元のtask_id: `BOUNDED_LOGIC-02`。初期ファイル数: 1。

**課題・インターフェース**

def normalize_tags(tags: list[str]) -> list[str]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task BOUNDED_LOGIC-02 --output work/BOUNDED_LOGIC-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | FAIL | FAIL | — | — | — | — | [R-84420b56c20a98](#r-84420b56c20a98) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-74134be36667b6](#r-74134be36667b6) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-0807e9c8274ab0](#r-0807e9c8274ab0) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-84420b56c20a98"></a>
### 根拠 R-84420b56c20a98

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/BOUNDED_LOGIC-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `648f8a082eecf1307232c29ac5dec08e10eb55fcb1b06d755e231949f832f4de`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-74134be36667b6"></a>
### 根拠 R-74134be36667b6

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/BOUNDED_LOGIC-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `88555829ccc81666808c7a529440fa92644249bc6e63180a9a9a1e06653961be`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-0807e9c8274ab0"></a>
### 根拠 R-0807e9c8274ab0

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/BOUNDED_LOGIC-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `0571b1e10e0a3b6656785c7a07a7b70034e8e25b4e635fb2c735c182a6c91a87`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        []
      ],
      "expected": []
    },
    {
      "args": [
        [
          " A ",
          "a",
          "",
          "  ",
          "B"
        ]
      ],
      "expected": [
        "a",
        "b"
      ]
    },
    {
      "args": [
        [
          "Straße",
          "STRASSE",
          "猫"
        ]
      ],
      "expected": [
        "strasse",
        "猫"
      ]
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="bounded_logic-03"></a>
## BOUNDED_LOGIC-03

Parse exactly ASCII YYYY-MM-DD into canonical ISO date. Calendar dates must exist; reject whitespace, unpadded digits and non-ASCII digits with ValueError.

元のtask_id: `BOUNDED_LOGIC-03`。初期ファイル数: 1。

**課題・インターフェース**

def iso_date(text: str) -> str:

取り出し方:

```sh
python materialize_task.py --set model-routing --task BOUNDED_LOGIC-03 --output work/BOUNDED_LOGIC-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-37a5694fe3531b](#r-37a5694fe3531b) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-4210d72a148a8f](#r-4210d72a148a8f) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | FAIL | FAIL | — | — | — | — | [R-f09cdbb3ce2b24](#r-f09cdbb3ce2b24) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-37a5694fe3531b"></a>
### 根拠 R-37a5694fe3531b

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/BOUNDED_LOGIC-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `01079e487f429262e1cfbff4039600524ea6f9739b4539f88f0796250c24ab33`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-4210d72a148a8f"></a>
### 根拠 R-4210d72a148a8f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/BOUNDED_LOGIC-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b730c9e62130fa90d96d7af9a5897f0fc2a07802ef995c11202be68457d49161`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-f09cdbb3ce2b24"></a>
### 根拠 R-f09cdbb3ce2b24

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/BOUNDED_LOGIC-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4bf35b766516b9476aa621cb40b8749530784a6b7e742d569b35576068c38f9f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        "2024-02-29"
      ],
      "expected": "2024-02-29"
    },
    {
      "args": [
        "2000-02-29"
      ],
      "expected": "2000-02-29"
    },
    {
      "args": [
        "1900-02-29"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "2023-02-29"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "2024-2-09"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        " 2024-01-01"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "2024-13-01"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "２０２４-01-01"
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        "0000-01-01"
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="debugging-01"></a>
## DEBUGGING-01

Mean incorrectly truncates fractions and does not implement empty-input ValueError. Identify cause briefly in summary and add a regression unittest that fails on original implementation.

元のtask_id: `DEBUGGING-01`。初期ファイル数: 2。

**課題・インターフェース**

def mean(values: list[float]) -> float:

取り出し方:

```sh
python materialize_task.py --set model-routing --task DEBUGGING-01 --output work/DEBUGGING-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | FAIL | FAIL | — | — | — | — | [R-8d119b749b0cbc](#r-8d119b749b0cbc) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-6595566003dbfd](#r-6595566003dbfd) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-d4cd52424b8933](#r-d4cd52424b8933) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8d119b749b0cbc"></a>
### 根拠 R-8d119b749b0cbc

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/DEBUGGING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `fec06afbcb28a93f6c049664bb451e4b4cae7473c515d3725843bc26cff9581a`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-6595566003dbfd"></a>
### 根拠 R-6595566003dbfd

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/DEBUGGING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `6c68dfdf1b54581c48af50b4cea183a297343bf878b8c1b80486b6f355ee98b6`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-d4cd52424b8933"></a>
### 根拠 R-d4cd52424b8933

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/DEBUGGING-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b26d81f1e71334960cc0d6d2de449a10bc8ecf5f7288a37a5bf107d3215876ba`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          1,
          2
        ]
      ],
      "expected": 1.5
    },
    {
      "args": [
        []
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        [
          -1,
          0
        ]
      ],
      "expected": -0.5
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="debugging-02"></a>
## DEBUGGING-02

Window should return count items from start, truncating at the list end; negative arguments raise ValueError. Identify cause briefly in summary and add a regression unittest that fails on original implementation.

元のtask_id: `DEBUGGING-02`。初期ファイル数: 2。

**課題・インターフェース**

def window(values: list[int], start: int, count: int) -> list[int]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task DEBUGGING-02 --output work/DEBUGGING-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-fb90ccdf67b238](#r-fb90ccdf67b238) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-96a0d30d27d593](#r-96a0d30d27d593) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-531ad032d1ff9b](#r-531ad032d1ff9b) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-fb90ccdf67b238"></a>
### 根拠 R-fb90ccdf67b238

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/DEBUGGING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f8d8e3b0af4ba5e082a461759ec4e96fe52f3be472ea6d0be3f3bc96e8d2a03f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-96a0d30d27d593"></a>
### 根拠 R-96a0d30d27d593

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/DEBUGGING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `0edf60bf864257c5e66eacdac928a341b13864cf15ac713c53197ff9e49da3bb`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-531ad032d1ff9b"></a>
### 根拠 R-531ad032d1ff9b

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/DEBUGGING-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `705262de3fbe642040ed452d5c2569c8091702a745eed5b472b80f2ea2d08bb6`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          0,
          1,
          2,
          3,
          4
        ],
        2,
        2
      ],
      "expected": [
        2,
        3
      ]
    },
    {
      "args": [
        [
          1
        ],
        0,
        0
      ],
      "expected": []
    },
    {
      "args": [
        [
          1
        ],
        4,
        3
      ],
      "expected": []
    },
    {
      "args": [
        [
          1
        ],
        -1,
        2
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="debugging-03"></a>
## DEBUGGING-03

First present means first value which is not None; false/zero/empty string are present. Identify cause briefly in summary and add a regression unittest that fails on original implementation.

元のtask_id: `DEBUGGING-03`。初期ファイル数: 2。

**課題・インターフェース**

def first_present(values: list) -> object:

取り出し方:

```sh
python materialize_task.py --set model-routing --task DEBUGGING-03 --output work/DEBUGGING-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | FAIL | FAIL | — | — | — | — | [R-587fcff19563ec](#r-587fcff19563ec) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-e32b148324c152](#r-e32b148324c152) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-69dfb87742edbc](#r-69dfb87742edbc) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-587fcff19563ec"></a>
### 根拠 R-587fcff19563ec

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/DEBUGGING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bae1b1ee9a16bf54375f4df000b48b0211f2e5713ba94754ad2bcbdedc28083a`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-e32b148324c152"></a>
### 根拠 R-e32b148324c152

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/DEBUGGING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `96428760792b2f38a7cf28c6f3b4adc1733404e1c2a825156c70b50d10f2d659`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-69dfb87742edbc"></a>
### 根拠 R-69dfb87742edbc

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/DEBUGGING-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f35e303b61432a21b6ab0a23baf7d1023bd4767be422045efd4d00b8c61f8747`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          null,
          0,
          2
        ]
      ],
      "expected": 0
    },
    {
      "args": [
        [
          null,
          false,
          2
        ]
      ],
      "expected": false
    },
    {
      "args": [
        [
          null,
          "",
          2
        ]
      ],
      "expected": ""
    },
    {
      "args": [
        [
          null
        ]
      ],
      "expected": null
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="error_analysis-01"></a>
## ERROR_ANALYSIS-01

Analyze this synthetic evidence only: pytest: test_retry_limit failed: assert attempts == 3; got 4. Trace: client.py:51 while attempts <= max_attempts; max_attempts=3, attempts initially0, increment after request. Transport succeeded each time.

元のtask_id: `ERROR_ANALYSIS-01`。初期ファイル数: 0。

**課題・インターフェース**

Structured diagnosis

取り出し方:

```sh
python materialize_task.py --set model-routing --task ERROR_ANALYSIS-01 --output work/ERROR_ANALYSIS-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-9749a2bc19ed41](#r-9749a2bc19ed41) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-6b15567afa4a0f](#r-6b15567afa4a0f) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-b3ada26137daeb](#r-b3ada26137daeb) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-9749a2bc19ed41"></a>
### 根拠 R-9749a2bc19ed41

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/ERROR_ANALYSIS-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `983f991893a6470753cd9da5635efc40c413b36ab5d795cdff11af2c596480f0`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-6b15567afa4a0f"></a>
### 根拠 R-6b15567afa4a0f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/ERROR_ANALYSIS-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bc4a3b911fd597af31f9caa883a13bed508caa42bf0ca2511af74a0f5f13b8ff`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-b3ada26137daeb"></a>
### 根拠 R-b3ada26137daeb

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/ERROR_ANALYSIS-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `d0e3d60458a3344f1007c8bcf592234eeb01b8dca75f547777cff2be03e00c98`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="error_analysis-02"></a>
## ERROR_ANALYSIS-02

Analyze this synthetic evidence only: test_import FAILED before collection: ModuleNotFoundError: No module named 'widgetlib'. pip show widgetlib: Package(s) not found. requirements.txt lists widgetlib==1.2.0. No application function executed.

元のtask_id: `ERROR_ANALYSIS-02`。初期ファイル数: 0。

**課題・インターフェース**

Structured diagnosis

取り出し方:

```sh
python materialize_task.py --set model-routing --task ERROR_ANALYSIS-02 --output work/ERROR_ANALYSIS-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-ffc4b01f96f5a4](#r-ffc4b01f96f5a4) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-d78166f1a75ee2](#r-d78166f1a75ee2) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-1b680fb18adf28](#r-1b680fb18adf28) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-ffc4b01f96f5a4"></a>
### 根拠 R-ffc4b01f96f5a4

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/ERROR_ANALYSIS-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4b71f207d6bbaceb129ef5af6b68bd7a702e45f1060eb10d4012ba559db516f3`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-d78166f1a75ee2"></a>
### 根拠 R-d78166f1a75ee2

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/ERROR_ANALYSIS-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `6ae8a309e2daf6e7bbcbfb6306aba7d3e22609f9fb2170701fea356062f0c163`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-1b680fb18adf28"></a>
### 根拠 R-1b680fb18adf28

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/ERROR_ANALYSIS-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b67122538f67c7fc57d3a15249ce7ed8e56e7791f83fcd992441522e17ad9ae2`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="error_analysis-03"></a>
## ERROR_ANALYSIS-03

Analyze this synthetic evidence only: pytest test_price: expected 1230 cents, actual 1200. Trace price.py: return int(float(text))*100; input '12.30'. No network or DB activity. The public contract requires exact decimal cents.

元のtask_id: `ERROR_ANALYSIS-03`。初期ファイル数: 0。

**課題・インターフェース**

Structured diagnosis

取り出し方:

```sh
python materialize_task.py --set model-routing --task ERROR_ANALYSIS-03 --output work/ERROR_ANALYSIS-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-b1cb965c553535](#r-b1cb965c553535) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-31bb87a3122167](#r-31bb87a3122167) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-09c95ce7c2c1d8](#r-09c95ce7c2c1d8) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-b1cb965c553535"></a>
### 根拠 R-b1cb965c553535

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/ERROR_ANALYSIS-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `68a3640fdefa51424eeef808509352eea52c92974bc95ad1a5e47ee46fff6fae`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-31bb87a3122167"></a>
### 根拠 R-31bb87a3122167

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/ERROR_ANALYSIS-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `238d4b77dfaa944eb9568a815d8773d10cd559692780005e601a2cf2370eef19`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-09c95ce7c2c1d8"></a>
### 根拠 R-09c95ce7c2c1d8

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/ERROR_ANALYSIS-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b29cdd6ac0da9dc45a62a9bd8026a6fbe51b6fe4176baea94d3f0fd603dd6f77`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="mechanical_code-01"></a>
## MECHANICAL_CODE-01

Format nonnegative integer seconds as unbounded hours:MM:SS (hours at least two digits). Reject negative values with ValueError.

元のtask_id: `MECHANICAL_CODE-01`。初期ファイル数: 1。

**課題・インターフェース**

def format_duration(seconds: int) -> str:

取り出し方:

```sh
python materialize_task.py --set model-routing --task MECHANICAL_CODE-01 --output work/MECHANICAL_CODE-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-17c8f4b1c11493](#r-17c8f4b1c11493) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-32607c09927c7a](#r-32607c09927c7a) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-ad2c5b72dd08d3](#r-ad2c5b72dd08d3) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-17c8f4b1c11493"></a>
### 根拠 R-17c8f4b1c11493

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/MECHANICAL_CODE-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `9b653540537fc13da980cb33a9aac07f257f77e961b2b83bc30a0a61b2af6d0f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-32607c09927c7a"></a>
### 根拠 R-32607c09927c7a

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/MECHANICAL_CODE-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `6f7955378fa4dc2aab393c66c725fd7d7b76c4a17a88f63bc861499b906cec9c`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-ad2c5b72dd08d3"></a>
### 根拠 R-ad2c5b72dd08d3

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/MECHANICAL_CODE-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7bd069f225447a153317e36ae4f660d6b5ac1bea1cad662351a4eab1caf8173b`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        0
      ],
      "expected": "00:00:00"
    },
    {
      "args": [
        59
      ],
      "expected": "00:00:59"
    },
    {
      "args": [
        3661
      ],
      "expected": "01:01:01"
    },
    {
      "args": [
        360000
      ],
      "expected": "100:00:00"
    },
    {
      "args": [
        -1
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="mechanical_code-02"></a>
## MECHANICAL_CODE-02

Map input rows to dictionaries with id and name only, preserving order; missing/None name becomes empty string. Never mutate input.

元のtask_id: `MECHANICAL_CODE-02`。初期ファイル数: 1。

**課題・インターフェース**

def map_rows(rows: list[dict]) -> list[dict]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task MECHANICAL_CODE-02 --output work/MECHANICAL_CODE-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-776c7cb0beca26](#r-776c7cb0beca26) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-3f4b2ac133a4d6](#r-3f4b2ac133a4d6) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-b398d340b5bf1f](#r-b398d340b5bf1f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-776c7cb0beca26"></a>
### 根拠 R-776c7cb0beca26

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/MECHANICAL_CODE-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `d39f59c530680582047ca699d66709bcdf8097d0167f4c201cf4409489bd0c2b`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-3f4b2ac133a4d6"></a>
### 根拠 R-3f4b2ac133a4d6

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/MECHANICAL_CODE-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1ad7738724460b7c141840cb394bf6ec9388b85bd6c4dc56a44957cfc058f3bc`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-b398d340b5bf1f"></a>
### 根拠 R-b398d340b5bf1f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/MECHANICAL_CODE-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `145f7e76c1d34e3a66ad04e8370149d34fba3ab017428073003f5a3dfa8a52c1`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        []
      ],
      "expected": []
    },
    {
      "args": [
        [
          {
            "id": 1,
            "name": "A",
            "extra": 4
          },
          {
            "id": 2
          },
          {
            "id": 3,
            "name": null
          }
        ]
      ],
      "expected": [
        {
          "id": 1,
          "name": "A"
        },
        {
          "id": 2,
          "name": ""
        },
        {
          "id": 3,
          "name": ""
        }
      ]
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="mechanical_code-03"></a>
## MECHANICAL_CODE-03

Return compact JSON of a mapping, with lexically sorted keys, Unicode preserved, and no whitespace outside strings.

元のtask_id: `MECHANICAL_CODE-03`。初期ファイル数: 1。

**課題・インターフェース**

def compact_json(value: dict) -> str:

取り出し方:

```sh
python materialize_task.py --set model-routing --task MECHANICAL_CODE-03 --output work/MECHANICAL_CODE-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-0dc73abe10165a](#r-0dc73abe10165a) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-7348a5a8a438eb](#r-7348a5a8a438eb) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-cac4e4be11eb1f](#r-cac4e4be11eb1f) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-0dc73abe10165a"></a>
### 根拠 R-0dc73abe10165a

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/MECHANICAL_CODE-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `2ad58fd3222b2e7d2e89fed96ba3df54c64a70237bbc844d270f134b113aad6b`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-7348a5a8a438eb"></a>
### 根拠 R-7348a5a8a438eb

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/MECHANICAL_CODE-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `61943a6c168e1fc77a80abb2573ce064c3e9638232ec324c7d2af2fbd566ee74`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-cac4e4be11eb1f"></a>
### 根拠 R-cac4e4be11eb1f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/MECHANICAL_CODE-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f76e24f3e14972ad669bf2cc0f7cd92b2eecaab05255635dc9809003c41802f2`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        {}
      ],
      "expected": "{}"
    },
    {
      "args": [
        {
          "z": 2,
          "a": "日本"
        }
      ],
      "expected": "{\"a\":\"日本\",\"z\":2}"
    },
    {
      "args": [
        {
          "b": [
            true,
            null
          ],
          "a": "a b"
        }
      ],
      "expected": "{\"a\":\"a b\",\"b\":[true,null]}"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="repo_edit-01"></a>
## REPO_EDIT-01

Count distinct exact strings in report; preserve case distinctions. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `REPO_EDIT-01`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def distinct_count(values: list[str]) -> int:

取り出し方:

```sh
python materialize_task.py --set model-routing --task REPO_EDIT-01 --output work/REPO_EDIT-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-91f0f0b7252fdc](#r-91f0f0b7252fdc) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-c9e76ae1ae84a4](#r-c9e76ae1ae84a4) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-b30468aa2da9d1](#r-b30468aa2da9d1) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-91f0f0b7252fdc"></a>
### 根拠 R-91f0f0b7252fdc

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/REPO_EDIT-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8e59bc8601e57ace5ea335d1f5c930f0a8453c1c3e55edef65f35b6757969234`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-c9e76ae1ae84a4"></a>
### 根拠 R-c9e76ae1ae84a4

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/REPO_EDIT-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1775b21f55c5bf9a055fb710a8390d5bd45cacb169a2572887eb53c56568d48c`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-b30468aa2da9d1"></a>
### 根拠 R-b30468aa2da9d1

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/REPO_EDIT-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `41edf681d64a42d997cf25570798dc86e49cc34abadddf7f4c3e6a20cc2d7a0c`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          "a",
          "a",
          "b"
        ]
      ],
      "expected": 2
    },
    {
      "args": [
        []
      ],
      "expected": 0
    },
    {
      "args": [
        [
          "A",
          "a"
        ]
      ],
      "expected": 2
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="repo_edit-02"></a>
## REPO_EDIT-02

Report keeps rows at or after cutoff, including equality; no mutation. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `REPO_EDIT-02`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def retain_recent(rows: list[dict], cutoff: int) -> list[dict]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task REPO_EDIT-02 --output work/REPO_EDIT-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-1bed3efe9922cc](#r-1bed3efe9922cc) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-605871bb4b1d1a](#r-605871bb4b1d1a) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-b9f035d34d6c37](#r-b9f035d34d6c37) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-1bed3efe9922cc"></a>
### 根拠 R-1bed3efe9922cc

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/REPO_EDIT-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7f1cc0190ea6f5c4b9fc0c1ce82da405c3dec0ca3fdc24afe08ac19567a76fdb`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-605871bb4b1d1a"></a>
### 根拠 R-605871bb4b1d1a

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/REPO_EDIT-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `83ff40d44267636689a05a4027f113fbf41e301239e18394d8eb5e53051c0ee3`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-b9f035d34d6c37"></a>
### 根拠 R-b9f035d34d6c37

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/REPO_EDIT-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b8eb6b194d9fb156a5add45f24d93b750dfe1c7bcd812837ee59fa6c0df9f148`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        [
          {
            "time": 3
          },
          {
            "time": 4
          },
          {
            "time": 5
          }
        ],
        4
      ],
      "expected": [
        {
          "time": 4
        },
        {
          "time": 5
        }
      ]
    },
    {
      "args": [
        [],
        4
      ],
      "expected": []
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="repo_edit-03"></a>
## REPO_EDIT-03

Report uses unknown for absent, None or empty name. Locate the implementation using search and read tools, edit minimally, then run targeted tests. Use raw failures for at most one repair.

元のtask_id: `REPO_EDIT-03`。初期ファイル数: 4。

**課題・インターフェース**

report.report(*args); underlying def display_name(row: dict) -> str:

取り出し方:

```sh
python materialize_task.py --set model-routing --task REPO_EDIT-03 --output work/REPO_EDIT-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-e93157c93ed5df](#r-e93157c93ed5df) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-ba8eb100a3bbf1](#r-ba8eb100a3bbf1) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-87f71b8c958f68](#r-87f71b8c958f68) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e93157c93ed5df"></a>
### 根拠 R-e93157c93ed5df

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/REPO_EDIT-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8be794bfd1ec70afcfafeab1439a049968317149969b70dc000c78b22653152c`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-ba8eb100a3bbf1"></a>
### 根拠 R-ba8eb100a3bbf1

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/REPO_EDIT-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `4d1659c24261feb2d7b64b3eaaaf1130579cab483037b31de81f56e154030077`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-87f71b8c958f68"></a>
### 根拠 R-87f71b8c958f68

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/REPO_EDIT-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `61a5ca711889fead9b27f13811b23c96f558a2b2b4d9f52cfb1e69e40062edf5`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        {}
      ],
      "expected": "unknown"
    },
    {
      "args": [
        {
          "name": null
        }
      ],
      "expected": "unknown"
    },
    {
      "args": [
        {
          "name": ""
        }
      ],
      "expected": "unknown"
    },
    {
      "args": [
        {
          "name": "Ada"
        }
      ],
      "expected": "Ada"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-01"></a>
## SPECIFICATION-01

For normalize_tags(tags), strip then casefold, remove blanks and duplicates preserving first occurrence. No input mutation, dependencies or network. Implement only subject.py, <=80 changed LOC. Write acceptance cases for [], [' A ', 'a', 'B'], ['Straße', 'STRASSE'].

元のtask_id: `SPECIFICATION-01`。初期ファイル数: 0。

**課題・インターフェース**

normalize_tags(tags)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-01 --output work/SPECIFICATION-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-db48c890b3d346](#r-db48c890b3d346) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-92f89ae583c93d](#r-92f89ae583c93d) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-c3b16255a61080](#r-c3b16255a61080) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-db48c890b3d346"></a>
### 根拠 R-db48c890b3d346

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `3054f54286ffd24da827e976567819656d1a1ea054f026039d1038609bb43bea`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-92f89ae583c93d"></a>
### 根拠 R-92f89ae583c93d

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7cb0b43ade2c794712e0bd41fb7c07736e2a15eb3f3972d6780db13de8f66f64`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-c3b16255a61080"></a>
### 根拠 R-c3b16255a61080

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `da4b7e93064e579d03a709496904188c7beb473d2859a2f8d33440823a9589b7`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-02"></a>
## SPECIFICATION-02

For page(items, index, size), index is ZERO based. Slice starting at index*size, truncate at end; index<0 or size<=0 raises ValueError, including empty inputs. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases: [[1,2,3],0,2], [[1,2,3],1,2], [[],0,2], [[],0,0].

元のtask_id: `SPECIFICATION-02`。初期ファイル数: 0。

**課題・インターフェース**

page(items, index, size)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-02 --output work/SPECIFICATION-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-dbbaf2992460ff](#r-dbbaf2992460ff) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-062cc34b1732d2](#r-062cc34b1732d2) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-0efc165854817e](#r-0efc165854817e) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-dbbaf2992460ff"></a>
### 根拠 R-dbbaf2992460ff

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `7764012e1c624244a2cd783a71cf0996fda70ec5ba568cc7984dfc5bac2a491a`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-062cc34b1732d2"></a>
### 根拠 R-062cc34b1732d2

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b1e270b8227d6f2ef14f2aff84baeaa101da6bb76720ca63fadd6675cbeaf31f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-0efc165854817e"></a>
### 根拠 R-0efc165854817e

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `ad05b2223409acee45ca0326936e688f99b7c58b5adb9006b156a18469f63a42`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-03"></a>
## SPECIFICATION-03

For expires(now, deadline), expiration begins at equality (now>=deadline). Integers only by contract; no runtime type validation. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases [9,10], [10,10], [11,10], [-2,-1].

元のtask_id: `SPECIFICATION-03`。初期ファイル数: 0。

**課題・インターフェース**

expires(now, deadline)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-03 --output work/SPECIFICATION-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-dda9314e49729d](#r-dda9314e49729d) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-b9994af66f0403](#r-b9994af66f0403) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-bd913cf038a720](#r-bd913cf038a720) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-dda9314e49729d"></a>
### 根拠 R-dda9314e49729d

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `c9e6529cc8354eb14dde9ddf70cc671ae75145df874e3c8e9589d5c54af974b3`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-b9994af66f0403"></a>
### 根拠 R-b9994af66f0403

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `390cbe9cf89a0e6885e11b7e326699c226a4ecf2a0be47a45912d1bebdef34f0`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-bd913cf038a720"></a>
### 根拠 R-bd913cf038a720

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `857d4a5ccdfc086d451b53f5247715f37610aacbab540318ba2ee68eed251d5f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-04"></a>
## SPECIFICATION-04

For normalize_tags(tags), strip then casefold, remove blanks and duplicates preserving first occurrence. No input mutation, dependencies or network. Implement only subject.py, <=80 changed LOC. Write acceptance cases for [], [' A ', 'a', 'B'], ['Straße', 'STRASSE']. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels.

元のtask_id: `SPECIFICATION-04`。初期ファイル数: 0。

**課題・インターフェース**

normalize_tags(tags)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-04 --output work/SPECIFICATION-04
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-e8f6139128de1f](#r-e8f6139128de1f) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | FAIL | FAIL | — | — | — | — | [R-e22b0a08ee62e2](#r-e22b0a08ee62e2) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-8add2102fbb558](#r-8add2102fbb558) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e8f6139128de1f"></a>
### 根拠 R-e8f6139128de1f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-04/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8cfcbe121750241d730bfd8038d8a766f3f20563f2b7ad4b6286ab2b7725118e`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-e22b0a08ee62e2"></a>
### 根拠 R-e22b0a08ee62e2

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-04/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8c0eec782ae7ac441b00882ae12a095a864df6ed4ee29be77191f623baee75a5`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-8add2102fbb558"></a>
### 根拠 R-8add2102fbb558

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-04/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `73f193b095ba90eadc2e94657695cc824787d8618c9515a09c2fc3885767c959`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-05"></a>
## SPECIFICATION-05

For page(items, index, size), index is ZERO based. Slice starting at index*size, truncate at end; index<0 or size<=0 raises ValueError, including empty inputs. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases: [[1,2,3],0,2], [[1,2,3],1,2], [[],0,2], [[],0,0]. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels.

元のtask_id: `SPECIFICATION-05`。初期ファイル数: 0。

**課題・インターフェース**

page(items, index, size)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-05 --output work/SPECIFICATION-05
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-549b108ed8bbc3](#r-549b108ed8bbc3) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-0744444836c399](#r-0744444836c399) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-4b5940860f98ca](#r-4b5940860f98ca) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-549b108ed8bbc3"></a>
### 根拠 R-549b108ed8bbc3

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-05/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `86a6dc5b2f38c4dafd2ba94ea1ffc60ad07c1c295ac4ebe53f39d5cd370efc75`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-0744444836c399"></a>
### 根拠 R-0744444836c399

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-05/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `15195e06c5ad6d30b047e318375b66c98b5927a4e02e572b2ae0bcb11bb06f85`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-4b5940860f98ca"></a>
### 根拠 R-4b5940860f98ca

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-05/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `76893746a0a60b49faa0ae304d80825e37b4421dae6b0abe3d25e8c27a856a32`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="specification-06"></a>
## SPECIFICATION-06

For expires(now, deadline), expiration begins at equality (now>=deadline). Integers only by contract; no runtime type validation. No mutation, dependencies or network. subject.py only, <=80 LOC. Cases [9,10], [10,10], [11,10], [-2,-1]. This is specification extraction for a FUTURE implementation, not permission to edit now. task_specification.allowed_files describes that future implementation in the request, NOT this extraction task's empty editable-file list. Extract ONLY domain constraints stated in the request, NOT general worker/system rules. Acceptance input and expected values must be actual JSON values, never JSON encoded into strings. Use the canonical vocabulary declared in answer_contract; do not invent synonymous labels.

元のtask_id: `SPECIFICATION-06`。初期ファイル数: 0。

**課題・インターフェース**

expires(now, deadline)

取り出し方:

```sh
python materialize_task.py --set model-routing --task SPECIFICATION-06 --output work/SPECIFICATION-06
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-63e84933e20def](#r-63e84933e20def) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-c5c8271259cd86](#r-c5c8271259cd86) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-31e61358ecad05](#r-31e61358ecad05) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-63e84933e20def"></a>
### 根拠 R-63e84933e20def

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/SPECIFICATION-06/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `a6a73bf49d46e90c4f835a411f875418e9226b43706fcaa6551652b507bf1486`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-c5c8271259cd86"></a>
### 根拠 R-c5c8271259cd86

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/SPECIFICATION-06/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `fc4dad2973c131fe2f0ac26cc882403d4f176f2ec99261dd411877df1d4459df`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-31e61358ecad05"></a>
### 根拠 R-31e61358ecad05

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/SPECIFICATION-06/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `0e8b9bfef8e37cfa1efe0e22ae2e794a4132dae6b1bff3b4f2ad109377a9a500`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="template_ui-01"></a>
## TEMPLATE_UI-01

Render a form with POST method; label for=email, required input id=email name=email type=email, submit button text Subscribe. No scripts/external resources.

元のtask_id: `TEMPLATE_UI-01`。初期ファイル数: 1。

**課題・インターフェース**

HTML fragment in content region

取り出し方:

```sh
python materialize_task.py --set model-routing --task TEMPLATE_UI-01 --output work/TEMPLATE_UI-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-8d9dfa889fc37e](#r-8d9dfa889fc37e) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-2671c9f2f343f3](#r-2671c9f2f343f3) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-d756ecb83c5927](#r-d756ecb83c5927) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-8d9dfa889fc37e"></a>
### 根拠 R-8d9dfa889fc37e

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/TEMPLATE_UI-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b5969b95a347165140563bf0c349116fbbf802b1a10fd6b9c4d7c40abfffe1a9`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-2671c9f2f343f3"></a>
### 根拠 R-2671c9f2f343f3

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/TEMPLATE_UI-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `bd89bba11a0f5f74cfa3eb1d1f80d99bc9318c39e7a2ead207b025ddbb5ef257`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-d756ecb83c5927"></a>
### 根拠 R-d756ecb83c5927

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/TEMPLATE_UI-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8d1619db1540ef99346b512baab4fbc3193e385ab062ea257b73dd254f68b579`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "tag": "form",
      "attrs": {
        "method": "post"
      }
    },
    {
      "tag": "label",
      "attrs": {
        "for": "email"
      }
    },
    {
      "tag": "input",
      "attrs": {
        "id": "email",
        "name": "email",
        "type": "email",
        "required": null
      }
    },
    {
      "tag": "button",
      "attrs": {
        "type": "submit"
      },
      "text": "Subscribe"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="template_ui-02"></a>
## TEMPLATE_UI-02

Render semantic table with caption Inventory, headers Item and Qty using th scope=col; body row Pen / 3; no scripts/external resources.

元のtask_id: `TEMPLATE_UI-02`。初期ファイル数: 1。

**課題・インターフェース**

HTML fragment in content region

取り出し方:

```sh
python materialize_task.py --set model-routing --task TEMPLATE_UI-02 --output work/TEMPLATE_UI-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-792054e8d7fb34](#r-792054e8d7fb34) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-0083d466ec7f94](#r-0083d466ec7f94) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-617221cffe18c9](#r-617221cffe18c9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-792054e8d7fb34"></a>
### 根拠 R-792054e8d7fb34

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/TEMPLATE_UI-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `f152b186368f42a1472effb25898bdb51591afc1cd03e2937ec36d3c4057877c`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-0083d466ec7f94"></a>
### 根拠 R-0083d466ec7f94

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/TEMPLATE_UI-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `92267fd124631297332b7f9f5dc1c1107f283a6395c9b5246449c2447fc03477`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-617221cffe18c9"></a>
### 根拠 R-617221cffe18c9

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/TEMPLATE_UI-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `47995c6e790be9208d3d7658bfb6e392b8758076ceb2f24f5af297481aa4188d`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "tag": "caption",
      "text": "Inventory"
    },
    {
      "tag": "th",
      "attrs": {
        "scope": "col"
      },
      "text": "Item"
    },
    {
      "tag": "th",
      "attrs": {
        "scope": "col"
      },
      "text": "Qty"
    },
    {
      "tag": "td",
      "text": "Pen"
    },
    {
      "tag": "td",
      "text": "3"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="template_ui-03"></a>
## TEMPLATE_UI-03

Render pagination nav aria-label=Pagination with span aria-current=page text 2, link href=?page=1 text Previous, link href=?page=3 text Next. No scripts/external resources.

元のtask_id: `TEMPLATE_UI-03`。初期ファイル数: 1。

**課題・インターフェース**

HTML fragment in content region

取り出し方:

```sh
python materialize_task.py --set model-routing --task TEMPLATE_UI-03 --output work/TEMPLATE_UI-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-e8c0831c1d6207](#r-e8c0831c1d6207) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-9ed830848be743](#r-9ed830848be743) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | PASS | PASS | — | — | — | — | [R-7bc633f7d165ba](#r-7bc633f7d165ba) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-e8c0831c1d6207"></a>
### 根拠 R-e8c0831c1d6207

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/TEMPLATE_UI-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `2f1e84c3bcc75a7690cdd7e158f1a91452837b2c74cae3eb8d8e9697c0a0d698`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-9ed830848be743"></a>
### 根拠 R-9ed830848be743

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/TEMPLATE_UI-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `8a62a76feaecc23bf0a97871ab653c3bc908e0a867d2fb8503a2e39c406c2187`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-7bc633f7d165ba"></a>
### 根拠 R-7bc633f7d165ba

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/TEMPLATE_UI-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `36d08cd162ed6148d457af183efb8e7e7bbc362207a655be18b2bc13919c11ff`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "tag": "nav",
      "attrs": {
        "aria-label": "Pagination"
      }
    },
    {
      "tag": "span",
      "attrs": {
        "aria-current": "page"
      },
      "text": "2"
    },
    {
      "tag": "a",
      "attrs": {
        "href": "?page=1"
      },
      "text": "Previous"
    },
    {
      "tag": "a",
      "attrs": {
        "href": "?page=3"
      },
      "text": "Next"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="unit_test_generation-01"></a>
## UNIT_TEST_GENERATION-01

Write unittest methods covering ALL supplied acceptance cases for clamp. Tests must pass on correct implementation and detect behavior regressions.

元のtask_id: `UNIT_TEST_GENERATION-01`。初期ファイル数: 2。

**課題・インターフェース**

def clamp(value: int, low: int, high: int) -> int:

取り出し方:

```sh
python materialize_task.py --set model-routing --task UNIT_TEST_GENERATION-01 --output work/UNIT_TEST_GENERATION-01
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-147db257ab079e](#r-147db257ab079e) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-0099a374b723ec](#r-0099a374b723ec) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | FAIL | FAIL | — | — | — | — | [R-789c8b37931de9](#r-789c8b37931de9) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-147db257ab079e"></a>
### 根拠 R-147db257ab079e

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/UNIT_TEST_GENERATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `41b2ff52f670377fbc8a7b4f0aaf7a19d6a822364265edab44931f864b91c0a5`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-0099a374b723ec"></a>
### 根拠 R-0099a374b723ec

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/UNIT_TEST_GENERATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `b8dcd2d555be4fcc141712a0cdc64e8d9574f5ed916def53c6c0d2bea226bc34`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-789c8b37931de9"></a>
### 根拠 R-789c8b37931de9

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/UNIT_TEST_GENERATION-01/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `95bcb6ad6ac19a64dc15ef787e7add7a857712fdc85d899a00bf1fe8c60528e0`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        -2,
        0,
        5
      ],
      "expected": 0
    },
    {
      "args": [
        9,
        0,
        5
      ],
      "expected": 5
    },
    {
      "args": [
        3,
        0,
        5
      ],
      "expected": 3
    },
    {
      "args": [
        2,
        2,
        2
      ],
      "expected": 2
    },
    {
      "args": [
        0,
        5,
        2
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="unit_test_generation-02"></a>
## UNIT_TEST_GENERATION-02

Write unittest methods covering ALL supplied acceptance cases for unique. Tests must pass on correct implementation and detect behavior regressions.

元のtask_id: `UNIT_TEST_GENERATION-02`。初期ファイル数: 2。

**課題・インターフェース**

def unique(values: list[int]) -> list[int]:

取り出し方:

```sh
python materialize_task.py --set model-routing --task UNIT_TEST_GENERATION-02 --output work/UNIT_TEST_GENERATION-02
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-00ce4ffba541e6](#r-00ce4ffba541e6) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-43ac187768f3b0](#r-43ac187768f3b0) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | FAIL | FAIL | — | — | — | — | [R-fd8350fe40f9cf](#r-fd8350fe40f9cf) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-00ce4ffba541e6"></a>
### 根拠 R-00ce4ffba541e6

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/UNIT_TEST_GENERATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `2968d4be2fb84ba040681c0b9d7ccc2de4009be7885b2388765327e482ed3188`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-43ac187768f3b0"></a>
### 根拠 R-43ac187768f3b0

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/UNIT_TEST_GENERATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `1071afce0565a2dfdb6e1f9f3b888961528876efa6eeb60d0de970e07256a7da`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-fd8350fe40f9cf"></a>
### 根拠 R-fd8350fe40f9cf

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/UNIT_TEST_GENERATION-02/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `99d1cf2a5d9690982c0e8ae1b7caae763779e0eb17b1b74074a9ea94a3d88d6f`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        []
      ],
      "expected": []
    },
    {
      "args": [
        [
          3,
          1,
          3,
          2
        ]
      ],
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "args": [
        [
          1,
          1,
          1
        ]
      ],
      "expected": [
        1
      ]
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>

<a id="unit_test_generation-03"></a>
## UNIT_TEST_GENERATION-03

Write unittest methods covering ALL supplied acceptance cases for divide. Tests must pass on correct implementation and detect behavior regressions.

元のtask_id: `UNIT_TEST_GENERATION-03`。初期ファイル数: 2。

**課題・インターフェース**

def divide_up(n: int, d: int) -> int:

取り出し方:

```sh
python materialize_task.py --set model-routing --task UNIT_TEST_GENERATION-03 --output work/UNIT_TEST_GENERATION-03
```

**条件別の結果**

代表記録は工程ごとに、課題別集計 → 実行履歴 → 個別結果の順で選んでいます。残りの同一課題の記録も結果JSONに保持しています。

| 工程 | 条件・モデル | 実行状態 | Local実装 | 最終品質 | 検証PASS | レビュー | Local採用 | 根拠 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ローカル実装 | results_condition=gemma4-26b / model=gemma4:26b | PASS | PASS | — | — | — | — | [R-48bf823037ec3f](#r-48bf823037ec3f) |
| ローカル実装 | results_condition=qwen2-5-coder-14b / model=qwen2.5-Coder:14b | PASS | PASS | — | — | — | — | [R-337f4c44d0a8be](#r-337f4c44d0a8be) |
| ローカル実装 | results_condition=qwen3-coder-next-latest / model=qwen3-coder-next:latest | FAIL | FAIL | — | — | — | — | [R-302569f9d146bd](#r-302569f9d146bd) |

`—` は、その項目の値がこの記録にないことを表します。Local採用のfalseは、Codexだけを使う対照条件ではLocal処理がないことも含みます。

<a id="r-48bf823037ec3f"></a>
### 根拠 R-48bf823037ec3f

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/gemma4-26b/UNIT_TEST_GENERATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `cab7e414de9765a97c79542ca3033dc018c76c32a1ecb158e5a45da29ab6a4d9`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-337f4c44d0a8be"></a>
### 根拠 R-337f4c44d0a8be

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen2-5-coder-14b/UNIT_TEST_GENERATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `0048a316769132e9b11f29c18b2e4f6ae4ba1617d266eabd770075930cef5160`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<a id="r-302569f9d146bd"></a>
### 根拠 R-302569f9d146bd

- 対応方法: 課題定義のSHA-256一致
- 出典: `results/qwen3-coder-next-latest/UNIT_TEST_GENERATION-03/result.json` / 位置: `/`
- 出典ファイルのSHA-256: `fe9d2d73f4b0e9a544b0a176cb731b431f2b3c327d2070bc17eaf1101240a1d4`
- [抽出した測定値・他の工程の記録](../results/model-routing.json)

<details>
<summary>受入条件・検証コマンド</summary>

```json
{
  "acceptance_cases": [
    {
      "args": [
        0,
        3
      ],
      "expected": 0
    },
    {
      "args": [
        6,
        3
      ],
      "expected": 2
    },
    {
      "args": [
        7,
        3
      ],
      "expected": 3
    },
    {
      "args": [
        -1,
        3
      ],
      "raises": "ValueError"
    },
    {
      "args": [
        1,
        0
      ],
      "raises": "ValueError"
    }
  ],
  "acceptance_criteria": null,
  "checks": []
}
```

</details>
