import csv
import json
from pathlib import Path
from .config import settings

class KnowledgeBase:
    def __init__(self, root: Path | None = None):
        self.root = Path(root or settings.knowledge_dir)
        self.baseline = self._json("oem_baseline_21DE.json")
        self.observations = self._json("unit_observations.json", {"observations":[]})
        self.parts = self._csv("oem_parts_core_21DE.csv")

    def _json(self, name: str, default=None):
        path = self.root / name
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else (default or {})

    def _csv(self, name: str):
        path = self.root / name
        if not path.exists():
            return []
        with path.open(encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    def part(self, part_number: str):
        needle = part_number.strip().upper()
        return [row for row in self.parts if row.get("part_number","").upper() == needle]

    def search(self, query: str, limit: int = 20):
        terms = [term for term in query.lower().split() if len(term) > 2]
        ranked = []
        for row in self.parts:
            haystack = " ".join(str(value) for value in row.values()).lower()
            score = sum(1 for term in terms if term in haystack)
            if score:
                ranked.append((score, row))
        ranked.sort(key=lambda item: item[0], reverse=True)
        return [row for _, row in ranked[:limit]]

    def context(self, query: str):
        return {
            "identity": self.baseline.get("identity", {}),
            "baseline": self.baseline,
            "parts": self.search(query, 12),
            "unit_observations": self.observations.get("observations", []),
        }
