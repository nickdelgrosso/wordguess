from mimetypes import guess_all_extensions
from turtle import back
from puzzle import Puzzle
from dictionary import Dictionary
from game import Game
from colorama import Fore, Back, Style
# from gui import MainWindow
from colorama import init

from puzzle import HintType


def colored(text, color='', background='',):
    render = ''
    if color:
        render += getattr(Fore, color.upper())
    if background:
        render += getattr(Back, background.upper())
    render += text
    render += Style.RESET_ALL
    return render


def main():
    dictionary = Dictionary.from_text_file("data/words.txt")
    game = Game(
        dictionary=dictionary,
        puzzle=Puzzle(solution=dictionary.get_random())
    )

    init()
    round = 0
    while not game.has_won():
        round += 1
        guess = input(f'Guess {round}: ')
        game.guess(word=guess)
        try:
            hints = game.hints[guess]
        except KeyError:
            round -= 1
            continue
        
        colors = {
            HintType.CORRECT: ('black', 'green'),
            HintType.WRONG_PLACE: ('white', 'red'),
            HintType.NOT_PRESENT: ('black', 'white'),
        }
        for letter, hint in hints:
            color = colors[hint]
            print(colored(letter, *color), end='')
        print('')


if __name__ == '__main__':
    main()