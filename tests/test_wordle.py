import enum
from typing import List
from pathlib import Path
from pytest import FixtureRequest, fixture
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse

from puzzle import HintType, Puzzle
from dictionary import Dictionary

@fixture(scope="session")
def dictionary() -> Dictionary:
    return Dictionary.from_text_file(Path("./data/words.txt"))



scenarios("")


@given(
    parse('a puzzle where the correct answer is "{solution}"'),
    target_fixture="puzzle",
)
def stepdef(solution):
    puzzle = Puzzle(solution=solution)
    return puzzle


@given(
    parse('the hints [{hint_words}]'),
    converters={
        'hint_words': lambda s: [h.strip() for h in s.split(',')]
    },
)
def stepdef(puzzle: Puzzle, hint_words: List[str]):
    for word in hint_words:
        puzzle.add_hint(word=word)
    


@when(
    parse('the player guesses "{guess}"'),
    target_fixture='won',
)
def stepdef(puzzle: Puzzle, guess):
    won = puzzle.guess(guess)
    return won


@then(
    parse('the player sees a {won} message.'),
    converters = {
        'won': lambda s: {'win': True, 'lose': False}
    }
)
def stepdef(won):
    assert won


@then('all of the hints will be words in the dictionary')
def stepdef(puzzle, dictionary):
    assert len(puzzle.hints) > 0
    for hint in puzzle.hints:
        assert hint in dictionary


@then(
    parse('the hint for "{hint_word}" shows that letters [{indices}] are {hint_type}'),
    converters={
        'indices': lambda s: [int(e) for e in s.split(',')],
        'hint_type': lambda s: {
            'correct': HintType.CORRECT,
            'not present': HintType.NOT_PRESENT,
            }[s]
    }
)
def stepdef(puzzle: Puzzle, hint_word, indices, hint_type):
    letter_hints = tuple(puzzle.check_hints(word=hint_word))
    matched_letter_hints = [letter_hints[ind - 1] for ind in indices]
    for _, ht in matched_letter_hints:
        assert ht is hint_type
        




