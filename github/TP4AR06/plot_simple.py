import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)

plt.figure("Exemple de plot simple")

plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy

plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")


plt.show()

print("Cette ligne s'affichera après la fermeture du plot")
