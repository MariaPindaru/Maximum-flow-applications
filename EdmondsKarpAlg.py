from Graph.Digraph import Digraph


class EdmondsKarpAlg:
    def __init__(self, graph: Digraph):
        self.graph = graph

    def compute_max_flow(self, src, dest):
        flow = 0
        src.clear_visit()
        dest.clear_visit()
        path = self.graph.get_shortest_path(src, dest)

        while path is not None:

            _s = ""
            for x in path:
                _s += str(x) + "->"
            _s = _s[0:len(_s) - 2]
            print("\nprinting path: " + _s)

            edges_in_path = []
            for vert_idx in range(0, len(path) - 1):
                edge = self.graph.get_edge_from_vertices(path[vert_idx], path[vert_idx + 1])
                edges_in_path.append(edge)

            min_flow = min([edge.flow_available for edge in edges_in_path])
            for edge in edges_in_path:
                self.graph.lower_flow_given_edge(edge, min_flow)

                if self.graph.has_reversed_edge(edge.src, edge.dest, min_flow):
                    pass
                else:
                    self.graph.create_reversed_edge(edge.dest, edge.src, min_flow)

            flow += min_flow
            print("actual minimum flow of edges: " + str(min_flow))
            print("actual maximum flow of graph: " + str(flow))
            path = self.graph.get_shortest_path(src, dest)
            print(self.graph)

        return flow