from dataclasses import dataclass, field
from typing import List

english_words = ["python", "great", "peach", "fleck"]

@dataclass()
class Dictionary:
    words: List[str] = field(default_factory=lambda: english_words)

    def word_exists(self, word: str) -> bool:
        return word in self.words