__author__ = 'adrie_000'

import numpy as np


class Pathfinder():
    def __init__(self, data_center):
        self.data_center = data_center

    def get_orders(self, objective):
        # Renvoie les ordres en [direction, vitesse, vitesse_rotation]
        objective_location = objective.position
        v = np.array([0, 0])
        if objective_location is not None:
            obstacles = self.data_center.obstacles
            # On cible l'approche par l'angle en question
            targ = np.array(objective_location) + np.array(
                [np.cos(objective.side * np.pi / 180), np.sin(objective.side * np.pi / 180)]) * self.data_center.radius
            loc = np.array(self.data_center.position)
            v = np.array([0, 0])
            v += (targ - loc) / np.linalg.norm(targ - loc)
            for obstacle in obstacles:
                v2obstacle = np.array(obstacle.center) - loc
                d2obstacle = np.linalg.norm(v2obstacle)
                v2obstacle /= np.linalg.norm(v2obstacle)
                v -= v2obstacle / (d2obstacle * d2obstacle)
        va = 0
        if objective.atelier is not None:
            target_ori = objective.atelier * 2 * np.pi / 3 - objective.side
            va = 3 * divmod(self.data_center.orientation - target_ori, 2 * np.pi)
        return [v[0], v[1], va]