"""Basic example."""
from consensus_engine import Consensus

c = Consensus()
r = c.ask("Should I learn Rust or Go in 2026 for backend development?")

print(f"Confidence: {r.confidence}")
print(f"Models: {r.models_responded}/{r.models_total}")
print()
print(r.consensus)
print()
print(f"Share: {r.share_url}")
