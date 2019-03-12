class Vecteur3D(object):
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, other): 
		return Vecteur3D(self.x + other.x, self.y + other.y, self.z + other.z)
	def __sub__(self, other):
		return Vecteur3D(self.x - other.x, self.y - other.y, self.z - other.z)
	def __neg__(self):
		return Vecteur3D(-self.x, -self.y, -self.z)
	def __mul__(self, other):
		if type(other) == Vecteur3D:
			X = self.y * other.z - other.y*self.z
			Y = self.z * other.x - other.z * self.x
			Z = self.x * other.y - other.x * self.y
			return Vecteur3D(X, Y ,Z)
		if type(other) != Vecteur3D:
			return Vecteur3D(self.x*other, self.y * other, self.z * other)
	def __pow__(self, other):
		if type(other) == Vecteur3D:
			return (self.x * other.x + self.y * other.y + self.z * other.z)
		else:
			X = other * self.x
			Y = other * self.y
			Z = other * self.z
			return Vecteur3D(X, Y, Z)
	def __rpow__(self, other):
		return self ** other
	def __str__(self):      	
		return "Vecteur(%g, %g, %g)" % (self.x, self.y, self.z)
		"""message = "Vecteur3d("+str(self.x)+','+str(self.y)+','+str(self.z)+")"
		return message"""
	"""if __name__ == "__main__" : false lors d'un import	"""
	def __rmul__(self, other):
		return self * other
		
	def __truediv__(self, other):
		return self * (1/other)
		
	def mod(self):
		return (self**self)**0.5
	def norm(self):
		return self / self.mod()
	
	def normed(self):
		M=self.norm()
		self.x=M.x
		self.y=M.y
		self.z=M.z

V1 = Vecteur3D(1, 0, 0)
V2 = Vecteur3D(0, 1, 0)
V3 = Vecteur3D(0, 0, 1)
Scal = 2
V12 = V1 + V2

print("-v1 =", -V1)
print("v1 + v2 =", V1+V2)
print("v1 - v2 =", V1-V2)
print("mul scal: v1 * Scal =", V1*Scal)
print("mul vect: v1 * v2 =", V1*V2)

print(V12.mod())
print(V12, V12.norm())
print(V12.normed())
print(V12, V12. mod())



class Torseur(object):
    def __init__(self,Pos=Vecteur3D(),Rot=Vecteur3D(),Mom=Vecteur3D()): #Position, Resultante, Moment
        self.Pos = Pos
        self.Rot = Rot
        self.Mom = Mom
        
    def __str__(self):
        print('Le torseur est :')
        return 'Position = {0}, Résultante = {1} et Moment = {2}'.format(self.Pos.__str__(),self.Rot.__str__(),self.Mom.__str__()) 
        
    def __add__(self,autre):
        return Torseur(self.Pos, self.Rot+autre.Rot, self.Mom + autre.Mom + (autre.Pos-self.Pos) * autre.Rot)
    
    def __mul__(self,autre):
        if not isinstance(autre,Torseur):
            return Torseur(self.Pos,self.Rot*autre,self.Mom*autre)

    def __rmul__(self,autre):
        return self*autre
        
    def __neg__(self):
        return Torseur(self.Pos,self.Rot*(-1),self.Mom*(-1))
    
    def __truediv__(self,autre):
        return Torseur(self.Pos,self.Rot*(1/autre),self.Mom*(1/autre))
    
    
    
if __name__== '__main__':
    P1 = Vecteur3D()
    P2 = Vecteur3D(y=2)
    P3 = Vecteur3D(z=2)

    R1 = Vecteur3D()
    R2 = Vecteur3D(z= -10)
    R3 = Vecteur3D(x= -10)

    M1 = Vecteur3D(x=10)
    M2 = Vecteur3D()
    M3 = Vecteur3D(x=2,y=14)

    T1 = Torseur(P1,R1,M1)
    T2 = Torseur(P2,R2,M2)
    T3 = Torseur(P3,R3,M3)

    print(T1+T3)

