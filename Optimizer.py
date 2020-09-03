# coding: utf-8
from Algorithm import *
from Simulator import *
import random
import json
from copy import deepcopy
class Optimizer:
    def __init__(self, algorithm, varibles, Outvariables, dataSet):
        self.algorithm = algorithm
        self.varibles = varibles
        self.Outvariables = Outvariables
        dataSet =  open(dataSet,'r')
        self.dataSet = json.loads(dataSet.read())

    def optimize(self, populationSize=100):
        return self.genetic(populationSize)

    def evalSubject(self, population ,sorted="ASC"):
        newPopulation = []
        for subject in population:
            fitness = 0
            for line in self.dataSet:
                for key in line:
                    fitness += line[key] - subject[key]
            subject["ss"] = fitness
            newPopulation.append(subject)
        population = newPopulation
        return population
        

    def genetic(self, populationSize):
        population  = []
        #=> Générer une population
        for i in range(0, populationSize):
            subject = deepcopy(self.varibles)
            for key in self.Outvariables:
                randomData = random.randint(0,24)
                subject[key] =  randomData
            population.append(subject)
            
        #=> evaluer la population

        population = self.evalSubject(population)
        print(population)
        
        #=> tant que pas de solution
            #=> Sélectionner les reproducteurs
            #=> croiser les reproducteurs
            #=> muter les enfants
            #=> Evaluer
            #=> Mise à jour de la population

        


        parametersDict={'w':60,'f':10,'x':0,'y':0,'t':0}
        simulator = Simulator()
        #print(parametersDict)
        #print(population[0])
        
        output = simulator.run(self.algorithm,population[5])
        #output = simulator.run(self.algorithm,parametersDict)

        return output