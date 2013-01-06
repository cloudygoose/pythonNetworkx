#!/usr/bin/env python
"""
Draw a graph with matplotlib, color edges.
You must have matplotlib>=87.7 for this to work.
"""
import matplotlib.pyplot as plt
import networkx as nx

n = 20;
edge_thres = 0.15;
G = nx.star_graph(n)
pos = nx.spring_layout(G) #you can change it to random_layout

edges = G.edges()
G.remove_edges_from(edges) #I only want the positions

for i in range(n + 1):
    for j in range(i + 1, n + 1):
        (x1, y1) = pos[i]
        (x2, y2) = pos[j]
        if (x2 - x1) ** 2 + (y2 - y1) ** 2 < edge_thres:
            G.add_edge(i, j)

colors = range(n)
plt.figure(figsize = (8,8))
#remember here's we can change whether to show the labels
DG = nx.DiGraph(G)

nx.draw_networkx_nodes(DG, pos, node_color = '#A0CBE2')
nx.draw_networkx_labels(DG, pos, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0)
nx.draw_networkx_edges(DG, pos, width = 1.0, edge_color ='k')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.savefig("edge_colormap.png") # save as png
plt.show() # display

