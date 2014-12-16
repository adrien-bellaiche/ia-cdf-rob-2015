# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from serial import *

LEFT = 0
RIGHT = 1
MOTOR = 0
HOKUYO = 1
codes = ['0', '1']


class GeneralSerialCom():
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        if port is None:
            possible_ports = self.findPorts()
            validPort = self.testPort(possible_ports, specific_test_request, specific_test_answer)
            if validPort is None:
                quit('Error : no serial port openable for request ' + specific_test_request
                     + ' and answer ' + specific_test_answer)
            self.port = validPort
        self.com = Serial(self.port)

    def write(self, message):
        self.com.write(message)

    def read(self):
        return self.com.read()


def find_ports():
    # TODO
    return 0


def test_port(possible_ports, specific_test_request, specific_test_answer):
    # TODO : ouvrir chaque connexion série possible, lui envoyer specific_test_request
    #  verifier si elle renvoie specific_test_answer
    return 0


class ArduinoCom(GeneralSerialCom):
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)

    def request_mission_parameters(self):
        self.write('RSS')  # Request Start Side
        if str(self.com.read(size=4)) == 'LEFT':
            return LEFT
        else:
            return RIGHT

    def hear_start(self):
        self.write('SL')  # Start Listening
        while self.com.read(1) != 'S':
            pass

    def send_conf(self, code):
        self.write(codes[code])

    def send_orders(self, orders):
        # TODO
        # Transforme orders et l'envoie
        pass


class HokuyoCom(GeneralSerialCom):
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)

    def get_fresh_data(self):
        # TODO
        pass
