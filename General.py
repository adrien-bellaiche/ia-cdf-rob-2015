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
        # TODO : add visual indicators for confirmation
        #self.objectives = None #Useless for now. Might be useful later
        self.hokuyo_com = HokuyoCom()
        self.current_objective = None
        self.obstacles = []
        self.position = startDict[self.start_side()]
        self.orientation = self.start_side() * 3.14
        self.pathfinder = Pathfinder(self)  # Gère le pathfinding local
        self.hokuyo_handler = HokuyoHandler(self.hokuyo_com, self)  # Gère l'hokuyo et traite ses données
        self.parse(sideDict[self.start_side()])
        self.started = False
        self.orders = [0, 0]
        self.wheel_radius = 0.02
        self.ticks_per_turn = 100 * 12
        self.motor_spacing = 0.15
        self.kp_rot = 1
        self.last_ticks = [0, 0, 0, 0]  # Left front, left rear, right front, right rear
        self.odometry_server_period = 0.01  # 10ms
        self.odometry_half_frequency = 0.5 / self.odometry_server_period

    def start(self):
        self.hokuyo_handler.start()  # démarre la détection
        self.startOdometryServer()
        self.started = True
        while self.started:
            # Pathfinding local
            self.orders = self.orders2motors(self.pathfinder.get_orders(self.current_objective.position))
            # Envoi des ordres de direction-vitesse-rotation à la motor_arduino dans le repère
        print 'Mission over'

    def start_side(self):
        # TODO
        return 0

    def startOdometryServer(self):
        # TODO : add here 4 threads, each one looking on two points.
        pass

    def OdometryRoutin(self):
        # TODO :
        # read the odometry pseudo-files
        temp_read = ['0', '0', '0', '0']  # open('/proc/odometry').readline().split()
        # deduces the current speed for each wheel
        delta_ticks = [int(temp_read[i]) - self.last_ticks[i] for i in [0, 1, 2, 3]]
        current_speed = (delta_ticks[0] + delta_ticks[2]) * self.odometry_half_frequency
        current_rotation = (delta_ticks[2] - delta_ticks[1]) * self.odometry_half_frequency / self.motor_spacing
        # PID to match the order

        pass

    def orders2motors(self, orders):
        # Determiner une vitesse de rotation
        w = self.kp_rot * (orders[1] - self.orientation)
        v1 = orders[0] - w * self.motor_spacing / 2
        v2 = orders[0] - w * self.motor_spacing / 2
        return [v1, v2]

    def parse(self, textfilename):
        # TODO : lit le fichier d'objectifs, prépare les données
        pass