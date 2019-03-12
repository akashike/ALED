'''
==============
3D scatterplot
==============

Demonstration du simple scatterplot en 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Générateur d'une liste de n points alétoire entre vmin et vmax
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure('Points')
ax = fig.gca(projection='3d')


# On fournit 3 listes: respectivement pour les coord X, y et z de chaque point. 
# ici on crée 100 points aléatoires.

n = 100

   
xs = randrange(n, 23, 32)
ys = randrange(n, 0, 100)
zs = randrange(n, 10, 25)
    
ax.scatter(xs, ys, zs, c='red', marker='*')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
###########################################################################

fig = plt.figure('Lignes')
ax = fig.gca(projection='3d')

ax.plot (xs, ys, zs, c='red', marker='o')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

