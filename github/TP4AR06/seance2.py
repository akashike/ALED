import numpy as np
import matplotlib.pyplot as plt

T = 2 #temps final
h = 1.e-3 #pas de temps
g = -9.81
nSteps = int(T/h)

x0 = np.random.rand(4,1)
xEvolv=np.zeros((4, nSteps))

xEvolv[:,[0]] = x0

dx = np.zeros((4,1))
'''
for k in range(1, nSteps):
	#integration
	dx[0,0] = xEvolv[2, k-1]
	dx[1,0] = xEvolv[3, k-1]
	
	xEvolv[:, [k]] = xEvolv[:, [k-1]] + h * dx
	
dx = np.zeros((4,))
dx[3,] = g*h
'''

dx = np.zeros((4,))
dx[3,] = g*h

for k in range (1,nSteps):
	dx[:2] = xEvolv[2:,k-1]*h
	
	xEvolv[:,k] = xEvolv[:,k-1] + dx
	
#Affichage
	
t = np.arange(0., T, h, dtype=np.float_)

fig,subplots = plt.subplots(2,2)


subplots[0,0].plot(xEvolv[0,:], xEvolv[1, :])
subplots[1, 0].plot(t, xEvolv[3,:])

energy = - xEvolv[1,:]*g + np.sum(np.square(xEvolv[2:,:]), axis=0)/2
subplots[0, 1].plot(t, energy)
plt.show()
