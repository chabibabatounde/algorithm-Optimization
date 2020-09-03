# coding: utf-8


class Genetic:
    def __init__(self, algorithm, dataSet):
        self.algorithm = algorithm
        dataSet =  open(dataSet,'r')
        self.dataSet = json.loads(dataSet.read())

    def optimize(self):
        parametersDict={'w':60,'f':10,'x':0,'y':0,'t':0}
        simulator = Simulator()
        output = simulator.run(self.algorithm,parametersDict)
        return output