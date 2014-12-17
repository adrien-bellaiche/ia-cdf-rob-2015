__author__ = 'adrie_000'
# -*- coding: utf8 -*-

from General import Robot
from time import sleep

if __name__ == '__main__':
    ''' Explication : en lançant ce script, le soft va en permanence checker si la mainduino a la languette tirée (info
    stockée dans robot.started, True si tirée, False si en place).
    Si la languette est repositionnée, la boucle du robot va se terminer.
    Une fois la languette retirée, le système reboucle.
    Ceci permettra de ne pas avoir de soucis avec une tirette accidentellement retirée trop tôt.
    '''

    robot = Robot()
    while True:
        if robot.started:
            robot.start()
        sleep(0.1)