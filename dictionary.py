from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from pathlib import Path


@dataclass()
class Dictionary:
    words: List[str] = field(default_factory=list, repr=False)

    @classmethod
    def from_text_file(cls, filename: Path) -> Dictionary:
        words = filename.read_text().splitlines()
        return cls(words=words)

    def __contains__(self, word: str) -> bool:
        return word in self.words
