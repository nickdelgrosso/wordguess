from dataclasses import dataclass, field


@dataclass(frozen=True)
class Puzzle:
    solution: str

    def guess(self, guess: str) -> bool:
        return guess == self.solution