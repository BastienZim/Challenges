import numpy as np


def createBoard(row = 6, col = 7):
    print(row,col)
    board = np.zeros((row, col))
    return board

def printBoard():
    print(board)

def getPlayableSlots():
    playableSlots = []
    for col in range(board.shape[1]):
        checking = True
        row = 0
        while(checking):
            #print(board[board.shape[0] - row - 1, col],board.shape[0] - row - 1, row, col)
            #print(board.shape[0] - row - 1)
            if board[board.shape[0] - row - 1, col] == 0:
                checking = False
                playableSlots.append((1, board.shape[0] - row - 1))
                #print("ok", row,col)
            else:
                if(row <5):
                    row+=1
                else:
                    checking = False
                    playableSlots.append((0))
            if(row>=board.shape[0]):
                playableSlots.append((0))
                #print("not ok",col)
    #print(playableSlots)
    return(playableSlots)

def play(col, player = 1):
    playableSlots = getPlayableSlots()
    if (playableSlots[col] != 0):
        board[playableSlots[col][1],col] = player
    else:
        print("NOT PLAYABLE", col)

def checkInsideBoard(x,y):
    if(-1<x<board.shape[0]):
        if(-1<y<board.shape[1]):
            return(True)
    return(False)

def checkWin(player = 1, coinsInaRow = 4):#full bourin
    for row in range(board.shape[0]):
        for col in range(board.shape[1]-3):
            for x_shift, y_shift in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                chainLength = 1
                x1, y1 = row, col
                x2, y2 = row+x_shift, col+y_shift
                #x_check, y_check = row+x_shift, col+y_shift
                if (checkInsideBoard(x2, y2)):
                    checking = True
                    while(checking and chainLength < coinsInaRow):
                        if(board[x1,y1] == player and board[x1,y1] == board[x2,y2]):
                            chainLength+=1
                            x1, y1, x2, y2 = x2, y2, x2 + x_shift, y2 + y_shift
                            if (not checkInsideBoard(x2, y2)):
                                checking = False
                        else:
                            checking = False
                if(chainLength == coinsInaRow):
                    #print("\n\nAAAAAAAAAAAAA", chainLength)
                    #print("||||||||||XXXXXXX|||||||||||||||")
                    #print("||||||||||X WON X|||||||||||||||")
                    #print("||||||||||XXXXXXX|||||||||||||||")
                    return(True, chainLength, x_shift, y_shift, row, col)                    
    return(False, chainLength)

def playerChainsStats(player = 1):
    return 0


def getReward(player = 1):
    reward = 0
    reward += maxChain - self.prev_maxChain
    reward -= Opp_maxChain - self.prev_opp_maxChain


board = createBoard()
#printBoard()
print(getPlayableSlots())
#play(2)
import random
for i in range(20):
    #play(2)
    #printBoard()
    play(random.randint(0,6),1)
    won = checkWin(player=1)
    if(won[0]==True):
        print("|||||||||| _1_ WON X|||||||||||||||")
        break
    play(random.randint(0,6),2)
    won = checkWin(player=2)
    if(won[0]==True):
        print("|||||||||| _2_ WON X|||||||||||||||")
        break

board = board-np.ones((6, 7))
chainBoard = np.array(list(map(lambda x: max(x,0), board.flatten()))).reshape(6,7)

from scipy.signal import convolve2d

kernel_horiz = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])


#chainBoard = np.ones((6, 7))

#conv = convolve2d(chainBoard, kernel_horiz)
#np.array(list(map(lambda x: max(x,0), board.flatten()))).reshape(6,7)
##print(conv)
#print(sum(list(map(lambda x: max(x,0), conv.flatten()))))
#print("AAA\n",np.array(listBoard))
#board = [x for x in board if (x>0) else 0]    
print(chainBoard)

#printBoard()
#print(board.shape[1])


#import gym


#__main__()










