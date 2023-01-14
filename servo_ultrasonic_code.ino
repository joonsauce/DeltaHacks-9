#include <C:\Users\Quinn\Documents\Arduino\ESP32_Servo.h>
Servo MyServo;

int Duration;
int ServoPos;

int ServoPin = 18;
int EchoPin = 21;
int TrigPin = 19;

void setup() {
  pinMode(TrigPin,OUTPUT);
  pinMode(EchoPin,INPUT);
  MyServo.attach(ServoPin);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(TrigPin,HIGH);
  delayMicroseconds(10);

  digitalWrite(TrigPin,LOW);

  Duration = pulseIn(EchoPin, HIGH)/58;

  ServoPos = map(Duration, 0, 131, 0, 360);

  MyServo.write(ServoPos);

  Serial.print(Duration);
  Serial.println(" cm");
  Serial.println(ServoPos);

  delay(400);
  }
