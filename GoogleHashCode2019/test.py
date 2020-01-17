import random
from math import exp
import rehan








def simulatedAnneal(pictureList):
    kmax = len(pictureList)
    T=1#1000
    oldscore = calculateScore(pictureList)
    while(T>0):
        T = newTemperature(T)
        k = random.randint(0,kmax-1)
        neighbour = random.randint(0,kmax-1)
        if(pictureList[k].orient == "V" and pictureList[neighbour].orient == "V"):#if both slides are vertical #problem we dont swap the tags.
            a,b = random.randint(0,1),random.randint(0,1)
            swapVertical(pictureList, k, neighbour,a,b)
            newScore = calculateNewScore(pictureList,oldscore,k,neighbour)
            #newScore = calculateScoreVSwap(pictureList,oldscore,k,neighbour,kmax,a,b)#not sure about the usefulness of this function
            if(not func(oldscore,newScore,T) >= random.random()):
                swapVertical(pictureList, k, neighbour,a,b)#undo the swap#
        else:
            newScore = calculateNewScore(pictureList,oldscore,k,neighbour)
            if(func(oldscore,newScore,T) >= random.random()):
                swap(pictureList, k, neighbour)#do the swap
        oldscore = newScore
    return pictureList

def newTemperature(T):
    return T - 0.0001 #001

def swap(pictureList,i,j):
    pictureList[i], pictureList[j] = pictureList[j], pictureList[i]

def swapVertical(pictureList,i,j,a,b):#we try to swap tags
    l1 = pictureList[i].id.split(" ")
    l2 = pictureList[i].id.split(" ")
    #00,10,01,11
    if(a==0):
        if(b==0):
            tagsi, tagsj = pictureList[i].getATags(), pictureList[j].getATags()
            pictureList[i].setATags(tagsj)
            pictureList[j].setATags(tagsi)
            pictureList[i].id = l2[0] + " " + l1[1]
            pictureList[j].id = l1[0] + " " + l2[1]
        else:
            tagsi, tagsj = pictureList[i].getATags(), pictureList[j].getBTags()
            pictureList[i].setATags(tagsj)
            pictureList[j].setBTags(tagsi)    
            pictureList[i].id = l2[0] + " " + l1[1]
            pictureList[j].id = l2[0] + " " + l1[1]
    else:
        if(b==0):
            tagsi, tagsj = pictureList[i].getBTags(), pictureList[j].getATags()
            pictureList[i].setBTags(tagsj)
            pictureList[j].setATags(tagsi)
            pictureList[i].id = l1[0] + " " + l2[1]
            pictureList[j].id = l1[0] + " " + l2[1]
        else:    
            tagsi, tagsj = pictureList[i].getBTags(), pictureList[j].getBTags()
            pictureList[i].setBTags(tagsj)
            pictureList[j].setBTags(tagsi)
            pictureList[i].id = l1[0] + " " + l2[1]
            pictureList[j].id = l2[0] + " " + l1[1]
    

def func(oldscore,newScore,T):
    if(newScore > oldscore):
        return 1
    if(oldscore-newScore)==1:
        return 1
    else:
        return(1/(1-(oldscore-newScore)/T))       #(exp((oldscore-newScore)/T))

def calculateNewScore(pictureList,oldscore,i,j):#not considering border cases.
    score = oldscore
    if(i>0 and j>0 and j< len(pictureList)-1 and i<len(pictureList)-1):
        score -= (pictureList[i].checkScore(pictureList[i-1]))
        score -= (pictureList[i].checkScore(pictureList[i+1]))
        score -= (pictureList[j].checkScore(pictureList[j-1]))
        score -= (pictureList[j].checkScore(pictureList[j+1]))

        score += (pictureList[j].checkScore(pictureList[i-1]))
        score += (pictureList[j].checkScore(pictureList[i+1]))
        score += (pictureList[i].checkScore(pictureList[j-1]))
        score += (pictureList[i].checkScore(pictureList[j+1]))
    return score

def calculateScoreVSwap(pictureList,oldscore,i,j,kmax,a,b):
    score = oldscore
    if(i>0 and j>0 and j< kmax-1 and i<kmax-1):
        score -= (pictureList[i].checkScore(pictureList[i-1]))
        score -= (pictureList[i].checkScore(pictureList[i+1]))
        score -= (pictureList[j].checkScore(pictureList[j-1]))
        score -= (pictureList[j].checkScore(pictureList[j+1]))

        score += (pictureList[j].checkScore(pictureList[i-1]))
        score += (pictureList[j].checkScore(pictureList[i+1]))
        score += (pictureList[i].checkScore(pictureList[j-1]))
        score += (pictureList[i].checkScore(pictureList[j+1]))
    return score


def calculateScore(pictureList):
    score = 0
    for i in range(len(pictureList)-1):
        score += (pictureList[i].checkScore(pictureList[i+1]))
    return score

def extractPictures(file):
    with open(file) as f:
            res = f.read()
    lines = res.splitlines()[1:]
    pictureList=[]
    id = 0
    for line in lines:
        tags = (line[5:]).split()
        orientation = line[0:1]
        pictureList.append(rehan.Picture(orientation,tags,str(id)))
        id+=1
    return pictureList

def writeSubmit(name,score,pictureList):
    name = name[2:]
    f= open("submit_" + str(score) + "_" + name,"w+")
    f.write(str(len(pictureList))+"\n")
    for i in range (len(pictureList)):
        f.write(str(pictureList[i].id)+"\n")

    f.close()

def extractVerticalPicts(pictureList):
    res = [x for x in pictureList if x.orient == "V"]
    return res
def extractHorizPicts(pictureList):
    res = [x for x in pictureList if x.orient == "H"]
    return res

def AddTogether(a):
    lst = []
    for i in range(0,len(a)-1,2):
        lst.append(createVerticalSlide(a[i],a[i+1]))
    return lst

def createVerticalSlide(a,b):
    new_tags = set(a.tags).union(set(b.tags))
    slide = rehan.Picture("V",new_tags,str(a.id) + " " + str(b.id))
    slide.defineVtags(a.tags)
    return slide





#fileList = ["a_example.txt","./b_lovely_landscapes.txt","c_memorable_moments.txt","d_pet_pictures.txt","e_shiny_selfies.txt"]
fileList = ["e_shiny_selfies.txt"]
for file in fileList:
    pictureList = extractPictures(file)
    horizPictures = extractHorizPicts(pictureList)
    verticalPictures = extractVerticalPicts(pictureList)
    verticalPictures = AddTogether(verticalPictures)
    if(len(verticalPictures)!= 0):
        pictureList = verticalPictures + horizPictures
    else:
        pictureList = horizPictures
    random.shuffle(pictureList)
    
    result = pictureList
    score = 0
    for i in range(80):#iterate the simulated annealing over the resulting file
        result = simulatedAnneal(result)
        newScore = calculateScore(result)
        scoreDiff = newScore - score
        score = newScore
        print(i, score, "+" + str(scoreDiff))
    #print(score)
    writeSubmit(file,score,result)

