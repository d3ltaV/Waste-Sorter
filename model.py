from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="C:/Users/Stoic/OneDrive/Desktop/Waste-Sorter/datasets/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
