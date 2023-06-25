from typing import List

from Graph.Digraph import Digraph
from Graph.Vertex import Vertex


class EdmondsKarpAlg:
    def __init__(self, graph: Digraph):
        self.graph = graph

    def compute_max_flow(self, src, dest):
        flow = 0
        src.clear_visit()
        dest.clear_visit()
        path = self.graph.get_shortest_path(src, dest)

        while path is not None:
            print_path(path)

            edges_in_path = []
            for index in range(0, len(path) - 1):
                edge = self.graph.get_edge_from_vertices(path[index], path[index + 1])
                edges_in_path.append(edge)

            min_residual_capacity = min([edge.residual_capacity for edge in edges_in_path])
            for edge in edges_in_path:
                edge.residual_capacity -= min_residual_capacity
                self.graph.update_reversed_edge(edge, min_residual_capacity)

            flow += min_residual_capacity
            print("actual minimum flow of edges: " + str(min_residual_capacity))
            print("actual maximum flow of graph: " + str(flow))
            path = self.graph.get_shortest_path(src, dest)
            print(self.graph)

        return flow

def print_path(path: List[Vertex]):
    path_str = ""
    for x in path:
        path_str += str(x) + "->"
    path_str = path_str[0:len(path_str) - 2]
    print("\nShortest path: " + path_str)
