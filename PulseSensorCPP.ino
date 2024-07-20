#include <PulseSensorPlayground.h>

PulseSensorPlayground pulseSensor;

void setup() {
  Serial.begin(9600);
  pulseSensor.analogInput(A0); // Connect the pulse sensor to analog pin A0
  pulseSensor.begin();
}

void loop() {
  int heartRate = pulseSensor.getBeatsPerMinute();
  if (pulseSensor.sawStartOfBeat()) {
    Serial.print("Heart Rate: ");
    Serial.println(heartRate);
  }
}
