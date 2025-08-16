from ultralytics import YOLO
import torch
import os
cuda_available = torch.cuda.is_available()
print(f"CUDA Available: {cuda_available}")
data_dir = os.path.abspath('../../data')
task2_data = os.path.join(data_dir,"task2/data.yaml")
print(os.path.exists(task2_data))
model = YOLO(model='yolov8s.yaml',
             task='detect')
result = model.train(data=task2_data,
                     epochs=200,
                     batch=64,
                     imgsz=420)