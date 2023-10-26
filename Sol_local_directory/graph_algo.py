import osmnx as ox
import networkx as nx
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

#Graph Algorithms

def get_odd_nodes(graph):
    odd_nodes = []
    for i,j in nx.degree(graph):
        if j%2==1:
            odd_nodes.append(i)
    return odd_nodes

def node_combo(odd_list):
    return list(itertools.combinations(odd_list, 2))

def get_shortest_paths(graph, pairs):
    short_paths = {}
    for pair in pairs:
        short_paths[pair] = nx.dijkstra_path_length(graph, pair[0], pair[1], weight='distance')
    return short_paths

def make_complete(pair_weights):
    graph = nx.Graph()
    for k, v in pair_weights.items():
        wt_i = - v
        graph.add_edge(k[0], k[1], attr_dict={'distance': v, 'weight': wt_i})
    return graph

def min_weight_matching(complete_odd_graph):
    odd_max_match = nx.algorithms.max_weight_matching(complete_odd_graph, True)
    odd_min_match = list(pd.unique([tuple(sorted([k, v])) for k, v in odd_max_match]))
    return odd_min_match

def join_aug_edges(graph,weight_pairs):
    graph_aug = nx.MultiGraph(graph.copy())
    for pair in weight_pairs:
        graph_aug.add_edge(pair[0],
                           pair[1],
                           attr_dict={'distance': nx.dijkstra_path_length(graph, pair[0], pair[1]),
                                      'trail': 'augmented'}
                          )
    return graph_aug

def create_eulerian_circuit(graph_augmented, graph_original, starting_node=None):
    euler_circuit = []
    naive_circuit = list(nx.eulerian_circuit(graph_augmented, source=starting_node))

    for edge in naive_circuit:
        edge_data = graph_augmented.get_edge_data(edge[0], edge[1])
        if "attr_dict" in edge_data[0] and edge_data[0]['attr_dict']['trail'] != 'augmented':
            # If `edge` exists in original graph, grab the edge attributes and add to eulerian circuit.
            edge_att = graph_original[edge[0]][edge[1]]
            euler_circuit.append((edge[0], edge[1], edge_att))
        else:
            aug_path = nx.shortest_path(graph_original, edge[0], edge[1], weight='distance')
            aug_path_pairs = list(zip(aug_path[:-1], aug_path[1:]))

            # print('Filling in edges for augmented edge: {}'.format(edge))
            # print('Augmenting path: {}'.format(' => '.join(str(aug_path))))
            # print('Augmenting path pairs: {}\n'.format(aug_path_pairs))

            # If `edge` does not exist in original graph, find the shortest path between its nodes and
            #  add the edge attributes for each link in the shortest path.
            for edge_aug in aug_path_pairs:
                edge_aug_att = graph_original[edge_aug[0]][edge_aug[1]]
                euler_circuit.append((edge_aug[0], edge_aug[1], edge_aug_att))

    return euler_circuit