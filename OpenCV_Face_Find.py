import serial
import cv2
import time

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while 1==1:
    ret, image = vid.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (11,11), 0)
    height, width = image.shape

    faces = face_cascade.detectMultiScale(image,1.5,4)

    x_alt = y_alt = h_alt = w_alt = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 1)
        x_alt = x
        y_alt = y
        w_alt = w
        h_alt = h

    x_pos = (2*x_alt+w_alt)//2
    y_pos = (2*y_alt+h_alt)//2

    x_pos_centre = x_pos - width//2
    y_pos_centre = y_pos - height//2

    if x_pos_centre > width//2-20 or y_pos_centre > height//2-20:
        x_pos = width//2
        y_pos = height//2

    if x_pos_centre > 99:
        x_pos_centre = 0
    if x_pos_centre < -99:
        x_pos_centre = 0
    if y_pos_centre > 99:
        y_pos_centre = 0
    if y_pos_centre < -99:
        y_pos_centre = 0

    cv2.line(image, (width//2,height//2), (x_pos,height//2), (255,255,255), 2)
    cv2.putText(image, "X_Pos: "+str(x_pos_centre), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.line(image, (width//2, height//2), (width//2, y_pos), (255, 255, 255), 2)
    cv2.putText(image, "Y_Pos: "+str(y_pos_centre), (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    serial_pos = x_pos_centre*100+y_pos_centre
    cv2.putText(image, "S_Pos: " + str(serial_pos), (10, 125), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Image", image)

    ser = serial.Serial(baudrate=115200, port='COM4')
    ser.write(b'serial_pos')
    ser.write(b'/n')
    ser.close()

    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
    time.sleep(0.4)

vid.release()
cv2.destroyAllWindows()