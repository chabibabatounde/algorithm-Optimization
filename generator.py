# coding: utf-8
from Simulator import *
import json
from classic_algo import *
simulator = Simulator()
subject = {'h':500,'g':1024, 'f':135}
algorithm = classic_algo()
subject_dataset = simulator.run(deepcopy(algorithm),subject)

f = open("output/dataset.json", "w")
f.write(json.dumps(subject_dataset))
f.close()



print("Data generated !")
