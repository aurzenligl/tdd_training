import sys
from .engine import Engine
from .game import Game
from .hardcoded_level import get_level

def main(argv=[]):
    game = Game(get_level())
    engine = Engine(game)
    engine.run()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
