# coding: utf-8
from Algorithm import *
from classic_algo import *
from Optimizer import *

algorithm = Algorithm()
algorithm = classic_algo()

optimizer = Optimizer(algorithm,"dataset.json")
result =  optimizer.optimize(100,1000,40)

print(result)