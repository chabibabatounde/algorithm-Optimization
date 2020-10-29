# coding: utf-8
import networkx as nx
from math import *
import matplotlib.pyplot as plt
from Operator.boolOperator import *

class article_algo:
    def __init__(self):
        #TO DEFINE
        self.config_items = ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10']
        self.program_variables = ['e','t','x','y']
        #INITIALISATION
        self.output = []
        self.graphe = nx.Graph()
        self.grapheNodes = []
        self.labeldict = {}
        self.start = 0
        self.defineAlgorithm()
        self.all_variables_value =  {}
        #OPTIONAL
        self.default_init()

    def default_init(self):
        for item in self.config_items:
            self.all_variables_value[item]=0
        for item in self.program_variables:
            self.all_variables_value[item]=0

    def config_init(self, config):
        for item in config:
            self.all_variables_value[item]= config[item]

    def addNode(self, nodeId, node, label=None):
        if label is None:
            label =  node
        self.graphe.add_node(nodeId, value=node)
        self.labeldict[nodeId] = label

    def defineAlgorithm(self):
        self.addNode(0,"x=10")
        self.addNode(1,"y=0")
        self.addNode(2,"e=300")


        self.addNode(3,"(t>=0 and t<=30)")
        #self.addNode(4,"x=x+h2+e+t")
        self.addNode(4,"x=x+(h2*cos(t))")
        #self.addNode(5,"y=(2+y)+(h3+e)+t")
        self.addNode(5,"y=(y+(e/500.0))")
        #self.addNode(6,"e=e+h4")
        self.addNode(6,"e=e-h4")
        

        self.addNode(7,"((t>=31 and t<=50) or (t>=80 and t<=100) )")
        #self.addNode(8,"x=(2+x)+(h5+e)+t")
        self.addNode(8,"x=0.25*(x+(e/h5))")
        #self.addNode(9,"y=y+(h6+e)-t")
        self.addNode(9,"y=(y*sin(t)) + h6")
        #self.addNode(10,"e=e+h7")
        self.addNode(10,"e=e+h7")


        self.addNode(11,"x=x+(h8/2)")
        self.addNode(12,"y=y+(e/(100*h9))")
        self.addNode(13,"e=e+h10")


        self.addNode(14,"logData")
        self.addNode(15,"t=t+1")
        self.addNode(16,"t==100")
        #self.addNode(16,"t==10")
        self.addNode(17,"t=100")
        #self.addNode(17,"t=10")


        self.addNode(18,"t=t")

        
        self.graphe.add_edge(0, 1)
        self.graphe.add_edge(1, 2)
        self.graphe.add_edge(2, 3)


        self.graphe.add_edge(3, 4, r="True")
        self.graphe.add_edge(4, 5)
        self.graphe.add_edge(5, 6)
        self.graphe.add_edge(6, 14, r='Pass')
        self.graphe.add_edge(14, 15)
        self.graphe.add_edge(15, 16)
        self.graphe.add_edge(16, 17, r="True")
        self.graphe.add_edge(16, 18, r="False")
        self.graphe.add_edge(18, 3, r="Loop")


        self.graphe.add_edge(3, 7, r="False")
        self.graphe.add_edge(7, 8, r="True")
        self.graphe.add_edge(8, 9)
        self.graphe.add_edge(9, 10)
        self.graphe.add_edge(10, 14, r='Pass')


        self.graphe.add_edge(7, 11, r="False")
        self.graphe.add_edge(11, 12)
        self.graphe.add_edge(12, 13)
        self.graphe.add_edge(13, 14, r='Pass')


        #self.graphe.add_edge(0, 1, r='Pass')
        #self.graphe.add_edge(0, 1, r='Pass')
        
        
        #self.addNode(1,"((t>=0 and t<=6) or (t>=22 and t<=23))")
        #self.addNode(0,"t=0")
        #self.addNode(24,"t=0")
        #self.graphe.add_edge(0, 1, r='Pass')
        #self.graphe.add_edge(1, 2, r="True")
        #self.graphe.add_edge(8, 1, r="Loop")
        #self.graphe.add_edge(1, 9, r="False")
        
        
        self.start = 0