import cv2

img = cv2.imread("ksunal.jpeg")
resized_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_cas.detectMultiScale(imgrey, scaleFactor=1.06, minNeighbors=5)
for x, y, w, h in faces: img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
cv2.imshow("Face Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
