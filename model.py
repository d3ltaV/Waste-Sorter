from ultralytics import YOLO

model = YOLO("yolov8s.pt") #changed to 8s
def main():
    model.train(
        data="C:/Users/Stoic/OneDrive/Desktop/Waste-Sorter/datasets/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        augment=True,
        device=0
    )

if __name__ == "__main__":
    main()