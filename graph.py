"""
Graphs library
"""

class UndirectedGraph:
    adjacency_list = {}

    def read_file(self) -> dict[int]:
        pass

    def write_file(self, pathname: str) -> bool:
        pass

    def search_component_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass

    def search_bridges(self, adjacency_list: dict[int]) -> list[tuple[int, int]]:
        pass

    def search_points_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass

class DirectedGraph:
    adjacency_list = {}

    def read_file(self) -> dict[int]:
        pass

    def write_file(self, pathname: str) -> bool:
        pass

    def search_component_strong_connectivity(self, adjacency_list: dict[int]) -> list[int]:
        pass
