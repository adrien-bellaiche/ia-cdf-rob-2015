# -*- coding: utf8 -*-
__author__ = 'adrie_000'

import time

from SerialCom import ArduinoCom, HokuyoCom, LEFT, MOTOR, HOKUYO
from HokuyoHandler import HokuyoHandler
from Strategy import StrategicMind
from Pathfinding import Pathfinder
from Utils import objectives


class Robot():
    def __init__(self):
        self.ardu_com = ArduinoCom(self, specific_test_request='V', specific_test_answer='arduino')
        self.ardu_com.start()
        self.position = [0, 0]
        self.radius = 185
        self.ardu_com.send_conf(MOTOR)
        self.hokuyo_com = HokuyoCom()
        self.ardu_com.send_conf(HOKUYO)
        self.ori_init = 0
        self.orientation = 0
        self.current_objective = None
        if self.ardu_com.request_mission_parameters() == LEFT:
            self.objectives = objectives("left")
        else:
            self.objectives = objectives("right")
        self.obstacles = []
        self.nObstacles = 0
        self.pathfinder = Pathfinder(self)  # Gère le pathfinding local
        self.hokuyo_handler = HokuyoHandler(self.hokuyo_com, self)  # Gère l'hokuyo et traite ses données
        self.objective_handler = StrategicMind(self.objectives, self)
        # Gère la stratégie pure (décision d'objectif, la gestion du temps est un objectif)
        self.started = False

    def init_orientation(self):
        init_orientation = self.ardu_com.request_orientation()

    def recompute_orientation(self):
        # TODO
        pass

    def start(self):
        # caractérisé par la réception d'un message de l'arduino
        self.hokuyo_handler.start()  # démarre la détection
        self.started = True
        self.init_orientation()
        timeInit = time.time()
        while self.started and time.time() < timeInit + 90:
            # Gestion des objectifs
            if self.current_objective is None:
                self.objective_handler.set_objective()
                if self.current_objective is None:
                    self.started = False
                    break
            else:
                doable_objective = self.objective_handler.update_objective()
                # agir si possible
                if doable_objective is not None:
                    doable_objective.act(self)
                # Sinon se positionner pour atteindre un objectif
                else:
                    # rejoindre la position de current_objective sinon
                    # Pathfinding local
                    orders = self.pathfinder.get_orders(self.current_objective)
                    # Envoi des ordres de direction-vitesse-rotation à la motor_arduino dans le repère
                    self.ardu_com.send_orders(orders)
        print 'Mission over'

    def get_position(self):
        # TODO
        return 0
        # Renvoie [x,y,theta] dans le référentiel arène
