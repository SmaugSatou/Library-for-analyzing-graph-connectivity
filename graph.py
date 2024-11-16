"""
Graphs library
"""

class Graph:
    def __init__(self) -> None:
        self.__adjacency_list = {}

    def __convert_to_adjacency_list(self, vertices: list[tuple[int, int]]) -> dict[int]:
        pass

    def read_file(self) -> list[tuple[int, int]]:
        pass

    def write_file(self, pathname: str) -> bool:
        pass

    def get_adjacency_list(self) -> dict[int]:
        return self.__adjacency_list

class UndirectedGraph(Graph):

    def __convert_to_adjacency_list(self, vertices: list[tuple[int, int]]) -> dict[int]:
        pass

    def search_component_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass

    def search_bridges(self, adjacency_list: dict[int]) -> list[tuple[int, int]]:
        pass

    def search_points_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass

class DirectedGraph(Graph):
    def __convert_to_adjacency_list(self, vertices: list[tuple[int, int]]) -> dict[int]:
        pass

    def search_component_strong_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass
