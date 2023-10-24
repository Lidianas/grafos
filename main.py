import time

import matrix_graph
import list_graph
import weighted_list_graph
class main():

    inputFile = "grafos/grafo_W_3.txt"

    #Escolher o tipo de representação para distâncias
    # 1 - Vetor
    # 2 - Heap

    distType = 1

    wlg = weighted_list_graph.WeightedListGraph(distType)
    wlg.readGraph(inputFile)
    dist, path = wlg.minDistPath(10)

    #Tipo 1 prints:
    print("20")
    print(dist.distV[19])
    print(path[19])
    print("30")
    print(dist.distV[29])
    print(path[29])
    print("40")
    print(dist.distV[39])
    print(path[39])
    print("50")
    print(dist.distV[49])
    print(path[49])
    print("60")
    print(dist.distV[59])
    print(path[59])
    #Tipo 2 prints:
    #print(dist.dist)
    #print(path)







    
