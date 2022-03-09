import os

print(os.getcwd())

import torch
from checkersmate.game import Game
from checkersmate.player.human import human_player
from checkersmate.player.deep import deep_player

import checkersnet.model.net as net

if __name__ == '__main__':
    model = net.Net(params=1)

    checkpoint = '/home/dawki/Projects/Checkersmate/checkersnet/experiments/base_model/best.pth.tar'
    checkpoint = torch.load(checkpoint)
    model.load_state_dict(checkpoint['state_dict']) 
    
    g = Game(p1=human_player(),p2=deep_player(model))
    g.play()
    # n = 1000
    # results = []
    # for i in range(n):
    #     g = Game(p1=deep_player(),silent=True)
    #     results.append(g.play())
    # print(sum(results)/n)

    