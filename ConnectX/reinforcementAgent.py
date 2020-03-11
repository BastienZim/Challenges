
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
from math import factorial

#from tqdm import tqdm

n_rows, n_cols = 5,6
#number of the states the board can be in.
#n_states = int((lambda x,y : sum([factorial(x*y)/factorial(k) for k in np.arange(x*y +1)]))(n_rows, n_cols))

n_actions = n_cols


def init_Q_player(player = 1, alpha = 0.3, epsilon = 0.2, gamma = 0.9):
    Q_TABLE = {}
    alpha = alpha
    epsilon = epsilon
    gamma = gamma
    return Q_TABLE

def getQ(Q_TABLE, state, action):
    if(Q_TABLE.get((state,action)) == None):
        Q_TABLE[(state,action)] = 1
    return (Q_TABLE[(state,action)])


#TODO:adapt Q_table function, getReward, getCurrentRole, random selection

def eps_greedy_Qlearning(S, A, alpha, gamma, Q_TABLE):
    if (eps_greedy):


        #first phase : we train
        for match in learning_match:
            record = getMatchRecord()#maybe do it along the way
            for state in record:
                myRole = getCurrentRole()
                reward = getReward(s,a)#s' is terminal state, getGoal(s',myrole):0
                # for reward see function defined in ./connect4.py

                s_, a_ = ????#TODO: find corresponding values for terminal state and terminal action.
                Q[player][(state,action)] = (1-alpha)*getQ(Q[player], s, a)+alpha*(reward + gamma* max(getQ(Q[player], s_, a_)))#the max est selon a' ; s_ et a_ sont s' et a'



        #second phase : we select the action
        selected = False
        expected_scope = 0
        for q_myrole in Q_TABLE(my_role, S, A):#q_myrole(s,a) in Q_myrole(S,A):
            if(current_state == s and expected_scope < q_myrole):
                expected_score = q_myrole
                selected_action = a
                selected = True
        if(not selected):
            selected_action = random()
    else:
        selected_action = random()
    return selected_action

def init_Game():
    alpha, gamma, epsilon = 0.3,0.9,0.2
    #Note we can have different parameters for player 1 and player 2.
    Q = {1: init_Q_player(1, alpha , epsilon, gamma), 2: init_Q_player(2, alpha , epsilon, gamma)}
    getQ(Q[player], s, a)
#getQ(Q[player], s, a)


