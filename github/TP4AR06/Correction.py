from Class_Vecteur3D import Vecteur3D as V3D
from Torseur import Torseur

class SolideEncastre(object):
	"""bla bla bal"""
	def __init__(self,CentreDeMasse=V3D(),masse =0, EffortsEXT=[]):
		
		self.CentreDeMasse = CentreDeMasse
		self.masse=masse
		self.Poids = Torseur(CentreDeMasse, V3D(0, 0, -masse*9.8), V3D())
		self.Poids.chgPt()
		self.EffortsExt = EffortsEXT + [self.Poids]
		self.EffortsLiaison = Torseur()
		self.Equilibre()
	def __str__(self):
		msg ="SolideEncastre("+str(self.CentreDeMasse)+','+str(self.masse)+','+str(self.EffortsExt)+')'
		return msg
	def __rpr__(self):
		msg ="SolideEncastre("+str(self.CentreDeMasse)+','+str(self.masse)+','+str(self.EffortsExt)+')'
		return msg
	def Equilibre(self):
		S=Torseur()
		for i in self.EffortsExt:
			S = S + i
			self.EffortLiaison = -S
			return S
	def ajoutFEXT(self,Fext=Torseur()):
		self.EffortsExt.append(Fext)
		self.Equilibre()
		
if __name__ == "__main__": #false lors d'un import
	
	S0 = SolideEncastre(masse=10)
	
	P1 = V3D(y=3)
	R1 = V3D(1,2,3)
	M1 = V3D(3,2,3)
    
	P2 = V3D()
	R2 = V3D(4,1,3)
	M2 = V3D(3,0,3)
    
	T1 = Torseur(P1,R1,M1)
	T0 = Torseur()
	T2 = Torseur(P2,R2,M2)
    
	S0.ajoutFEXT(T2)
    
	print(S0)
	print(S0.EffortLiaison)
	
