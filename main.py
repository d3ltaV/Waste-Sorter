from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/Stoic/OneDrive/Desktop/Waste-Sorter/runs/detect/train17/weights/last.pt")

id_to_category = {
    0: ("Aluminium foil", "Recycling"),
    1: ("Bottle", "Recycling"),
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

last_detected = {"label":"None", "category":"None","confidence":0.0}

def generate_frames():
    global last_detected
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
    
        results = model(frame, verbose=False)

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_id = int(box.cls)
                conf = float(box.conf)

                label, category = id_to_category.get(class_id, ("Unknown", "Trash"))

                last_detected = {
                    "label": label,
                    "category": category,
                    "confidence": round(conf, 2)
                }

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}",
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detection')
def detection():
    return jsonify(last_detected)

if __name__ == "__main__":
    app.run(debug=True)