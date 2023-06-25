import json
from typing import List

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

    def init_graph_edges(self, supply_transit, transit_transit, transit_demand):
        # source -> supply with supplies_quantities
        for index, supply in enumerate(self.supplies):
            self.graph.add_edge(Edge(self.source, supply, self.supply_quantities[index]))

        # demand -> sink with project_times
        for index, demand in enumerate(self.demands):
            self.graph.add_edge(Edge(demand, self.sink, self.demand_quantities[index]))

        # supply -> transit with inf
        for index, supply_vertex in enumerate(self.supplies):
            transit_indexes = supply_transit[index]
            for transit_index in transit_indexes:
                self.graph.add_edge(Edge(supply_vertex, self.transits[transit_index], float('inf')))

        # transit -> transit with inf
        for index, transit in enumerate(self.transits):
            transit_indexes = transit_transit[index]
            for transit_index in transit_indexes:
                self.graph.add_edge(Edge(transit, self.transits[transit_index], float('inf')))

        # transit -> demand with inf
        for index, transit in enumerate(self.transits):
            demand_indexes = transit_demand[index]
            for demand_index in demand_indexes:
                self.graph.add_edge(Edge(transit, self.demands[demand_index], float('inf')))

    def print_solution(self):
        alg = PreFlowFIFOAlg(self.graph)
        max_flow_value = alg.compute_max_flow(self.source, self.sink)
        print(f'Maximum flow: {max_flow_value}')

        for edge in self.graph.edgeList:
            if edge.dest == self.sink:
                if edge.residual_capacity != 0:
                    print('The problem does not have a solution')
                    return

        print('The problem has a solution')

        solution_demand = {}
        for demand_vertex in self.demands:
            solution_demand[demand_vertex.name] = {}
            deposits = self.graph.coming_out_of(demand_vertex)
            for x in deposits:
                if x == self.sink:
                    continue
                edge = self.graph.get_edge_from_vertices(demand_vertex, x)
                solution_demand[demand_vertex.name][x.name] = edge.residual_capacity

        print(json.dumps(solution_demand, indent=4))

        print("=====================")

        solution_supply = {}
        for supply in self.supplies:
            solution_supply[supply.name] = {}
            deposits = self.graph.coming_into(supply)
            for x in deposits:
                if x == self.source:
                    continue
                edge = self.graph.get_edge_from_vertices(x, supply)
                solution_supply[supply.name][x.name] = edge.residual_capacity

        print(json.dumps(solution_supply, indent=4))

def print_path(path: List[Vertex]):
    path_str = ""
    for x in path:
        path_str += str(x) + "->"
    path_str = path_str[0:len(path_str) - 2]
    print("\nPath: " + path_str)
