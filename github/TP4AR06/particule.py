from Vecteur3D import Vecteur3D as V3D

class particule(object):
    def __init__(self,nom='sat',mass=1,pos=V3D(),vit=V3D(),accel=V3D()):
        self.nom=nom
        self.pos=[pos]
        self.vit=[vit]
        self.accel=[accel]
        self.mass=mass
        
    def __str__(self):
        msg = 'particule ('+self.nom+','+str(self.m)+','+str(self.pos)+','+str(self.vit)+','+str(self.accel)+')'
        return msg
        
    def __repr__(self):
        msg = 'particule ('+self.nom+','+str(self.m)+','+str(self.pos)+','+str(self.vit)+','+str(self.accel)+')'
        return msg
        
    def setForce(self,Force=V3D()):
        self.accel.append(Force/self.mass)
        
    def simule(self,dt=0.001):
        self.vit.append(self.vit[-1]+self.accel[-1]*dt)
        self.pos.append(self.pos[-1]+self.vit[-1]*dt)
        
    def chocx(self,coeff):
        self.vit[-1].x = -self.vit[-1].x * coeff 
        
    def chocy(self,coeff):
        self.vit[-1].y = -self.vit[-1].y * coeff
        
    def chocz(self,coeff):
        self.pos[-1].z = -self.pos[-1].z 
        self.vit[-1].z = -self.vit[-1].z * coeff
        
    def trace(self):

        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        
        fig = plt.figure('Trajectoire de '+self.nom)
        ax = fig.gca(projection='3d')
        
        X=[]
        Y=[]
        Z=[]
        
        for i in self.pos:
            X.append(i.x)
            Y.append(i.y)
            Z.append(i.z)
            
        ax.plot (X, Y, Z, c='red')#, marker='o')
        plt.show()        



if __name__ == "__main__": # false lors d'un import

    Voyager = particule(mass=1,vit=V3D(0,9,500))
   
    for i in range(10000):
        Voyager.setForce(V3D(0,0,-Voyager.mass*9.8))
        Voyager.simule(.01)
    
    
    Voyager.trace()    
