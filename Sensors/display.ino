#include <LiquidCrystal.h>

#define LCD_RS 22
#define LCD_EN 23
#define LCD_D4 21   
#define LCD_D5 19
#define LCD_D6 18
#define LCD_D7 17
#define tempPin 25

LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

float temperature;
bool enabled;

byte readAnalogESP(int pin) {
    return map(analogRead(pin), 0, 4095, 0, 1023);
}

void setup() {
    Serial.begin(115200);
    lcd.begin(16, 2);
}

void loop() {
    int val = readAnalogESP(tempPin);
    float volts = (val / 1024.0) * 5.0;
    temperature = (volts - 0.7) * 100;
    Serial.println(temperature);
    Serial.println(readAnalogESP(tempPin));
    display(temperature, enabled, 1);
    delay(1000);
}


void display(int temperature, bool enabled, int rV){
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Temp:");
    lcd.setCursor(9, 0);
    lcd.print("ON:");
    lcd.setCursor(5, 0);
    lcd.print(temperature);
    lcd.setCursor(12, 0);
    lcd.print(enabled);
    Serial.println();
}
