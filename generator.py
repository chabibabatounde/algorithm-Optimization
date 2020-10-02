# coding: utf-8
from Simulator import *
import json
from classic_algo import *
from classic_algo_2 import *
from article_algo import *
import numpy as np
import matplotlib.pyplot as plt

simulator = Simulator()
subject = {'h2':-1,'h3':0.6,'h4':-2.2,'h5':0.25,'h6':1.1,'h7':-6.3,'h8':0.3,'h9':1.1,'h10':1.9}
algorithm = article_algo()
subject_dataset = simulator.run(deepcopy(algorithm),subject)
for line in subject_dataset:
    print(line['t'],line['x'],line['y'],line['e'])
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



