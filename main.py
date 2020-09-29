# coding: utf-8
from Algorithm import *
from classic_algo import *
from Optimizer import *
import numpy as np
import matplotlib.pyplot as plt
from Simulator import *
import json




algorithm = Algorithm()
algorithm = classic_algo()

optimizer = Optimizer(algorithm,"dataset.json")
#result, metric, dataset=  optimizer.optimize(150,500,40)
result, metric, dataset =  optimizer.optimize(10,5,5)

iterations =  []

for i in range(1, len(metric['worse_fitness'])+1):
    iterations.append(i)

fig, axs = plt.subplots(2, 1)
axs[0].plot(iterations, metric['best_fitness'], iterations, metric['worse_fitness'], label="Evolution des solutions")
axs[0].set_xlabel('Iterations')
axs[0].set_ylabel("Evaluation de l'adaptation")
axs[0].set_title("Evolution des solutions")
axs[0].legend(['Solution la plus bonne','Solution la plus mauvaise'])

axs[1].plot(iterations, metric['fitness_average'], label="Evaluation  moyenne de la population")
axs[1].set_xlabel('Iterations')
axs[1].set_ylabel("Evaluation de l'adaptation")
axs[1].set_title("Evaluation  moyenne de la population")
axs[1].legend()


#fig.tight_layout()
#plt.show()
plt.clf()

simulator = Simulator()
del result['_']
subject_dataset = simulator.run(deepcopy(algorithm),result)

x2 =  []
y2 =  []
e2 =  []

x1 =  []
y1 =  []
e1 =  []

i = 0
itab= []
for item in subject_dataset:
    itab.append(i)
    x1.append(item['x'])
    x2.append(dataset[i]['x'])

    y1.append(item['y'])
    y2.append(dataset[i]['y'])

    e1.append(item['e'])
    e2.append(dataset[i]['e'])
    i +=1



fig, axs = plt.subplots(2, 1)
axs[0].plot(x1, y1, x2, y2, label="Trajectoires")
axs[0].legend()
axs[0].set_ylabel("position sur a l'ordonnee")
axs[0].set_xlabel("position sur a l'abscisse")
axs[0].set_title("Trajectoires")
axs[0].legend(['Jeux de donnees','Solution trouvee'])

axs[1].plot(itab, e1, itab, e2, label= "Energie")
axs[1].legend()
axs[1].set_ylabel("valeur de E")
axs[1].set_xlabel("temps")
axs[1].set_title("Variable e (Energie)")
axs[1].legend(['Jeux de donnees','Solution trouvee'])

#fig.tight_layout()
#plt.show()



plt.clf()

fig, axs = plt.subplots(2, 1)
axs[0].plot(x1, y1, x2, y2, label="Trajectoires")
axs[0].legend()
axs[0].set_ylabel("position sur a l'ordonnee")
axs[0].set_xlabel("position sur a l'abscisse")
axs[0].set_title("Trajectoires")
axs[0].legend(['Jeux de donnees','Solution trouvee'])

axs[1].plot(itab, e1, itab, e2, label= "Energie")
axs[1].legend()
axs[1].set_ylabel("valeur de E")
axs[1].set_xlabel("temps")
axs[1].set_title("Variable e (Energie)")
axs[1].legend(['Jeux de donnees','Solution trouvee'])

fig.tight_layout()
plt.show()