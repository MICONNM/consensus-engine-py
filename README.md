# Consensus Engine Python Client

[![PyPI](https://img.shields.io/badge/api-yanmiayn.com-blue)](https://api.yanmiayn.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Query **11 frontier LLMs in parallel** and get **one synthesized answer with confidence score**.

```python
from consensus_engine import Consensus

c = Consensus()  # uses public demo (10 questions/day per IP)
result = c.ask("Should I price my SaaS at $19 or $39 to maximize first-year revenue?")

print(result.consensus)        # synthesized answer
print(result.confidence)       # 0.0 - 1.0
print(result.divergences)      # where models disagreed
print(result.share_url)        # shareable result page
```

## What it does

POST a question, 11 frontier AI models reply in parallel, a synthesizer (Llama 4) merges them with a confidence score and notes where models disagreed.

**Models polled:**
- DeepSeek V4 Pro (1.6T MoE flagship)
- Llama 4 Maverick (Meta MoE)
- Mistral Large 3 (675B dense)
- Qwen 3.5 (397B MoE)
- Qwen3-Coder (480B coding specialist)
- Llama 3.1 (405B dense)
- Nemotron Ultra (253B NVIDIA flagship)
- GLM-5.1 (Z.AI)
- Kimi K2.5 (Moonshot)
- MiniMax M2.7 (agentic specialist)
- + Llama 4 synthesizer

**Stack:** Hetzner CX22 VPS · NVIDIA NIM free tier · FastAPI · Cloudflare Tunnel

## Why?

1 AI = 1 opinion = bias. 11 AIs = signal vs noise.

The most useful output isn't always the consensus — **it's the divergence map** (where models disagreed). That's harder to fake with a single LLM.

## Install

```bash
pip install consensus-engine
```

Or copy `consensus_engine.py` directly — single file, no deps beyond `urllib`.

## Usage

### Free public demo (no signup)

```python
from consensus_engine import Consensus

c = Consensus()
r = c.ask("Postgres or SQLite for a 100k-user SaaS?")
print(r.consensus)
```

10 questions/day per IP. For unlimited, get a beta key at https://api.yanmiayn.com.

### With API key

```python
c = Consensus(api_key="ck_beta_xxx")
r = c.ask("Should I learn Rust or Go in 2026 for backend?", max_models=11)
```

## CLI

```bash
$ consensus-engine "Best vector database for 1M embeddings under $50/mo?"
```

## Curl

```bash
curl -X POST https://api.yanmiayn.com/v1/public \
  -H "Content-Type: application/json" \
  -d '{"question": "Should I use Bun or Node.js in production in 2026?"}'
```

## Live demo

https://api.yanmiayn.com/demo — try it without signup.

## License

MIT. Use freely. Star if useful.

## Status

Open beta. Honest about uncertainty: I don't know yet if 11-AI consensus is genuinely better than asking 1 strong model deeply. The free beta exists to find out. Most interesting output so far is when models DISAGREE.

Issues / PRs welcome.
