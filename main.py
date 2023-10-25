import time

import matrix_graph
import list_graph
import weighted_list_graph
class main():

    inputFile = "grafos/grafo_W_4.txt"

    #Escolher o tipo de representação para distâncias
    # 1 - Vetor
    # 2 - Heap

    distType = 1

    wlg = weighted_list_graph.WeightedListGraph(distType)
    wlg.readGraph(inputFile)
    dist, path = wlg.minDistPath(10)

    #Tipo 1 prints:
    
    #Tipo 2 prints:
    print(dist.distVector[19])
    print(path[19])
    print("--------------------")
    print(dist.distVector[29])
    print(path[29])
    print("--------------------")
    print(dist.distVector[39])
    print(path[39])
    print("--------------------")
    print(dist.distVector[49])
    print(path[49])
    print("--------------------")
    print(dist.distVector[59])
    print(path[59])
    print("--------------------ß")

    







    
