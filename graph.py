"""
Graphs Library
"""

from collections import defaultdict

def convert_to_adjacency_list(vertices: list[tuple[int, int]], \
                               is_directed: bool) -> dict[int, list[int]]:
    """Converts a list of edges into an adjacency list for an undirected graph.

    Args:
        vertices (list[tuple[int, int]]): The list of edges.

    Returns:
        dict[int, list[int]]: The adjacency list of the graph.
    """

    new_adjacency_list = defaultdict(list)

    for v1, v2 in vertices:
        new_adjacency_list[v1].append(v2)
        if not is_directed:
            new_adjacency_list[v2].append(v1)

    return new_adjacency_list

def read_file(pathname: str) -> dict[int, list[int]]:
    """Reads a graph from a file and assigns it to the private variable.

    Args:
        pathname (str): The name of the file to read.

    Returns:
        dict[int, list[int]]: The adjacency list of the graph.
    """
    pass

def write_file(pathname: str, adjacency_list: dict[int, list[int]]) -> bool:
    """Writes the graph into a file.

    Args:
        pathname (str): The name of the file to write.

    Returns:
        bool: True if the operation is successful, False otherwise.
    """
    pass

def search_component_connectivity(adjacency_list: dict[int, list[int]]) -> list[int]:
    """Searches for connected components in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
        Defaults to the private variable if None.

    Returns:
        list[int]: The smallest vertices of each connected component.
    """
    pass

def search_bridges(adjacency_list: dict[int, list[int]]) -> list[tuple[int, int]]:
    """Searches for bridges in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
        Defaults to the private variable if None.

    Returns:
        list[tuple[int, int]]: The edges of the graph that are bridges.
    """
    pass

def __dfs(adjacency_list: dict[int, list[int]],
        node: int, visited: set | None = None) -> set:
    """
    Implements the DFS algorithm.

    :param adjacency_list: dict[int, list[int]], The graph we want go through.
    :param node: int, The node you are starting with.
    :param visited: set | None, Set of visited nodes.

    :return: set, All visited nodes from a whole graph.
    """
    if visited is None:
        visited = set()

    if node not in visited:
        visited.add(node)
        for next_el in adjacency_list.get(node):
            __dfs(adjacency_list, next_el, visited)

    return visited

def search_points_connectivity(adjacency_list: dict[int, list[int]]) -> set[int]:
    """Searches for articulation points (points of connectivity) in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
        Defaults to the private variable if None.

    Returns:
        list[int]: The vertices that are points of connectivity.

    Examples:
    >>> search_points_connectivity({\
    5: [3, 7], \
    7: [8, 5], \
    2: [3, 6], \
    3: [2, 4, 5], \
    6: [2], \
    4: [8, 3], \
    8: [7, 4]}) == {2, 3}
    True

    >>> search_points_connectivity({\
0: [1, 2],\
1: [0, 2, 5],\
2: [0, 1, 5],\
3: [4, 5],\
4: [3, 5],\
5: [1, 2, 3, 4]}) == {5}
    True
    """
    adjacency_dfs = __dfs(adjacency_list, list(adjacency_list.keys())[0])
    output = set()

    for node in adjacency_list:
        new_adjacency = {key: values for key, values in adjacency_list.items()
                            if key != node}

        for k in new_adjacency:
            new_adjacency[k] = [i for i in new_adjacency.get(k) if i != node]

        if len(__dfs(new_adjacency, list(new_adjacency.keys())[0])) < len(adjacency_dfs) - 1:
            output.add(node)

    return output

def search_component_strong_connectivity(adjacency_list: dict[int, list[int]]) -> list[int]:
    """Searches for strongly connected components in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
        Defaults to the private variable if None.

    Returns:
        list[int]: The smallest vertices of each strongly connected component.
    """
    pass
