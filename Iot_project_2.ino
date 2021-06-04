/// Message Display on Lcd
#include <LiquidCrystal.h>
LiquidCrystal lcd(9,8,5,4,3,2);
int i=0,j=0;
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
pinMode(12,INPUT);
pinMode(13,INPUT);
lcd.createChar(1,man);
lcd.begin(16,2);
}
void loop() {
 
   int msg=digitalRead(13);
  if(msg==1){
    lcd.begin(16,2);
  lcd.setCursor(0,0);
    lcd.write(1);
    lcd.setCursor(1,0);
    lcd.print("HELLO");
    lcd.setCursor(0,1);
    lcd.print("YOU ARE WELCOME");
  }
  int scroll=digitalRead(12);
  if(scroll==1){
  for (int j=15;j>=-21;j--)
    {
      lcd.setCursor(j,i);
      lcd.print("IT'S MY FIRST PROJECT");
      delay(200);
      lcd.clear();
      lcd.setCursor(1,1);
      lcd.print("DUSHYANT SINGH");
    }for (int j=-21;j<=15;j++)
    {
      lcd.setCursor(j,i);
      lcd.print("IT'S MY FIRST PROJECT");
      delay(200);
      lcd.clear();
      lcd.setCursor(1,1);
      lcd.print("DUSHYANT SINGH");
    }
}
}
