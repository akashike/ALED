class Vecteur3D(object):
    """Objet vecteur 3d avec des attribut x, y, et z.
    Les valeurs par défaut sont (0,0,0)
    scalare est implementé avec '*',
    '**' fait:
        - un Vecteuriel entre 2 Vecteur3D, 
        - une puissance scalaire entre un Vecteur3D et un scalaire,
        - un scalaire entre un scalaire et un Vecteur3D
    
    """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        msg = 'Vecteur3D('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
        return msg
    
    def __repr__(self):
        msg = 'Vecteur3D('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
        return msg
        
    def __add__(self,other):
        S = Vecteur3D(self.x+other.x,self.y+other.y,self.z+other.z)
        return(S)
    
    def __neg__(self):
        return Vecteur3D(-self.x,-self.y,-self.z)
        
    def __sub__(self,other):
        return self+ (-other)
    
    def __mul__(self,other):
        """ Operation scalaire"""
        try:
            S = self.x*other.x+self.y*other.y+self.z*other.z
        except:
            S = Vecteur3D(self.x*other,self.y*other,self.z*other)
        return S
        
    def __rmul__(self,other):
        return (self*other)
        
    def __pow__(self,other):
        """Opération Vecteuriel, ou puissance scalaire, en fct de l'opérand droite"""
        try:
            X = (self.y*other.z-self.z*other.y)
            Y = (self.z*other.x-self.x*other.z)
            Z = (self.x*other.y-self.y*other.x)
            S = Vecteur3D(X,Y,Z)
        except:
            S = 1
            for i in range(int(other)):
                S = S * self
        return(S)
        
    def __rpow__(self,other):
        return (self*other)
        
    def __truediv__(self,other):
        return (self * (1/other))
    
    def mod(self):
        """module d'un vecteur"""
        S = (self.x**2+self.y**2+self.z**2)**(.5)
        return(S)
        
    def norm(self):
        """retourne un vectuer normalisé"""
        return self /self.mod()
        
    def normalize(self):
        """normalise le vecteur, ne retourne rien"""
        if self.mod() != 0:
            X = self.norm().x
            Y = self.norm().y
            Z = self.norm().z
            self.x = X
            self.y = Y
            self.z = Z
        return self
    
    def __eq__(self,other):
        if (self.x == other.x and self.y == other.y and self.z == other.z ):
            return True
        else :
            return False
        
    def __gt__(self,other):
        """compare les modules"""
        return (self.mod() > other.mod())
        
    def __lt__(self,other):
        """compare les modules"""
        return (self.mod() < other.mod())
        


if __name__ == "__main__": # false lors d'un import

    help(Vecteur3D)
    
    V1 = Vecteur3D(y=3)
    V2 = Vecteur3D(1,2,3)
    V3 = Vecteur3D(1,2,3)
    
    
    
    print("V1*V2 =",  V1*V2 )
    print ("V2 * 4 = ", V2 * 4)
    print()
    print("5**V1 = " ,5**V1)
    print("5*V1 = " ,5*V1)
    print()    
    print("V1**V2 = ", V1**V2)
    print("V2 ** 2 =", V2**2)
    print()
    print("mod de V2 = ", V2.mod())
    print("V2 normalisé = ", V2.norm())
    V2.normalize()
    print("V2.normalize() = ",V2)

    print("mod de V2 = ", V2.mod())
    print("V2 normalisé = ", V2.norm())
    V2.normalize()
    print("V2.normalize() = ",V2)

    print("mod de V2 = ", V2.mod())
    print("V2 normalisé = ", V2.norm())
    V2.normalize()
    print("V2.normalize() -> ",V2)


    print("V2 == V3", V2==V3)
    print("V1 < V3", V1<V3)
