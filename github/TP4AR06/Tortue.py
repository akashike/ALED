#  Tortue.py
#  
#  Copyright 2019 haliyo <haliyo@pc5565-106-00.meca.ingenierie.upmc.fr>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from Vecteur3D import Vecteur3D
from math import sin,cos, pi

class Tortue(object):
    """Une tortue qui peut tourner et marcher. Elle se souvient où elle a été."""
    def __init__(self,nom='toto',position=Vecteur3D(),orientation=0,color='red'):
        self.nom=nom
        self.color=color
        self.positions=[position]
        self.orientations=[orientation]
    
        
    def __str__(self):
        msg = 'Tortue('+self.nom+','+str(self.positions[-1])+','+str(self.orientations[-1])+')'
        return msg
        
    def __repr__(self):
        msg = 'Tortue('+self.nom+','+str(self.positions[-1])+','+str(self.orientations[-1])+')'
        return msg
        
    def marche(self,distance):
        a = self.orientations[-1]
        v = Vecteur3D(distance*cos(a),distance*sin(a))
        self.positions.append(self.positions[-1]+v)
        self.orientations.append(self.orientations[-1])

    def tourne(self,rad):
        self.positions.append(self.positions[-1])
        self.orientations.append(self.orientations[-1]+rad)

    def ouEstElle(self):
        return (self.positions[-1],self.orientations[-1] )
    
    def teleport(self,position=Vecteur3D(),orientation=0):
        self.positions.append(position)
        self.orientations.append(orientation)
 
        
    def plot(self):
        from math import sin,cos,pi
        import matplotlib.pyplot as plt
        
        X=[]
        Y=[]
        plt.figure("La route de "+self.nom)
        for i in self.positions:
            X.append(i.x)
            Y.append(i.y)
            
        plt.plot(X,Y,color=self.color)  
        plt.show()        
        
    def sauve(self,fichier):
        if fichier=="":
            fichier=self.nom+'.trt'
        if not fichier[-4:]=='.trt':
            fichier +='.trt'
                
        f1=open(fichier,'wt')
        f1.write(self.nom+':'+self.color+'\n')
        for i in range(len(self.positions)):
            f1.write('%f:%f:%f\n' % (self.positions[i].x,self.positions[i].y,self.orientations[i]) )
            
        f1.close()
  
        
    def charge(self,fichier):
        self.positions=[]
        self.orientation=[]
        
        if fichier=="":
            fichier=self.nom+'.trl'
        if not fichier[-4:]=='.trl':
            fichier +='.trl'

        f1=open(fichier,'rt')
        data=f1.readline().split(':')
        
        self.nom=data[0]
        self.color=data[1][:-1]
        
        data = f1.read().split()
        
        for d in data[:-1]:
            coord = [float(i) for i in d.split(':')]
            self.positions.append(Vecteur3D(coord[0],coord[1]))
            self.orientations.append(coord[2])
            
            
class Plage(object):
    
    Tortues=[]
    
    def __init__(self,nom):
        self.nom=nom
    
    def ajoutTortue(self,T=Tortue()):
        self.Tortues.append(T)
    
    def enleveTortue(self,nom):
        for t in self.Tortues:
            if t.nom==nom:
                self.Tortues.remove(t)
    
    #~ def update_plot(self):
        #~ """ fonction qui crée le contenu d'un plot 
        #~ MAIS NE LE TRACE PAS"""

        #~ self.plot = plt
        #~ return plt
        
    def trace(self,hold=True):

        import matplotlib.pyplot as plt

        fig = plt.figure('La plage de '+self.nom)

        for t in self.Tortues:
            X=[]
            Y=[]
            for i in t.positions:
                X.append(i.x)
                Y.append(i.y)
            plt.plot(X,Y,color=t.color,label=t.nom)  
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
            print(self.Tortues[no])
            angle = recu[1]
            pas = recu[2]
            self.Tortues[no].tourne(angle)
            self.Tortues[no].marche(pas)
            
            print ("Commande executé: ", self.Tortues[no])
            
        except:
            print(addr, "Message pas bon: << " + str(recu) +" >> ", "\n\n")
    
        

    
    

if __name__ == "__main__": # false lors d'un import
    
    bob = Tortue('bob')
    mimi = Tortue('mimi',Vecteur3D(2,4),pi/4,'blue')
    
    Paris=Plage('Paris')
    
    Paris.ajoutTortue(bob)
    Paris.ajoutTortue(mimi)
    Paris.Tortues[0].marche(3)
    
    print(bob)
 
    
    bob.tourne(pi/5)
    bob.marche(10)
    bob.tourne(-pi/3)
    bob.marche(4)
    bob.tourne(pi/9)
    bob.marche(6)
    #~ bob.plot()
    
    
    mimi.marche(4)
    mimi.tourne(pi/2)
    mimi.teleport(Vecteur3D(1,1))
    mimi.tourne(pi/.15)
    mimi.marche(8)
    #~ mimi.plot()
    
    
    Paris.trace()
    #~ bob.save()
    
    #~ T = Tortue()
    #~ T.load('bob')
    #~ T.plot()

    #Party à la plage
    from random import random , seed
    seed()
    for i in range(20):
        name = 'toto'+str(i)
        Paris.ajoutTortue(Tortue(name,Vecteur3D(10*random(),10*random()),color=[random(),random(),random()]))
    
    for s in range(10):
        for t in Paris.Tortues:
            
            t.tourne(random()*pi - (pi/2))
            t.marche(10*random())
        
        Paris.trace(False)  
    
    Paris.trace()
    
    #~ while (True):
        #~ Paris.teleplage_server(11110)

    
        
