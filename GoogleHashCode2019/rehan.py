# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:42:02 2019

@author: Rehan Rajput
"""

class Picture:
    def __init__(self,orient,tags,id):
        self.tags = tags
        self.id = id
        self.orient = orient

    def commonTags(self,otherObject):
        return list(set(self.tags).intersection(otherObject.tags))
    
    def checkScore(self,otherObject):
        ct = self.commonTags(otherObject)
        a = len(set(self.tags) - set(ct))
        b = len(set(otherObject.tags) - set(ct))
        return min([len(ct),a,b])
    
class Slide:
     
    def __init__(self, orient, id, picture1, picture2 = Picture("V",[],-1)):
         
         self.orient = orient
         self.id = id
         self.picture1 = picture1
         self.picture2 = picture2

    def getTags(self):
        if(self.orient == "H"):
            return list(set(self.picture1.tags))
        else:
            return list(set(self.picture1.tags).union(self.picture2.tags))
    
    def getTagsP1(self):
        return self.picture1.tags

    def getTagsP2(self):#no safety if user uses it on H pic
        return self.picture2.tags

    def setTagsP1(self, tags):
        self.picture1.tags = tags

    def setTagsP2(self, tags):#no safety if user uses it on H pic
        self.picture2.tags = tags

    def commonTags(self,otherObject):
        return list(set(self.getTags()).intersection(otherObject.getTags()))

    def checkScore(self,otherObject):
        ct = self.commonTags(otherObject)
        a = len(set(self.getTags()) - set(ct))
        b = len(set(otherObject.getTags()) - set(ct))
        return min([len(ct),a,b])


def calculateNewScore(slideList,oldscore,i,j):#not considering border cases.
    score = oldscore
    if(i>0 and j>0 and j< len(slideList)-1 and i<len(slideList)-1):#non limit cases
        score -= (slideList[i].checkScore(slideList[i-1]))
        score -= (slideList[i].checkScore(slideList[i+1]))
        score -= (slideList[j].checkScore(slideList[j-1]))
        score -= (slideList[j].checkScore(slideList[j+1]))
        score += (slideList[j].checkScore(slideList[i-1]))
        score += (slideList[j].checkScore(slideList[i+1]))
        score += (slideList[i].checkScore(slideList[j-1]))
        score += (slideList[i].checkScore(slideList[j+1]))
    elif(i==0 and j< len(slideList)-1):
        score -= (slideList[i].checkScore(slideList[i+1]))
        score -= (slideList[j].checkScore(slideList[j-1]))
        score -= (slideList[j].checkScore(slideList[j+1]))
        score += (slideList[j].checkScore(slideList[i+1]))
        score += (slideList[i].checkScore(slideList[j-1]))
        score += (slideList[i].checkScore(slideList[j+1]))
    elif(j==0 and i< len(slideList)-1):
        score -= (slideList[i].checkScore(slideList[i-1]))
        score -= (slideList[i].checkScore(slideList[i+1]))
        score -= (slideList[j].checkScore(slideList[j+1]))
        score += (slideList[j].checkScore(slideList[i-1]))
        score += (slideList[j].checkScore(slideList[i+1]))
        score += (slideList[i].checkScore(slideList[j+1]))
    elif(i==len(slideList)-1 and j>0):
        score -= (slideList[i].checkScore(slideList[i-1]))
        score -= (slideList[j].checkScore(slideList[j-1]))
        score -= (slideList[j].checkScore(slideList[j+1]))
        score += (slideList[j].checkScore(slideList[i-1]))
        score += (slideList[i].checkScore(slideList[j-1]))
        score += (slideList[i].checkScore(slideList[j+1]))
    elif(j==len(slideList)-1 and i>0):
        score -= (slideList[i].checkScore(slideList[i-1]))
        score -= (slideList[i].checkScore(slideList[i+1]))
        score -= (slideList[j].checkScore(slideList[j-1]))
        score += (slideList[j].checkScore(slideList[i-1]))
        score += (slideList[j].checkScore(slideList[i+1]))
        score += (slideList[i].checkScore(slideList[j-1]))
    elif(j==len(slideList)-1 and i==0):
        score -= (slideList[i].checkScore(slideList[i+1]))
        score -= (slideList[j].checkScore(slideList[j-1]))
        score += (slideList[j].checkScore(slideList[i+1]))
        score += (slideList[i].checkScore(slideList[j-1]))
    elif(i==len(slideList)-1 and j==0):
        score -= (slideList[i].checkScore(slideList[i-1]))
        score -= (slideList[j].checkScore(slideList[j+1]))
        score += (slideList[j].checkScore(slideList[i-1]))
        score += (slideList[i].checkScore(slideList[j+1]))
    return score




def swap(slideList,i,j):
    slideList[i], slideList[j] = slideList[j], slideList[i]



def calculateScore(slideList):
    score = 0
    for i in range(len(slideList)-1):
        score += (slideList[i].checkScore(slideList[i+1]))
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
        pictureList.append(Picture(orientation,tags,str(id)))
        id+=1
    return pictureList

def extractVerticalPicts(pictureList):
    res = [x for x in pictureList if x.orient == "V"]
    return res
    
def extractHorizPicts(pictureList):
    res = [x for x in pictureList if x.orient == "H"]
    return res

def createSlideList(horizPictures, verticalPictures):
    slideList = []
    for i in range(0,len(verticalPictures)-1,2):
        slideList.append(Slide(verticalPictures[i].orient, str(verticalPictures[i].id)+" "+str(verticalPictures[i+1].id) ,verticalPictures[i] ,verticalPictures[i+1]))
    for picture in horizPictures:
        slideList.append(Slide(picture.orient, picture.id, picture))
    return slideList

def writeSubmit(name,score,slideList):
    name = name[2:]
    f= open("submit_" + str(score) + "_" + name,"w+")
    f.write(str(len(slideList))+"\n")
    for i in range (len(slideList)):
        f.write(str(slideList[i].id)+"\n")
    f.close()