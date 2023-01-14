#include <Servo.h>
Servo my_servo;

int duration;
int servo_pos;

void setup() {
  pinMode(5,OUTPUT);
  pinMode(6,INPUT);
  my_servo.attach(3);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(5, LOW);
  delayMicroseconds(2);

  digitalWrite(5,HIGH);
  delayMicroseconds(10);

  digitalWrite(5,LOW);

  duration = pulseIn(6, HIGH)/58;

  servo_pos = map(duration, 0, 131, 0, 360);

  my_servo.write(servo_pos);

  Serial.print(duration);
  Serial.println(" cm");
  Serial.println(servo_pos);

  delay(400);
  }
