#!/usr/bin/env python

import chess

class State(object):
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bits according to readme
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TOTO : add neural net here
        return 1 # communists will be happy. all board positions are equal

if __name__ == "__main__":
    s = State()
    print(s.edges())
