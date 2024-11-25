"""
Demonstration program
"""

import argparse

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
        "search-component-strong-connectivity"
    ], help="Functions to perform")

    parser.add_argument("graph_file", type=str, help="Path to the CSV file containing the vertices")
    parser.add_argument("--directed", action="store_true", help="Define if the graph is directed")
    parser.add_argument("--output", type=str,
                        help="Path to save the graph adjacency list as a file", default=None)

    args = parser.parse_args()

    try:
        adjacency_list = g.read_file(args.graph_file, args.directed)
    except (FileNotFoundError, PermissionError, IOError) as err:
        print(err)
        return

    result = ''

    if args.function == "search-bridges":
        result = g.search_bridges(adjacency_list)
    elif args.function == "search-component-connectivity":
        result = g.search_component_connectivity(adjacency_list)
    elif args.function == "search-points-connectivity":
        result = g.search_points_connectivity(adjacency_list)
    elif args.function == "search-component-strong-connectivity":
        result = g.search_component_strong_connectivity(adjacency_list)
    elif args.function == "read-file":
        result = f'The adjacency list of graph: {adjacency_list}'
    else:
        parser.error("Unknown command")

    print(f'Result: {result}')

    if args.output:
        if g.write_file(args.output, adjacency_list):
            print(f"Graph was written to {args.output}")
        else:
            print("Failed to write graph to file.")

if __name__ == "__main__":
    main()
