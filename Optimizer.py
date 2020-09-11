# coding: utf-8
from Algorithm import *
from Simulator import *
import random
import json
import math
from copy import deepcopy
import struct
from operator import itemgetter

class Optimizer:
    def __init__(self, algorithm, dataSet):
        self.algorithm = algorithm
        dataSet =  open(dataSet,'r')
        self.dataSet = json.loads(dataSet.read())

    def optimize(self, populationSize=5, maxIterration=100, pourcentage=40):
        return self.genetic(populationSize, maxIterration, pourcentage)

    def genetic(self, populationSize, maxIterration, pourcentage):
        iterration = 1
        population  = []
        #Générer une population
        for i in range(0, populationSize):
            subject = {}
            for key in self.algorithm.config_items:
                randomData = random.randint(0,24)
                subject[key] =  randomData
            population.append(subject)
        #evaluer la population
        population = self.gentic_evalSubject(population)
        #Trier la population
        population =  sorted(population, key=itemgetter('_'))
        #tant que pas de solution
        while iterration <= maxIterration:
            crossing = int(round(populationSize/100. * pourcentage))
            #Debut des croisements
            new_generation = []
            for i in range(0, crossing):
                #sélection des parents et croisements
                parents = self.genetic_parents_selection(population)
                childs = self.genetic_crossing(parents)
                #childs = self.genetic_crossing_with_normal_law(parents)
                #creation de la nouvelle génération
                new_generation.append(childs[0])
                new_generation.append(childs[1])
            #evaluation de la nouvelle génération
            new_generation = self.gentic_evalSubject(new_generation)
            #Fusion des populations
            population =  population + new_generation
            #Ordonner la population
            population =  sorted(population, key=itemgetter('_'))
            '''for item in new_generation:
                print(item['_'])'''
            #Mise à jour de la population
            population = population[:populationSize]
            print("\t[Iterration "+str(iterration)+"] : \t most_best = "+str(population[0]['_'])+" \t most_bad = "+str(population[populationSize-1]['_']))
            iterration += 1
        return population[0]

    def gentic_evalSubject(self, population ,sorted="ASC"):
        newPopulation = []
        for subject in population:
            fitness = 0
            #simulate subject and get dataset
            simulator = Simulator()
            subject_dataset = simulator.run(deepcopy(self.algorithm),subject)
            #Bon jusqu'ici
            for i in range(0,len(self.dataSet)):
                dataset_line = deepcopy(self.dataSet[i])
                subject_line = deepcopy(subject_dataset[i])
                '''
                print(dataset_line)
                print(subject_line)
                print("")
                '''
                for key in dataset_line:
                    #print(key)
                    try:
                        #ans = math.exp(200000)
                        fitness += math.pow(subject_line[key] - dataset_line[key],2)
                    except OverflowError:
                        fitness = float('inf')
            #subject["_"] = fitness
            subject["_"] = fitness / float(len(self.dataSet))
            newPopulation.append(subject)
        return newPopulation

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
        return result

    def genetic_codage(self, subject):
        binaryStr =  ""
        for key in subject:
            value = subject[key]
            bin = self.genetic_float_to_bin(value)
            binaryStr += bin
        return binaryStr

    def genetic_decodage(self, code, ref):
        start_index = 0
        end_index = 64
        subject = {}
        for key in ref:
            if key!="_":
                value =  self.genetic_bin_to_float(code[start_index:end_index])
                #print("key="+key+" bin ="+code[start_index:end_index]+" value="+str(value))
                start_index = start_index+64
                end_index = end_index+64
                subject[key] =  value
        return subject
    
    def genetic_crossing_point(self, subject_length):
        maximum_croissing = 64
        points = []
        number_of_crossing =  random.randint(1,maximum_croissing)
        for i in range (0, number_of_crossing):
            points.append(random.randint(1,subject_length))
        points.append(0)
        points.append(subject_length)
        points = sorted(points)
        return points

    def genetic_crossing_with_normal_law(self, parents):
        proportion = random.uniform(0, 1)
        child1 = {}
        child2 = {}
        for key in parents[0]:
            if key != "_":
                child1[key] = proportion*parents[0][key]+ (1-proportion)*parents[1][key]
                child2[key] = (1-proportion)*parents[0][key]+ proportion*parents[1][key]
        return child1, child2

    def genetic_bin_mutation(self, code):
        number = random.uniform(0,1)
        if number > 0.95:
            code = list(code)
            mutation_number = random.randint(1,8)
            mutation_index = []
            for i in range(1, mutation_number):
                mutation_index.append(random.randint(0,len(code)))
            mutation_index =  sorted(mutation_index)
            for index in mutation_index:
                if(index%16!=0):
                    if(code[index]=="0"):
                        code[index]="1"
                    else:
                        code[index]="0"
        return "".join(code)

    def genetic_crossing(self, parents):
        #parent1 = deepcopy(parents[0])
        parent1 = deepcopy(parents[0])
        parent2 = deepcopy(parents[1])
        parent1.pop("_")
        parent2.pop("_")
        code1 =  self.genetic_codage(parent1)
        code2 =  self.genetic_codage(parent2)
        
        points = self.genetic_crossing_point(len(code1))
        #print(points)
        child1 = ""
        child2 = ""
        switch = False

        for i in range(0, len(points)-1):
            if(switch):
                child1 = child1+code2[points[i]:points[i+1]]
                child2 = child2+code1[points[i]:points[i+1]]
            else:
                child1 = child1+code1[points[i]:points[i+1]]
                child2 = child2+code2[points[i]:points[i+1]]
            switch = not switch

        child1 = self.genetic_bin_mutation(child1)
        child2 = self.genetic_bin_mutation(child2)

        child1 = self.genetic_decodage(child1, parent1)
        child2 = self.genetic_decodage(child2, parent2)
        return child1,child2