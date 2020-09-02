# coding: utf-8
from Algorithm import *
from Simulator import *

alg = Algorithm()
simulator = Simulator()

parametersDict={'w':60,'f':10,'x':0,'y':0,'t':0}
output = simulator.run(alg,parametersDict)

print(output)