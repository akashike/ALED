import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)

fig = plt.figure("Exemple de plot animé")

#plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy

plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")

plt.ion()
plt.show()

print("on peut faire autre chose sans attendre la fermeture du plot")

for i in range(100):
    
    plt.cla() # Efface le contenu
    
    # On recalcule tout
    y = np.sin(x+i/10)
    plt.plot(x,y) 
    plt.ylabel('fonction sinus')
    plt.xlabel("l'axe des abcisses")
    
    fig.canvas.flush_events() # on affiche
        

input("Press a key") # pour empecher la fin du programme et fermeture du plot
