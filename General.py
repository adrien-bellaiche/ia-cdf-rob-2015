# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from SerialCom import ArduinoCom, HokuyoCom, LEFT, RIGHT, MOTOR, HOKUYO
from HokuyoHandler import HokuyoHandler
from Strategy import StrategicMind
from Pathfinding import Pathfinder
from State import StatusHandler
from Utils import parse


class Robot():
    def __init__(self):
        self.ardu_com = ArduinoCom(specific_test_request='V', specific_test_answer='mainduino')
        self.ardu_com.start()
        self.motor_arduino = ArduinoCom(specific_test_request='V', specific_test_answer='motorduino')
        self.ardu_com.send_conf(MOTOR)
        self.hokuyo_com = HokuyoCom()
        self.ardu_com.send_conf(HOKUYO)
        self.current_objective = None
        if self.ardu_com.request_mission_parameters() == LEFT:
            self.objectives = parse('left.txt')
        else:
            self.objectives = parse('right.txt')
        self.opponents = []
        self.ally = []
        self.pathfinder = Pathfinder(self) # Gère le pathfinding local
        self.status = StatusHandler(self)  # Permet d'avoir les infos sur l'état actuel du robot
        self.hokuyo_handler = HokuyoHandler(self.hokuyo_com, self)  # Gère l'hokuyo et traite ses données
        self.objective_handler = StrategicMind(self.objectives, self)
            # Gère la stratégie pure (décision d'objectif, la gestion du temps est un objectif)
        self.started = False

    def start(self):
        # caractérisé par la réception d'un message de l'arduino
        self.hokuyo_handler.start()  # démarre la détection
        self.started = True
        while self.started:
            # mets à jour l'état du robot
            self.status.update()
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
                    orders = self.pathfinder.get_orders(self.current_objective.position)
                        # Envoi des ordres de direction-vitesse-rotation à la motor_arduino dans le repère
                    self.motor_arduino.send_orders(orders)
        print 'Mission over'

    def get_position(self):
        return self.status.get_position()
        # Renvoie [x,y,theta] dans le référentiel arène

    def get_state(self):
        return self.status.get_state()
        # Renvoie [x,y,theta,