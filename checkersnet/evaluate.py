"""Evaluates the model"""

import argparse
import logging
import os

import numpy as np
import torch
import utils
import model.net as net
from model.data_loader import CheckersDataset
from torch.utils.data import DataLoader
from tqdm import trange

import sys
sys.path.append('/home/dawki/Projects/Checkersmate')
from checkersmate.game import Game
from checkersmate.player.random import random_player
from checkersmate.player.deep import deep_player


parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', default='data/small', help="Directory containing the dataset")
parser.add_argument('--model_dir', default='experiments/base_model', help="Directory containing params.json")
parser.add_argument('--restore_file', default='best', help="name of the file in --model_dir \
                     containing weights to load")


def evaluate(model, n):
    """Evaluate the model's win rate against a random oponent.

    Args:
        model: (torch.nn.Module) the neural network
        n: (int) number of games to play against random oponent
    """
    
    # set model to evaluation mode
    model.eval()

    # summary for current eval loop
    results = []
    for i in trange(n):
        g = Game(p1=deep_player(model),silent=True)
        results.append(g.play())


    # compute mean of all metrics in summary
    logging.info("- Test metrics: win rate : " + str(sum(results)/n))
    return {'win_rate': sum(results)/n}


if __name__ == '__main__':
    """
        Evaluate the model on the test set.
    """
    # Load the parameters
    args = parser.parse_args()
    json_path = os.path.join(args.model_dir, 'params.json')
    assert os.path.isfile(json_path), "No json configuration file found at {}".format(json_path)
    params = utils.Params(json_path)

    # use GPU if available
    params.cuda = torch.cuda.is_available()     # use GPU is available

    # Set the random seed for reproducible experiments
    torch.manual_seed(230)
    if params.cuda: torch.cuda.manual_seed(230)
        
    # Get the logger
    utils.set_logger(os.path.join(args.model_dir, 'evaluate.log'))

    # Define the model
    model = net.Net(params).cuda() if params.cuda else net.Net(params)
    
    loss_fn = net.loss_fn
    metrics = net.metrics
    
    logging.info("Starting evaluation")

    # Reload weights from the saved file
    utils.load_checkpoint(os.path.join(args.model_dir, args.restore_file + '.pth.tar'), model)

    # Evaluate
    num_games = 1000
    test_metrics = evaluate(model,num_games)
    save_path = os.path.join(args.model_dir, "metrics_test_{}.json".format(args.restore_file))
    utils.save_dict_to_json(test_metrics, save_path)
