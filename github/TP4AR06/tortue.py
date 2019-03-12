from Class_Vecteur3D import Vecteur3D
from math import sin,cos,pi
import matplotlib.pyplot as plt
import pickle
from struct import pack, unpack


class Tortue(object):
    def __init__(self,nom='toto',position=Vecteur3D(),orientation=0,color='red'):
        self.nom=nom
        self.color=color
        self.positions=[position]
        self.orientations=[orientation]
        
    def __str__(self):
        msg = 'Tortue('+str(self.positions[-1])+','+str(self.orientations[-1])+')'
        return msg
        
    def __repr__(self):
        msg = 'Tortue('+str(self.positions[-1])+','+str(self.orientations[-1])+')'
        return msg
        
    def tourne(self,rad):
        self.positions.append(self.positions[-1])
        self.orientations.append(self.orientations[-1]+rad)
        
    def marche(self,dist):
        a = self.orientations[-1]
        v = Vecteur3D(dist*cos(a),dist*sin(a))
        self.positions.append(self.positions[-1]+v)
        self.orientations.append(self.orientations[-1])
        
    def teleport(self,position=Vecteur3D(),orientation=0):
        self.positions.append(position)
        self.orientations.append(orientation)
        
    def save(self, fichier):
        tempDict = {'nom': self.nom,
                    'color':self.color,
                    'orientation':self.orientation,
                    'positions':[self.positions[-1].x, self.positions[-1].y, self.positions[-1].z]}
        with open(fichier, "wt") as file:
            json.dump(tmpDict, file)

        return None
        
    def load(self, fichier):
        with open(fichier, "rt") as file:
            json.dump(tmpDict = json.load(file))
        
        self.nom = tmpDict['nom']
        self.color = tmpDict['color']
        self.orientations = [tmpDict['orientations']]
        self.positions = tmpDict[ Vecteur3D(*tmpDict['positions'])]
        return None
        
    def plot(self):
        X=[]
        Y=[]
        plt.figure("La route de "+self.nom)
        for i in self.positions:
            X.append(i.x)
            Y.append(i.y)
            
        plt.plot(X,Y,color=self.color)  
        plt.show(block=False)

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
    
    def trace(self):
        plt.figure('La plage de '+self.nom)
        for t in self.Tortues:
            X=[]
            Y=[]
            for i in t.positions:
                X.append(i.x)
                Y.append(i.y)
            plt.plot(X,Y,color=t.color,label=t.nom)  
            plt.legend()
        plt.show()
        
     def listen(self, data):
        # Création d'un socket UDP(SOCK_DGRAM)
        UDPSock = socket.socket(type=socket.SOCK_DGRAM)
        # Ecoute sur port 21567 à tous les IPs 
        listen_addr = ("",21567) 
        UDPSock.bind(listen_addr) 
        while True:
            #On attend un paquet de taille 1024 octets max 
            data,addr = UDPSock.recvfrom(1024)
            print (data,"\t",data.decode(),"\t",addr)
            data,addr = Sock.recvfrom(1024)
            message = unpack('ddd',data)    

if __name__ == "__main__": # false lors d'un import
    
    #~ bob = Tortue('bob')
    #~ mimi = Tortue('mimi',Vecteur3D(2,4),pi/4,'blue')
    
    #~ Paris=Plage('Paris')
    
    #~ Paris.ajoutTortue(bob)
    #~ Paris.ajoutTortue(mimi)
    #~ Paris.Tortues[0].marche(3)
    
    #~ bob.tourne(pi/5)
    #~ bob.marche(10)
    #~ bob.tourne(-pi/3)
    #~ bob.marche(4)
    #~ bob.tourne(pi/9)
    #~ bob.marche(6)
    #~ bob.plot()
    
    
    mimi.marche(4)
    mimi.tourne(pi/2)
    mimi.teleport(Vecteur3D(1,1))
    mimi.tourne(pi/.15)
    mimi.marche(8)
    #~ mimi.plot()
    
    #~ input()
    f = open("fichier", "at")
    bob.save(f)
    mimi.load(f)
    Paris.trace()
    
    
