# coding: utf-8
import matplotlib.pyplot as plt
import networkx as nx
import json
from time import sleep
from math import *
from copy import deepcopy

class Simulator:
    def __init__(self):
        pass

    def run(self, algorithm, config=None):
        nx.draw(algorithm.graphe, labels=algorithm.labeldict, with_labels = True)
        #edge_labels=nx.draw_networkx_edge_labels(algorithm.graphe,pos=nx.spring_layout(algorithm.graphe))
        #plt.show()
        plt.clf()
        #print(algorithm.all_variables_value)
        #print(config)
        algorithm.config_init(config)
        #print(algorithm.all_variables_value)
        new_algorithm = self.computeNode(algorithm, algorithm.start)
        return new_algorithm.output

    def computeNode(self, algorithm, nodeId, previousNode=None):
        if len(algorithm.graphe[nodeId]) >= 1:
            neighbors = []
            nextNode = None
            otherMethods =  True
            booleanOperator = [">=",">","<","=<","=="]
            isBooleanOperator =  False
            value = algorithm.graphe.nodes[nodeId]['value']
            for element in booleanOperator:
                if element in value:
                    isBooleanOperator = True
                    break
            if isBooleanOperator :
                otherMethods =  False
                for variable in algorithm.program_variables:
                    value = value.replace(str(variable), str(algorithm.all_variables_value[variable]))
                for variable in algorithm.config_items:
                    value = value.replace(str(variable), str(algorithm.all_variables_value[variable]))
                
            if "logData" in value:
                otherMethods =  False
                algorithm.output.append(deepcopy(algorithm.all_variables_value))
                #algorithm.output.append()                

            if otherMethods:
                tab =  value.split("=")
                leftExpression = tab[0]
                rightExpression = tab[1]
                for variable in algorithm.program_variables:
                    rightExpression = rightExpression.replace(str(variable), str(algorithm.all_variables_value[variable]))
                for variable in algorithm.config_items:
                    rightExpression = rightExpression.replace(str(variable), str(algorithm.all_variables_value[variable]))
                algorithm.all_variables_value[leftExpression] =  eval(rightExpression)
                

            #Getting Next Node
            neighbors = list(algorithm.graphe.neighbors(nodeId))
            if isBooleanOperator :
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        if(nodeId < line):
                            branch = algorithm.graphe[nodeId][line]
                            if(branch['r']==str(eval(value))):
                                nextNode = line
                                break
            else:
                for line in neighbors:
                    branch = algorithm.graphe[nodeId][line]
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        if(nodeId==18):
                            nextNode = line
                            break
                        if(nodeId < line):
                            nextNode = line
                            break


            if nextNode is not None: 
                algorithm = self.computeNode(algorithm, nextNode, nodeId)
            
            return algorithm
