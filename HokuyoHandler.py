# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from threading import Thread


class HokuyoHandler(Thread):
    # Pourquoi ceci est un thread : parce qu'il faut que l'information donneé par l'Hokuyo soit utilisée aussi
    # fréquemment que possible. Du coup une boucle à part.

    def __init__(self, hokuyo_com, data_center):
        Thread.__init__(self)
        self.hokuyo = hokuyo_com
        self.data_center = data_center
        self.started = False
        self.data = None

    def stop(self):
        self.started = False

    def run(self):
        self.started = True
        while self.started:
            # - lit l'hokuyo
            self.data = self.hokuyo.get_fresh_data()
            # - Récupère la liste des nouvelles positions d'obstacles
            positions = self.find_positions_in_data()
            # - Relie les positions avec les anciennes & stocke tout dans le data_center.
            self.match_positions(positions)
            # - Envoie les nouvelles positions via l'arduino_com du data_center au robot secondaire
            self.send_data_to_ally()

    def find_positions_in_data(self):
        # TODO : nettoie les données capteur, renvoie la liste des positions
        p = self.data
        return 0

    def match_positions(self, new_positions):
        # TODO : detecte l'allié via son ancienne position, les autres positions sont foes
        pass

    def send_data_to_ally(self):
        # TODO
        pass