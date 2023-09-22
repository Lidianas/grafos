import matrix_graph
import list_graph

class main():
    inputFile = "grafos/exemplo_3.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()

    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    #mg.dfs(4)
    #mg.bfs(4)
    #lg.dfs(4)
    #lg.bfs(4)

    print(mg.dist(1,6))

    #print(mg.diameter())
    #print(lg.diameter())

    print(mg.connectedComponents())
    #print(lg.connectedComponents())

    #mg.graphInfo("graphInfos_matrixGraph.txt")
    #lg.graphInfo("graphInfos_listGraph.txt")


    
