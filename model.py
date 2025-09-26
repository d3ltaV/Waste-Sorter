from ultralytics import YOLO
model = YOLO("yolov8s.pt") 

def main():
    model.train(
        data="filtered_dataset/data.yaml",
        epochs=400,
        imgsz=640,
        batch=16,
        augment=True,
        device=0,
        optimizer="SGD"
    )

if __name__ == "__main__":
    main()