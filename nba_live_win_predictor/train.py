# use data pulled from stats.py to train a logistic regression model to predict win probability in live games
# model as neural-network using pytorch with a binary output 

import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.model_selection import train_test_split


class WinPredictor(nn.Module):
    def __init__(self, input_size):
        super(WinPredictor, self).__init__()

        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

# load data from csv
data = pd.read_csv('nba_data.csv')


# export model weights to file for use in main.py, write output to model_weights.pth and store in model_weights directory