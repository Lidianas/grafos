import time
import random
import matrix_graph
import list_graph
import weighted_list_graph
class main():
    #Escolher o tipo de representação para distâncias
    # 1 - Vetor
    # 2 - Heap
    distType = 1
    execTime = []
    for c in range(1,6,1):
        inputFile = "grafos/grafo_W_"+str(c)+".txt"

        wlg = weighted_list_graph.WeightedListGraph(distType)
        wlg.readGraph(inputFile)

        for k in range(10):
            randV = random.randrange(1, wlg.n)
            iTime = time.time()
            dist, path = wlg.minDistPath(randV)
            fTime = time.time()
            rTime = fTime - iTime
            execTime.append([c, randV, rTime])
        
    with open('grafos/execTim_type1.txt', 'w') as et:
        for item in execTime:
            et.write("%s\n" % item)



    #Tipo 1 prints:
    #print(dist.distV)
    #Tipo 2 prints:
    #print(dist.distVector[19])
    #print(path[19])







    
