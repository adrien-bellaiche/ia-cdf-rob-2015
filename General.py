# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from SerialCom import ArduinoCom, HokuyoCom
from HokuyoHandler import HokuyoHandler
from Strategy import StrategicMind
from State import StatusHandler
from Utils import parse


class Robot():
    def __init__(self):
        # TODO : inserer les requetes d'identification (en envoyant V sur l'hokuyo par exemple)
        self.ardu_com = ArduinoCom()
        self.motor_arduino = ArduinoCom()
        self.ardu_com.send_motor_conf()
        self.hokuyo_com = HokuyoCom()
        self.ardu_com.send_hokuyo_conf()
        self.current_objective = None
        if self.ardu_com.request_mission_parameters() == 'LEFT':
            self.objectives = parse('left.txt')
        else:
            self.objectives = parse('right.txt')
        self.obstacles = []
        self.ally = []
        self.status = StatusHandler(self)  # Permet d'avoir les infos sur l'état actuel du robot
        self.hokuyo_handler = HokuyoHandler(self.hokuyo_com, self)  # Gère l'hokuyo et traite ses données
        self.objective_handler = StrategicMind(self.objectives, self.current_objective, self)  # Gère la stratégie pure (décision d'objectif, la gestion du temps est un objectif)
        self.started = False


    def start(self):
        self.ardu_com.hear_start()  # doit être blocante jusqu'à ce que la tirette soit ... bah tirée.
        self.hokuyo_handler.start()  # démarre la détection
        self.started = True
        while self.started:
            # TODO :
            # agir si possible
            # rejoindre la position de current_objective sinon
                # Pathfinding local
                # Envoi des ordres de direction-vitesse-rotation à la motor_arduino dans le repère
            #
            pass

    def get_position(self):
        return self.status.get_position()

    def get_state(self):
        return self.status.get_state()