#include <Wire.h>

#define MOTORDUINO 0x10
#define COMDUINO 0x12
#define PROXYDUINO 0x14

double pos[3] = {0, 0, 0};
double ally[3] = {0, 0, 0};

double obs1[3] = {0, 0, 0};
double obs2[3] = {0, 0, 0};
double obs3[3] = {0, 0, 0};
int nobs = 1;

double speedOrder = 0;
double angleOrder = 0;

void setup() {
    getConfig();
    Wire.begin();
    attachInterrupt(0, alertProxy, SWITCH); //TODO
}

void loop() {
    checkCom();
    checkProximity();
    defineOrders();

}

void getConfig() {
    // Define nobs
    // Define pos initiale (fonction du côté)
}

void checkCom() {

}

void checkProximity() {
    //
    Wire.requestFrom(PROXYDUINO,2);
    while(Wire.available()<2);
    char c = Wire.read();
    if((c>>7)==1) {
        sendStopMotor();
    }

}

void defineOrders() {

}


void sendStopMotor() {

}

void alertProxy() {
    // TODO : si la pin d'interrupt est HIGH alerte proxy (stop moteurs etc)
    // Si LOW, reprendre le cours des activités
}