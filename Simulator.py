# coding: utf-8
import matplotlib.pyplot as plt
import networkx as nx
import json
class Simulator:
    def __init__(self):
        pass

    def run(self, algorithm, config=None):
        nx.draw(algorithm.graphe, labels=algorithm.labeldict, with_labels = True)
        #edge_labels=nx.draw_networkx_edge_labels(algorithm.graphe,pos=nx.spring_layout(algorithm.graphe))
        #plt.show()
        plt.clf()
        outputFile = open(".output.json", "w")
        outputFile.write("[\n")
        outputFile.close()
        self.computeNode(algorithm, algorithm.start)
        outputFile = open(".output.json", "r")
        data = outputFile.read()[:-2]
        outputFile.close()
        #OPTIONAL
        outputFile = open(".output.json", "w")
        outputFile.write(data+"\n]")
        outputFile.close()
        #OPTIONAL
        return json.loads(data+"\n]")

    def computeNode(self, algorithm, nodeId, previousNode=None):
        if len(algorithm.graphe[nodeId]) >= 1:
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
                
                neighbors = list(algorithm.graphe.neighbors(nodeId))
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        branch = algorithm.graphe[nodeId][line]
                        if(branch['r']==str(eval(value))):
                            nextNode = line
                            break
            if "logData" in value:
                otherMethods =  False
                algorithm.output.append(algorithm.all_variables_value)
                outputFile = open(".output.json","a")
                outputFile.write("\t"+ json.dumps(algorithm.all_variables_value)+",\n")
                outputFile.close()
                #algorithm.output.append()

                neighbors = list(algorithm.graphe.neighbors(nodeId))
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        nextNode = line
                        break
            if otherMethods:
                tab =  value.split("=")
                leftExpression = tab[0]
                rightExpression = tab[1]
                for variable in algorithm.program_variables:
                    rightExpression = rightExpression.replace(str(variable), str(algorithm.all_variables_value[variable]))
                for variable in algorithm.config_items:
                    rightExpression = rightExpression.replace(str(variable), str(algorithm.all_variables_value[variable]))
                algorithm.all_variables_value[leftExpression] =  eval(rightExpression)
                
                neighbors = list(algorithm.graphe.neighbors(nodeId))
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        nextNode = line
                        break
            
            if nextNode is not None:        
                self.computeNode(algorithm, nextNode, nodeId)
            return algorithm
