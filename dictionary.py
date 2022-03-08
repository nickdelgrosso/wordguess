from __future__ import annotations
from dataclasses import dataclass, field
import random
from typing import List, Optional
from pathlib import Path

@dataclass()
class Dictionary:
    words: List[str] = field(default_factory=list, repr=False)

    @classmethod
    def from_text_file(cls, filename: str | Path) -> Dictionary:
        words = Path(filename).read_text().splitlines()
        return cls(words=words)

    def __contains__(self, word: str) -> bool:
        return word in self.words

    def get_random(self, seed: Optional[int] = None) -> str:
        if seed is not None:
            random.seed(seed)
        word = random.choice(self.words)
        return word
