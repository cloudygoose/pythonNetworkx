#!/usr/bin/env python
"""
Draw a graph with matplotlib, color edges.
You must have matplotlib>=87.7 for this to work.
"""

"""backup I store some functions that might be useful here
plt.show() # display the picture in a window  attention that this will block the process, if you want to continue, close it.
"""

import matplotlib.pyplot as plt
import networkx as nx
import time

imagecount = 0

def savePicture():
    global imagecount
    plt.savefig("edge_color" + str(imagecount) + ".png")
    imagecount = imagecount + 1

def drawGraph(G, pos):
    plt.figure(figsize = (8,8))
    nx.draw_networkx_nodes(G, pos, node_color = '#A0CBE2')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0)
    nx.draw_networkx_edges(G, pos, width = 1.0, edge_color ='k')
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)

def remove_all_edges(G):
    edges = G.edges()
    G.remove_edges_from(edges) #I only want the positions

def get_pairing(G, edges):
    nodes = G.nodes()
    for (x, y) in edges:
        if ((x in nodes) and (y in nodes)):
            G.add_edge(x, y)
            nodes.remove(x)
            nodes.remove(y)
    
n = 20;
edge_thres = 0.15;
G = nx.star_graph(n)
pos = nx.spring_layout(G) #you can change it to random_layout

remove_all_edges(G)
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        (x1, y1) = pos[i]
        (x2, y2) = pos[j]
        if (x2 - x1) ** 2 + (y2 - y1) ** 2 < edge_thres:
            G.add_edge(i, j)

DG = nx.DiGraph(G) #turn it to a directional

drawGraph(DG, pos)
savePicture() #the original graph

edges = DG.edges()
remove_all_edges(DG)
get_pairing(DG, edges)
drawGraph(DG, pos)
savePicture()
plt.clf() #clear the image
savePicture()
