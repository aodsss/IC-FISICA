void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

float time = 0.00;

void loop() {
  // put your main code here, to run repeatedly:
  float reading = analogRead(A0);
  float volt = (reading / 1023) * 5;
  time = time + 100;

  Serial.print(time);
  Serial.print(",");
  Serial.println(volt);

  delay(100);
}
