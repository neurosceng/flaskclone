from ultralytics import YOLO
import cv2
import requests


def yolov8_predict(results):
    result = results[0].numpy()

    classes = result.boxes.cls
    confidence = result.boxes.conf
    bbox = result.boxes.xyxy

    for cls, conf, xyxy in zip(classes, confidence, bbox):
        xmin, ymin, xmax, ymax = xyxy

        url = "https://ultralytics.com/images/bus.jpg"
        response = requests.get(url)
        with open("bus.jpg", "wb") as f:
            f.write(response.content)

        img = cv2.imread("bus.jpg")
        cv2.rectangle(img,
                      pt1=(int(xmin), int(ymin)),
                      pt2=(int(xmax), int(ymax)),
                      color=(0, 0, 255),
                      thickness=3)
        cv2.imwrite("bus_result.jpg", img)


if __name__ == "__main__":
    model = YOLO('yolov8l.pt')
    results = model('https://ultralytics.com/images/bus.jpg', save=False)
    yolov8_predict(results)