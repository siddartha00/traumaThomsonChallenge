import os
import cv2
import json

def extractFrames(sourceImgDir, outputImgDir, outputLableDir):
    splitIndex = 0
    split = 'train'
    trainCount = 0
    valCount = 0
    testCount = 0
    frameDir = os.path.join(outputImgDir)
    lableDir = os.path.join(outputLableDir)
    videoDir = os.path.join(sourceImgDir,'videos')
    print(videoDir)
    for videoFile in sorted(os.listdir(videoDir)):
        videoPath = os.path.join(videoDir, videoFile)
        videoName = os.path.splitext(videoFile)[0]
        sourceLableDir = os.path.join(sourceImgDir, 'bbox', videoName)
        cap = cv2.VideoCapture(videoPath)
        videoHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        videoWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frameCount = 0
        while cap.isOpened():
            if splitIndex<14 and splitIndex>=0:
                split = 'train'
                trainCount += 1
            elif splitIndex<17 and splitIndex>=14:
                split = 'val'
                valCount += 1
            elif splitIndex<20 and splitIndex>=17:
                split = 'test'
                testCount += 1
            splitIndex += 1
            if splitIndex >= 20:
                splitIndex = 0
            splitIndex += 1
            ret, frame = cap.read()
            if not ret:
                break
            frameName = f'{videoName}_frame_{frameCount:05d}.jpg'
            framePath = os.path.join(frameDir, split, 'images', frameName)
            lableName = f'{videoName}_frame_{frameCount:05d}.txt'
            lablePath = os.path.join(lableDir, split, 'labels', lableName)
            sourceLablePath = os.path.join(sourceLableDir, f'frame_{frameCount:06d}.json')
            cv2.imwrite(framePath,frame)
            frameCount += 1
            try:
                annotationSource = json.load(open(sourceLablePath, 'r'))
                with open(lablePath, 'w') as f:
                    for annotation in annotationSource['annotations']:
                        if annotation.get('category_id') == 1:
                            classId = 1
                        elif annotation.get('category_id') == 0:
                            classId = 0
                        bbox = annotation.get('bbox')
                        if bbox:
                            x, y, w, h = bbox
                            f.write(f'{classId} {abs(x)/videoWidth} {abs(y)/videoHeight} {abs(w)/videoWidth} {abs(h)/videoHeight}\n')
                    f.close()
            except:
                continue
        cap.release()
        print(f'Extracted {frameCount} frames from {videoName}')
        print(f"Train count: {trainCount}, Val count: {valCount}, Test count: {testCount}")
    print(os.listdir(outputImgDir))
    

if __name__=='__main__':
    sourceVidDir = os.path.abspath(os.path.join('..\..\data','task2_hands','train'))
    outputImgDir = os.path.abspath(os.path.join('..\..\data','task2'))
    outputLableDir = os.path.abspath(os.path.join('..\..\data','task2'))
    extractFrames(sourceImgDir=sourceVidDir, outputImgDir=outputImgDir, outputLableDir=outputLableDir)