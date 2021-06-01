void setup() {
  for(int i=2;i<=8;i++) 
  pinMode(i,OUTPUT);
  for(int i=13;i>=10;i--) 
  pinMode(i,INPUT);
}
void pat1(){
    for(int i= 8;i>=2;i--){
    digitalWrite(i,HIGH);
    delay(100);
    digitalWrite(i,LOW);
    delay(100);
  }
  for(int i=2;i<=8;i++){
    digitalWrite(i,HIGH);
    delay(100);
    digitalWrite(i,LOW);
    delay(100);
  }

}
void pat2(){
  int j=5;
  for(int i=5;i>=2 ;i--){
    digitalWrite(i,HIGH);
    digitalWrite(j,HIGH);
    delay(100);
    digitalWrite(i,LOW);
    digitalWrite(j,LOW);
    j++;
  }
}

void pat3(){
  int j= 8;
  for(int i= 2;i<=5 ;i++){
    digitalWrite(i,HIGH);
    digitalWrite(j,HIGH);
    delay(100);
    digitalWrite(i,LOW);
    digitalWrite(j,LOW);
    j--;
  }
}
void loop() {
  
  int pattern1 = digitalRead(13);
  int pattern2 = digitalRead(12);
  int pattern3 = digitalRead(11);
  
  if(pattern1) pat1();
  if(pattern2) pat2();
  if(pattern3) pat3();

}
