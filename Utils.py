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
    if side == "left":
        pass
        # TODO
        # claps à droite
        clap1=Clap([2000,250],1)
        clap2=Clap([2000,250],1)

        # distributeurs
        distrib1=Distributeur([30,300],1)
        distrib2=Distributeur([30,600],1)

        # Plots
        plot1=Plot([200,90],0)
        plot2=Plot([200,850],0)
        plot3=Plot([100,850],0)
        plot4=Plot([1750,90],0)
        plot5=Plot([1850,90],0)
        plot6=Plot([1770,1100],0)
        plot7=Plot([1400,1300],0)
        plot8=Plot([1355,870],0)

    else:
        # TODO
        # claps à droite
        clap1=Clap([2000,2750],1)
        clap2=Clap([2000,2750],1)

        # distributeurs
        distrib1=Distributeur([30,2700],1)
        distrib2=Distributeur([30,2400],1)

    return [clap1, clap2, distrib1, distrib2]
