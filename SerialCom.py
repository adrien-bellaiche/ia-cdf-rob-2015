# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from serial import *
from math import pi
from time import sleep
from threading import Thread
import sys
import glob

LEFT = 0
RIGHT = 1
MOTOR = 0
HOKUYO = 1
codes = ['0', '1']


class GeneralSerialCom():
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        if port is None:
            possible_ports = find_ports()
            valid_port = test_port(possible_ports, specific_test_request, specific_test_answer)
            if valid_port is None:
                quit('Error : no serial port openable for request ' + specific_test_request
                     + ' and answer ' + specific_test_answer)
            self.port = valid_port
        self.com = Serial(self.port)

    def write(self, message):
        self.com.write(message)

    def read(self):
        return self.com.read()


def find_ports():
    """Lists serial ports
    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for portID in ports:
        try:
            s = Serial(portID)
            s.close()
            result.append(portID)
        except (OSError, SerialException):
            pass
    return result


def test_port(possible_ports, specific_test_request, specific_test_answer):
    # TODO : ouvrir chaque connexion série possible, lui envoyer specific_test_request
    #  verifier si elle renvoie specific_test_answer
    return 0


class ArduinoCom(GeneralSerialCom, Thread):
    def __init__(self, data_center, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)
        Thread.__init__(self)
        self.started = False
        self.data_center = data_center
        self.order_list = []

    def request_mission_parameters(self):
        self.write('RSS')  # Request Start Side
        if str(self.com.read(size=4)) == 'LEFT':
            return LEFT
        else:
            return RIGHT

    def run(self):
        while self.started:
            if len(self.order_list) > 0:
                self.com.write(self.order_list.pop(0))
            n = self.com.inWaiting()
            if n > 0:
                self.parse_receiver(self.com.read(n))

    def send(self, order):
        self.order_list.append(order)

    def send_conf(self, code):
        self.send(codes[code])

    def send_orders(self, orders):
        # TODO
        # Transforme orders et les envoie
        pass

    def parse_receiver(self, data):
        for letter in data:
            if data == 'W':
                self.data_center.started = True
            elif data == 'Q':
                self.data_center.started = False


class HokuyoCom(GeneralSerialCom):
    def __init__(self, port=None, specific_test_request=None, specific_test_answer=None):
        GeneralSerialCom.__init__(self, port, specific_test_request, specific_test_answer)

    def get_fresh_data(self):
        # TODO : test
        start = 44
        end = 725
        # Returns [arraylist of millimeters,arraylist of corresponding rads]
        self.write('M')
        self.write('S')
        s = [bytes(0x30+start/1000), bytes(0x30+(start/100) % 10), bytes(0x30+(start/10) % 10), bytes(0x30+start % 10)]
        e = [bytes(0x30+(end/1000)), bytes(0x30+(end/100) % 10), bytes(0x30+(end/10) % 10), bytes(0x30+end % 10)]
        cluster = 1
        cc = [bytes(0x30 + ((cluster / 10) % 10)), bytes(0x30 + (cluster % 10))]
        si = 0x30
        sn = [0x30, 0x31]
        self.write(s)
        self.write(e)
        self.write(cc)
        self.write(si)
        self.write(sn)
        self.write(LF)
        doub = []
        for k in range(start, end):
            doub.append(((k-44)*4*pi/(3*681)-2*pi/3))
             # 681 : max size of mesure on correct stuff
        sleep(0.250)
        ret = []
        mes_count = 0
        count = 0
        possible_end = False
        while self.com.inWaiting() > 0:
            c1 = self.com.read()
            count += 1
            if not possible_end or c1 != LF:
                c2 = self.com.read()
                count += 1
                if c1 == 'M' and c2 == 'S':
                    print 'MS SPOTTED : some nexts avoided'
                    for k in range(47):
                        self.com.read()
                    print 'End of avoidance'
                elif c1 != '?' and c2 != LF:
                    mes_count += 1
                    data = ((c1-0x30) << 6) | (c2 - 0x30)
                    print 'Mesure', mes_count, 'is', data
                    ret.append(data)
                else:
                    print 'End of block detected at :',count,'bytes'
                    count = 0
                    possible_end = True
            else:
                possible_end = False
        return [ret, doub]