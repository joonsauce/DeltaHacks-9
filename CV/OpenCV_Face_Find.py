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

    x_pos_centre = x_pos - width//2 + 100
    y_pos_centre = y_pos - height//2 + 100

    x_pos_centre = x_pos_centre//20
    y_pos_centre = y_pos_centre//20

    if x_pos_centre < 0 or y_pos_centre < 0:
        x_pos_centre = 5
        y_pos_centre = 5

    cv2.line(image, (width//2,height//2), (x_pos,height//2), (255,255,255), 2)
    cv2.putText(image, "X_Pos: "+str(x_pos_centre), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.line(image, (width//2, height//2), (width//2, y_pos), (255, 255, 255), 2)
    cv2.putText(image, "Y_Pos: "+str(y_pos_centre), (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Image", image)

    ser = serial.Serial(baudrate=115200, port='COM4')
    if x_pos_centre == 1:
        ser.write(b'1')
    if x_pos_centre == 2:
        ser.write(b'2')
    if x_pos_centre == 3:
        ser.write(b'3')
    if x_pos_centre == 4:
        ser.write(b'4')
    if x_pos_centre == 5:
        ser.write(b'5')
    if x_pos_centre == 6:
        ser.write(b'6')
    if x_pos_centre == 7:
        ser.write(b'7')
    if x_pos_centre == 8:
        ser.write(b'8')
    if x_pos_centre == 9:
        ser.write(b'9')
    if y_pos_centre == 1:
        ser.write(b'1')
    if y_pos_centre == 2:
        ser.write(b'2')
    if y_pos_centre == 3:
        ser.write(b'3')
    if y_pos_centre == 4:
        ser.write(b'4')
    if y_pos_centre == 5:
        ser.write(b'5')
    if y_pos_centre == 6:
        ser.write(b'6')
    if y_pos_centre == 7:
        ser.write(b'7')
    if y_pos_centre == 8:
        ser.write(b'8')
    if y_pos_centre == 9:
        ser.write(b'9')
    ser.close()

    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
    time.sleep(0.1)

vid.release()
cv2.destroyAllWindows()