# coding: utf-8
from Algorithm import *
from Optimizer import *

algorithm = Algorithm()

Outvariables = {'w':0,'f':0,}
variables = {'x':0,'y':0,'t':0}
optimizer = Optimizer(algorithm, variables, Outvariables,"dataset.json")

result =  optimizer.optimize()

#print(result)