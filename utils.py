import osmnx as ox
import networkx as nx
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
#Map Utilities

def get_node_position(G):
    return {node[0]: (node[1]['x'], -node[1]['y']) for node in G.nodes(data=True)}
            
def euler_circuit_to_route(euler_circuit):
    route = []
    for edge in euler_circuit:
        route.append(edge[0])
    return route


def route_to_long_lat(G, route):
    long = []
    lat = []
    for i in route:
        point = G.nodes[i]
        long.append(point['x'])
        lat.append(point['y'])
    return long, lat


def long_lat_to_points(long, lat):
    origin_point = long[0], lat[0]
    dest_point = long[-1], lat[-1]
    return origin_point, dest_point

def get_first_element_from_multi_edge_graph(multi_edge_graph):
  
    for e in multi_edge_graph:
        return e[0]
