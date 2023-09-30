import time

import matrix_graph
import list_graph

class main():
    inputFile = "grafos/grafo_1.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()

    #Estudo de caso 1
    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    #Estudo de caso 2
    times = []
    for i in range(100):
        inicial = time.time()
        lg.bfs(i + 1)
        final = time.time()
        times.append(final - inicial)
    print(sum(times) / len(times))

    #Estudo de caso 3
    times = []
    for i in range(100):
        inicial = time.time()
        lg.dfs(i+1)
        final = time.time()
        times.append(final-inicial)
    print(sum(times)/len(times))

    #Estudo de caso 4 - Os respectivos pais foram encontrados no arquivo de output com a arvore gerado pelas buscas
    lg.bfs(1)
    lg.bfs(2)
    lg.bfs(3)

    lg.dfs(1)
    lg.dfs(2)
    lg.dfs(3)

    #Estudo de caso 5
    print(lg.dist(10,20))
    print(lg.dist(10,30))
    print(lg.dist(20,30))

    #Estudo de caso 6
    print(lg.connectedComponents())

    #Estudo de caso 7
    print(lg.approxDiameter())



    
