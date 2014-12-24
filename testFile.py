__author__ = 'adrie_000'

import numpy as np
import numpy.matrixlib as nm

p = nm.matrix([[3, 3, 3], [3, 5, 7]])
q = p - p.mean(1)
print q
r = [np.array([q.getA()[0][k], q.getA()[1][k]]) for k in range(q.shape[1])]
print r
d = [np.linalg.norm(w) for w in r]
print d