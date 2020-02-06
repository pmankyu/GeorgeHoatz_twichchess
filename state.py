#!/usr/bin/env python

import chess
import numpy as np

class State(object):
    def __init__(self,board=None):
        if board is None: 
            self.board = chess.Board()
        else:
            self.board = board

    def serialize(self):
        assert self.board.is_valid()
        bstate = np.zeros(64, np.uint8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                bstate[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6 \
                             "P": 9, "N":10, "B":11, "R":12, "Q":13, "K":14}[pp.symbol()] 
        if self.board.ep_Square is not None:
            assert bstate[self.board.ep_Square] == 0
            bstate[self.board.ep_Square] == 0
        bstate = bstate.reshape(8,8) 
        exit(0)

        state = np.zeros((8,8,5), np.uint8)
        
        state[:,:,0] = (bstate>>3)&1
        state[:,:,1] = (bstate>>2)&1
        state[:,:,2] = (bstate>>1)&1
        state[:,:,3] = (bstate>>0)&1

        # 4th column is who's turn it is
        state[:, :, 4] = (self.board.turn*1.0)
        
        return state

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TOTO : add neural net here
        return 1 # communists will be happy. all board positions are equal

if __name__ == "__main__":
    s = State()
    print(s.edges())
