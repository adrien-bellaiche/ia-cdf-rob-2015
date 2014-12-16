# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from serial import *


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

    def findPorts(self):
        # TODO
        return 0

    def testPort(self, possible_ports, specific_test_request, specific_test_answer):
        # TODO : ouvrir chaque connexion série possible, lui envoyer specific_test_request
        #  verifier si elle renvoie specific_test_answer
        return 0


class ArduinoCom(GeneralSerialCom):
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)

    def request_mission_parameters(self):
        # TODO : faire la requete auprès de l'arduino et renvoyer 'LEFT' ou 'RIGHT' selon le coté de départ donné par l'arduino
        return 0

    def hear_start(self):
        # TODO
        return 0


class HokuyoCom(GeneralSerialCom):
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)

    def get_fresh_data(self):
        # TODO
        pass