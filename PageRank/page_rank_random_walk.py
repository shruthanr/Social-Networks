# -*- coding: utf-8 -*-
"""
@author: shrut
"""
import networkx as nx
import random
import numpy as np

def add_edges(G, p=0.3):
    for u in G.nodes():
        for v in G.nodes():
            if (u != v):
                r = random.random()
                if (r <= p):
                    G.add_edge(u, v)
                else:
                    continue
    return G


def random_walk(G):
    nodes = list(G.nodes())
    points = [0 for i in range(len(nodes))]
    
    r = random.choice(nodes)
    points[r] += 1
    
    outlinks = list(G.out_edges(r))
    
    c = 100000
    while (c > 0):
        if len(outlinks) == 0:
            current_node = random.choice(nodes)
        else:
            
            current_node = random.choice(outlinks)[1]
        
        points[current_node] += 1
        outlinks = list(G.out_edges(current_node))
        c -= 1
    return points
    


def sort_nodes_by_points(points):
    points = np.array(points)
    sorted_nodes = np.argsort(-points)
    return sorted_nodes
    
    
def main():
    # Create a graph
    G = nx.DiGraph()
    G.add_nodes_from(list(range(10)))
    G = add_edges(G, p=0.3)


    # Random Walk
    points = random_walk(G)
    
    # Rank the nodes
    sorted_nodes = sort_nodes_by_points(points)
    
    print("Nodes sorted by points: ", sorted_nodes)
    
    # Compare with NetworkX's imolementation
    print("Result from the networkx implementation of PageRank(for comparision):")
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key=lambda x : x[1], reverse=True)
    
    for i in pr_sorted:
        print(i[0], end=' ')
    
    
main()
