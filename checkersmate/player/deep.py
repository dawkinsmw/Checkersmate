from checkersmate.game import Game

## Torch
import torch
import torch.nn as nn
import torch.nn.functional as F

from checkersnet.model.net import Net

class deep_player():

    def __init__(self, net):
        self.net = net

    def select_move(self,boards):
        '''Given a list of boards, returns a randomly chosen board'''
        scores = [self.net(torch.Tensor(b)).item() for b in boards]
        move = scores.index(max(scores))
        return boards[move]



