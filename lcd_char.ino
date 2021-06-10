#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,6,5,4,3);
byte arrowhead[8]={
  0b00001,
  0b00011,
  0b00111,
  0b01111,
  0b00111,
  0b00011,
  0b00001,
  0b00000,
};

byte arrowbody[8]={
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b00000,
  0b00000,
  0b00000
};

byte arrowtail[8]={
  0b00011,
  0b00111,
  0b11111,
  0b11111,
  0b11111,
  0b00111,
  0b00011,
  0b00000,
};

byte man[8] = {
  0b01110,
  0b01110,
  0b00100,
  0b01110,
  0b10101,
  0b00100,
  0b01010,
  0b10001,
};

void setup() {
  lcd.createChar(0,arrowhead);
  lcd.createChar(1,arrowbody);
  lcd.createChar(2,arrowtail);
  lcd.createChar(3,man);
  lcd.begin(16, 2);
}

void loop() {
  int n,m;
  n=0;
  m=15;
  while(n!=16){
    lcd.clear();
    delay(50);
    lcd.setCursor(n+0,0);
    lcd.write(3);
    lcd.setCursor(n+1,0);
    lcd.write(byte(0));
    lcd.setCursor(n+2,0);
    lcd.write(1);
    lcd.setCursor(n+3,0);
    lcd.write(2);
    delay(50);
    n++;
  }
  while(m!=-1){
    lcd.clear();
    delay(50);
    lcd.setCursor(m-2,1);
    lcd.write(byte(0));
    lcd.setCursor(m-1,1);
    lcd.write(1);
    lcd.setCursor(m,1);
    lcd.write(2);
    lcd.setCursor(m-3,1);
    lcd.write(3);
    delay(50);
    m--;
  }
}
