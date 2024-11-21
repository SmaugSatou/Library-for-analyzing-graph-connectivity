"""
Graphs Library
"""
from copy import deepcopy


def convert_to_adjacency_list(
        vertices: list[tuple[int, int]], is_directed: bool
) -> dict[int, list[int]]:
    """Converts a list of edges into an adjacency list for an undirected graph.

    Args:
        vertices (list[tuple[int, int]]): The list of edges.
        is_directed (bool): True if graph is directed. False if undirected.

    Returns:
        dict[int, list[int]]: The adjacency list of the graph.

    Examples:
        >>> convert_to_adjacency_list([(1, 2), (1, 3), (3, 1)], False) == \
        {1: [2, 3], \
        2: [1], \
        3: [1]}
        True
        >>> convert_to_adjacency_list([(1, 2), (1, None), (3, None)], False) == \
        {1: [2], \
        2: [1], \
        3: []}
        True
        >>> convert_to_adjacency_list([(1, None), (2, None), (3, None)], False) == \
        {1: [], \
        2: [], \
        3: []}
        True
        >>> convert_to_adjacency_list([(1, 2), (1, 3), (3, 1)], True) == \
        {1: [2, 3], \
        2: [], \
        3: [1]}
        True
        >>> convert_to_adjacency_list([(1, 2), (1, 3), (3, None)], True) == \
        {1: [2, 3], \
        2: [], \
        3: []}
        True
    """

    new_adjacency_list = {}

    for vert1, vert2 in vertices:
        new_adjacency_list.setdefault(vert1, [])

        if vert2:
            if vert2 not in new_adjacency_list[vert1]:
                new_adjacency_list[vert1].append(vert2)

            new_adjacency_list.setdefault(vert2, [])
            if not is_directed and vert1 not in new_adjacency_list[vert2]:
                new_adjacency_list[vert2].append(vert1)

    return new_adjacency_list

def read_file(pathname: str, is_directed: bool) -> dict[int, list[int]]:
    """Reads a graph from a file and assigns it to the private variable.

    Args:
        pathname (str): The name of the file to read.

    Returns:
        dict[int, list[int]]: The adjacency list of the graph.
        is_directed (bool): True if graph is directed. False if undirected.
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

def search_bridges(adjacency_list: dict[int, list[int]]) -> list[tuple[int, int]]:
    """Searches for bridges in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.

    Returns:
        list[tuple[int, int]]: The edges of the graph that are bridges.

    >>> search_bridges({0: [1], 1: [0,2,4], 2: [1,3], 3: [2,5], \
    4: [1,6,7], 5: [3,6], 6: [4,5], 7: [4], 8:[9], 9:[8,10,11], 10:[9], 11:[9]})
    [(0, 1), (4, 7), (8, 9), (9, 10), (9, 11)]
    >>> search_bridges({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    []
    >>> search_bridges({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
    [(3, 4)]
    """
    bridges = []

    connectivity = search_component_connectivity(adjacency_list)

    for node in adjacency_list:
        for vert in adjacency_list[node]:
            adjacency_list__to_check_bridge = deepcopy(adjacency_list)

            adjacency_list__to_check_bridge[node].remove(vert)
            adjacency_list__to_check_bridge[vert].remove(node)

            new_connectivity = search_component_connectivity(adjacency_list__to_check_bridge)

            if new_connectivity != connectivity:
                is_in = False
                bridge = (node, vert)
                set_bridge = set(bridge)

                for el in bridges:
                    if set_bridge == set(el):
                        is_in = True

                if not is_in:
                    bridges.append(bridge)

    return bridges

def __dfs(
        adjacency_list: dict[int, list[int]], node: int, visited: set | None = None
) -> set:
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

def search_component_connectivity(
        adjacency_list: dict[int, list[int]] | None = None
) -> list[int]:
    """Searches for connected components in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.

    Returns:
        list[int]: The smallest vertices of each connected component.

    >>> search_component_connectivity({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]})
    [0, 3]
    >>> search_component_connectivity({0: [1], 1: [0,2,4], 2: [1,3], 3: [2,5],\
 4: [1,6,7], 5: [3,6], 6: [4,5], 7: [4], 8:[9], 9:[8,10,11], 10:[9], 11:[9]})
    [0, 8]
    >>> search_component_connectivity({1: [2], 2: [3, 4], 3: [4, 6],\
 4: [1, 5], 5: [6], 6: [7], 7: [5]})
    'Граф є орієнтованим. Скористайтесь функцією search_component_strong_connectivity()'
    """

    def orientation_check(adjacency_list: dict[int, list[int]]) -> True:
        """
        Checks if graph is oriented.

        Args:
            adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.

        Returns:
            True if graph is oriented, False if not.

        >>> orientation_check({1: [2], 2: [3, 4], 3: [4, 6],\
    4: [1, 5], 5: [6], 6: [7], 7: [5]})
        True
        >>> orientation_check({0: [1, 2], 1: [0, 2], 2: [0,1], 3: [4], 4: [3]})
        False
        """
        for i in adjacency_list:
            for g in adjacency_list[i]:
                if not i in adjacency_list[g]:
                    return True
        return False

    if orientation_check(adjacency_list):
        return "Граф є орієнтованим. Скористайтесь функцією search_component_strong_connectivity()"

    closed = []
    component = []
    faded = []
    for i in adjacency_list:
        if i in closed:
            continue
        faded = __dfs(adjacency_list, i)
        component.append(min(faded))
        closed += list(faded)
    return component

def search_points_connectivity(adjacency_list: dict[int, list[int]]) -> set[int]:
    """Searches for articulation points (points of connectivity) in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.

    Returns:
        set[int]: The vertices that are points of connectivity.

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
        new_adjacency = {
            key: values for key, values in adjacency_list.items() if key != node
        }

        for k in new_adjacency:
            new_adjacency[k] = [i for i in new_adjacency.get(k) if i != node]

        if (
                len(__dfs(new_adjacency, list(new_adjacency.keys())[0]))
                < len(adjacency_dfs) - 1
        ):
            output.add(node)

    return output

def search_component_strong_connectivity(
        adjacency_list: dict[int, list[int]]
) -> set[int]:
    """Searches for strongly connected components in the graph.

    Args:
        adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.

    Returns:
        set[int]: The smallest vertices of each strongly connected component.

    Examples
        >>> search_component_strong_connectivity({1: [2], 2: [3, 4], 3: [4, 6], \
        4: [1, 5], 5: [6], 6: [7], 7: [5]}) == {1, 5}
        True
        >>> search_component_strong_connectivity({1: [2], 2: [3, 4], 3: [4, 6], \
        4: [1, 5], 5: [6], 6: [7], 7: [5, 1]}) == {1}
        True
        >>> search_component_strong_connectivity({1: [2, 3], 2: [], 3: [2, 4], \
        4: [3]}) == {1, 2, 3}
        True
        >>> search_component_strong_connectivity({1: [2, 3], 2: [], 3: [2, 4], \
        4: []}) == {1, 2, 3, 4}
        True
    """

    def dfs_find_path_to_vertice(
            curr_vert: int,
            adj_list: dict[int, list[int, int]],
            visited_vert: list[int],
            start_vert: int,
            dest_vert: int,
    ) -> bool:
        """Depth first search to find a path between starting vertice to destination vertice.

        Args:
            curr_vert (int): The current vertice.
            adj_list (dict[int, list[int, int]]): The adjacency list of graph.
            start_vert (int): The starting vertice.
            dest_vert (int): The destination vertice.

        Returns:
            bool: True if a path is found. False if there is no path.
        """

        if curr_vert == dest_vert:
            return True

        visited_vert[curr_vert] = True

        for next_vert in adj_list[curr_vert]:
            if not visited_vert[next_vert]:
                if dfs_find_path_to_vertice(
                        next_vert, adj_list, visited_vert, start_vert, dest_vert
                ):
                    return True

        return False

    def is_connection(
            adj_list: dict[int, list[int, int]], vert_1: int, vert_2: int
    ) -> bool:
        """Checks whether there is a path between vertice 1 to vertice 2.

        Args:
            adj_lst (dict[int, list[int, int]]): The adjacency list of the graph.
            vert_1 (int): The starting vertice.
            vert_2 (int): The destination vertice.
        Returns:
            bool: True if a path is found. False if there is no path.
        """
        visited_vertices = [False] * (len(adj_list) + 1)

        return dfs_find_path_to_vertice(
            vert_1, adj_list, visited_vertices, vert_1, vert_2
        )

    number_of_vertices = len(adjacency_list)

    strong_components_connectivity = set()

    is_part_of_component = [False] * (number_of_vertices + 1)

    for vertice_1 in range(1, number_of_vertices + 1):
        if not is_part_of_component[vertice_1]:

            curr_component = [vertice_1]

            for vertice_2 in range(vertice_1 + 1, number_of_vertices + 1):
                if (
                        not is_part_of_component[vertice_2]
                        and is_connection(adjacency_list, vertice_1, vertice_2)
                        and is_connection(adjacency_list, vertice_2, vertice_1)
                ):
                    is_part_of_component[vertice_2] = True
                    curr_component.append(vertice_2)

            strong_components_connectivity.add(min(curr_component))

    return strong_components_connectivity

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
