import os
import shutil
import random
import re
from typing import Union

def create_random_ones_array():
    # Create array of 20 zeros
    arr = [0] * 20
    # Get 6 unique random indices
    random_indices = random.sample(range(20), 6)
    # Set ones at random indices
    for idx in random_indices:
        arr[idx] = 1
    return arr

def copy2Train(fileName:str, imgDir:str, imgDataDir:str, labelDir:str, labelDataDir:str):
    shutil.copy2(str(os.path.join(imgDir, fileName+'.jpg')), str(os.path.join(imgDataDir,'train')))
    shutil.copy2(str(os.path.join(labelDir, fileName+'.txt')), str(os.path.join(labelDataDir,'train')))

def copy2Val(fileName:str, imgDir:str, imgDataDir:str, labelDir:str, labelDataDir:str):
    shutil.copy2(str(os.path.join(imgDir, fileName+'.jpg')), str(os.path.join(imgDataDir,'val')))
    shutil.copy2(str(os.path.join(labelDir, fileName+'.txt')), str(os.path.join(labelDataDir,'val')))

def copy2Test(fileName:str, imgDir:str, imgDataDir:str, labelDir:str, labelDataDir:str):
    shutil.copy2(str(os.path.join(imgDir, fileName+'.jpg')), str(os.path.join(imgDataDir,'test')))
    shutil.copy2(str(os.path.join(labelDir, fileName+'.txt')), str(os.path.join(labelDataDir,'test')))

def randomPick(sourceList:list[int])->Union[None,int]:
    if not sourceList:
        return None
    else:
        randIndex = random.choice(range(len(sourceList)))
        randInt = sourceList.pop(randIndex)
        return randInt


def dataRandomSplit():
    sourceDir = os.path.abspath(__file__)
    dataLabels = os.path.join(sourceDir,'..','..','data')
    data = str(os.path.abspath(dataLabels))
    dataDir = str(os.path.join(data, 'task3_tools'))
    if not os.path.exists(os.path.join(data,'task3_data')):
        os.mkdir(str(os.path.join(data,'task3_data')))
        os.mkdir(str(os.path.join(data,'task3_data','images')))
        os.mkdir(str(os.path.join(data,'task3_data','images','train')))
        os.mkdir(str(os.path.join(data,'task3_data','images','val')))
        os.mkdir(str(os.path.join(data,'task3_data','images','test')))
        os.mkdir(str(os.path.join(data,'task3_data','labels')))
        os.mkdir(str(os.path.join(data,'task3_data','labels','train')))
        os.mkdir(str(os.path.join(data,'task3_data','labels','test')))
        os.mkdir(str(os.path.join(data,'task3_data','labels','val')))
    imgDataDir = os.path.join(data,'task3_data','images')
    labelDataDir = os.path.join(data,'task3_data','labels')
    imgDir = os.path.join(dataDir, 'images/train')
    labelDir = os.path.join(dataDir, 'labels/train')
    labelFileList = os.listdir(labelDir)
    trackList = list(range(1,len(labelFileList)))
    randList = create_random_ones_array()
    valTestFlag = 0
    count = 0
    trainCount = 0
    valCount = 0
    testCount = 0

    for i in range(len(labelFileList)):
        id = randomPick(trackList)
        if not id:
            print(f"Train count\t:{trainCount}\nVal count\t:{valCount}\nTest count\t:{testCount}")
            break
        labelFile = labelFileList[id]
        regEx = re.compile('(P0[0-9]_0[0-9]_[0-9]+).txt')
        regExMatch = regEx.match(labelFile)
        if regExMatch:
            fileName = regExMatch.group(1)
        if count >= 20:
            count = 0
        if randList[count] == 0:
            copy2Train(fileName=fileName,imgDir=imgDir,imgDataDir=imgDataDir,labelDataDir=labelDataDir,labelDir=labelDir)
            count += 1
            trainCount += 1
            continue
        elif randList[count] == 1 and valTestFlag == 0:
            copy2Val(fileName=fileName,imgDir=imgDir,imgDataDir=imgDataDir,labelDataDir=labelDataDir,labelDir=labelDir)
            count += 1
            valCount += 1
            valTestFlag = 1
            continue
        elif randList[count] == 1 and valTestFlag == 1:
            copy2Test(fileName=fileName,imgDir=imgDir,imgDataDir=imgDataDir,labelDataDir=labelDataDir,labelDir=labelDir)
            count += 1
            testCount += 1
            valTestFlag = 0
            continue


dataRandomSplit()