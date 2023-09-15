import matrix_graph
import list_graph

class main():
    inputFile = "exemplo.txt"
    outputFile = "graphInfos.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()


    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    mg.dfs(4)
    mg.bfs(4)
    lg.dfs(4)
    lg.bfs(4)

    print(mg.diameter())
    print(lg.diameter())

    print(mg.connectedComponents())
    print(lg.connectedComponents())

    print(mg.ccDescendingOrder)
    print(lg.connectedComponents())


    mg.max_min_cc()
    lg.max_min_cc()
    mg.graphInfo("graphInfos_matrixGraph.txt")
    lg.graphInfo("graphInfos_listGraph.txt")


    
