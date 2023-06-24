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

    def get_reversed_edge(self, edge):
        for edge_r in self.edgeList:
            if edge_r.src == edge.dest and edge_r.dest == edge.src:
                return edge_r
    def update_reversed_edge(self, edge: Edge, min_flow: int):
        if reversed_edge := self.get_reversed_edge(edge):
            reversed_edge.flow += min_flow
        else:
            reversed_edge = Edge(edge.dest, edge.src, edge.capacity)
            reversed_edge.flow = min_flow
            self.edgeList.append(reversed_edge)
            self.edges[edge.dest].append(edge.src)

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
                    if self.get_edge_from_vertices(vertex, child).flow > 0:
                        path_ = list(path)
                        path_.append(child)
                        q.put(path_)

                visited.add(vertex)

    def __str__(self):
        output = "Graph edges: \n"
        for edge in self.edgeList:
            output = output + str(edge) + "\n"
        return output
