import cv2
import numpy as np

class Escaner():
    def escanear(self):
        capture = cv2.VideoCapture(0)

        while(capture.isOpened()):
            ret, frame = capture.read()
            if (cv2.waitKey(1)) == ord('s'):
                break
            qrDetector = cv2.QRCodeDetector()
            data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
            if len(data) > 0:
                capture.release()
                cv2.destroyAllWindows()
                return data
                cv2.imshow('webCam', rectifiedImage)
            else:
                cv2.imshow('webCam', frame)

        capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    test = Escaner()
    res = test.escanear()
    print(res)