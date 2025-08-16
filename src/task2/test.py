import cv2
import json

sample_image_path = 'C:/Users/allen_rg6201i/gitProjects/traumaThomsonChallenge/data/task2/train/images/P05_02_frame_00456.jpg'
sample_image = cv2.imread(sample_image_path)

annotation_path = 'C:/Users/allen_rg6201i/gitProjects/traumaThomsonChallenge/data/task2_hands/train/bbox/P05_02/frame_000456.json'
annotaion = json.load(open(annotation_path, 'r'))

for annotation in annotaion['annotations']:
    bbox = annotation['bbox']
    print(f"Bounding Box: {bbox}")
    cv2.rectangle(sample_image,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,0),2)

cv2.imshow('Sample Image with Annotations', sample_image)
cv2.waitKey(0)
cv2.destroyAllWindows()