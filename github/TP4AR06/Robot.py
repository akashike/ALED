from Class_Vecteur3D import Vecteur3D as V3D
from Torseur import Torseur
import math
import matplotlib
import numpy as np

class Tortue(object):
	
	def __init__(self, nom='toto', position = V3D, orientation=0, color='red'):
		self.nom=nom
		self.color=color
		self.positions=[position]
		self.orientations=[orientation]
	def __str__(self):
		pass
		
	def __repr__(self):
		pass
		
	def marche(self, distance):
		pass
		
	def tourne(self,rad):
		pass
		
	def ouEstElle(self):
		pass
		
	def teleport(self,position,orientation):
		pass
		
	def plot(self):
		pass
		
	def sauve(self,fichier):
		pass
		
	def charge(self)
		pass
		
	def mouv(self, Longueur, Angle):
		self.Orientation = self.Orientation + (0, 0, Angle)
		self.Position = self.Position + (Longueur*math.cos(Angle), Longueur*math.sin(Angle), 0)
		return Torseur(self.Position, self.Orientation, 0)
		
Angle=60
Longueur=10

t = np.arange(0, 2)

MVT = Tortue.mouv(60, 10)
MVT2 = Tortue.mouv(90, 15)
plot(MVT.Position, t)
