# coding: utf-8
from Algorithm import *
from Simulator import *

alg = Algorithm()

simulator = Simulator()
alg = simulator.run(alg)

print(alg.variables)
