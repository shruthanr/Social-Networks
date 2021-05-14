# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:52:44 2021

@author: shruthan
"""

import networkx as nx
import matplotlib.pyplot as plt
import random


def display_graph(G, i, newEdges):
    """
    Display graph when a new node i and newEdges are added
    """
    pos = nx.circular_layout(G)
    if (i == '' and newEdges == ''):
        new_node = []
        other_nodes = G.nodes()
        new_edges = []
        other_edges = G.edges()
    else:
        new_node = [i]
        other_nodes = list(set(G.nodes) - set(new_node))
        new_edges = newEdges
        other_edges = list(set(G.edges() - set(newEdges) - set([(b, a) for (a, b) in new_edges])))

    plt.plot()
    nx.draw_networkx_nodes(G, pos, nodelist=new_node, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=other_nodes, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=new_edges, edge_color='g', style='dashdot')
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='r')
    plt.show()

def add_nodes_barabasi(G, n, m0):
    m = m0-1
    
    for i in range(m0+1, n+1):
        G.add_node(i)
        
        degrees = nx.degree(G)
        node_probabilities = {i : degrees[i]/sum(dict(degrees).values()) for i in G.nodes()}
        
        cumulative_probs = []
        prev = 0
        for node, prob in node_probabilities.items():
            cumulative_probs.append([node, prev + prob])
            prev += prob
        
        new_edges = []
        num_edges_added = 0
        target_nodes = []
        
        while (num_edges_added < m):
            prev_cumulative = 0
            r = random.random()
            k = 0
            while (not(r > prev_cumulative and r <= cumulative_probs[k][1])):
                prev_cumulative = cumulative_probs[k][1]
                k += 1
            target_node = cumulative_probs[k][0]
            
            if target_node in target_nodes:
                continue
            
            target_nodes.append(target_node)
            G.add_edge(i, target_node)
            num_edges_added += 1
            new_edges.append((i, target_node))
            
        print("Number of edges added: ", num_edges_added)
        display_graph(G, i, new_edges)
    
    return G
        
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
        

def main():
    n = int(input("Enter the number of nodes: "))
    m0 = random.randint(2, n/5)
    
    G = nx.path_graph(m0)
    display_graph(G, '', '')
    
    G = add_nodes_barabasi(G, n, m0)
    plot_degree_distribution(G)
    
main()
    
    
