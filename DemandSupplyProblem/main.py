from Graph.Digraph import Digraph
from Graph.Edge import Edge
from Graph.Vertex import Vertex
from PreFlowFIFOAlg import PreFlowFIFOAlg

if __name__ == "__main__":
    graph = Digraph()

    source: Vertex = Vertex('1')
    sink: Vertex = Vertex('5')

    v1, v2, v3 = Vertex('2'), Vertex('3'), Vertex('4')

    graph.add_vertex(source)
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_vertex(v3)
    graph.add_vertex(sink)

    ## 11
    # graph.add_edge(Edge(source, v1, 7))
    # graph.add_edge(Edge(source, v2, 5))
    # graph.add_edge(Edge(v1, v2, 2))
    # graph.add_edge(Edge(v1, v3, 2))
    # graph.add_edge(Edge(v1, sink, 2))
    # graph.add_edge(Edge(v2, v1, 1))
    # graph.add_edge(Edge(v2, sink, 8))
    # graph.add_edge(Edge(v3, sink, 5))

    ## 12
    graph.add_edge(Edge(source, v1, 8))
    graph.add_edge(Edge(source, v2, 5))
    graph.add_edge(Edge(v1, v2, 2))
    graph.add_edge(Edge(v1, v3, 3))
    graph.add_edge(Edge(v1, sink, 2))
    graph.add_edge(Edge(v2, v1, 3))
    graph.add_edge(Edge(v2, sink, 7))
    graph.add_edge(Edge(v3, sink, 4))

    alg = PreFlowFIFOAlg(graph)
    max_flow_value = alg.max_flow(source, sink)
    print(max_flow_value)

