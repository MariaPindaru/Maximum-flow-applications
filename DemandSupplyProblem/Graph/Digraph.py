import abc
import queue

from Graph.Edge import Edge
from Graph.Vertex import Vertex


class Graph(metaclass=abc.ABCMeta):
    def __init__(self):
        self.vertices = []
        self.edges = {}  # adj list
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
        self.level = {}  # vertex : level

    def add_vertex(self, vertex: Vertex):
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
            reversed_edge.residual_capacity += min_flow
        else:
            reversed_edge = Edge(edge.dest, edge.src, edge.capacity)
            reversed_edge.residual_capacity = min_flow
            self.edgeList.append(reversed_edge)
            self.edges[edge.dest].append(edge.src)

    def get_edge_from_vertices(self, start: Vertex, end: Vertex) -> Edge:
        for edge in self.edgeList:
            if edge.src == start and edge.dest == end:
                return edge

    def coming_out_of(self, vertex):
        return self.edges[vertex]

    def coming_into(self, vertex):
        list_of_nodes = []
        for edge in self.edgeList:
            if edge.dest == vertex and edge.dest not in list_of_nodes:
                list_of_nodes.append(edge.src)

        return list_of_nodes

    def has_vertex(self, vertex):
        return vertex in self.vertices

    def clear_visits_bfs(self):
        [vert.clear_visit() for vert in self.vertices]

    def get_vertices_names(self) -> list:
        return [ver.name for ver in self.vertices]

    def get_edges(self, vertex):
        adm_edges = []
        for out_vertex in self.edges[vertex]:
            edge = self.get_edge_from_vertices(vertex, out_vertex)

            if edge.residual_capacity > 0:
                adm_edges.append(edge)

        return adm_edges

    def get_adm_edges(self, vertex):
        adm_edges = []
        for out_vertex in self.edges[vertex]:
            edge = self.get_edge_from_vertices(vertex, out_vertex)

            if edge.residual_capacity > 0 and self.level[out_vertex] == self.level[vertex] - 1:
                adm_edges.append(edge)

        return adm_edges

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
                    if self.get_edge_from_vertices(vertex, child).residual_capacity > 0:
                        path_ = list(path)
                        path_.append(child)
                        q.put(path_)

                visited.add(vertex)

    def compute_exact_distances(self, start: Vertex, end: Vertex):
        self.level = dict.fromkeys(self.vertices, -1)
        self.level[start] = len(self.vertices)

        for vertex in self.vertices:
            if vertex == start:
                continue
            self.level[vertex] = len(self.get_shortest_path(vertex, end)) - 1

        return self.level[end] >= 0

    def __str__(self):
        output = "Graph edges: \n"
        for edge in self.edgeList:
            output = output + str(edge) + "\n"
        return output
