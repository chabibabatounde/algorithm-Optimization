# coding: utf-8
from Algorithm import *
from classic_algo import *
from classic_algo_2 import *
from Optimizer import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Simulator import *
import json

algorithm = Algorithm()
algorithm = classic_algo()
algorithm = classic_algo_2()

dataset_file = "dataset.json"

dataset =  open(dataset_file,'r')
dataset = json.loads(dataset.read())

optimizer = Optimizer(algorithm,dataset_file)
result, metrics =  optimizer.optimize(100,100,60)
#result, metrics =  optimizer.optimize(10,10,5)

#Performances
iterations =  range(1, len(metrics['worse_fitness'])+1)

simulator = Simulator()
del result['_']
start = metrics['start_solution']
midle = metrics['midle_solution']
del start['_']
del midle['_']

start_solution_dataset = simulator.run(deepcopy(algorithm),start)
midle_solution_dataset = simulator.run(deepcopy(algorithm),midle)
end_solution_dataset = simulator.run(deepcopy(algorithm),result)

dataset =  open(dataset_file,'r')
dataset = json.loads(dataset.read())

start_x =  []
start_y =  []
start_e =  []

midle_x = []
midle_y = []
midle_e = []

solution_x =[]
solution_y =[]
solution_e =[]

dataset_x =[]
dataset_y =[]
dataset_e =[]

i = 0
itab= []

bar_width = 0.35
for item in dataset:
    itab.append(i)

    start_x.append(start_solution_dataset[i]['x'])
    midle_x.append(midle_solution_dataset[i]['x'])
    solution_x.append(end_solution_dataset[i]['x'])
    dataset_x.append(item['x'])

    start_y.append(start_solution_dataset[i]['y'])
    midle_y.append(midle_solution_dataset[i]['y'])
    solution_y.append(end_solution_dataset[i]['y'])
    dataset_y.append(item['y'])

    start_e.append(start_solution_dataset[i]['e'])
    midle_e.append(midle_solution_dataset[i]['e'])
    solution_e.append(end_solution_dataset[i]['e'])
    dataset_e.append(item['e'])

    i +=1

width = 0.27  
fig, axs = plt.subplots(3, 2)
axs[0,0].plot(start_x, start_y, dataset_x, dataset_y, label="Trajectoires")
axs[0,0].set_ylabel("position sur a l'ordonnee")
axs[0,0].set_xlabel("position sur a l'abscisse")
axs[0,0].set_title("Trajectoires")
axs[0,0].legend(['Solution au demarrage','Jeux de donnees'])
axs[0,1].bar(itab, start_e, bar_width,   label="Energie")
axs[0,1].bar(itab, dataset_e, bar_width, label="Energie")
axs[0,1].set_ylabel("valeur de e")
axs[0,1].set_xlabel("temps")
axs[0,1].set_title("Variable e")
axs[0,1].legend(['Solution au demarrage','Jeux de donnees'])


axs[1,0].plot(midle_x, midle_y, dataset_x, dataset_y, label="Trajectoires")
axs[1,0].set_ylabel("position sur a l'ordonnee")
axs[1,0].set_xlabel("position sur a l'abscisse")
axs[1,0].set_title("Trajectoires")
axs[1,0].legend(['Solution au demarrage','Jeux de donnees'])
axs[1,1].bar(itab, midle_e, bar_width, label="Energie")
axs[1,1].bar(itab, dataset_e, bar_width, label="Energie")
axs[1,1].set_ylabel("valeur de e")
axs[1,1].set_xlabel("temps")
axs[1,1].set_title("Variable e")
axs[1,1].legend(['Solution au demarrage','Jeux de donnees'])


axs[2,0].plot(solution_x, solution_y, dataset_x, dataset_y, label="Trajectoires")
axs[2,0].set_ylabel("position sur a l'ordonnee")
axs[2,0].set_xlabel("position sur a l'abscisse")
axs[2,0].set_title("Trajectoires")
axs[2,0].legend(['Solution au demarrage','Jeux de donnees'])
axs[2,1].bar(itab, solution_e, bar_width, label="Energie")
axs[2,1].bar(itab, dataset_e, bar_width, label="Energie")
axs[2,1].set_ylabel("valeur de E")
axs[2,1].set_xlabel("temps")
axs[2,1].set_title("Variable e")
axs[2,1].legend(['Solution au demarrage','Jeux de donnees'])

fig.set_size_inches((8.5, 11), forward=False)
fig.tight_layout()
plt.savefig('Data.png', dpi=100)


plt.clf()
fig, axs = plt.subplots(3, 1)
axs[0].plot(iterations, metrics['best_fitness'],  label="Evolution de la meilleure solution de la population")
axs[0].set_xlabel('Iterations')
axs[0].set_ylabel("Adaptation")
axs[0].legend()

axs[1].plot(iterations, metrics['worse_fitness'], label="Evolution de la solution la moins bonne de la population")
axs[1].set_xlabel('Iterations')
axs[1].set_ylabel("Adaptation")
axs[1].legend()

axs[2].plot(iterations, metrics['fitness_average'], label="Evaluation  moyenne de la population")
axs[2].set_xlabel('Iterations')
axs[2].set_ylabel("Adaptation")
axs[2].set_title("Evaluation  moyenne de la population")
axs[2].legend()

fig.tight_layout()
plt.savefig('Evolution.png')

plt.clf()

'''
fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(itab, start_e, bar_width,   label="Energie")
rects2 = ax.bar(itab, dataset_e, bar_width, label="Energie")
ax.set_ylabel("valeur de e")
ax.set_xlabel("temps")
ax.set_title("Variable e")
ax.legend(['Solution au demarrage','Jeux de donnees'])
plt.savefig('A.png')
'''