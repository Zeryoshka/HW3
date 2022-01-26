from typing import Dict, Set
import networkx as nx

def find_impostor(edgelist, pseudocenters):
    graph = nx.Graph()
    graph.add_edges_from(edgelist)

    pseudocenters_neighbors: Dict[int, Set[int]] = dict()
    all_neighbors = set()
    for pseudocenter in pseudocenters:
        pseudocenters_neighbors[pseudocenter] = set(graph.neighbors(pseudocenter))
        all_neighbors = all_neighbors.union(pseudocenters_neighbors[pseudocenter])

    for pseudocenter in pseudocenters:
        for pseudocenter_index in pseudocenters:
            if pseudocenter in pseudocenters_neighbors[pseudocenter_index]:
                pseudocenters_neighbors[pseudocenter_index].remove(pseudocenter)
                if len(pseudocenters_neighbors[pseudocenter_index]) == 0:
                    return pseudocenter

    for neighbor in all_neighbors:
        pseudocenters_of_this_negihbor = []

        for pseudocenter in pseudocenters:
            if neighbor in pseudocenters_neighbors[pseudocenter]:
                pseudocenters_of_this_negihbor.append(pseudocenter)
        if len(pseudocenters_of_this_negihbor) > 1:
            for pseudocenter in pseudocenters_of_this_negihbor:
                pseudocenters_neighbors[pseudocenter].remove(neighbor)
                if len(pseudocenters_neighbors[pseudocenter]) == 0:
                    return pseudocenter

    raise ValueError()
