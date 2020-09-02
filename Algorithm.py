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
        self.variables = {'w':60,'f':10,'x':0,'y':0,'t':0}
        #self.variables = {'a':3,'b':2,'c':1}
        #self.variables = {'a':0,'b':1,'c':2}

    def addNode(self, nodeId, node, label=None):
        if label is None:
            label =  node
        self.graphe.add_node(nodeId, value=node)
        self.labeldict[nodeId] = label

    def defineAlgorithm(self):
        self.addNode(1,"t>8 and t<=12")
        self.addNode(0,"t=t+1")
        self.addNode(2,"w=w-2")
        self.addNode(3,"x=y+(w/10)")
        self.addNode(4,"y=x+f")
        self.addNode(5,"logData")
        self.addNode(6,"t==24")
        self.addNode(7,"t=0")
        self.addNode(8,"t=t+1")
        self.addNode(9,"w=w+5")
        self.addNode(10,"y=y-(w/10 + x)")
        self.addNode(11,"logData")
        self.addNode(12,"t==24")
        self.addNode(13,"t=0")

        self.graphe.add_edge(0, 1, r="True")
        self.graphe.add_edge(0, 8, r="False")
        self.graphe.add_edge(1, 2)
        self.graphe.add_edge(2, 3)
        self.graphe.add_edge(3, 4)
        self.graphe.add_edge(4, 5)
        self.graphe.add_edge(5, 6)
        self.graphe.add_edge(6, 7, r="True")
        self.graphe.add_edge(6, 0, r="False")
        self.graphe.add_edge(8, 9)
        self.graphe.add_edge(9, 10)
        self.graphe.add_edge(10, 11)
        self.graphe.add_edge(11, 12)
        self.graphe.add_edge(12, 13, r="True")
        self.graphe.add_edge(12, 0, r="False")

        self.start = 0