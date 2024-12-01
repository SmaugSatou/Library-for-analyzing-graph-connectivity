# Graph Connectivity Analysis Library

This library provides tools for analyzing the connectivity of both directed and undirected graphs, including functions for finding connected components, strongly connected components, points of connectivity, and bridges. It allows reading graphs from files, saving graphs to CSV format, and visualizing graphs with highlighted critical elements for better understanding of graph structures.

## Features

1. **Graph Reading**  
   Load a graph from a CSV file where each row contains two values representing the vertices of an edge. For directed graphs, the order of vertices matters.

2. **Graph Saving**  
   Save the graph to a CSV file in a format similar to the input data.

3. **Connectivity Analysis**  
   - **Connected Components**: Identify groups of vertices that are connected in undirected graphs.  
   - **Strongly Connected Components**: Find groups of vertices in directed graphs that have bidirectional connectivity.

4. **Critical Graph Elements**  
   - **Points of Connectivity**: Vertices whose removal increases the number of connected components.  
   - **Bridges**: Edges whose removal increases the number of connected components in undirected graphs.

5. **Graph Visualization**  
   Visualize the graph using the `matplotlib` and `networkx` libraries. The visualization highlights critical elements such as bridges, points of connectivity, or components.

## Used Discrete Mathematics Principles

- **Graph Theory**: The project uses basic graph theory concepts, where graphs are sets of vertices connected by edges. It distinguishes between **directed** and **undirected** graphs, each requiring different methods for analyzing connectivity.

- **DFS (Depth-First Search)**: DFS is used to traverse the graph and search for the needed elements.

- **Bridges**: A **bridge** is an edge in a graph that, if removed, would disconnect parts of the graph, increasing the number of connected components.

- **Points of connectivity**: **Points of connectivity** are vertices whose removal increases the number of connected components.

- **Connected Components**: A **connected component** is a group of vertices in a graph where there is a path between every pair of vertices. Identifying connected components involves finding all groups of interconnected vertices.

- **Data Structures**: The graph is stored using **adjacency lists**, which efficiently represent vertices and their connections. This structure supports efficient DFS.

## Usage Examples

The `main.py` script provides a command-line interface for running the library's functions. Examples of usage are provided below:

1. **Read a graph and display adjacency list:**  
   ```bash
   python main.py read graph.csv
   ```

2. **Find bridges in the graph:**  
   ```bash
   python main.py s-bridges graph.csv --show --output result.csv
   ```  
   - `--show`: Generates a graph image highlighting the bridges.
   - `--output result.csv`: Saves the graph to the file `result.csv`.

3. **Find connected components:**  
   ```bash
   python main.py s-component-conn graph.csv --output connectivity.csv
   ```  
   Saves the list of connected components to the file `connectivity.csv`.

4. **Identify points of connectivity:**  
   ```bash
   python main.py s-points-conn graph.csv --show
   ```  
   - `--show`: Generates a graph image highlighting the points.

5. **Find strongly connected components:**  
   ```bash
   python main.py s-component-strong-conn graph.csv --directed --show
   ```
   - `--directed`: Defines the graph as directed. 
   - `--show`: Generates a graph image highlighting the smallest points of each component.
 
## Contributions

Each team member is responsible for implementing specific functionality.

### read_file (Zakhar Veresniuk)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### write_file (Zakhar Veresniuk)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### search_bridges (Yarema Mykhasiak)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### orientation_check (Anton Deputat)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### search_component_connectivity (Anton Deputat)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### __dfs (Vladyslav Danylyshyn)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### search_points_connectivity (Vladyslav Danylyshyn)
- **Description:**  
  Explain the purpose of your function.

- **Input:**  
  Describe the expected input format, such as the structure of the data (e.g., a graph represented as an adjacency list, a CSV file, etc.) and any specific requirements (e.g., directed or undirected graph).

- **Output:**  
  Explain the output, including the format of the result (e.g., a list of bridges, a dictionary of connected components, etc.).

- **Algorithm:**  
  Explain how the function works, step by step.

### convert_to_adjacency_list (Roman Prokhorov)
- **Description:**  
  The function converts a list of edges (gained from a file) into an adjacency list for a graph.

- **Input:**  
  - `vertices` (list[tuple[int, int]]): A list of edges where each edge is represented by a tuple of two vertices (e.g., `(1, 2)`).
  - `is_directed` (bool): A boolean flag that determines whether the graph is directed (`True`) or undirected (`False`).

- **Output:**  
  - A dictionary (`dict[int, list[int]]`) where each key represents a vertex and its corresponding value is a list of vertices that are connected to it by an edge.

- **Algorithm:**  
  The function iterates over each edge in the list and adds the vertices to a dictionary. It ensures that the dictionary contains each vertex as a key with its associated list of neighboring vertices as the value. If the graph is undirected, it adds the reverse edge.

### search_component_strong_connectivity (Roman Prokhorov)
- **Description:**  
    The function determines all components of strong connectivity in a graph. It identifies vertices that form strongly connected components, where there is a path between any pair of vertices within the same component.

- **Input:**  
   - `adjacency_list` (dict[int, list[int]]): A dictionary representing the adjacency list of the graph where each key represents a vertex and its corresponding value is a list of vertices that are connected to it by an edge.

- **Output:**  
   - `set[int]`: A set containing the smallest vertices of each strongly connected component.

- **Algorithm:**  
  The function uses depth-first search (DFS) to find paths between vertices. It iterates over all vertices and checks if there is mutual path between any two vertices. If both vertices are mutually reachable, they belong to the same strongly connected component. The function then adds the smallest vertex from each SCC to a set of strongly connected components.

  1. **DFS Helper Functions:**
     - `dfs_find_path_to_vertice`: A recursive function that performs DFS to find if there is a path from one vertex to another.
     - `is_connection`: This function uses DFS to check if there is a path between two vertices in both directions.
  
  2. **Main Function Logic:**
     - It iterates over all vertices, and for each unvisited vertex, which is not a part of any component, it determines the component of strongly connected vertices it belongs to.
     - The smallest vertex from each SCC is added to the result set

## Installing

To install and use this library, follow these steps:

1. **Clone the Repository**:  
   Clone the repository to your local machine using Git:  
   ```bash
   git clone https://github.com/SmaugSatou/Library-for-analyzing-graph-connectivity.git
   ```

2. **Verify Installation**:  
   Run a basic command to ensure the setup is working correctly:  
   ```bash
   python main.py read test.csv
   ```

## Requirements

To run this library, the following dependencies must be installed:  
- Python 3.8+  
- Libraries: `argparse`, `matplotlib`, `networkx`  

Install dependencies with:  
```bash
pip install matplotlib networkx
```

The script is flexible and customizable through command-line options, making it suitable for various graph analysis tasks.