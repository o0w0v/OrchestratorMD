# Orchestrator Local 0.1.0 — Windows preview

**Ask your usual chat to organize a table or total up a list, using an AI running on your own PC to share the work.**

Give it a CSV of orders or transaction details, explain what you need, and receive the resulting table and a short report as files.

**[日本語の導入手順・使い方](README_JA.md)**

## Why use it?

For example, ask: “Total these transactions by customer and save a CSV,” or “Use these orders and stock figures to list what we can supply and what is short.” Clarify the rules in the conversation, then request changes such as “Add this column” or “Change this sentence in the report.”

- **Hand over routine table work.** Ask the AI to group, total, classify or organize your data using the rules you provide.
- **Receive files you can use.** Open the saved results later instead of rebuilding a table from a chat response.
- **Change only what you need.** Keep the useful parts, ask for specific edits and retain the earlier files.
- **Put your PC's AI to work.** Continue using your familiar chat while an AI on your computer shares some of the work.

This is aimed at people who already run a local AI and repeatedly organize similar CSV/JSON data. Sharing work with the PC is intended to reduce work done in the cloud; any cost or speed benefit depends on the task and hardware.

## Before installing

This is a source release for Windows users who already have Python 3.11+ and a working Ollama installation with `gemma4:26b`. Model weights, Ollama, Python, user configuration, job data and credentials are not included. This is not a one-click installer or a reviewed plugin-directory listing. macOS/Linux and other machines have not been acceptance tested.

The model creates candidates only. The conversation checks them against the original request, accepts usable output, or patches errors that affect use. It does not regenerate results to improve style. Files and SQLite jobs survive MCP reconnects; failed or interrupted generations are not retried automatically.

The local service talks only to a configured loopback Ollama endpoint. Inputs and candidates are also returned to the conversation for review, so this is not an entirely offline workflow. Conversation usage is not measured by this application, and cost savings are not guaranteed.

See [validation and scope](VALIDATION.md), [the design](DESIGN_JA.md), and the repository [license](LICENSE).
