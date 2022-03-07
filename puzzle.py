from __future__ import annotations
from dataclasses import dataclass, field
from multiprocessing.sharedctypes import Value
from typing import List, Tuple, Iterable
from enum  import Enum, auto


class HintType(Enum):
    CORRECT = auto()
    WRONG_PLACE = auto()
    NOT_PRESENT = auto()


@dataclass(frozen=True)
class Puzzle:
    solution: str
    hints: List[str] = field(default_factory=list)

    def add_hint(self, word: str):
        assert len(word) == len(self.solution)
        self.hints.append(word)

    def guess(self, guess: str) -> bool:
        return guess == self.solution

    def get_hint(self, word: str) -> str:
        for hint in self.hints:
            if str(hint) == word:
                return hint
        else:
            raise ValueError(f"{word} not found in hints")

    def check(self, word: str) -> Iterable[Tuple[str, HintType]]:
        for idx, letter in enumerate(word):
            if letter == self.solution[idx]:
                yield letter, HintType.CORRECT
            elif letter in self.solution:
                yield letter, HintType.WRONG_PLACE
            else:
                yield letter, HintType.NOT_PRESENT
