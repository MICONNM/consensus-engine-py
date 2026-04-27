"""Consensus Engine Python client — single-file, urllib only."""
import json
import urllib.request
import urllib.error
from dataclasses import dataclass
from typing import List, Optional

DEFAULT_API = "https://api.yanmiayn.com"


@dataclass
class ConsensusResult:
    """Result from Consensus Engine."""
    consensus: str
    confidence: float
    models_responded: int
    models_total: int
    elapsed_ms: int
    votes: List[dict]
    share_url: Optional[str] = None
    question: Optional[str] = None

    @property
    def divergences(self) -> List[dict]:
        """Models that responded but with notably different answers."""
        return [v for v in self.votes if v.get("ok") and v.get("answer_preview")]


class Consensus:
    """Client for Consensus Engine API.

    Examples:
        >>> c = Consensus()  # uses public demo (10/day per IP)
        >>> r = c.ask("Should I learn Rust or Go in 2026?")
        >>> print(r.consensus)
    """

    def __init__(self, api_key: Optional[str] = None, base_url: str = DEFAULT_API):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def ask(self, question: str, max_models: int = 7, timeout: int = 180) -> ConsensusResult:
        """Ask the consensus engine.

        Args:
            question: Your question (5-500 chars).
            max_models: How many of the 11 models to poll (3-11).
            timeout: Seconds to wait.

        Returns:
            ConsensusResult with synthesized answer + confidence.
        """
        endpoint = "/v1/consensus" if self.api_key else "/v1/public"
        payload = json.dumps({"question": question, "max_models": max_models}).encode()
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["X-API-Key"] = self.api_key

        req = urllib.request.Request(
            self.base_url + endpoint, data=payload, headers=headers, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            raise RuntimeError(f"HTTP {e.code}: {body[:300]}")

        return ConsensusResult(
            consensus=data.get("consensus", ""),
            confidence=data.get("confidence", 0.0),
            models_responded=data.get("models_responded", 0),
            models_total=data.get("models_total", 0),
            elapsed_ms=data.get("elapsed_ms", 0),
            votes=data.get("votes", []),
            share_url=data.get("share_url"),
            question=data.get("question") or question,
        )


def main():
    """CLI entry point."""
    import sys
    if len(sys.argv) < 2:
        print("Usage: consensus-engine '<your question>'")
        sys.exit(1)
    q = " ".join(sys.argv[1:])
    c = Consensus()
    r = c.ask(q)
    print(f"\n=== {r.models_responded}/{r.models_total} models · confidence {r.confidence} ===\n")
    print(r.consensus)
    if r.share_url:
        print(f"\nShare: {r.share_url}")


if __name__ == "__main__":
    main()
