"""
Graphs Library
"""

class Graph:
    def __init__(self) -> None:
        self.__adjacency_list: dict[int, list[int]] = {}

    def __convert_to_adjacency_list(self, vertices: list[tuple[int, int]]) -> dict[int, list[int]]:
        """Converts a list of edges into an adjacency list for an undirected graph.

        Args:
            vertices (list[tuple[int, int]]): The list of edges.

        Returns:
            dict[int, list[int]]: The adjacency list of the graph.
        """
        pass

    def read_file(self, pathname: str) -> dict[int, list[int]]:
        """Reads a graph from a file and assigns it to the private variable.

        Args:
            pathname (str): The name of the file to read.

        Returns:
            dict[int, list[int]]: The adjacency list of the graph.
        """
        pass

    def write_file(self, pathname: str) -> bool:
        """Writes the graph into a file.

        Args:
            pathname (str): The name of the file to write.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        pass

    def get_adjacency_list(self) -> dict[int, list[int]]:
        """Returns the private adjacency list variable.

        Returns:
            dict[int, list[int]]: The adjacency list of the graph.
        """
        return self.__adjacency_list


class UndirectedGraph(Graph):
    def search_component_connectivity(self,
        adjacency_list: dict[int, list[int]] = None) -> list[int]:
        """Searches for connected components in the graph.

        Args:
            adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
            Defaults to the private variable if None.

        Returns:
            list[int]: The smallest vertices of each connected component.
        """
        pass

    def search_bridges(self, adjacency_list: dict[int, list[int]] = None) -> list[tuple[int, int]]:
        """Searches for bridges in the graph.

        Args:
            adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
            Defaults to the private variable if None.

        Returns:
            list[tuple[int, int]]: The edges of the graph that are bridges.
        """
        pass

    def dfs(self, adjacency_list: dict[int, list[int]],
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
                self.dfs(adjacency_list, next_el, visited)

        return visited

    def search_points_connectivity(self, adjacency_list: dict[int, list[int]] = None) -> list[int]:
        """Searches for articulation points (points of connectivity) in the graph.

        Args:
            adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
            Defaults to the private variable if None.

        Returns:
            list[int]: The vertices that are points of connectivity.

        Examples:
        >>> UndirectedGraph().search_points_connectivity({\
        5: [3, 7], \
        7: [8, 5], \
        2: [3, 6], \
        3: [2, 4, 5], \
        6: [2], \
        4: [8, 3], \
        8: [7, 4]})
        [2, 3]

        >>> UndirectedGraph().search_points_connectivity({\
    0: [1, 2],\
    1: [0, 2, 5],\
    2: [0, 1, 5],\
    3: [4, 5],\
    4: [3, 5],\
    5: [1, 2, 3, 4]})
        [5]
        """
        adjacency_dfs = self.dfs(adjacency_list, list(adjacency_list.keys())[0])
        output = []

        for node in adjacency_list:
            new_adjacency = {key: values for key, values in adjacency_list.items()
                             if key != node}

            for k in new_adjacency:
                new_adjacency[k] = [i for i in new_adjacency.get(k) if i != node]

            if len(self.dfs(new_adjacency, list(new_adjacency.keys())[0])) < len(adjacency_dfs) - 1:
                output += [node]

        return output


class DirectedGraph(Graph):
    def __convert_to_adjacency_list(self, vertices: list[tuple[int, int]]) -> dict[int, list[int]]:
        """Converts a list of edges into an adjacency list for a directed graph.

        Args:
            vertices (list[tuple[int, int]]): The list of edges.

        Returns:
            dict[int, list[int]]: The adjacency list of the graph.
        """
        pass

    def search_component_strong_connectivity(self,
        adjacency_list: dict[int, list[int]] = None) -> list[int]:
        """Searches for strongly connected components in the graph.

        Args:
            adjacency_list (dict[int, list[int]], optional): The adjacency list of the graph.
            Defaults to the private variable if None.

        Returns:
            list[int]: The smallest vertices of each strongly connected component.
        """
        pass
