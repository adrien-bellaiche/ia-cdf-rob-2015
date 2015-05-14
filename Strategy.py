__author__ = 'adrie_000'
# -*- coding: utf8 -*-

class StrategicMind():
    # TODO

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
        # TODO
        return 0

    def update_objective(self):
        # TODO : voit si un objectif est remplissable a courte portee (le renvoie si oui)
        # recupere sa position
        [x, y] = self.data_center.position
        # recupere la position de l'objectif
        [Ox, Oy] = self.data_center.current_objective.position

        #compare les distances
        dist=((Ox-x)**2+(Oy-y)**2)**0.5
        if dist < 1950:
            doable_objective = self.data_center.current_objective
        else:
            doable_objective = None

        return doable_objective
