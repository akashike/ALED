class Repertoire(object):
	""" un repertoire téléphonique utilisant un dictionnaire"""
	def __init__(self,nom="monRepertoire"):
		self.nom=nom
		self.contenu={}
		
	def __str__(self):
		msg = "Repertoire("+self.nom+")\n"+str(self.contenu)
		return msg
		
	def __repr__(self):
		msg = "Repertoire("+self.nom+")\n"+str(self.contenu)
		return msg
		
	def nouvelEntree(self,nom,numero):
		if type(nom) == str and \
		type (numero) == str and \
		nom not in self.contenu:
			
			self.contenu[nom]=[numero]
		
		elif type(nom) == str and \
		type (numero) == str and \
		nom in self.contenu:

			# cas un numéro par nom, on incréménte le nom
			
			i = 0
			newnom = nom+str(i)
			while newnom in self.contenu:
				i=i+1
				newnom = nom+str(i)
			self.contenu[newnom]=numero
			
			# cas plusieurs numero par nom 
			
			#~ self.contenu[nom].append(numero)
		
		else:
			print("Erreur de Format")
			
			
	
		
	def enleveEntree(self,nom):
		if nom in self.contenu:
			self.contenu.pop(nom)
	
	def sauve(fichier):
		pass
		
	def charge(fichier):
		pass
		
if __name__ == "__main__": # false lors d'un import

	RepPro= Repertoire('Professionel')
	RepPro.nouvelEntree("Toto",'0144561384')
	RepPro.nouvelEntree("Toto",'0678991356')
	RepPro.nouvelEntree("Toto",'5678991356')
	
	print(RepPro)
	#RepPro.enleveEntree("Toto")
	print()
	print(RepPro)
	
		
	
