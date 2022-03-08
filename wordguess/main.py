from colorama import Fore, Back, Style
from colorama import init
import pkg_resources


from .puzzle import Puzzle, HintType
from .dictionary import Dictionary
from .game import Game


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
    breakpoint()
    filename = pkg_resources.resource_filename('wordguess', 'data/words.txt')
    dictionary = Dictionary.from_text_file(filename)
    game = Game(
        dictionary=dictionary,
        puzzle=Puzzle(solution=dictionary.get_random())
    )

    init()
    print('Wordguess: Guess the 5-letter word!')
    while not game.has_won():
        guess = input(f'Guess {game.round}: ')
        game.guess(word=guess)
        try:
            hints = game.hints[guess]
        except KeyError:
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