__author__ = 'adrie_000'
# -*- coding: utf8 -*-

import numpy as np


class StrategicMind():
    def __init__(self, data_center):
        self.data_center = data_center

    def set_objective(self):
        best_obj = None
        best_score = 0
        for objective in self.data_center.objectives:
            score = self.compute_score(objective)
            if best_obj is None:
                best_obj = objective
                best_score = score
            else:
                if best_score < score:
                    best_score = score
                    best_obj = objective
        return best_obj

    def compute_score(self, objective):
        distance = np.linalg.norm(np.array(objective.position) - np.array(self.data_center.position))
        return objective.max_score - distance

    def update_objective(self):
        for objective in self.data_center.objectives:
            if not objective.completed:
                if objective.is_startable_from_here():
                    return objective
        return None
