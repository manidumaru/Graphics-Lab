
import networkx as nx
import matplotlib.pyplot as plt
import app

networks = [
    nx.read_edgelist("graphs/aves-sparrowlyon-flock-season2.edges", nodetype=int, data=(("Type", str),)), #46 nodes
    nx.read_edgelist("graphs/inf-power.mtx", nodetype=int, data=(("Type", str),)), #4941 nodes
    nx.read_edgelist("graphs/uk.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("graphs/n4c5-b7.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("graphs/USpowerGrid.mtx", nodetype=int, data=(("Type", str),)),
    nx.read_edgelist("graphs/model3.mtx", nodetype=int, data=(("Type", str),)),
]

for graph in networks:

    print(f"Number of Nodes = {app.number_of_nodes(graph)}")
    print(f"Number of Edges = {app.number_of_edges(graph)} \n")

    avg_degree = app.calculate_average_degree(graph)
    print(f"Average degree = {avg_degree} \n")

    density = app.calculate_density(graph)
    print(f"calculated density = {density}")
    print(f"built in function density = {nx.density(graph)} \n")

    diameter = app.calculate_diameter(graph)
    print(f"calculated diameter = {diameter}")
    if diameter == "infinite":
        print("Disconnected Graph: Diamter infinite \n")
    else:
        print(f"built in diameter = {nx.diameter(graph)} \n")
    
    ###################### Calculation of Diameter took very long time for network with more than 5K nodes

    clustering_coefficient = app.calculate_clustering(graph)
    print(f"calculated clustering coefficient = {clustering_coefficient}")
    print(f"built in function clustering = {nx.average_clustering(graph)}")

    y = app.degree_distribution(graph)
    x = [0 for _ in range(0, len(y))]
    for i in range(0, len(x)):
        x[i] = i
    plt.plot(x,y)
    plt.title(f"{len(graph.nodes)} nodes graph")
    plt.xlabel("Degree")
    plt.ylabel("p(k)")
    plt.show()
    print("---------------------------------------------------------------------")
