"""Use Consensus Engine for a real decision."""
from consensus_engine import Consensus

c = Consensus()

questions = [
    "Should I price my SaaS at $19 or $39 to maximize first-year revenue?",
    "Postgres vs SQLite for a 100k-user SaaS in 2026?",
    "Best vector database for 1M embeddings under $50/month?",
]

for q in questions:
    r = c.ask(q, max_models=5)
    print(f"\nQ: {q}")
    print(f"   confidence: {r.confidence}")
    print(f"   {r.consensus[:200]}...")
