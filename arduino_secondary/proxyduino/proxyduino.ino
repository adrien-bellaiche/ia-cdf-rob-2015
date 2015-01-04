#include <Wire.h>

#define MOTORDUINO 0x10
#define COMDUINO 0x12
#define PROXYDUINO 0x14

#define US_FRONT A0
#define US_LEFT A1
#define US_RIGHT A2
#define US_DIAG_LEFT A3
#define US_DIAG_RIGHT A4
#define US_REAR A5

#define IR_FRONT A0
#define IR_LEFT A1
#define IR_RIGHT A2
#define IR_DIAG_LEFT A3
#define IR_DIAG_RIGHT A4
#define IR_REAR A5

#define REAR_START 1
#define LEFT_START 4
#define LEFT_DIAG_START 7
#define FRONT_START 9
#define RIGHT_DIAG_START 12
#define RIGHT_START 15

#define REAR_BITS 3
#define LEFT_BITS 3
#define LEFT_DIAG_BITS 2
#define FRONT_BITS 3
#define RIGHT_BITS 3
#define RIGHT_DIAG_BITS 2

#define FRONT_ALERT 0
#define REAR_ALERT 1
#define LEFT_DIAG_ALERT 2
#define RIGHT_DIAG_ALERT 3
#define LEFT_ALERT 4
#define RIGHT_ALERT 5

#define alertPin 10

int state = 0;
int newState = 0;
bool raised[6] = {false, false, false, false, false, false};


void setup() {
    Wire.begin(PROXYDUINO);
    Wire.onReceive(receiveEvent);
    Wire.onRequest(requestEvent);
}


void loop() {
    resetState();
    checkRanging(US_FRONT, IR_FRONT, FRONT_START, FRONT_BITS, FRONT_ALERT);
    checkRanging(US_REAR, IR_REAR, REAR_START, REAR_BITS, REAR_ALERT);
    checkRanging(US_DIAG_RIGHT, IR_DIAG_RIGHT, RIGHT_DIAG_START, RIGHT_DIAG_BITS, RIGHT_DIAG_ALERT);
    checkRanging(US_LEFT, IR_LEFT, LEFT_START, LEFT_BITS, LEFT_DIAG_ALERT);
    checkRanging(US_RIGHT, IR_RIGHT, RIGHT_START, RIGHT_BITS, RIGHT_DIAG_ALERT);
    validateState();
}

void requestEvent() {

}

void receiveEvent(int bytesReceived) {

}

void checkRanging(int us_pin, int ir_pin, byte alert_start, byte alert_bits, byte alertID){
    // TODO : if too close raise alert
    // else lowerAlert & encode distance into alert
}

void resetState(){
    newState = 0;
}

void validateState() {

}

void raiseAlert(int alertID) {
    raised[alertID] = true;
    digitalWrite(alertPin, HIGH);
}

void lowerAlert(int alertID) {
    raised[alertID] = false;
    for(int k=0;k<6;k++) {
        if(raised[k]) {
            return;
        }
    }
    digitalWrite(alertPin, LOW);
}