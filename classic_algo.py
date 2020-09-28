# coding: utf-8
import networkx as nx
from Operator.boolOperator import *

class classic_algo:
    def __init__(self):
        #TO DEFINE
        self.config_items = ['f','g', 'h']
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
        self.addNode(0,"t=0")

        #Repos
        self.addNode(1,"((t>=0 and t<=6) or (t>=22 and t<=23))")
        self.addNode(2,"e=e+h")
        self.addNode(3,"x=x+((1/10)*e)")
        self.addNode(4,"y=y+1")
        self.addNode(5,"logData")
        self.addNode(6,"t==23")
        self.addNode(7,"t=t+1")
        self.addNode(8,"t=0")
        #Balade
        self.addNode(9,"((t>=7 and t<=12) or (t>=16 and t<=21))")
        self.addNode(10,"e=e+f")
        self.addNode(11,"y= y + ((2/10)*e)")
        self.addNode(12,"x=x+3")
        self.addNode(13,"logData")
        self.addNode(14,"t==23")
        self.addNode(15,"t=t+1")
        self.addNode(16,"t=0")
        #Restau
        self.addNode(17,"t>=13 and t<=15")
        self.addNode(18,"e=e+g")
        self.addNode(19,"x=x+0.01")
        self.addNode(20,"y=y-0.01")
        self.addNode(21,"logData")
        self.addNode(22,"t==23")
        self.addNode(23,"t=t+1")
        self.addNode(24,"t=0")

        self.graphe.add_edge(0, 1, r='Pass')
        self.graphe.add_edge(1, 2, r="True")
        self.graphe.add_edge(2, 3)
        self.graphe.add_edge(3, 4)
        self.graphe.add_edge(4, 5)
        self.graphe.add_edge(5, 6)
        self.graphe.add_edge(6, 7, r="False")
        self.graphe.add_edge(6, 8, r="True")

        self.graphe.add_edge(7, 1, r="Loop")
        #self.graphe.add_edge(8, 1, r="Loop")


        self.graphe.add_edge(1, 9, r="False")
        self.graphe.add_edge(9, 10, r="True")
        self.graphe.add_edge(10, 11)
        self.graphe.add_edge(11, 12)
        self.graphe.add_edge(12, 13)
        self.graphe.add_edge(13, 14)
        self.graphe.add_edge(14, 15, r="False")
        self.graphe.add_edge(14, 16, r="True")

        self.graphe.add_edge(16, 1, r="Loop")
        self.graphe.add_edge(15, 1, r="Loop")


        self.graphe.add_edge(9, 17, r="False")
        self.graphe.add_edge(17, 18, r="True")
        self.graphe.add_edge(18, 19)
        self.graphe.add_edge(19, 20)
        self.graphe.add_edge(20, 21)
        self.graphe.add_edge(21, 22)
        self.graphe.add_edge(22, 23, r="False")
        #self.graphe.add_edge(22, 24, r="True")

        self.graphe.add_edge(24, 1, r="Loop")
        self.graphe.add_edge(23, 1, r="Loop")


        self.start = 0
