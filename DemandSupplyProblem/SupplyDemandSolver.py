from Graph.Digraph import Digraph
from Graph.Edge import Edge
from Graph.Vertex import Vertex
from PreFlowFIFOAlg import PreFlowFIFOAlg


class SupplyDemandSolver:
    def __init__(self):
        self.graph: Digraph = Digraph()

        self.source: Vertex = Vertex('Source')
        self.sink: Vertex = Vertex('Sink')

        self.graph.add_vertex(self.source)
        self.graph.add_vertex(self.sink)

        self.supplies = []
        self.supply_quantities = []

        self.demands = []
        self.demand_quantities = []

        self.transits = []

    def create_supply_nodes(self, count):
        for index in range(count):
            supply_vertex = Vertex('Supply ' + str(index))
            self.supplies.append(supply_vertex)
            self.graph.add_vertex(supply_vertex)

    def create_demand_nodes(self, count):
        for index in range(count):
            demand_vertex = Vertex('Demand ' + str(index))
            self.demands.append(demand_vertex)
            self.graph.add_vertex(demand_vertex)

    def create_transit_nodes(self, count):
        for index in range(count):
            transit_vertex = Vertex('Transit ' + str(index))
            self.transits.append(transit_vertex)
            self.graph.add_vertex(transit_vertex)

    def set_constraints(self, supply_quantities, demand_quantity):
        self.supply_quantities = supply_quantities
        self.demand_quantities = demand_quantity

    def init_graph_edges(self):
        if all(len(constraint) == 0 for constraint in
               [self.supply_quantities, self.demand_quantities, self.supplies, self.demands, self.transits]):
            return False

        # source -> supply with supplies_quantities
        for index, supply in enumerate(self.supplies):
            self.graph.add_edge(Edge(self.source, supply, self.supply_quantities[index]))

        # demand -> sink with project_times
        for index, demand in enumerate(self.demands):
            self.graph.add_edge(Edge(demand, self.sink, self.demand_quantities[index]))

        # supply -> transit with inf
        for supply_vertex in self.supplies:
            for transit_vertex in self.transits:
                self.graph.add_edge(Edge(supply_vertex, transit_vertex, float('inf')))

        # transit -> demand with inf
        for transit_vertex in self.transits:
            for demand_vertex in self.demands:
                self.graph.add_edge(Edge(transit_vertex, demand_vertex, float('inf')))

        return True

    def print_solution(self):
        self.init_graph_edges()

        alg = PreFlowFIFOAlg(self.graph)
        max_flow_value = alg.compute_max_flow(self.source, self.sink)
        print(f'Maximum flow: {max_flow_value}')

        for edge in self.graph.edgeList:
            if edge.dest == self.sink:
                if edge.residual_capacity != 0:
                    print('The problem does not have a solution')
                    return

        print('The problem does have a solution')
