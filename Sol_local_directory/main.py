import osmnx as ox
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import graph_algo as algo
import plot
import utils as utl


def main():
    G = ox.graph_from_point((47.5837984, -52.7126917), dist=1000, network_type='drive')
    G = ox.utils_graph.get_undirected(G)
    
  
    #find odd degree Nodes: odd_nodes() returns list
    #computes all nodes with odd degree in the graph object
    odd_nodes = algo.get_odd_nodes(G)
    
    #computing odd combos: node_combo() returns list
    #computes and return a list containing 2-pair combinations of odd nodes
    odd_combo = algo.node_combo(odd_nodes)
    
    #Computing shortest paths between all odd degree vertices
    # : get_shortest_paths() returns dict
    odd_pair_shortest_paths = algo.get_shortest_paths(G,odd_combo)
    
    #joining odd vertex to every other vertex to make a complete graph
    # :make_complete() returns graph
    odd_complete_graph = algo.make_complete(odd_pair_shortest_paths)
    
    #Matching odd vertices to their closest odd neighbour
    # min_weight_match(): returns list
    odd_min_match = algo.min_weight_matching(odd_complete_graph)
    
    #adding odd_min_matches edges to graph G
    g_aug = algo.join_aug_edges(G,odd_min_match)
    
    s = g_aug.edges()
    source_s = utl.get_first_element_from_multi_edge_graph(s)
    euler_circuit = algo.create_eulerian_circuit(g_aug, G, source_s)
    
    route = utl.euler_circuit_to_route(euler_circuit)
    
    long, lat = utl.route_to_long_lat(G, route)
    origin_point, dest_point = utl.long_lat_to_points(long, lat)
    print("Plotting the route")
    # Plot the route
    plot.plot_path(lat, long, origin_point, dest_point)
    
    
    


if __name__ == '__main__':
    main()