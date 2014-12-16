# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from threading import Thread

class HokuyoHandler(Thread):
    def __init__(self, hokuyo_com, data_center):
        Thread.__init__(self)
        self.hokuyo = hokuyo_com
        self.data_center = data_center
        self.started = False

    def stop(self):
        self.started = False

    def run(self):
        #TODO : boucle sur
        # - lit l'hokuyo
        # - Récupère la liste des nouvelles positions d'obstacles
        # - Relie les positions avec les anciennes
        # - stocke tout dans le data_center.
        # - Envoie les nouvelles positions via l'arduino_com du data_center au robot secondaire
        self.started = True
        while self.started:
            pass