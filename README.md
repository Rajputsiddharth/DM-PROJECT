# DM Project

This repository contains code for generating undirected graphs using the Snap library, checking graph properties such as connectivity, cycles, and Hamiltonian cycles.

## Introduction
This project utilizes the Snap library to generate undirected graphs, analyze their properties, and check for Hamiltonian cycles. The code demonstrates how to create graphs, check connectivity, detect cycles, and determine the presence of Hamiltonian cycles.

## Dependencies
- Python 3.x
- Snap library

## Usage
1. Clone the repository:
     ```
     git clone https://github.com/Rajputsiddharth/DM-Project.git
     ```
2. Install the required dependencies.
3. Run the Python script `graph_analysis.py` to execute the code.

## Graph Generation
The code generates two types of graphs: a randomly generated graph and a Petersen graph.

To generate a randomly generated graph, the Snap library is used. The generated graph is saved as a tab-separated list of edges in a file named `generated_graph.txt`.

To create a Petersen graph, the code manually adds nodes and edges to the graph. The Petersen graph is also saved as a tab-separated list of edges in a file named `petersen.txt`.

## Graph Properties
The code checks the properties of the generated graph, such as connectivity and cycles.

To check if the graph is connected, the code performs a depth-first search (DFS) traversal. If all nodes are visited during the DFS, the graph is considered connected.

To check if the graph is cyclic, the code performs a modified DFS traversal. If a back edge is encountered during the traversal, the graph contains a cycle.

## Hamiltonian Cycle
The code checks if the graph has a Hamiltonian cycle, which is a cycle that visits each node exactly once.

The Hamiltonian cycle is checked for each node in the graph. If a Hamiltonian cycle is found, it is printed along with a confirmation message. Otherwise, the code indicates that the graph does not have a Hamiltonian cycle.

