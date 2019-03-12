from Class_Vecteur3D import Vecteur3D
from Torseur import Torseur


def input_Vecteur():
	print ("nouveau vecteur:")
	x = float(input("entrez x :"))
	y = float(input("entrez y :"))
	z = float(input("entrez z :"))
	return Vecteur3D(x, y ,z)

def input_torseur():
	P = input_Vecteur()
	R = input_Vecteur()
	M = input_Vecteur()
	return Torseur(P, R, M)
	
class SOLIDE(object):
	
	def __init__(self, Liste=[], P0=Vecteur3D(0, 0, 0)): 
		
		self.Liste= Liste
		self.P0 = P0
		
	def Equilibre(self):
		for i in len(liste):
			self.Liste[i].P = Torseur.chgPt(self.T0.P)
			somme +=  Liste[i]
		
		T0.R = somme.R
		T0.M = somme.M
		
		return T0
		
		
List=[]
i=0		

while i<=2:
	print ("nouveau torseur:")
	T=input_torseur()
	List.append(T)
	i= i+1


X = SOLIDE()
print(X.Equilibre())
