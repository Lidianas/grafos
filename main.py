import matrix_graph
import list_graph

class main():
    inputFile = "exemplo.txt"
    outputFile = "graphInfos.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()

    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    mg.bfs()



    
