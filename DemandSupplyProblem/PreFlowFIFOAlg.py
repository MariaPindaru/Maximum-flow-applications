import queue

from Graph.Digraph import Digraph


class PreFlowFIFOAlg:
    def __init__(self, graph: Digraph):
        self.graph = graph
        self.queue = None

    def init(self, source, sink):
        self.queue = queue.Queue()
        excess = 0
        for vertex in self.graph.edges[source]:
            edge = self.graph.get_edge_from_vertices(source, vertex)
            edge.residual_capacity = 0
            edge.dest.excess = edge.capacity
            excess += edge.capacity
            self.graph.update_reversed_edge(edge, edge.capacity)
            if vertex != sink:
                self.queue.put(vertex)

        source.excess = -excess

    def compute_max_flow(self, source, sink):
        self.graph.compute_exact_distances(source, sink)
        self.init(source, sink)

        while not self.queue.empty():
            vertex = self.queue.get()
            adm_edges = self.graph.get_adm_edges(vertex)
            while vertex.excess > 0 and len(adm_edges) > 0:
                edge = adm_edges.pop()
                # se mareste fluxul cu min(e[x],r[(x,y)]) pe arcul (x,y)
                min_flow = min(vertex.excess, edge.residual_capacity)
                edge.residual_capacity -= min_flow
                self.graph.update_reversed_edge(edge, min_flow)
                edge.src.excess -= min_flow
                edge.dest.excess += min_flow

                print(self.graph)
                # y nu e in coada si nu e s/t -> se adauga in coada
                if edge.dest not in self.queue.queue and edge.dest not in [source, sink]:
                    self.queue.put(edge.dest)

            if vertex.excess > 0:
                min_level = min(self.graph.level[e.dest] for e in self.graph.get_edges(vertex))
                self.graph.level[vertex] = min_level + 1
                self.queue.put(vertex)

        return sink.excess
