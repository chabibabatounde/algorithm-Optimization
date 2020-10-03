# coding: utf-8
from Simulator import *
import json
from classic_algo import *
from classic_algo_2 import *
from article_algo import *
import numpy as np
import matplotlib.pyplot as plt

simulator = Simulator()
subject = {
    'h2':11,
    'h3':5,
    'h4':9,
    'h5':4,
    'h6':1,
    'h7':6,
    'h8':1,
    'h9':7,
    'h10':3
    }
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

plt.savefig('data_set.png', dpi=100)
f = open("output/dataset.json", "w")
f.write(json.dumps(subject_dataset))
f.close()
print("Data generated !")



