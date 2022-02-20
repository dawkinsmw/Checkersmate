from checkersmate.game import Game

## Torch
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(32, 50)
        self.fc2 = nn.Linear(50, 100)
        self.fc3 = nn.Linear(100, 25)
        self.fc4 = nn.Linear(25, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


class deep_player():

    def __init__(self):
        self.net = Net()
        self.net.load_state_dict(torch.load(f"/home/dawki/Projects/deep_checkers/model/32.pth"))

    def select_move(self,boards):
        '''Given a list of boards, returns a randomly chosen board'''
        scores = [self.net(torch.Tensor(b)).item() for b in boards]
        move = scores.index(max(scores))
        return boards[move]



