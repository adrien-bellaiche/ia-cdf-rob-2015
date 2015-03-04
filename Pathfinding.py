__author__ = 'adrie_000'

from math import atan2

import numpy as np

from Utils import distance


class Pathfinder():
    attractive_intensity = 1

    def __init__(self, data_center):
        self.data_center = data_center
        # TODO
        pass

    def get_orders(self, objective_location):
        # Renvoie les ordres en [direction, vitesse]
        if objective_location is not None:
            # -2*(pj-qj)
            target = np.array(objective_location)
            pos = np.array(self.data_center.position)
            fieldvect = np.array([0, 0])
            for obstacle in self.data_center.obstacles:
                # NOTE : may require a change of sign...
                fieldvect += obstacle.repulsion_intensity(pos) * (np.array(obstacle.get_repulsing_origin()) - pos)
            fieldvect += Pathfinder.attractive_intensity * (target - pos)
            targ_v = np.sqrt(np.sum(np.power(fieldvect, [2, 2])))
            targ_h = atan2(fieldvect[1], fieldvect[0])
            return [targ_h, targ_v]


class Obstacle():
    safety = 0.05  # Margin the robot is NOT allowed to go any closer.
    accountability = 0.7  # Margin to which the robot does take into account
    intensity = 1

    def __init__(self):
        pass

    def get_repulsing_origin(self, pos):
        return [0, 0]

    def range(self, pos):
        return -1

    def repulsion_intensity(self, pos):
        d = self.range(pos)
        if d > Obstacle.accountability:
            return 0
        t = pow(self.range(pos), -1)
        return Obstacle.intensity * (1 / Obstacle.accountability - t) * pow(t, 3)


class Wall(Obstacle):
    # Infinite line. Simpler for calculations. Will be updated in future reference for finite walls.
    def __init__(self, x=None, y=None):
        Obstacle.__init__(self)
        self.x = x
        self.y = y

    def get_repulsing_origin(self, pos):
        if self.y is None:  # vertical wall
            return [self.x, pos[1]]
        # horizontal wall
        return [pos[0], self.y]

    def range(self, pos):
        if self.y is None:  # equation is x=cst aka vertical wall
            return abs(self.x - pos[0])
        # otherwise, y=cst aka horizontal wall
        return abs(self.y - pos[1])


class Orb(Obstacle):
    def __init__(self, centerx, centery, radius):
        Obstacle.__init__(self)
        self.centerx = centerx
        self.centery = centery
        self.radius = radius

    def get_repulsing_origin(self, pos):
        return [self.centerx, self.centery]

    def range(self, pos):
        return distance([self.centerx, self.centery], pos)