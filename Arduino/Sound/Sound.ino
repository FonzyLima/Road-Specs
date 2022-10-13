#define DO 8
unsigned long last_event = 0;

void setup() {
  pinMode(DO, INPUT); 
  Serial.begin(115200);
}

void loop() {
  int output = digitalRead(DO);
  Serial.println(output);
  if (output == HIGH) {
    Serial.println("Sound was detected!");
//    if (millis() - last_event > 25) {
//      Serial.println("Clap sound was detected!");
//    }
//    last_event = millis();
  }
  delay(100);
}
