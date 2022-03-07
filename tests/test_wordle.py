from typing import List
from pathlib import Path

from pytest import fixture
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import parse

from game import Game
from puzzle import HintType, Puzzle
from dictionary import Dictionary


@fixture(scope="session")
def dictionary() -> Dictionary:
    return Dictionary.from_text_file(Path("./data/words.txt"))


scenarios("")


@given(
    parse('a puzzle where the correct answer is "{solution}"'),
    target_fixture="game",
)
def stepdef(solution, dictionary):
    puzzle = Puzzle(solution=solution)
    game = Game(
        puzzle=puzzle,
        dictionary=dictionary
    )
    return game


@given(
    parse('the hints [{hint_words}]'),
    converters={
        'hint_words': lambda s: [h.strip() for h in s.split(',')]
    },
)
def stepdef(game: Game, hint_words: List[str]):
    for word in hint_words:
        game.guess(word=word)
    

@when(
    parse('the player guesses a non-word "{word}"'),
    target_fixture='guess'
)
@when(
    parse('the player guesses "{word}"'),
    target_fixture='guess'
)
def stepdef(game: Game, word):
    game.guess(word=word)
    return word
    

@given(
    parse('the game does {won} say the player has won'),
    converters = {
        'won': lambda s: {'': True, 'not': False}[s]
    }
)
@then(
    parse('the player sees a {won} message.'),
    converters = {
        'won': lambda s: {'win': True, 'lose': False}[s]
    }
)
def stepdef(game: Game, won: bool):
    assert game.has_won() == won


@then(
    parse('the hint does {is_registered} get registered in the list of guesses.'),
    converters = {
        'is_registered': lambda s: {'yes': True, 'not': False}[s]
    }
)
def stepdef(game: Game, guess: str, is_registered: bool):
    assert (guess in game.guesses) == is_registered


@then('all of the hints will be words in the dictionary')
def stepdef(game: Game, dictionary: Dictionary):
    hints = game.get_word_hints()
    assert len(puzzle.hints) > 0
    for hint in puzzle.hints:
        assert hint in dictionary


@then(
    parse('the hint for "{hint_word}" shows that letters [{indices}] are {hint_type}'),
    converters={
        'indices': lambda ss: ([int(ee) for ee in ss.split(',')] if ss != 'None' else []),
        'hint_type': lambda s: {
            'correct': HintType.CORRECT,
            'in the wrong position': HintType.WRONG_PLACE,
            'not present': HintType.NOT_PRESENT,
            }[s]
    }
)
def stepdef(game: Game, hint_word, indices, hint_type):
    letter_hints = game.hints[hint_word]
    matched_letter_hints = [letter_hints[ind - 1] for ind in indices]
    for _, ht in matched_letter_hints:
        assert ht is hint_type
        




