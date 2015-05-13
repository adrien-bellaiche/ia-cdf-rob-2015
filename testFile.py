__author__ = 'adrie_000'

#test


class Patate():
    def __init__(self):
        self.p = "je suis une patate"

    def disp(self):
        print "banana"


p = ["hello", 'c', 3, 3.0125, [Patate(), Patate(), Patate()]]
p[4][0].disp()