from particule_nonbloquant import particule as part
from Vecteur3D import Vecteur3D as V3D
import math

theta = input('Rotation de visée !:')
theta = float (theta)

elevation = input('Aaaaangle de tiiiir ?! :')
elevation = float(elevation)

force = input('Puissance du tir mon capitaine ? :')
force = float(force)

coeff = input('coefficient de trainée :')
coeff = float(coeff)

V0 = force * V3D(math.cos(theta) * math.cos(elevation), math.sin(theta), math.sin(elevation)).norm()

boulet = part(mass = 10, pos = V3D(0, 0, 1.5), vit = V0)

LimiteX = 10
LimiteZ = 0
LimiteY = 12

for i in range(600):
    if boulet.pos[-1].z < LimiteZ:
       boulet.chocz(coeff)
       
    if boulet.pos[-1].x > LimiteX: 
       boulet.chocx(coeff)
       
    if boulet.pos[-1].y > LimiteY: 
       boulet.chocy(coeff)
           
    boulet.setForce(V3D(0, 0, -9.81 * boulet.mass))
    boulet.simule(0.01)
    
    
boulet.trace()

