__author__ = 'adrie_000'


class StrategicMind():
    # TODO

    def __init__(self, data_center):
        self.data_center = data_center
        self.i = 0

    def set_objective(self):
        self.data_center.current_objective = self.data_center.current_objectives[self.i]
        self.i += 1

    def update_objective(self):
        # TODO : voit si un objectif est remplissable a courte portee (le renvoie si oui)

        # Mets a jour current_objective aussi.

        #récupère sa position
        [x, y] = self.data_center.position

        #récupère la position de l'objectif
        [Ox, Oy] = self.data_center.current_objective.position

        #compare les distances
        dist=((Ox-x)**2+(Oy-y)**2)**0.5
        if dist < 1950:
            doable_objective = self.data_center.current_objective
        else:
            doable_objective = None

        return doable_objective
