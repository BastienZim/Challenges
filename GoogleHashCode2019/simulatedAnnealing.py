import random
from math import exp
from rehan import *



def simulatedAnneal(slideList):
    kmax = len(slideList)
    T=1#1000
    oldscore = calculateScore(slideList)
    while(T>0):
        T = newTemperature(T)
        k, neighbour = random.sample(range(0, kmax-1), 2)#2 different slides to concider
        
        newScore = calculateNewScore(slideList,oldscore,k,neighbour)
        if(func(oldscore,newScore,T) >= random.random()):
            swap(slideList, k, neighbour)#do the swap
        oldscore = newScore
    return slideList

def newTemperature(T):
    return T - 0.0001 #001

def func(oldscore,newScore,T):
    if(newScore > oldscore):
        return 1
    if(oldscore-newScore)==1:
        return 1
    else:
        return(1/(1-(oldscore-newScore)/T))       #(exp((oldscore-newScore)/T))


def swapVertical(slideList,i,j,a,b):#we try to swap tags # C DEGEULASSE et ca peut cree des doublons peut etre que ca vient de la
    #00,10,01,11
    id1, id2 = slideList[i].id.split(" "), slideList[j].id.split(" ")
    
    if(a==0):
        if(b==0):#00
            tags1, tags2 = slideList[i].getTagsP1(), slideList[j].getTagsP1()
            slideList[i].setTagsP1(tags2) #swap tags
            slideList[j].setTagsP1(tags1)
            slideList[i].id = id2[0]+" "+id1[1] #swap id
            slideList[j].id = id1[0]+" "+id2[1]
        else:#01 --> ab cd -> db ca 
            tags1, tags2 = slideList[i].getTagsP1(), slideList[j].getTagsP2()
            slideList[i].setTagsP1(tags2) #swap tags
            slideList[j].setTagsP2(tags1)
            slideList[i].id = id2[1]+" "+id1[1] #swap id
            slideList[j].id = id2[0]+" "+id1[0]
    else:
        if(b==0):#10 --> ab cd -> ac bd
            tags1, tags2 = slideList[i].getTagsP2(), slideList[j].getTagsP1()
            slideList[i].setTagsP2(tags2) #swap tags
            slideList[j].setTagsP1(tags1)
            slideList[i].id = id1[0]+" "+id2[0] #swap id
            slideList[j].id = id1[1]+" "+id2[1]
        else:
            tags1, tags2 = slideList[i].getTagsP2(), slideList[j].getTagsP2()    
            slideList[i].setTagsP2(tags2) #swap tags
            slideList[j].setTagsP2(tags1)
            slideList[i].id = id1[0]+" "+id2[1] #swap id
            slideList[j].id = id2[0]+" "+id1[1]



#fileList = ["a_example.txt","./b_lovely_landscapes.txt","c_memorable_moments.txt","d_pet_pictures.txt","e_shiny_selfies.txt"]
fileList = ["./b_lovely_landscapes.txt"]
for file in fileList:
    pictureList = extractPictures(file)
    horizPictures = extractHorizPicts(pictureList)
    verticalPictures = extractVerticalPicts(pictureList)
    slideList = createSlideList(horizPictures,verticalPictures)
    random.shuffle(slideList)
    
    result = slideList
    score = 0
    for i in range(80):#iterate the simulated annealing over the resulting file
        result = simulatedAnneal(result)
        newScore = calculateScore(result)
        scoreDiff = newScore - score
        score = newScore
        print(i, score, "+" + str(scoreDiff))
    #print(score)
    writeSubmit(file,score,result)

