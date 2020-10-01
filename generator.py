# coding: utf-8
from Simulator import *
import json
from classic_algo import *
from classic_algo_2 import *
import numpy as np
import matplotlib.pyplot as plt


simulator = Simulator()
subject = {'h':15.09,'g':38.084, 'f':-30}
algorithm = classic_algo_2()
subject_dataset = simulator.run(deepcopy(algorithm),subject)

start_x =  []
start_y =  []
start_e =  []

for item in subject_dataset:
    start_x.append(item['x'])
    start_y.append(item['y'])
    start_e.append(item['e'])


fig, axs = plt.subplots()
axs.plot(start_x, start_y)

plt.show()
f = open("output/dataset.json", "w")
f.write(json.dumps(subject_dataset))
f.close()



print("Data generated !")
