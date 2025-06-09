void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int time = 0;

void loop() {
  // put your main code here, to run repeatedly:
  float reading = analogRead(A0);
  float volt = (reading / 1023) * 5;
  time = time + 1;

  Serial.print(time);
  Serial.print(",");
  Serial.println(volt);

  delay(10);
}
