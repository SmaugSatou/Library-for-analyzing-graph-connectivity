"""
Demonstration program
"""

import argparse

import matplotlib.pyplot as plt
import networkx as nx
import random

import graph as g

def random_color() -> str:
    """ Return random color.

    Returns:
        str: random color.
    """
    return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'

def color_nodes(graph: (nx.Graph | nx.DiGraph), \
                 node_colors: list[str], nodes_to_color: (list[int] | set[int])):
    """ Colors nodes in graph.

    Args:
        graph (nx.Graph  |  nx.DiGraph): The graph.
        nodes_to_color (list[int]  |  set[int]): The nodes to be colored.
    """

    for node in nodes_to_color:
        node_index = list(graph.nodes).index(node)
        node_colors[node_index] = random_color()

def main():
    """
    Demonstration main function
    """

    parser = argparse.ArgumentParser(description="Library for analyzing graph connectivity")
    parser.add_argument("function", choices=[
        "read",
        "s-bridges",
        "s-component-conn",
        "s-points-conn",
        "s-component-strong-conn",
    ], help="Functions to perform")

    parser.add_argument("graph_file", type=str, help="Path to the CSV file containing the vertices")
    parser.add_argument("--directed", action="store_true", help="Define if the graph is directed")
    parser.add_argument("--output", type=str,
                        help="Path to save the graph adjacency list as a file", default=None)
    parser.add_argument("--show", action="store_true", help="Define if the png file will be made")

    args = parser.parse_args()

    try:
        adjacency_list = g.read_file(args.graph_file, args.directed)
    except (FileNotFoundError, PermissionError, IOError) as err:
        print(err)
        return

    result = ''

    graph = nx.DiGraph(adjacency_list) if args.directed else nx.Graph(adjacency_list)

    node_colors = ['#d1d1d1'] * len(graph.nodes)
    edges_colors = ['#400080'] * len(graph.edges)
    hint_graph = ''

    match(args.function):
        case "s-bridges":
            result = g.search_bridges(adjacency_list)

            if isinstance(result, list):
                hint_graph = '(Bridges are colored red)'

                for bridge in result:
                    edge_index = list(graph.edges).index(bridge)
                    edges_colors[edge_index] = '#ff0000'

        case"s-component-conn":
            result = g.search_component_connectivity(adjacency_list)

            if isinstance(result, list):
                hint_graph = '(The smallest nodes of each component are colored different colors)'

                color_nodes(graph, node_colors, result)

        case "s-points-conn":
            result = g.search_points_connectivity(adjacency_list)

            if isinstance(result, set):
                hint_graph = '(Points of connectivity are colored different colors)'

                color_nodes(graph, node_colors, result)

        case "s-component-strong-conn":
            result = g.search_component_strong_connectivity(adjacency_list)

            if isinstance(result, set):
                hint_graph = '(The smallest nodes of each component are colored different colors)'

                color_nodes(graph, node_colors, result)

        case "read":
            result = f'The adjacency list of graph: {adjacency_list}'
        case _:
            parser.error("Unknown command")

    graph_options = {
        'node_color': node_colors,
        'edge_color': edges_colors,
        'with_labels': True,
        'font_weight': 'bold',
        'node_size': 500,
        'width': 5
    }

    print(f'Result: {result}')

    if args.show:
        nx.draw_kamada_kawai(graph, **graph_options)
        plt.savefig("graph.png")
        print(f'Graph was represented in new file "graph.png". {hint_graph}')

    if args.output:
        if g.write_file(args.output, adjacency_list):
            print(f"Graph was written to {args.output}.")
        else:
            print("Failed to write graph to file.")

if __name__ == "__main__":
    main()
