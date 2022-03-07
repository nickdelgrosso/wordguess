from __future__ import annotations
from dataclasses import dataclass, field
import enum
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
        if len(word) != len(self.solution):
            raise ValueError(f"Guess must contain {len(self.solution)} letters.")
        self.hints.append(word)

    def has_won(self) -> bool:
        return self.solution in self.hints

    def get_hint(self, word: str) -> str:
        for hint in self.hints:
            if str(hint) == word:
                return hint
        else:
            raise ValueError(f"{word} not found in hints")

    def check_hints(self, word: str) -> Iterable[Tuple[str, HintType]]:
        hint = self.get_hint(word)
        solution_remaining = list(self.solution) 
        hint_remaining = list(enumerate(hint))
        gg = [None for _ in range(len(word))]
        for idx, letter in enumerate(word):
            if letter == self.solution[idx]:
                solution_remaining.remove(letter)
                hint_remaining.remove((idx, letter))
                gg[idx] = HintType.CORRECT
        for idx, letter in hint_remaining:
            if letter in solution_remaining:
                solution_remaining.remove(letter)
                hint_remaining.remove((idx, letter))
                gg[idx] = HintType.WRONG_PLACE
        for idx, _ in hint_remaining:
            gg[idx] = HintType.NOT_PRESENT
        assert all(h is not None for h in gg)
        
        for letter, hint in zip(word, gg):
            yield letter, hint
        
