// @Balaji303

#include <Arduino.h>

#define LED LED_BUILTIN
//LED->2
//.\wget.exe "https://ritchennai.org/naac/naac/" --recursive --level=5

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED, HIGH);
  Serial.println("LED is on");
  delay(1000);
  digitalWrite(LED, LOW);
  Serial.println("LED is off");
  delay(1000);
}