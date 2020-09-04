# coding: utf-8
from Algorithm import *
from Simulator import *
import random
import json

from copy import deepcopy
import struct
from operator import itemgetter

class Optimizer:
    def __init__(self, algorithm, varibles, Outvariables, dataSet):
        self.algorithm = algorithm
        self.varibles = varibles
        self.Outvariables = Outvariables
        dataSet =  open(dataSet,'r')
        self.dataSet = json.loads(dataSet.read())

    def optimize(self, populationSize=100, maxIterration=1000):
        return self.genetic(populationSize, maxIterration)

    def evalSubject(self, population ,sorted="ASC"):
        newPopulation = []
        for subject in population:
            fitness = 0
            for line in self.dataSet:
                for key in line:
                    fitness += line[key] - subject[key]
            subject["_"] = fitness
            newPopulation.append(subject)
        #population =  sorted(newPopulation, key=itemgetter('fit'))
        population = newPopulation
        return population

    def genetic_parents_selection(self, population):
        return population[random.randint(0, len(population)-1)], population[random.randint(0, len(population)-1)]

    def genetic_float_to_bin(self, num):
        if(num!=0):
            getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
            val = struct.unpack('Q', struct.pack('d', num))[0]
            result = getBin(val)
            if (len(result) < 64):
                for i in range(0, 64-len(result)):
                    result = "0"+result
            return result
        else:
            return "0000000000000000000000000000000000000000000000000000000000000000"

    def genetic_bin_to_float(self, bin):
        hx = hex(int(bin, 2))   
        result = struct.unpack("d", struct.pack("q", int(hx, 16)))[0]
        if (len(result) < 64):
            for i in range(0, 64-len(result)):
                result = "0"+result
        return result

    def genetic_codage(self, subject):
        binaryStr =  ""
        for key in subject:
            value = subject[key]
            bin = self.genetic_float_to_bin(value)
            binaryStr += bin
        return binaryStr
        

    def genetic_decodage(self, code):
        return {}

    def genetic_crossing(self, parents):
        code1 =  self.genetic_codage(parents[0])
        code2 =  self.genetic_codage(parents[1])
        
        return parents

    def genetic(self, populationSize, maxIterration):
        iterration = 1
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
        
        #=> tant que pas de solution
        while iterration < maxIterration:
            maxIterration
            #=> Sélectionner les reproducteurs
            parents = self.genetic_parents_selection(population)
            #=> croiser les reproducteurs
            enfants = self.genetic_crossing(parents)
            #=> muter les enfants
            #=> Evaluer
            #=> Mise à jour de la population
            iterration += 1

        


        parametersDict={'w':60,'f':10,'x':0,'y':0,'t':0}
        simulator = Simulator()
        #print(parametersDict)
        #print(population[0])
        
        output = simulator.run(self.algorithm,population[5])
        #output = simulator.run(self.algorithm,parametersDict)

        return output