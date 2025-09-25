import cv2
from ultralytics import YOLO


model = YOLO("C:/Users/Stoic/OneDrive/Desktop/Waste-Sorter/runs/detect/train17/weights/last.pt")

id_to_category = {
    0: ("Aluminium foil", "Recycling"),
    1: ("Bottle", "Recycling"), #bottle cap always supersedes bottle for some reason, so incorrectly named on purpose
    2: ("Bottle", "Recycling"),
    3: ("Broken glass", "Recycling"),
    4: ("Can", "Recycling"),
    5: ("Carton", "Recycling"),
    6: ("Cigarette", "Trash"),
    7: ("Cup", "Recycling"),
    8: ("Lid", "Recycling"),
    9: ("Other litter", "Trash"),
    10: ("Other plastic", "Trash"),
    11: ("Paper", "Recycling"),
    12: ("Plastic bag - wrapper", "Trash"),
    13: ("Plastic container", "Recycling"),
    14: ("Pop tab", "Recycling"),
    15: ("Straw", "Trash"),
    16: ("Styrofoam piece", "Trash"),
    17: ("Unlabeled litter", "Trash"),
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)

    # found online
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls)
            conf = float(box.conf)

            label = id_to_category.get(class_id, "Trash")

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2)

    cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

