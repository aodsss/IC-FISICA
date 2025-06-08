void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float reading = analogRead(A0);
  float volt = (reading / 1023) * 5;

  Serial.println(volt);

  delay(100);
}
