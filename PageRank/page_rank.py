# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:10:13 2021

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


def distribute_points(G, points):
    new_points = [0 for _ in range(G.number_of_nodes())]
    for u in G.nodes():
        outlinks = G.out_edges(u)
        if len(outlinks) == 0:
            new_points[u] += points[u]
        
        else:
            share = points[u]/len(outlinks)
            for link in outlinks:
                new_points[link[1]] += share
    return new_points

def taxation(G, points, s=0.8):
    for i in range(len(points)):
        points[i] = points[i]*s
    
    n = G.number_of_nodes()
    extra = (n * 100 * (1-s)) / n
    for i in range(len(points)):
        points[i] += extra
        
    return points
    
    
def distribute_points_till_conv(G, points):
    print("Enter # to stop")
    while(1):
        new_points = distribute_points(G, points)
        
        new_points = taxation(G, new_points)
        points = new_points
        print(points)
        c = input()
        if c == '#':
            break
    return points

def sort_nodes_by_points(points):
    points = np.array(points)
    sorted_nodes = np.argsort(-points)
    return sorted_nodes
    
    
def main():
    G = nx.DiGraph()
    G.add_nodes_from(list(range(10)))
    G = add_edges(G, p=0.3)
    points = [100 for _ in range(G.number_of_nodes())]
    print(points)
    points = distribute_points_till_conv(G, points)
    sorted_nodes = sort_nodes_by_points(points)
    
    print("Nodes sorted by points: ", sorted_nodes)
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key=lambda x : x[1], reverse=True)
    
    for i in pr_sorted:
        print(i[0], end=' ')
    
    
main()
