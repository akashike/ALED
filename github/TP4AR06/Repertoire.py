class Repertoire(object):
	def __init__(self, nom="Mon Repertoire"):
		self.nom=nom
		self.contenu={}
		
	def __str__(self):
		msg = "Repertoire("+self.nom+")\n"+str(self.contenu)
		return msg
		
	def __repr__():
		msg = "Repertoire("+self.nom+")\n"+str(self.contenu)
		return msg
		
	def nouvelEntree(self, nom, numero):
		if type(nom) == str and \
		type(numero) == str and \
		nom not in self.contenu:
			self.contenu[nom] = numero
		
		elif type(nom) == str and \
		type(numero) == str and \
		nom in self.contenu:
			i=0
			newnom = nom+str(i)
			while newnom in self.contenu:
				i=i+1
				newnom = nom + str(i)
			self.contenu[newnom] = numero
		else:
			print("Erreur de Format")
			
	def enleveEntree(self, nom):
		if nom in self.contenu:
			self.contenu.pop(nom)
				
		
if __name__ == "__main__" : #false lors d'un import
	
	RepPro = Repertoire('DOZO')
	RepPro.nouvelEntree("Totoro", "0112457885")
	RepPro.nouvelEntree("Mikasa", "0875485896")
	print(RepPro)
	RepPro.nouvelEntree("Mikasa", "0112457885")
	print(RepPro)
