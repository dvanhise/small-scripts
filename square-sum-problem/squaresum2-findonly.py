# The Square-Sum Problem - Numberphile https://www.youtube.com/watch?v=G1m7goLCJDY
# Using a graph network, only finds first instance for each number of nodes

from itertools import count, combinations
import networkx
import sys
from math import sqrt

start_from = max(int(sys.argv[1]), 2) if len(sys.argv) > 1 else 2


def sum_is_square(num1, num2):
    return sqrt(num1 + num2).is_integer()


def get_hamiltonian_paths(g, path_visited=None):
    if not path_visited:
        for starting_node in sorted(g.nodes, key=lambda x: len(g.adj[x])):
            for p in get_hamiltonian_paths(graph, [starting_node]):
                yield p
    else:
        if set(path_visited) == set(g.nodes):
            yield str(path_visited)
        else:
            for adj in sorted(list(g.adj[path_visited[-1]]), key=lambda x: len(g.adj[x])):
                if adj not in path_visited:
                    for p in get_hamiltonian_paths(g, path_visited + [adj]):
                        yield p

# Build initial graph
graph = networkx.Graph()
graph.add_nodes_from(range(1, start_from))
for i, j in combinations(range(1, start_from), 2):
    if sum_is_square(i, j):
        graph.add_edge(i, j)
        
for n in count(start_from):
    # Add node and its edges to existing graph
    other_nodes = list(graph.nodes)
    graph.add_node(n)
    for node in other_nodes:
        if sum_is_square(node, n):
            graph.add_edge(node, n)
    try:
        path = next(get_hamiltonian_paths(graph))
        print('%d nodes has at least one Hamiltonian Path: %s' % (n, path))
    except StopIteration:
        print('%d nodes does not have a Hamiltonian Path' % n)

