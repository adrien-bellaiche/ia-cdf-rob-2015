# -*- coding: utf8 -*-
__author__ = 'adrie_000'

from math import sqrt


def distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[0] - pos2[0]) ** 2)


class Objective():
    def __init__(self, position=None, atelier=None, reward=None):
        self.position = position
        self.atelier = atelier
        self.reward = reward

    def getPrice(self, current_location):
        return self.reward - distance(current_location, self.position)

    def act(self):
        pass


class Stairs(Objective):
    position = {0: [0, 0, 0],
                1: [0, 0, 0]}

    def __init__(self, side):
        Objective.__init__(self, Stairs.position[side])

    def act(self):
        # TODO
        pass