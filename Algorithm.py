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
        self.output = []

    def defineVariables(self):
        self.variables = {'w':0,'f':5,'g':8,'x':1,'y':2,'t':0}
        #self.variables = {'a':3,'b':2,'c':1}
        #self.variables = {'a':0,'b':1,'c':2}

    def addNode(self, nodeId, node, label=None):
        if label is None:
            label =  node
        self.graphe.add_node(nodeId, value=node)
        self.labeldict[nodeId] = label

    def defineAlgorithm(self):
        self.addNode(0,"w>f and f<g")
        self.addNode(1,"w=5")
        self.addNode(2,"f>g")
        self.addNode(3,"g=6")
        self.addNode(4,"w=g-w")
        self.addNode(5,"g=w+f")
        self.addNode(6,"logData")
        self.addNode(7,"logData")

        self.graphe.add_edge(0, 1, r="True")
        self.graphe.add_edge(0, 2, r="False")
        self.graphe.add_edge(2, 3, r="True")
        self.graphe.add_edge(2, 4, r="False")
        self.graphe.add_edge(4, 5)
        self.graphe.add_edge(5, 6)
        self.graphe.add_edge(6, 7)

        self.start = 0