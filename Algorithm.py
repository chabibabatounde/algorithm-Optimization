# coding: utf-8
import networkx as nx
from Operator.boolOperator import *

class Algorithm:
    def __init__(self):
        self.graphe = nx.Graph()
        self.grapheNodes = []
        self.labeldict = {}
        self.start = 0
        self.defineAlgorithm()
        self.defineVariables()

    def defineVariables(self):
        self.variables = {'a':0,'b':5,'c':8}
        self.variables = {'a':3,'b':2,'c':1}
        self.variables = {'a':0,'b':1,'c':2}

    def addNode(self, nodeId, node, label=None):
        if label is None:
            label =  node
        self.graphe.add_node(nodeId, value=node)
        self.labeldict[nodeId] = label

    def defineAlgorithm(self):
        self.addNode(0,"a>b")
        self.addNode(1,"a=5")
        self.addNode(2,"b>c")
        self.addNode(3,"c=6")
        self.addNode(4,"a=c")
        self.addNode(5,"c=b")

        self.graphe.add_edge(0, 1, r="True")
        self.graphe.add_edge(0, 2, r="False")
        self.graphe.add_edge(2, 3, r="True")
        self.graphe.add_edge(2, 4, r="False")
        self.graphe.add_edge(4, 5)

        self.start = 0