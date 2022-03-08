from dataclasses import dataclass, field
from typing import Dict, Tuple
from .dictionary import Dictionary
from .puzzle import HintType, Puzzle


@dataclass()
class Game:
    dictionary: Dictionary
    puzzle: Puzzle

    def guess(self, word: str) -> None:
        if word not in self.dictionary:
            return
        self.puzzle.add_hint(word=word)

    @property
    def hints(self) -> Dict[str, Tuple[Tuple[str, HintType], ...]]:
        hints = {word: tuple(self.puzzle.check_hints(word=word)) for word in self.puzzle.hints}
        return hints

    @property
    def guesses(self) -> Tuple[str, ...]:
        return tuple(self.puzzle.hints)

    def has_won(self) -> bool:
        return self.puzzle.has_won()
        
    @property
    def round(self) -> int:
        return len(self.hints) + 1

