from Torseur import Torseur
from Vecteur3D import Vecteur3D as V3D

class SolideEncastre(object):
    """Un solide rigide, encastré à l'origine de son repère local"""
    def __init__(self,CentreDeMasse=V3D(),masse=0.,EffortsExt=[]):
        self.CentreDeMasse =CentreDeMasse
        self.masse = masse
        self.Poids = Torseur(CentreDeMasse,V3D(0,0,-masse*9.8),V3D())
        self.Poids.chgPt()
        self.EffortsExt = EffortsExt + [self.Poids]
        self.EffortLiaison = Torseur()
        self.equilibre()
        
    def __str__(self):
        msg = "SolideEncastre("+str(self.CentreDeMasse)+',\n'+str(self.masse)+',\n'+str(self.EffortsExt)+')'
        return msg
        
    def __repr__(self):
        msg = "SolideEncastre("+str(self.CentreDeMasse)+','+str(self.masse)+','+str(self.EffortsExt)+')'
        return msg
        
    def equilibre(self):
        S=Torseur()
        for i in self.EffortsExt:
            S = S + i
        self.EffortLiaison=-S
        return -S
        
    def ajoutFEXT(self,Fext=Torseur()):
        self.EffortsExt.append(Fext)
        self.equilibre()


#~ class Structure(object):
    
    #~ def __init__(self,CentreDeMasse=V3D(),masse=0.,EffortsExt=[],Enfants={},Parent=None):
        #~ self.Solide=SolideEncastre(CentreDeMasse,masse,EffortsExt)
        #~ self.Enfants=Enfants
        #~ self.Parent=Parent
        #~ self.EnfantstoTorseur()
        
 
     #~ def ajoutEnfant(self,S=SolideEncastre(),Position=Vecteur3D()):
         #~ self.Enfants[S]=Position
         #~ self.EnfantstoTorseur()
         
    #~ def EnfantstoTorseur():
        #~ for enfant in self.Enfants:
            #~ position = self.Enfants[enfant]
            #~ if len(enfant.Enfants) = 0:
                #~ S = Torseur()
                #~ S.P = position
                #~ S.R = -enfant.EffortLiaison.R
                #~ S.P = -enfant.EffortLiaison.P
            
            #~ else :
                #~ enfant.EnfantstoTorseur()

            
            
            
            
            
    
    

if __name__ == "__main__": # false lors d'un import

    P1 = V3D(y=3)
    R1 = V3D(1,2,3)
    M1 = V3D(3,2,3)
    
    P2 = V3D()
    R2 = V3D(4,1,3)
    M2 = V3D(3,0,3)
    
    T1 = Torseur(P1,R1,M1)
    T0 = Torseur()
    T2 = Torseur(P2,R2,M2)
    
    S0 = SolideEncastre(masse=10)
    
    S0.ajoutFEXT(T1)
    
    print(S0)
    print()
    print(S0.EffortLiaison)

    S0.ajoutFEXT(T2)
    
    print(S0)
    print()
    print(S0.EffortLiaison)
