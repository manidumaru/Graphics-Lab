import networkx as nx
import matplotlib as plt

def number_of_nodes(graph):
    return len(graph.nodes)

def number_of_edges(graph):
    return len(graph.edges)

def calculate_average_degree(graph):
    sum = 0
    for node in graph.degree:
        sum += node[1]
    avg_degree = sum/len(graph.nodes)
    return avg_degree

def calculate_density(graph):
    e = graph.edges
    n = graph.nodes
    if len(n) > 1:
        density = 2*len(e) / (len(n) * (len(n)-1))
    else:
        density = 0
    return density

def calculate_diameter(graph):
    if not nx.is_connected(graph):
        return "infinite"
    diameter = 0
    nodes = graph.nodes
    for i in nodes:
        for j in nodes:
            if i == j:
                continue
            path_length = nx.shortest_path_length(graph, source = i, target = j)
            if path_length > diameter:
                diameter = path_length
    return diameter

def calculate_clustering(graph):
    nodes = graph.nodes
    total_cluster = 0
    for i in nodes:
        neighbour = list(nx.neighbors(graph, i))
        connection = 0
        for j in neighbour:
            for k in neighbour:
                if nx.is_path(graph, [j,k]):
                    connection += 1

        # connection should be fivided by 2 here because
        # the loop counts 1,2 as a connection and also counts
        # 2,1 as another connection since it is an undirected graph.

        if len(neighbour) > 1:
            total_cluster += (2*(connection/2))/ (len(neighbour) * (len(neighbour)-1))
    
    c = total_cluster / len(nodes)
    return c

def degree_distribution(graph):
    degree = graph.degree
    max_degree = max(y for (x,y) in degree)
    c_degree = [0 for _ in range(0, max_degree+1)]
    for i in range(0, max_degree+1):
        count = 0
        for (x,y) in degree:
            if y == i:
                count += 1
        if i == 0:
            pk = 0
        else:
            pk = count/len(graph.nodes)

        c_degree[i] = pk
    return c_degree