# coding: utf-8
from Algorithm import *
from classic_algo import *
from Optimizer import *

algorithm = Algorithm()
algorithm = classic_algo()

optimizer = Optimizer(algorithm,"dataset.json")
result =  optimizer.optimize(100,100,10)

print(result)
