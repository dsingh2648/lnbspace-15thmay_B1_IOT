int timer=10000;
void setup(){
  pinMode(13,OUTPUT);
}
void loop(){
  digitalWrite(13,HIGH);
 delay(timer);
 digitalWrite(13,LOW);
  delay (5000);
}
