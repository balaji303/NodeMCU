bool val;
void setup() {
  // put your setup code here, to run once:
pinMode(01,INPUT);
pinMode(16,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
val=digitalRead(01);
digitalWrite(16,val);
delay(500);
}
