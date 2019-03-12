#Equilibre d'un solide encastré avec sa classe 

from Torseur import Torseur
from Vecteur3D import Vecteur3D
from SolideEncastre import SolideEncastre as SE

def inputVecteur3D(msg=''):
    print(msg)
    x = float(input("Entrez x: "))
    y = float(input("Entrez y: "))
    z = float(input("Entrez z: "))
    
    return(Vecteur3D(x,y,z))
    
def inputTorseur(msg=''):
    print(msg)
    P = inputVecteur3D("Point")
    R = inputVecteur3D("Resultant")
    M = inputVecteur3D("Moment")
    
    return Torseur(P,R,M)

rep = 'o'

S = SE(masse=5)

while (rep == "o"):
    T = inputTorseur()
    S.ajoutFEXT(T)
    rep = input("Entrer un effort extern? o/n \n")

print("l'effort d'encastrement est: ", S.EffortLiaison)

    
