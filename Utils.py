# -*- coding: utf8 -*-
__author__ = 'adrie_000'

import numpy as np

# Side : coté par lequel approcher l'item. en degrés
# prof : profondeur à rentrer dans l'axe side.

pos_tolerance = 0.1  # Tolérance à l'erreur de position
ori_tolerance = np.pi / 10  # Tolérance à l'erreur de rotation

class Plot():
    def __init__(self, data_center, position=None, atelier=0, side=None, prof=70, max_score=3):
        self.completed = False
        self.side = side
        self.data_center = data_center
        self.position = position
        self.atelier = atelier
        self.prof = prof
        self.max_score = max_score

    def is_startable_from_here(self):
        entry = 0  # Position de référence depuis laquelle il faut être proche
        side_bool = True
        if self.side is None:
            entry = self.position
        else:
            side_bool = abs(self.data_center.orientation - self.atelier * 2 * np.pi / 3 - self.side) < ori_tolerance
            entry = np.array(self.position) + np.array(
                [np.cos(self.side * np.pi / 180), np.sin(self.side * np.pi / 180)]) * self.data_center.radius
        return side_bool and np.linalg.norm(np.array(self.data_center.position) - np.array(entry)) < (
                                                                                                     1 + pos_tolerance) * self.prof


    def act(self):
        pass


class Clap():
    def __init__(self, data_center, position=None, atelier=1, side=90, prof=0, max_score=3):
        self.completed = False
        self.side = side
        self.data_center = data_center
        self.position = position
        self.atelier = atelier
        self.prof = prof
        self.max_score = max_score
        pass

    def is_startable_from_here(self):
        entry = 0  # Position de référence depuis laquelle il faut être proche
        side_bool = True
        if self.side is None:
            entry = self.position
        else:
            side_bool = abs(self.data_center.orientation - self.atelier * 2 * np.pi / 3 - self.side) < ori_tolerance
            entry = np.array(self.position) + np.array(
                [np.cos(self.side * np.pi / 180), np.sin(self.side * np.pi / 180)]) * self.data_center.radius
        return side_bool and np.linalg.norm(np.array(self.data_center.position) - np.array(entry)) < (
                                                                                                     1 + pos_tolerance) * self.prof


    def act(self):
        pass


class Distributeur():
    def __init__(self, data_center, position=None, atelier=1, side=-90, prof=5, max_score=3):
        self.completed = False
        self.side = side
        self.data_center = data_center
        self.position = position
        self.atelier = atelier
        self.prof = prof
        self.max_score = max_score

    def is_startable_from_here(self):
        entry = 0  # Position de référence depuis laquelle il faut être proche
        side_bool = True
        if self.side is None:
            entry = self.position
        else:
            side_bool = abs(self.data_center.orientation - self.atelier * 2 * np.pi / 3 - self.side) < ori_tolerance
            entry = np.array(self.position) + np.array(
                [np.cos(self.side * np.pi / 180), np.sin(self.side * np.pi / 180)]) * self.data_center.radius
        return side_bool and np.linalg.norm(np.array(self.data_center.position) - np.array(entry)) < (
                                                                                                     1 + pos_tolerance) * self.prof



    def act(self):
        pass


def objectives(side):
    res = []
    if side == "left":
        # claps à droite
        res.append(Clap([2000, 250], 1))
        res.append(Clap([2000, 250], 1))

        # distributeurs
        res.append(Distributeur([30, 300], 1))
        res.append(Distributeur([30, 600], 1))

        # Plots
        res.append(Plot([200, 90], 0))
        res.append(Plot([200, 850], 0))
        res.append(Plot([100, 850], 0))
        res.append(Plot([1750, 90], 0))
        res.append(Plot([1850, 90], 0))
        res.append(Plot([1770, 1100], 0))
        res.append(Plot([1400, 1300], 0))
        res.append(Plot([1355, 870], 0))

    else:
        res.append(Clap([2000, 2750], 1))
        res.append(Clap([2000, 2750], 1))

        # distributeurs
        res.append(Distributeur([30, 2700], 1))
        res.append(Distributeur([30, 2400], 1))

        res.append(Plot([200, 90], 0))
        res.append(Plot([200, 850], 0))
        res.append(Plot([100, 850], 0))
        res.append(Plot([1750, 90], 0))
        res.append(Plot([1850, 90], 0))
        res.append(Plot([1770, 1100], 0))
        res.append(Plot([1400, 1300], 0))
        res.append(Plot([1355, 870], 0))

    return res
