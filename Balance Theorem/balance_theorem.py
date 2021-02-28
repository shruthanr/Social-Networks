# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:20:46 2021

@author: shrut
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

# Create Graph
G = nx.Graph()
N = 8
G.add_nodes_from(list(range(1, N+1)))


# Add edges and signs to the edges
signs = ['+', '-']
for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i, j, sign=random.choice(signs))

# Display Graph
edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# Get all triangles in the graph
nodes = G.nodes()
triangles = [list(x) for x in itertools.combinations(nodes, 3)]

# Store details of the signs of the triangles
def get_signs_of_triangles(triangles, G):
    
    all_signs = []
    
    for tgle in triangles:
        current_signs = []
        current_signs.append(G[tgle[0]][tgle[1]]['sign'])
        current_signs.append(G[tgle[1]][tgle[2]]['sign'])
        current_signs.append(G[tgle[0]][tgle[2]]['sign'])
        all_signs.append(current_signs)
    
    return all_signs
   
all_signs = get_signs_of_triangles(triangles, G)
# Count stable and unstable triangles
def count_unstable(all_signs):
    stable = 0
    unstable = 0
    for curr_sign in all_signs:
        if curr_sign.count('+') == 3 or curr_sign.count('+') == 1:
            stable += 1
        elif curr_sign.count('+') == 2 or curr_sign.count('+') == 0:
            unstable += 1
    
    print("Number of stable triangles:", stable)
    print("Number of unstable triangles:", unstable)
    print()
    return unstable

unstable = count_unstable(all_signs)

    
# Stabilize the network
def stabilize_triangle(G, triangles, all_signs):
    found_unstable = False
    
    # Find one unstable triangle
    while (found_unstable == False):
        index = random.randint(0, len(triangles)-1)
        if all_signs[index].count('+') == 0 or all_signs[index].count('+') == 2:
            found_unstable = True
        else:
            continue
    
    # Stabilize the found unstable triangle
    r = random.randint(1, 3)
    
    # 2 positive edges, 1 negative edge -> 1 positive edge, 2 neg edges
    if all_signs[index].count('+') == 2:
        if r == 1:
            if G[triangles[index][0]][triangles[index][1]]['sign'] == '+':
                G[triangles[index][0]][triangles[index][1]]['sign'] = '-'
            else:
                G[triangles[index][0]][triangles[index][1]]['sign'] = '+'

        elif r == 2:
            if G[triangles[index][1]][triangles[index][2]]['sign'] == '+':
                G[triangles[index][1]][triangles[index][2]]['sign'] = '-'
            else:
                G[triangles[index][1]][triangles[index][2]]['sign'] = '+'
        else:
            if G[triangles[index][0]][triangles[index][2]]['sign'] == '+':
                G[triangles[index][0]][triangles[index][2]]['sign'] = '-'
            else:
                G[triangles[index][0]][triangles[index][2]]['sign'] = '+'            
    
    # 3 negative edges -> 2 negative edges, 1 positive edge
    else:
        if r == 1:
            G[triangles[index][0]][triangles[index][1]]['sign'] = '+'
        elif r == 2:
            G[triangles[index][1]][triangles[index][2]]['sign'] = '+'
        else:
            G[triangles[index][0]][triangles[index][2]]['sign'] = '+'
            
    return G

num_of_unstables = [unstable]

while (unstable > 0):
    G = stabilize_triangle(G, triangles, all_signs)
    all_signs = get_signs_of_triangles(triangles, G)
    unstable = count_unstable(all_signs)
    num_of_unstables.append(unstable)
    
#plt.bar(list(range(0, len(num_of_unstables))), num_of_unstables)
#plt.show()

# Form two coalitions
def form_coalitions(G):
    first_coalition = []
    second_coalition = []
    
    node = random.choice(list(G.nodes()))
    
    first_coalition.append(node)
    
    processed_nodes = []
    to_be_processed = [node]
    
    while len(to_be_processed) > 0:
        n = to_be_processed.pop(0)
        if n not in processed_nodes:
            neigh = G.neighbors(n)
            
            for i in neigh:
                if G[n][i]['sign'] == '+':
                    if i not in first_coalition:
                        first_coalition.append(i)
                    if i not in to_be_processed:
                        to_be_processed.append(i)
                elif G[n][i]['sign'] == '-':
                    if i not in second_coalition:
                        second_coalition.append(i)
                        processed_nodes.append(i)
            processed_nodes.append(n)
    return first_coalition, second_coalition
       
first, second = form_coalitions(G) 
print("First coalition:", first)
print("Second coalition: ", second)

# Display Graph
edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=first, node_color='red', alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=second, node_color='green', alpha=0.8)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()




