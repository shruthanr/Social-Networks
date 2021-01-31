import networkx as nx
import matplotlib.pyplot as plt

# G1 = nx.read_edgelist('Datasets/facebook_combined.txt')
# print(nx.info(G1))
# print(nx.number_of_nodes(G))
# print(nx.number_of_edges(G))
# print(nx.is_directed(G))

# G2 = nx.read_pajek('Datasets/football.net')
# print(nx.info(G2))

# nx.draw(G2)
# plt.show()

# G = nx.read_graphml('Datasets/wikipedia.graphml')
# G = nx.read_gexf('Datasets/EuroSIS_Generale_Pays.gexf')

G = nx.read_gml('Datasets/karate.gml', label='id')
# nx.draw(G)
# nx.draw_circular(G)
# plt.show()

def plot_degree_distribution(G):
    all_degrees = list(dict(nx.degree(G)).values())
    unique_degrees = list(set(all_degrees))

    count_of_degrees = []
    for i in unique_degrees:
        count_of_degrees.append(all_degrees.count(i))

    plt.plot(unique_degrees, count_of_degrees, 'yo-')
    # plt.loglog(unique_degrees, count_of_degrees, 'yo-')
    plt.xlabel("Degrees")
    plt.ylabel("Number of Nodes")
    plt.title('Degree Distribution')
    plt.show()





plot_degree_distribution(G)
