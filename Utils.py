# -*- coding: utf8 -*-
__author__ = 'adrie_000'
#merci de metre un switch physique pour choisir la couleur du robot

def parse(textfilename,myColor): #NOT USERPROOF soyer intelligent ne faites pas lire de la bullshit
        #TODO : lit le fichier d'objectifs, renvoie la liste d'objectifs (partiellement fait)
        filein=open(textfilename,"r")
        txt="you can modify this for anything except \"End\""
        dico=dict()
        while not(txt=="End"):
            txt=readALine(filein,myColor,dico)

        if myColor=='Blue':
            a='clap1B'
        else:
            a='clap1R'
        #print dico[a].toString()
        return dico

def readALine(filein,myColor,dico):
    objstr=filein.readline()
    if not(objstr=="EndOfFile"):
        obj=objstr.split()
        nom=obj[0]
        type=obj[1]
        X=obj[2].split("=")[1]
        Y=obj[3].split("=")[1]
        Color=obj[4].split("=")[1] #"Blue" ou "Red", vous avez le droit de modifier ça
        angle=obj[5].split("=")[1]
        if myColor==Color:
            dico[nom]=Objective(type,X,Y,angle)
            #il faudra nommer les objectifs tous différents en conséquence
        else:
            pass
    else:
        return "End"


class Objective():  # TODO
    def __init__(self,type,X,Y,angle):
        self.position = [X,Y]
        self.action=type
        self.angleAtt=angle

    def getPosition(self):
        return self.position

    def getAction(self):
        return self.action

    def getAngleAtt(self):
        return self.angleAtt

    def setPosition(self,position):
        self.position = position

    def setAction(self,action):
        self.action = action

    def setAngleAtt(self,angle):
        self.angleAtt=angle

    def toString(self):
        print self.getAction()
        print self.getPosition()
        print self.getAngleAtt()

if __name__=='__main__':
    print "writing test file : \n"
    out=open("objtest","w")
    out.write("clap1B clap x=1 y=0 color=Blue angle=0\n")
    out.write("clap1R clap x=2 y=0 color=Red angle=0\n")
    out.write("clap2B clap x=3 y=0 color=Blue angle=0\n")
    out.write("clap2R clap x=4 y=0 color=Red angle=0\n")
    out.write("EndOfFile")
    out.close()
    print "done\n"

    print "testing parse function for color red:\n"
    dico = parse("objtest","Red")
    print dico['clap1R'].getPosition()
    print "done"

    print "testing parse function for color blue:\n"
    parse("objtest","Blue")
    print "done"

