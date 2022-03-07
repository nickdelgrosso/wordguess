from mimetypes import guess_all_extensions
from puzzle import Puzzle
from dictionary import Dictionary
from game import Game
from gui import Gui


game = Game(
    dictionary=Dictionary.from_text_file("data/words.txt"),
    puzzle=Puzzle(solution="perch")
)

gui = Gui(game=game)
gui.run()
