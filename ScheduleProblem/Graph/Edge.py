from Graph.Vertex import Vertex


class PlainEdge:
    nodes = []

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        self.nodes.append(first_vertex)
        self.nodes.append(second_vertex)

    def get_nodes(self):
        return self.nodes


class Edge(PlainEdge):
    def __init__(self, src: Vertex, dest: Vertex, capacity: int):
        super().__init__(src, dest)
        self.src = src
        self.dest = dest
        self.capacity = capacity
        self.residual_capacity = self.capacity

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def get_capacity(self):
        return self.capacity

    def get_residual_capacity(self):
        return self.residual_capacity

    def __str__(self):
        return '(' + str(self.src.get_name()) + ' --> ' + str(self.dest.get_name()) + ') ' + \
               ' with flow: ' + str(self.get_residual_capacity()) + \
               ' and capacity: ' + str(self.get_capacity())
