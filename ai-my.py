# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:05:53 2018

@author: Xiaoyu's MSI
"""

import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional  as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

class Network(nn.Module):
    
    def __init__(self, input_size, nb_action):
        super(Network, self).__init__()
        self.input_size = input_size
        self.nb_action = nb_action
        self.fc1 = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30, nb_action)
        print(type(self.fc1))
    def forward(self, state):
        x = F.relu(self.fc1(state))

n = Network(5,3)

class Dog():
    def __init__(self, name):
        self.name = name
        print(type(self))
        
d = Dog('a')
print(type(n.fc1))
help (n.fc1)