import osmnx as ox
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import graph_algo as algo
import plot
import utils as utl


def main():
    G = ox.graph_from_point((47.5837984, -52.7126917), dist=1200, network_type='drive')
    G2 = ox.graph_from_point((47.567049, -52.718366), dist=1200, network_type='drive')
    
    G = ox.utils_graph.get_undirected(G)
    G2 = ox.utils_graph.get_undirected(G2)
    
    
    
  
    #find odd degree Nodes: odd_nodes() returns list
    #computes all nodes with odd degree in the graph object
    odd_nodes = algo.get_odd_nodes(G)
    odd_nodes2 = algo.get_odd_nodes(G2)
    
    #computing odd combos: node_combo() returns list
    #computes and return a list containing 2-pair combinations of odd nodes
    odd_combo = algo.node_combo(odd_nodes)
    odd_combo2 = algo.node_combo(odd_nodes2)
    
    #Computing shortest paths between all odd degree vertices
    # : get_shortest_paths() returns dict
    odd_pair_shortest_paths = algo.get_shortest_paths(G,odd_combo)
    odd_pair_shortest_paths2 = algo.get_shortest_paths(G2,odd_combo2)
    
    #joining odd vertex to every other vertex to make a complete graph
    # :make_complete() returns graph
    odd_complete_graph = algo.make_complete(odd_pair_shortest_paths)
    odd_complete_graph2 = algo.make_complete(odd_pair_shortest_paths2)
    
    #Matching odd vertices to their closest odd neighbour
    # min_weight_match(): returns list
    odd_min_match = algo.min_weight_matching(odd_complete_graph)
    odd_min_match2 = algo.min_weight_matching(odd_complete_graph2)
    
    #adding odd_min_matches edges to graph G
    g_aug = algo.join_aug_edges(G,odd_min_match)
    g_aug2 = algo.join_aug_edges(G2,odd_min_match2)
    
    s = g_aug.edges()
    s2 = g_aug2.edges()
    source_s = utl.get_first_element_from_multi_edge_graph(s)
    source_s2 = utl.get_first_element_from_multi_edge_graph(s2)
    euler_circuit = algo.create_eulerian_circuit(g_aug, G, source_s)
    euler_circuit2 = algo.create_eulerian_circuit(g_aug2, G2, source_s2)
    
    route = utl.euler_circuit_to_route(euler_circuit)
    route2 = utl.euler_circuit_to_route(euler_circuit2)
    
    long, lat = utl.route_to_long_lat(G, route)
    long2, lat2 = utl.route_to_long_lat(G2, route2)
    
    origin_point, dest_point = utl.long_lat_to_points(long, lat)
    origin_point2, dest_point2 = utl.long_lat_to_points(long2, lat2)
    print("Plotting the route")
    # Plot the route
    plot.plot_path(lat, long, lat2, long2, origin_point, dest_point, origin_point2, dest_point2)
    
    
    


if __name__ == '__main__':
    main()