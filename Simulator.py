# coding: utf-8
import matplotlib.pyplot as plt
import networkx as nx

class Simulator:
    def __init__(self):
        pass

    def run(self, algorithm, config=None):
        nx.draw(algorithm.graphe, labels=algorithm.labeldict, with_labels = True)
        #edge_labels=nx.draw_networkx_edge_labels(algorithm.graphe,pos=nx.spring_layout(algorithm.graphe))
        #plt.show()
        plt.clf()
        return self.computeNode(algorithm, algorithm.start)

    def computeNode(self, algorithm, nodeId, previousNode=None):
        if len(algorithm.graphe[nodeId]) >= 2:
            nextNode = None
            booleanOperator = [">=",">","<","=<","=="]
            isBooleanOperator =  False
            variables = algorithm.variables
            value = algorithm.graphe.nodes[nodeId]['value']
            print(value)

            for element in booleanOperator:
                if element in value:
                    isBooleanOperator = True
                    break
                    
            if isBooleanOperator :
                for variable in variables:
                    value = value.replace(str(variable), str(variables[variable]))
                
                neighbors = list(algorithm.graphe.neighbors(nodeId))
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        branch = algorithm.graphe[nodeId][line]
                        if(branch['r']==str(eval(value))):
                            nextNode = line
                            break
            else:
                tab =  value.split("=")
                leftExpression = tab[0]
                rightExpression = tab[1]
                for variable in variables:
                    rightExpression = rightExpression.replace(str(variable), str(variables[variable]))
                variables[leftExpression] = eval(rightExpression)
                algorithm.variables=variables

                neighbors = list(algorithm.graphe.neighbors(nodeId))
                for line in neighbors:
                    if((line!=previousNode and previousNode is not None) or (previousNode is None)):
                        nextNode = line
                        break
            self.computeNode(algorithm, nextNode, nodeId)
            return algorithm
