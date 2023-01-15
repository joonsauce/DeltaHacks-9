#include <ESP32_Servo.h>
#include <LiquidCrystal.h>

#define LCD_RS 22
#define LCD_EN 23
#define LCD_D4 21   
#define LCD_D5 19
#define LCD_D6 18
#define LCD_D7 17
#define tempPin 25

Servo MyServo1;
Servo MyServo2;
LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

byte readAnalogESP(int pin) {
    return map(analogRead(pin), 0, 4095, 0, 1023);
}

float temperature;
bool enabled;

int Duration;
int ServoPos;

int ServoPin1 = 26;
int ServoPin2 = 4;
int EchoPin = 33;
int TrigPin = 32;

void setup() {
  pinMode(TrigPin,OUTPUT);
  pinMode(EchoPin,INPUT);
  MyServo1.attach(ServoPin1);
  MyServo2.attach(ServoPin2);
  lcd.begin(16, 2);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TrigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin,LOW);

  Duration = pulseIn(EchoPin, HIGH)/58;

  ServoPos = map(Duration, 0, 131, 0, 179);

  int x, y;
  if(Serial.available()>0){
    int x1 = Serial.read();
    int x2 = Serial.read();
    x = x1*10+x2
    int y1 = 

   // x = map(x_pos, 0, 99, 0, 179);
   // y = map(y_pos, 0, 99, 0, 179);
  }
 
  MyServo1.write(x);
  MyServo2.write(y);
  Serial.print("x_pos: ");
  Serial.println(x);
  Serial.print("y_pos: ");
  Serial.println(y);

  int val = readAnalogESP(tempPin);
  float volts = (val / 1024.0) * 5.0;
  temperature = (volts - 0.7) * 100;
  //Serial.println(temperature);
  //Serial.println(readAnalogESP(tempPin));
  display(x_pos, enabled, 0);
  display(y_pos, enabled, 1);
  delay(300);
  }


void display(int temperature, bool enabled, int line){
  lcd.setCursor(0, line);
  lcd.print("Temp:");
  lcd.setCursor(9, line);
  lcd.print("ON:");
  lcd.setCursor(5, line);
  lcd.print(temperature);
  lcd.setCursor(12, line);
  lcd.print(enabled);
  //Serial.println();
}
