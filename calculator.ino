#include <LiquidCrystal.h> 
#include <Keypad.h> 
LiquidCrystal lcd(A0,A1,A2,A3,A4,A5); 
char buttons [4][4] = {
  {'7', '8', '9', '/'},
  {'4', '5', '6', '*'},
  {'1', '2', '3', '-'}, 
  {'C', '0', '=', '+'}
};
byte col[4]= {9,8,7,6};
byte row[4]= {13,12,11,10}; 

Keypad keypad = Keypad( makeKeymap(buttons), row, col, 4,4 );

boolean presentValue = false;
boolean next = false;
boolean final = false;         
String num1, num2;
int answer;
char op;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.setCursor(0, 0);
  lcd.print ("CALCULATOR");
  delay(1000);
  lcd.clear (); 
} 
void loop() {
  char button = keypad.getKey();
  
if (button != NO_KEY && (button == '1' || button == '2' || button == '3' || button == '4' || button == '5' || button == '6' || button == '7' || button == '8' || button == '9' || button == '0'))
  {
    if (presentValue != true)
    {
      num1 = num1 + button;
      int numLength = num1.length();
      lcd.setCursor(15 - numLength, 0);
      lcd.print(num1);
    }
    else
    {
      num2 = num2 + button;
      int numLength = num2.length();
      lcd.setCursor(15 - numLength, 1);
      lcd.print(num2);
      final = true;
    }
  }

  else if (presentValue == false && button != NO_KEY && (button == '/' || button == '*' || button == '-' || button == '+'))
  {
    if (presentValue == false)
    {
      presentValue = true;
      op = button;
      lcd.setCursor(15, 0);
      lcd.print(op);
    }
  }

  else if (final == true && button != NO_KEY && button == '=') {
  if (op == '/') {
      answer = num1.toInt() / num2.toInt();
    }
    else if (op == '*') {
      answer = num1.toInt() * num2.toInt();
      }
   else if (op=='-') {
      answer = num1.toInt()- num2.toInt();
    }
      else if (op == '+') {
      answer = num1.toInt() + num2.toInt();
    }
    lcd.clear();
    lcd.setCursor(15, 0);
    lcd.autoscroll();
    lcd.print(answer); 
    lcd.noAutoscroll();
  }
  else if (button != NO_KEY && button == 'C') {
    lcd.clear();
    presentValue = false;
    final = false;
    num1 = "";
    num2 = "";
    answer = 0;
    op = ' ';
  }}
