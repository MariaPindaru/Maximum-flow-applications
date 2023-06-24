from Graph.Vertex import Vertex


class PlainEdge:
    nodes = []

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        self.nodes.append(first_vertex)
        self.nodes.append(second_vertex)

    def get_nodes(self):
        return self.nodes


class Edge(PlainEdge):
    def __init__(self, src: Vertex, dest: Vertex, weight: int):
        super().__init__(src, dest)
        self.src = src
        self.dest = dest
        self.weight = weight
        self.flow_available = self.weight
        self.flow = self.weight

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def get_weight(self):
        return self.weight

    def get_available_flow(self):
        return self.flow_available

    def getFlow(self):
        return self.flow

    def update_flow_available(self, to_lower):
        self.flow_available -= to_lower

    def clear_actual_flow(self):
        self.flow_available = self.flow

    def __str__(self):
        if self.flow > 0:
            return '( ' + str(self.src.get_name()) + ' --> ' + \
                   str(self.dest.get_name()) + ' ) with weigh: ' \
                   + str(self.get_weight()) + ' with flow: ' + str(self.getFlow()) \
                   + ' with remaining flow: ' + str(self.get_available_flow())
        else:
            return '( ' + str(self.src.get_name()) + ' --> ' + \
                   str(self.dest.get_name())  \
                   + ' ) residual edge with remaining flow: ' + str(self.get_available_flow())
