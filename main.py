# coding: utf-8
from Algorithm import *
from classic_algo import *
from classic_algo_2 import *
from article_algo import *
from Optimizer import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Simulator import *
import json

def plot_bar(solution, attente, filename="", title="Comparaison de l'energie"):
    bar_width = 0.35

    partial_attente=[]
    partial_solution=[]

    start_index = range(0,100,10)
    stop_index = range(5,100,10)

    for i in range(0, len(stop_index)):
        partial_attente = partial_attente + attente[start_index[i]:stop_index[i]]
        partial_solution = partial_solution + solution[start_index[i]:stop_index[i]]

    attente = partial_attente
    solution = partial_solution


    fig, ax = plt.subplots()
    n_groups = len(attente)
    index = np.arange(n_groups)
    opacity = 0.8
    rects1 = plt.bar(index, attente, bar_width,
    alpha=opacity,
    label='energie attendue')
    rects2 = plt.bar(index + bar_width, solution, bar_width,
    alpha=opacity,
    label='energie obtenue')
    plt.xlabel('unite de temps')
    plt.ylabel("Valeur de l'energie")
    plt.title(title)
    plt.xticks()
    #plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/'+filename+".png",dpi=200)
    plt.clf()

def subplot_path(data_1, data_2,  filename="", title="Comparaison des trajectoires", label_1="Trajectoire attendue", label_2="Trajectoire attendue", axe_x="Position sur l'abscisse", axe_y="Position sur l'ordonnee"):
    
    plt.plot(data_1[0],data_1[1])
    plt.plot(data_2[0],data_2[1])
    trim =  3
    plt.xlim(min(data_2[0])-trim, max(data_2[0])+trim)
    plt.ylim(min(data_2[1])-trim, max(data_2[1])+trim)

    plt.xlabel(axe_x)
    plt.ylabel(axe_y)
    plt.legend([label_1, label_2])
    plt.title(title)
    plt.savefig('graphics/'+filename+".png", dpi=200)
    plt.clf()

def plot_path(data, iterations, filename="", title="Evolution de l'adapation des solutions", axe_x="Iterarion", axe_y="log (adaptation)", max_fitness=100000):
    plt.plot(data,iterations)
    '''
    plt.xlim(0, len(iterations))
    plt.ylim(0, max(data)+5)
    '''
    plt.xlabel(axe_x)
    plt.ylabel(axe_y)
    plt.title(title)
    plt.savefig('graphics/'+filename+".png", dpi=200)
    plt.clf()

algorithm = Algorithm()
algorithm = classic_algo()
algorithm = classic_algo_2()
algorithm = article_algo()

dataset_file = "dataset.json"

dataset =  open(dataset_file,'r')
dataset = json.loads(dataset.read())

optimizer = Optimizer(algorithm,dataset_file)
result, metrics =  optimizer.optimize(100,500,40)

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

sommes_ecart= {}
sommes_ecart['start_traj'] = 0
sommes_ecart['start_bar'] = 0
sommes_ecart['midle_traj'] = 0
sommes_ecart['midle_bar'] = 0
sommes_ecart['stop_traj'] = 0
sommes_ecart['stop_bar'] = 0
sommes_ecart['data_traj'] = 0
sommes_ecart['data_bar'] = 0

for item in dataset:
    itab.append(i)

    start_x.append(start_solution_dataset[i]['x'])
    start_y.append(start_solution_dataset[i]['y'])
    start_e.append(start_solution_dataset[i]['e'])
    sommes_ecart['start_traj'] += sqrt(pow((start_solution_dataset[i]['x'] - item['x']), 2) +  pow((start_solution_dataset[i]['y'] - item['y']), 2)) 
    sommes_ecart['start_bar'] += sqrt(pow((start_solution_dataset[i]['e'] - item['e']), 2))


    midle_x.append(midle_solution_dataset[i]['x'])
    midle_y.append(midle_solution_dataset[i]['y'])
    midle_e.append(midle_solution_dataset[i]['e'])
    sommes_ecart['midle_traj'] += sqrt(pow((midle_solution_dataset[i]['x'] - item['x']), 2) +  pow((midle_solution_dataset[i]['y'] - item['y']), 2)) 
    sommes_ecart['midle_bar'] += sqrt(pow((midle_solution_dataset[i]['e'] - item['e']), 2))


    
    solution_x.append(end_solution_dataset[i]['x'])
    solution_y.append(end_solution_dataset[i]['y'])
    solution_e.append(end_solution_dataset[i]['e'])
    sommes_ecart['stop_traj'] += sqrt(pow((end_solution_dataset[i]['x'] - item['x']), 2) +  pow((end_solution_dataset[i]['y'] - item['y']), 2)) 
    sommes_ecart['stop_bar'] += sqrt(pow((end_solution_dataset[i]['e'] - item['e']), 2))


    dataset_x.append(item['x'])
    dataset_y.append(item['y'])
    dataset_e.append(item['e'])


    i +=1

subplot_path((solution_x,solution_y), (dataset_x, dataset_y),label_1="Trajectoire finale", filename="trajet_solution", title="Comparaison des trajectoires : Ecart =  " + str(sommes_ecart['start_traj']))
subplot_path((midle_x,midle_y), (dataset_x, dataset_y),label_1="Trajectoire a mi parcours", filename="trajet_mi_parcours", title="Comparaison des trajectoires : Ecart =  " + str(sommes_ecart['midle_traj']))
subplot_path((start_x,start_y), (dataset_x, dataset_y), label_1="Trajectoire au demarrage", filename="trajet_demarrage", title="Comparaison des trajectoires : Ecart =  " + str(sommes_ecart['stop_traj'] -  sommes_ecart['data_traj']))

plot_bar(start_e,dataset_e,filename="bar_demarrage", title="Comparaison de l'energie : Ecart =  "  + str(sommes_ecart['start_bar']))
plot_bar(midle_y,dataset_e,filename="bar_mi_parcours", title="Comparaison de l'energie : Ecart =  " + str(sommes_ecart['midle_bar']))
plot_bar(solution_e,dataset_e,filename="bar_solution", title="Comparaison de l'energie : Ecart =  " + str(sommes_ecart['stop_bar']))

plot_path(iterations, metrics['best_fitness'],  filename="evolution_best", title="Evolution de l'adapation de la meilleure solutions")
plot_path( iterations, metrics['fitness_average'],filename="evolution_mean", title="Evolution de l'adapation moyenne de la population")
