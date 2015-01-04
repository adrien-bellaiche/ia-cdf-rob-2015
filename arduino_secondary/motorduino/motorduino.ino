#include <Wire.h>

#define MOTORDUINO 0x10
#define COMDUINO 0x12
#define PROXYDUINO 0x14


void setup() {
    Wire.begin(MOTORDUINO);

}


void loop() {

}

void requestEvent() {

}

void receiveEvent(int bytes) {

}