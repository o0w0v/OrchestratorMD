# Orchestrator Local 0.1.0 — Windows preview

Create CSV/JSON work products with a local Gemma model, review them in your existing ChatGPT/Codex conversation, and save the original or a precise patch. Small jobs can be completed directly in the conversation. The application does not call a separate Cloud model or require an OpenAI API key.

**[日本語の導入手順・使い方](README_JA.md)**

This is a source release for Windows users who already have Python 3.11+ and a working Ollama installation with `gemma4:26b`. Model weights, Ollama, Python, user configuration, job data and credentials are not included. This is not a one-click installer or a reviewed plugin-directory listing. macOS/Linux and other machines have not been acceptance tested.

The model creates candidates only. The conversation checks them against the original request, accepts usable output, or patches errors that affect use. It does not regenerate results to improve style. Files and SQLite jobs survive MCP reconnects; failed or interrupted generations are not retried automatically.

The local service talks only to a configured loopback Ollama endpoint. Inputs and candidates are also returned to the conversation for review, so this is not an entirely offline workflow. Conversation usage is not measured by this application, and cost savings are not guaranteed.

See [validation and scope](VALIDATION.md), [the design](DESIGN_JA.md), and the repository [license](LICENSE).
