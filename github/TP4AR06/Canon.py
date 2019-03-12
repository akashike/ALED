from particule import particule as part
from Vecteur3D import Vecteur3D as V3D
import math

theta = input('Rotation de visée !:')
theta = float (theta)

elevation = input('Aaaaangle de tiiiir ?! :')
elevation = float(elevation)

force = input('Puissance du tir mon capitaine ? :')
force = float(force)

coeff = input('coefficient de trainée :')
coeff = float(coeff)

V0 = force * V3D(math.cos(theta) * math.cos(elevation), math.sin(theta), math.sin(elevation)).norm()

LimiteX = 10
LimiteZ = 0
LimiteY = 12

class Tirs(object):

    Particules=[]

    def __init__(self,nom):
        self.nom=nom

    def ajoutParticule(self,P=part()):
        self.Particules.append(P)

    def enleveParticule(self,nom):
        for t in self.Particules:
            if t.nom==nom:
                self.Particules.remove(t)

    #~ def update_plot(self):
        #~ """ fonction qui crée le contenu d'un plot
        #~ MAIS NE LE TRACE PAS"""

        #~ self.plot = plt
        #~ return plt

    def trace(self,hold=True):

        import matplotlib.pyplot as plt

        fig = plt.figure('L\'Univers'+self.nom)

        for t in self.Particules:
            X=[]
            Y=[]
            Z=[]
            for i in t.pos:
                X.append(i.x)
                Y.append(i.y)
                Z.append(i.z)
            plt.plot(X,Y,Z,label=t.nom)
        plt.legend()

        if not hold :
            plt.ion()
            plt.show()
            fig.canvas.flush_events()

        else:
            plt.ioff()
            plt.show()



    def teleplage_server(self,port):

        import socket
        from struct import unpack

        UDPSock = socket.socket(type=socket.SOCK_DGRAM)
        print(" Ecoute sur port %i à tous les IPs" % port)

        listen_addr = ("",port)
        UDPSock.bind(listen_addr)

        data2, addr = UDPSock.recvfrom(1024)
        fmt = 'ldd' #data.decode()

        try:
            recu = unpack(fmt, data2)
            no = int(recu[0])
            print("tortue %d à l'écoute" % no)
            print(self.Particules[no])
            angle = recu[1]
            pas = recu[2]
            self.Particules[no].tourne(angle)
            self.Particules[no].marche(pas)

            print ("Commande executé: ", self.Particules[no])

        except:
            print(addr, "Message pas bon: << " + str(recu) +" >> ", "\n\n")

if __name__ == "__main__": # false lors d'un import


    Tirs=Tirs('Univ')

    from random import random , seed
    seed()
    for i in range(5):
        nom = 'toto'+str(i)
        Tirs.ajoutParticule(part(nom,mass=10,pos= V3D(0,0,10*random()), vit=random()*V0))
    for s in range(500):
        for t in Tirs.Particules:

            if t.pos[-1].z < LimiteZ:
                t.pos[-1].z = LimiteZ
                t.chocz(coeff)
            if t.pos[-1].x > LimiteX:
                t.pos[-1].z = LimiteZ
                t.chocx(coeff)
            if t.pos[-1].y > LimiteY:
                t.pos[-1].z = LimiteZ
                t.chocy(coeff)

            t.setForce(V3D(0, 0, -9.81*t.mass))
            t.simule(0.01)
        Tirs.trace(False)
    Tirs.trace()
