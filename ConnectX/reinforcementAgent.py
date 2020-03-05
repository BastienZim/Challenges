
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
from math import factorial
'''
import torch
import torch.nn.functional as F
from torch import nn, optim
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import transforms, models
'''
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import confusion_matrix
#from sklearn.utils.multiclass import unique_labels

#from tqdm import tqdm

n_rows, n_cols = 5,6
#number of the states the board can be in.
n_states = int((lambda x,y : sum([factorial(x*y)/factorial(k) for k in np.arange(x*y +1)]))(n_rows, n_cols))

x,y = n_rows, n_cols
#print(sum([factorial(x)/factorial(x*y) for x in np.arange(x*y +1)]))
#print([factorial(x)/factorial(x*y) for x in np.arange(x*y +1)])

n_actions = n_cols
print([n_states, n_actions])
Q_TABLE = np.zeros([n_states, n_actions])