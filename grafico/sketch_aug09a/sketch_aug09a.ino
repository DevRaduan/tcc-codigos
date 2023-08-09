const int ledPins[] = {4, 5, 6, 11, 12, 13}; // Pinos dos LEDs
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command >= '1' && command <= '6') {
      int ledIndex = command - '1';
      digitalWrite(ledPins[ledIndex], !digitalRead(ledPins[ledIndex])); // Inverte o estado do LED
    }
  }
}
