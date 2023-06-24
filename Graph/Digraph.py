import abc
import queue

from Graph.Edge import Edge
from Graph.Vertex import Vertex


class Graph(metaclass=abc.ABCMeta):
    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.edgeList = []

    @abc.abstractmethod
    def add_vertex(self, vertex: Vertex):
        pass

    @abc.abstractmethod
    def add_edge(self, edge: Edge):
        pass


class Digraph(Graph):
    def __init__(self):
        super().__init__()

    def add_vertex(self, vertex: Vertex):
        names = self.get_vertices_names()
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, edge: Edge):
        start = edge.get_source()
        end = edge.get_destination()
        if start not in self.vertices and end not in self.vertices:
            raise ValueError('one of vertices or both are not in graph')

        self.edges[start].append(end)
        self.edgeList.append(edge)

    def has_reversed_edge(self, start: Vertex, end: Vertex, min_flow: int) -> bool:
        for edge in self.edgeList:
            if edge.src == end and edge.dest == start:
                edge.flow_available += min_flow
                return True
        return False

    def create_reversed_edge(self, start: Vertex, end: Vertex, min_flow: int):
        reversed_edge = Edge(start, end, 0)
        reversed_edge.flow_available = min_flow

        self.edgeList.append(reversed_edge)
        self.edges[start].append(end)

    def get_edge_from_vertices(self, start: Vertex, end: Vertex) -> Edge:
        for edge in self.edgeList:
            if edge.src.name == start.name and edge.dest.name == end.name:
                return edge

    def coming_out_of(self, vertex):
        return self.edges[vertex]

    def has_vertex(self, vertex):
        return vertex in self.vertices

    def clear_visits_bfs(self):
        [vert.clear_visit() for vert in self.vertices]

    def get_vertices_names(self) -> list:
        return [ver.name for ver in self.vertices]

    def lower_flow_given_edge(self, edge: Edge, minFlow: int):
        for edge_idx in range(0, len(self.edgeList)):
            if self.edgeList[edge_idx].src == edge.src and self.edgeList[edge_idx].dest == edge.dest:
                self.edgeList[edge_idx].update_flow_available(minFlow)

    def get_shortest_path(self, start: Vertex, end: Vertex):
        self.clear_visits_bfs()
        start.clear_visit()
        end.clear_visit()
        visited = set()
        q = queue.Queue()
        q.put([start])

        while not q.empty():
            path = q.get()

            vertex = path[-1]
            if vertex == end:
                return path
            elif vertex not in visited:
                for child in self.coming_out_of(vertex):
                    if self.get_edge_from_vertices(vertex, child).flow_available > 0:
                        path_ = list(path)
                        path_.append(child)
                        q.put(path_)

                visited.add(vertex)

    def __str__(self):
        output = "Graph edges: \n"
        for edge in self.edgeList:
            output = output + str(edge) + "\n"
        return output
