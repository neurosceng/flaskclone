from ultralytics import YOLO
import cv2
import requests


def yolo_predict(results,jpg_path):
    result = results[0].numpy()

    classes = result.boxes.cls
    confidence = result.boxes.conf
    bbox = result.boxes.xyxy

    for cls, conf, xyxy in zip(classes, confidence, bbox):
        xmin, ymin, xmax, ymax = xyxy
        '''
        url = "https://ultralytics.com/images/bus.jpg"
        response = requests.get(url)
        with open("bus.jpg", "wb") as f:
            f.write(response.content)
        '''
        img = cv2.imread(jpg_path)
        cv2.rectangle(img,
                      pt1=(int(xmin), int(ymin)),
                      pt2=(int(xmax), int(ymax)),
                      color=(0, 0, 255),
                      thickness=3)
        save_folder_path = '/Users/okmac/flask/flaskbook/apps/minimalapp/result/'
        save_path = save_folder_path + 'result.jpg'
        cv2.imwrite(save_path, img)


if __name__ == "__main__":
    model = YOLO('/Users/okmac/flask/flaskbook/yolov5/yolov5s.pt')
    folder_path = '/Users/okmac/flask/flaskbook/apps/minimalapp/'
    jpg_path = folder_path + 'bus.jpg'
    #results = model('https://ultralytics.com/images/bus.jpg', save=False)
    results = model(jpg_path , save=False)
    yolo_predict(results,jpg_path)