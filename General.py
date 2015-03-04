# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from SerialCom import HokuyoCom
from HokuyoHandler import HokuyoHandler
from Pathfinding import Pathfinder

sideDict = {0: "left.txt",
            1: "right.txt"}

startDict = {0: [0, 0, 0],
             1: [0, 0, 0]}

class Robot():
    def __init__(self):
        # TODO : add thread for localisation
        # TODO : add motor command
        #TODO : add visual indicators for confirmation
        #self.objectives = None #Useless for now. Might be useful later
        self.hokuyo_com = HokuyoCom()
        self.current_objective = None
        self.obstacles = []
        self.position = startDict[self.startSide()]
        self.pathfinder = Pathfinder(self)  # Gère le pathfinding local
        self.hokuyo_handler = HokuyoHandler(self.hokuyo_com, self)  # Gère l'hokuyo et traite ses données
        self.parse(sideDict[self.startSide()])
        self.started = False
        self.orders = [0, 0]
        self.pwms = [127, 127, 127, 127]  # Left front, left rear, right front, right rear

    def start(self):
        # caractérisé par la réception d'un message de l'arduino
        self.hokuyo_handler.start()  # démarre la détection
        self.started = True
        while self.started:
            # Pathfinding local
            self.orders = self.pathfinder.get_orders(self.current_objective.position)
            # Envoi des ordres de direction-vitesse-rotation à la motor_arduino dans le repère
        print 'Mission over'

    def startSide(self):
        # TODO
        pass

    def startOdometryServer(self):
        # TODO
        pass

    def OdometryRoutin(self):
        # TODO :
        # read the odometry pseudo-files
        # deduces the current speed for each wheel
        # PID to match the order
        pass

    def orders2motors(self, orders):
        # TODO : invert state equations here

        pass

    def parse(self, textfilename):
        # TODO : lit le fichier d'objectifs, prépare les données
        pass