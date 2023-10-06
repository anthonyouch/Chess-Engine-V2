import chess
import random
class Player:
    def __init__(self, board, colour):
        self.board = board
        self.colour = colour

    def generate_move(self):
        raise NotImplementedError('generate_move not implemented')

    def make_move(self):
        move = self.generate_move()
        self.board.push(move)

class Human(Player):
    """ testing player to play against engine"""

    def __init__(self, board, color):
        super().__init__(board, color)

    def get_move(self):
        move = input("Player move:")
        return move


class Engine(Player):
    """This class represents the engine player in the game"""
    def __init__(self, board, colour):
        super().__init__(board, colour)
        self.is_opening = True

    def generate_opening_move(self):
        try:
            with chess.polyglot.open_reader("data/polyglot/Elo2400.bin") as reader:
                opening_moves = []
                for entry in reader.find_all(self.board):
                    opening_moves.append((entry.move, entry.weight, entry.learn))
                random.shuffle(opening_moves)
                return opening_moves[0][1], opening_moves[0][0]
        except:
            return False
