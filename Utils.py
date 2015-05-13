# -*- coding: utf8 -*-
__author__ = 'adrie_000'


class Plot():
    def __init__(self, position=None, atelier=None):
        pass

    def act(self):
        pass


class Clap():
    def __init__(self, position=None, atelier=None):
        pass

    def act(self):
        pass


class Distributeur():
    def __init__(self, position=None, atelier=None):
        pass

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
