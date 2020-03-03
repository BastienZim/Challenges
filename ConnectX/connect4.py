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


def getReward(move, player = 1):
    """
        Calculate reward based on neighbouring coins
        and chains involve.
        enemy neighbours -> +1
        chains involved -> +(4/3)*len(chain) for every chain.

        Note we can tweak the parameters to make it more proactive or defensive
    """
    #default value
    reward = 0

    col = move
    row = board.shape[0]-len(np.trim_zeros(np.flip(board[:,move])))
    #check if the player corresponds to the move provided
    if (int(board[row, col]) == player):
        for x_shift, y_shift in [(0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:#-1,0 is not needed to check as it will always be empty (there cannot be a coin above your last move)
            #x1, y1 = row, col
            x2, y2 = row+x_shift, col+y_shift
            #x_check, y_check = row+x_shift, col+y_shift
            if (checkInsideBoard(x2, y2)):
                #MY CHAINS : First checking the involved chains.
                if(int(board[x2, y2]) == player and (y_shift == 1 or (y_shift == 0 and x_shift == 1))):#as we alternate we check half of the possibilities.
                    alternate = True#to check both sides
                    chainLen = 2
                    while(alternate == True):
                        x_shift, y_shift = x_shift*-chainLen , y_shift*-chainLen
                        x2, y2 = row+x_shift, col+y_shift
                        if (checkInsideBoard(x2, y2)):
                            if(int(board[x2, y2]) == player):
                                chainLen += 1
                            else:
                                alternate = False
                    x_shift, y_shift = x_shift*-chainLen , y_shift*-chainLen
                    checking = True
                    while(checking):
                        x2, y2 = row+x_shift, col+y_shift
                        if (checkInsideBoard(x2, y2)):
                            if(int(board[x2, y2]) == player):
                                chainLen += 1
                            else:
                                checking = False
                        else:
                            checking = False

                    #we weight more chains than blocking in order to orient toward proactivity rather than blocking.
                    reward += chainLen*4/3

                    #count chains
                else:
                    #NEIGHBOURING COINS : Check Neighbouring coins.
                    reward += (lambda x: -1 if x != player else 0)(board[x2, y2])

    print("REWARD", reward)
    return (reward)









board = createBoard()
#printBoard()
print(getPlayableSlots())
#play(2)
import random
for i in range(20):
    #play(2)
    #printBoard()
    move_1 = random.randint(0,6)
    play(move_1,1)
    won = checkWin(player=1)
    if(won[0]==True):
        print("|||||||||| _1_ WON X|||||||||||||||")
        last_move = move_1
        print("last_mode : ", last_move)
        break
    move_2 = random.randint(0,6)
    play(move_2,2)
    won = checkWin(player=2)
    if(won[0]==True):
        print("|||||||||| _2_ WON X|||||||||||||||")
        last_move = move_2
        print("last_mode : ", last_move)
        break

print(board)
reward = getReward(last_move)
print(reward)

#chainBoard = np.ones((6, 7))

#conv = convolve2d(chainBoard, kernel_horiz)
#np.array(list(map(lambda x: max(x,0), board.flatten()))).reshape(6,7)
##print(conv)
#print(sum(list(map(lambda x: max(x,0), conv.flatten()))))
#print("AAA\n",np.array(listBoard))
#board = [x for x in board if (x>0) else 0]
#print(chainBoard)

#printBoard()
#print(board.shape[1])


#import gym


#__main__()










