import matrix_graph
import list_graph

class main():
    inputFile = "exemplo.txt"
    outputFile = "graphInfos.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()

    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    lg_tree_v4 = lg.bfs(4)
    print(lg_tree_v4)

    d13 = lg.dist(1,3)
    print(d13)


    
