"""Defines the neural network, losss function and metrics"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self, params):
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



loss_fn = nn.MSELoss()

def accuracy(outputs, labels):
    """
    Compute the accuracy, given the outputs and labels for all tokens. 
    Args:
        outputs: (np.ndarray) dimension batch_size*seq_len x num_tags - log softmax output of the model
        labels: (np.ndarray) dimension batch_size x seq_len where each element is either a label in
                [0, 1, ... num_tag-1], or -1 in case it is a PADding token.

    Returns: (float) accuracy in [0,1]
    """

    predicted = 2*((outputs>0)-0.5)
    total = len(labels)
    correct = (predicted == labels).sum().item()
    return 100 * correct / total

metrics = {
    'accuracy': accuracy,
    # could add more metrics such as accuracy for each token type
}