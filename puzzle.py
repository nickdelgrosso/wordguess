from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Puzzle:
    solution: str
    hints: List[str]

    @classmethod
    def create(cls, solution: str) -> Puzzle:
        return Puzzle(solution=solution, hints=["python"])
        
    def guess(self, guess: str) -> bool:
        return guess == self.solution

