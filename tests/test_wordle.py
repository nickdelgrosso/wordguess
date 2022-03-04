from pytest import FixtureRequest, fixture
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse

from puzzle import Puzzle
from dictionary import Dictionary

@fixture
def dictionary() -> Dictionary:
    return Dictionary()



scenarios("")


@given(
    parse('a puzzle where the correct answer is "{solution}"'),
    target_fixture="puzzle",
)
def stepdef(solution):
    puzzle = Puzzle.create(solution=solution)
    return puzzle


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
        assert dictionary.word_exists(hint)