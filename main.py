import time

import matrix_graph
import list_graph

class main():
    inputFile = "grafos/exemplo_1.txt"

    mg = matrix_graph.MatrixGraph()
    lg = list_graph.ListGraph()

    mg.readGraph(inputFile)
    lg.readGraph(inputFile)

    mg.bfs(1, "grafos/mg_bfs_output_test_file.txt")
    lg.bfs(1, "grafos/mg_bfs_output_test_file.txt")

    mg.dfs(1, "grafos/mg_dfs_output_test_file.txt")
    lg.dfs(1, "grafos/lg_dfs_output_test_file.txt")

    mg.dist(1,4)
    lg.dist(1,4)

    mg.approxDiameter()
    lg.approxDiameter()

    mg.connectedComponents()
    lg.connectedComponents()

    mg.graphInfo("grafos/mg_gi_output_test_file.txt")
    lg.graphInfo("grafos/lg_gi_output_test_file.txt")








    
