import os
import shutil
import re

def dataSplit():
    """
    
    """
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

    testFilePattern = re.compile("(P01_01_[0-9]+|P05_01_[0-9]+).txt")
    valFilePattern = re.compile("(P0[1 2]_02_[0-9]+).txt")
    filePattern = re.compile("(P0[0-5]_0[0-9]_[0-9]+).txt")
    testCount = 0
    valCount = 0
    trainCount = 0

    for labelFile in labelFileList:
        testMatch = re.match(testFilePattern,labelFile)
        valMatch = re.match(valFilePattern,labelFile)
        if testMatch:
            testCount += 1
            pathCheck = os.path.exists(os.path.join(imgDir,testMatch.group(1)+'.jpg'))
            shutil.copy2(str(os.path.join(imgDir, testMatch.group(1) + '.jpg')), str(os.path.join(imgDataDir,'test')))
            shutil.copy2(str(os.path.join(labelDir, testMatch.group(1) + '.txt')), str(os.path.join(labelDataDir,'test')))
            if not pathCheck:
                print('image not found')
                break
        elif valMatch:
            valCount += 1
            shutil.copy2(str(os.path.join(imgDir, valMatch.group(1) + '.jpg')), str(os.path.join(imgDataDir,'val')))
            shutil.copy2(str(os.path.join(labelDir, valMatch.group(1) + '.txt')), str(os.path.join(labelDataDir,'val')))
        else:
            fileMatch = re.match(filePattern,labelFile)
            trainCount += 1
            shutil.copy2(str(os.path.join(imgDir, fileMatch.group(1) + '.jpg')), str(os.path.join(imgDataDir,'train')))
            shutil.copy2(str(os.path.join(labelDir, fileMatch.group(1) + '.txt')), str(os.path.join(labelDataDir,'train')))
    
    print(f"Test count\t:{testCount}\nVal count\t:{valCount}\nTrain count\t:{trainCount}")




dataSplit()