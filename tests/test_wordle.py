from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse
from puzzle import Puzzle


scenarios("")


@given(
    parse('a puzzle where the correct answer is "{solution}"'),
    target_fixture="puzzle",
)
def stepdef(solution):
    puzzle = Puzzle(solution=solution)
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