import cv2
import numpy as np
import pyautogui

yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0
cap = cv2.VideoCapture(0)
# j for downward
# k for upwards
while True:
    ret, frame = cap.read()
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(c)
            thing = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(thing, 'Object detected ,Yellow', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 3)
            if y < prev_y:
                pyautogui.press('space')
            prev_y = y

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('s'):
        break

cv2.release()
cv2.destroyAllWindows()
