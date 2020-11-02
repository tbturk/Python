import cv2
import imutils
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.resize(cv2.imread("license_plate.png"), (620, 480))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray = cv2.bilateralFilter(imgray, 13, 15, 15)
edged = cv2.Canny(imgray, 300, 0)
cv2.imshow("Edged",edged)
cv2.waitKey(0)
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print ("No contour detected")
else:
     detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(imgray.shape, np.uint8)
new_image_with_contours = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image_with_contours = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
cropped = imgray[topx:bottomx+1, topy:bottomy+1]

plaka_yazi = pytesseract.image_to_string(cropped, config='--psm 11')
print(plaka_yazi)
