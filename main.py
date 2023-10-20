import time

import matrix_graph
import list_graph
import weighted_list_graph
class main():

    inputFile = "grafos/exemplo_1.txt"

    #Escolher o tipo de representação para distâncias
    # 1 - Vetor
    # 2 - Heap

    distType = 2

    wlg = weighted_list_graph.WeightedListGraph(distType)
    wlg.readGraph(inputFile)
    dist, path = wlg.minDistPath(1)

    #Tipo 1 prints:
    #print(dist.distV)
    #print(path)

    #Tipo 2 prints:
    print(dist.dist.distV)
    print(path)







    
