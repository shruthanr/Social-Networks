# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:19:00 2021

@author: shruthan
"""

# Schelling Model
import networkx as nx
import matplotlib.pyplot as plt
import random

N = 10
G = nx.grid_2d_graph(N, N)
pos = dict((n, n) for n in G.nodes())
labels = dict( ((i, j), i*10+j) for i, j in G.nodes())


    
for ((u,v), d) in G.nodes(data=True):
    if (u+1 <= N-1) and (v+1 <= N-1):
        G.add_edge((u,v), (u+1, v+1))
        
for ((u,v), d) in G.nodes(data=True):
    if (u+1 <= N-1) and (v-1 >= 0):
        G.add_edge((u,v), (u+1, v-1))
    
# nx.draw(G, pos, with_labels=False)
# nx.draw_networkx_labels(G, pos, labels=labels)
# plt.show()

# Adding People
for n in G.nodes():
    G.nodes[n]['type'] = random.randint(0, 2)
    
empty_cells = [n for (n, d) in G.nodes(data=True) if d['type'] == 0]
type1_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 1]
type2_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 2]

def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G, pos,  nodelist=type1_node_list, node_color='green')
    nodes_r = nx.draw_networkx_nodes(G, pos,  nodelist=type2_node_list, node_color='red')
    nodes_w = nx.draw_networkx_nodes(G, pos,  nodelist=empty_cells, node_color='white')
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=labels)
    
    plt.show()

display_graph(G)


def get_boundary_nodes(G):
    boundary_nodes_list = []
    
    for ((u, v), d) in G.nodes(data=True):
        if (u == 0  or u == N-1 or v == 0 or v == N-1):
            boundary_nodes_list.append((u, v))
            
    return boundary_nodes_list

boundary_nodes_list = get_boundary_nodes(G)
internal_nodes_list = list(set(G.nodes()) - set(boundary_nodes_list))

def get_neigh_for_internal(u, v):
    return [(u-1, v), (u+1, v), (u, v-1), (u, v+1), (u-1, v+1), (u+1, v-1), (u-1, v-1), (u+1, v+1)]

def get_neigh_for_boundary(u, v):
    
    if (u == 0 and v == 0):
        return [(0, 1), (1, 1), (1, 0)]

    elif u == N-1 and v == N-1:
        return [(N-2, N-2), (N-1, N-2), (N-2, N-1)]
    
    elif u == N-1 and v == 0:
        return [(u-1, v), (u, v+1), (u-1, v+1)]
    
    elif u == 0 and v == N-1:
        return [(u+1, v), (u+1, v-1), (u, v-1)]
    
    elif u == 0:
        return [(u, v-1), (u, v+1), (u+1, v), (u+1, v-1), (u+1, v+1)]
    
    elif u == N-1:
        return [(u-1, v), (u, v-1), (u, v+1), (u-1, v+1), (u-1, v-1)]
    
    elif v == N-1:
        return [(u, v-1), (u-1, v), (u+1, v), (u-1, v-1), (u+1, v-1)]
    
    elif v == 0:
        return [(u-1, v), (u+1, v), (u, v+1), (u-1, v+1), (u+1, v+1)]



def get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list, t=3):
    unsatisfied_nodes_list = []
    for u, v in G.nodes():
        curr_type = G.nodes[(u, v)]['type']
        
        if curr_type == 0:
            continue
    
        similar_nodes = 0
        
        if (u, v) in internal_nodes_list:
            neighbors = get_neigh_for_internal(u, v)   
        else:
            neighbors = get_neigh_for_boundary(u, v)
        
        for neigh in neighbors:
            if G.nodes[neigh]['type'] == curr_type:
                similar_nodes += 1
                
        if similar_nodes <= t:
            unsatisfied_nodes_list.append((u, v))
    
    return unsatisfied_nodes_list
            
        
# uns_list = get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list)
# print(uns_list)

def satisfy_node(uns_list, empty_cells):
    if len(uns_list) == 0:
        return
    node_to_shift = random.choice(uns_list)
    new_position = random.choice(empty_cells)
    
    G.nodes[new_position]['type'] = G.nodes[node_to_shift]['type']
    G.nodes[node_to_shift]['type'] = 0
    
    labels[node_to_shift], labels[new_position] = labels[new_position], labels[node_to_shift]
 
    
 
display_graph(G)
for i in range(5000):
    uns_list = get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list)
    satisfy_node(uns_list, empty_cells)
    empty_cells = [n for (n, d) in G.nodes(data=True) if d['type'] == 0]
    type1_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 1]
    type2_node_list = [n for (n, d) in G.nodes(data=True) if d['type'] == 2]
    
display_graph(G)

        
    