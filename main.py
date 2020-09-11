# coding: utf-8
from Algorithm import *
from Optimizer import *

algorithm = Algorithm()

optimizer = Optimizer(algorithm,"dataset.json")
result =  optimizer.optimize(100,200,40)

print(result)