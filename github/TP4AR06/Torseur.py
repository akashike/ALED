from Vecteur3D import Vecteur3D

class Torseur(object):
    
    def __init__(self,P = Vecteur3D(),R = Vecteur3D(), M = Vecteur3D()):
        self.P = P
        self.R = R
        self.M = M
        
    def __str__(self):
        msg = 'Torseur('+str(self.P)+',\n\t'+str(self.R)+',\n\t'+str(self.M)+')\n'
        return msg
  
    def __repr__(self):
        msg = 'Torseur('+str(self.P)+','+str(self.R)+','+str(self.M)+')'
        return msg
        
    def chgPt(self,PD = Vecteur3D()):
        MD = self.M + (self.P - PD) ** self.R
        self.P = PD
        self.M = MD
    
    def __add__(self,other):
        
        if self.P != other.P:
            Ptemp = other.P
            other.chgPt(self.P)
                
        S = Torseur(self.P,self.R+other.R,self.M+other.M)
        
        try: 
            other.chgPt(Ptemp)
        except:
            pass
            
        return(S)
                
    def __neg__(self):
        return(Torseur(self.P,-self.R,-self.M))
        
    def __sub__(self,other):
        return (self + (-other))
        
    def __eq__(self,other):
        if not(self.P  == other.P):
            Ptemp = other.P
            other.chgPt(self.P)
        
        S = (self.R == other.R and self.M == other.M)
        
        try: 
            other.chgPt(Ptemp)
        except:
            pass
        return(S)        


if __name__ == "__main__": # false lors d'un import

    P1 = Vecteur3D(y=3)
    R1 = Vecteur3D(1,2,3)
    M1 = Vecteur3D(3,2,3)
    
    P2 = Vecteur3D()
    R2 = Vecteur3D(4,1,3)
    M2 = Vecteur3D(3,0,3)
    
    T1 = Torseur(P1,R1,M1)
    T0 = Torseur()
    T2 = Torseur(P2,R2,M2)
    
    print(T0)
    #T1.chgPt(P2)
    print(T1)
    print(T2)
    T3 = -T2
    print(T1-T2 == T1+T3)
    print(T3)
    
    
    
    
