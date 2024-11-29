"""
Demonstration program
"""

import argparse

import matplotlib.pyplot as plt
import networkx as nx

import graph as g

def main():
    """
    Demonstration main function
    """

    parser = argparse.ArgumentParser(description="Library for analyzing graph connectivity")
    parser.add_argument("function", choices=[
        "read-file",
        "search-bridges",
        "search-component-connectivity",
        "search-points-connectivity",
        "search-component-strong-connectivity",
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

    match(args.function):
        case "search-bridges":
            result = g.search_bridges(adjacency_list)
        case"search-component-connectivity":
            result = g.search_component_connectivity(adjacency_list)
        case "search-points-connectivity":
            result = g.search_points_connectivity(adjacency_list)
        case "search-component-strong-connectivity":
            result = g.search_component_strong_connectivity(adjacency_list)
        case "read-file":
            result = f'The adjacency list of graph: {adjacency_list}'
        case _:
            parser.error("Unknown command")

    graph = nx.Graph(adjacency_list)

    if args.directed:
        graph = nx.DiGraph(adjacency_list)

    graph_options = {
        'node_color': '#07c2db',
        'edge_color': '#400080',
        'with_labels': True,
        'font_weight': 'bold',
        'node_size': 350,
        'width': 4
    }

    nx.draw_kamada_kawai(graph, **graph_options)
    plt.savefig("graph.png")

    result = 'Graph was represented in new file "graph.png"'

    print(f'Result: {result}')

    if args.output:
        if g.write_file(args.output, adjacency_list):
            print(f"Graph was written to {args.output}")
        else:
            print("Failed to write graph to file.")

if __name__ == "__main__":
    main()
