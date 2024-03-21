import networkx as nx
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

def plot_path(lat, long, lat2, long2, origin_point, dest_point, origin_point2, dest_point2):
    """
    Plot two paths on a map with origin and destination points for each.
    :param lat: list of latitudes for the first path
    :param long: list of longitudes for the first path
    :param lat2: list of latitudes for the second path
    :param long2: list of longitudes for the second path
    :param origin_point: coordinates of the first path's origin
    :param dest_point: coordinates of the first path's destination
    :param origin_point2: coordinates of the second path's origin
    :param dest_point2: coordinates of the second path's destination
    """
    fig = go.Figure()

    # Path 1
    fig.add_trace(go.Scattermapbox(
        name="Path 1",
        mode="lines+markers",
        lon=long,
        lat=lat,
        marker={'size': 10, 'color': 'blue'},
        line=dict(width=4.5, color='blue')))

    # Path 2
    fig.add_trace(go.Scattermapbox(
        name="Path 2",
        mode="lines+markers",
        lon=long2,
        lat=lat2,
        marker={'size': 10, 'color': 'green'},
        line=dict(width=4.5, color='green')))

    # Origin and Destination Markers for both paths
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lon=[origin_point[1], dest_point[1], origin_point2[1], dest_point2[1]],
        lat=[origin_point[0], dest_point[0], origin_point2[0], dest_point2[0]],
        marker={'size': 12, 'color': ['red', 'red', 'yellow', 'yellow']},
        text=["Origin 1", "Destination 1", "Origin 2", "Destination 2"]))

    # Adjusting the map layout
    fig.update_layout(mapbox_style="open-street-map",
                      mapbox={'center': {'lat': np.mean(lat + lat2), 'lon': np.mean(long + long2)}, 'zoom': 12})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.show()



def plot_complete_graph_odd_degree(g_odd_complete, node_positions):
    """
    Plot a complete graph of odd degree
    :param g_odd_complete: complet graph of odd nodes
    :param G: original graph
    :param node_positions: x and y position of the nodes
    """
    plt.figure(figsize=(8, 6))
    pos_random = nx.random_layout(g_odd_complete)

    nx.draw_networkx_nodes(g_odd_complete, node_positions, node_size=20, node_color="red")
    nx.draw_networkx_edges(g_odd_complete, node_positions, alpha=0.1)
    plt.axis('off')
    plt.title('Complete Graph of Odd-degree Nodes')
    plt.show()


def plot_min_weight_matching_complete(g_odd_complete, g_odd_complete_min_edges, node_positions):
    """
    :param g_odd_complete: complete graph of odd nodes
    :param g_odd_complete_min_edges: graph of the edge of the min weight matching
    :param node_positions: x and y position of the nodes
    """
    plt.figure(figsize=(8, 6))

    # Plot the complete graph of odd-degree nodes
    nx.draw(g_odd_complete, pos=node_positions, node_size=20, alpha=0.05)

    # Create a new graph to overlay on g_odd_complete with just the edges from the min weight matching
    nx.draw(g_odd_complete_min_edges, pos=node_positions, node_size=20, edge_color='blue', node_color='red')

    plt.title('Min Weight Matching on Complete Graph')
    plt.show()


def plot_min_weight_matching_original(G, g_odd_complete_min_edges, node_positions):
    """
    :param G: original graph
    :param g_odd_complete_min_edges: graph of the edge of the min weight matching
    :param node_positions: x and y position of the nodes
    """
    plt.figure(figsize=(8, 6))

    # Plot the original trail map graph
    nx.draw(G, pos=node_positions, node_size=20, alpha=0.1, node_color='black')

    # Plot graph to overlay with just the edges from the min weight matching
    nx.draw(g_odd_complete_min_edges, pos=node_positions, node_size=20, alpha=1, node_color='red', edge_color='blue')

    plt.title('Min Weight Matching on Orginal Graph')
    plt.show()


def plot_visiting_edges(edge_visits):
    """
    :param edge_visits: Number of edges per number of visits
    """
    edge_visits.plot.bar(x='number of visits', y='number of edges', rot=0)
    plt.show()


def plot_visiting_nodes(node_visits):
    """
    :param node_visits: Number of nodes per number of visits
    """
    node_visits.plot.bar(x='number of visits', y='number of nodes', rot=0)
    plt.show()