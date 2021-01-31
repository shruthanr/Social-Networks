# To show that on adding ~(N/2) * log N edges to a graph with N nodes will
# make it connected

import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

def create_graph_n_nodes(n):
    """
    Returns a graph with n nodes from 0 ... n-1
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

# G = create_graph_n_nodes(10)
# print("Graph Created")
# print(f"Number of nodes: {G.number_of_nodes()}")
# print(f"Is graph connected? {nx.is_connected(G)}")

def add_random_edge(G):
    """
    Add a random edge in G
    """
    s = random.choice(list(G.nodes()))
    t = random.choice(list(G.nodes()))
    if s != t:
        G.add_edge(s, t)
    return G

# G = add_random_edge(G)
# print("After adding one edge: ")
# print(G.edges())

def add_till_connectivity(G):
    while (nx.is_connected(G) == False):
        G = add_random_edge(G)
    return G

# number_of_vertices = []
# edges_needed = []
# value_of_log = []
def single_instance(n):
    G = create_graph_n_nodes(n)
    print(nx.info(G))
    G = add_till_connectivity(G)
    return G.number_of_edges()
    # print(f"N is: {n}")
    # print("Number of edges added for connectivity: " + str(G.number_of_edges()))
    # print(f"Value of nlogn is  {n * np.log(n)}")
    # print(f"Value of n/2 * logn is  {(n/2) * np.log(n)}")
    # number_of_vertices.append(n)
    # edges_needed.append(G.number_of_edges())
    # value_of_log.append((n) * float(np.log(n)))

# Average number of edges needed over 20 instances
def create_avg_instance(n):
    m = 20
    avg = 0
    print(n)
    for i in range(m):
        avg += single_instance(n)
    return avg/m


def plot_connectivity():
    number_of_nodes = []
    edges_needed = []
    log_values = []
    for i in range(10, 400, 20):
        number_of_nodes.append(i)
        edges_needed.append(create_avg_instance(i))
        log_values.append((i/2) * float(np.log(i)))

    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Edges needed')
    plt.title("Emergences of connectedness")
    plt.plot(number_of_nodes, edges_needed)
    plt.plot(number_of_nodes, log_values)
    plt.show()

plot_connectivity()
