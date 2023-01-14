import cv2
import time

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while 1==1:
    ret, image = vid.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = image.shape

    faces = face_cascade.detectMultiScale(image,1.5,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)

    x_pos = (2*x+w)//2
    y_pos = (2*y+h)//2

    cv2.line(image, (width//2,height//2), (x_pos,height//2), (255,255,255), 2)
    cv2.putText(image, "X_Pos: "+str(width//2-x_pos), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.line(image, (width//2, height//2), (width//2, y_pos), (255, 255, 255), 2)
    cv2.putText(image, "Y_Pos: "+str(height//2-y_pos), (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Image", image)

    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
    time.sleep(1)

vid.release()
cv2.destroyAllWindows()