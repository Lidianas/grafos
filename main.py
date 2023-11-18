import time

import matrix_graph
import list_graph
from weighted_list_graph import WeightedListGraph
class main():

    inputFile = "grafos/grafo_rf_ex.txt"

    wlg = WeightedListGraph(2, True)
    wlg.readGraph(inputFile)
    maxFlow, flowAllocation = wlg.fordFulkerson(1, 2)
    print("Max flow: ", maxFlow)
    print("Flow allocation: ", flowAllocation)







    
