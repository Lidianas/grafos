import matrix_graph
import list_graph

class main():
    inputFile = "exemplo.txt"
    outputFile = "graphInfos.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()


    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    mg.dfs(1)
    mg.bfs(1)
    lg.dfs(1)
    lg.bfs(1)
    """
    print(mg.diameter())
    print(lg.diameter())

    print(mg.connectedComponents())

    mg.graphInfo("graphInfos_matrixGraph.txt")
    lg.graphInfo("graphInfos_listGraph.txt")"""


    
