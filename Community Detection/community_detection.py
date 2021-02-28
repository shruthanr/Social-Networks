# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:17:41 2021

@author: shrut
"""

# Community: Form many connections within the community
# Very few connection between communities
# Community Detection - Brute Force

import networkx as nx
import itertools
import matplotlib.pyplot as plt

def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()
   
    first_community = []
    
    for i in range(1, n//2 + 1):
        combs = [list(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(combs)
    
    second_community = []
    
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community[i]))
        second_community.append(l)
    

    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    
    # Ratio of number of intra : number of inter community edges
    ratio = []
    
    for i in range(len(first_community)):
        num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())
        num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())
        
    e = G.number_of_edges()
    for i in range(len(first_community)):
        num_inter_edges.append(e - (num_intra_edges1[i] + num_intra_edges2[i]))
    
    for i in range(len(first_community)):
        ratio.append(float((num_intra_edges1[i] + num_intra_edges2[i]) / num_inter_edges[i]))
        
    max_value = max(ratio)
    max_index = ratio.index(max_value)
    
    print('(', first_community[max_index], ')', '(', second_community[max_index], ')')
    

G = nx.barbell_graph(5, 0)
#communities_brute(G)

#nx.draw(G, with_labels=1)
#plt.show()
    

# Girvan Newman  Algorithm

def girvan_newman(G):

    c = [G.subgraph(i) for i in nx.connected_components(G)]
    l = len(c)
    
    print("The number of connected components are: {}".format(l))

    def edge_to_remove(G):
        """
        Returns the edge to be removed based on betweenness centrality 
        """
        dict1 = nx.edge_betweenness_centrality(G)
        list_of_tuples = list(dict1.items())
        
        # Sort by betweenness centrality 
        list_of_tuples.sort(key = lambda x : x[1], reverse=True)
        
        return list_of_tuples[0][0]
    
    while (l == 1):
        G.remove_edge(*edge_to_remove(G))
        c = [G.subgraph(i) for i in nx.connected_components(G)]
        l = len(c)
        print("The number of connected components are: {}".format(l))
        
    return c

#nx.draw(G, with_labels=True)
#plt.show()
#c = girvan_newman(G)

#for i in c:
#    print(i.nodes)
#    print('--------------')

G = nx.karate_club_graph()
c = girvan_newman(G)
for i in c:
    print(i.nodes)
    print('-----------')
    
    
    
    
    
    
    