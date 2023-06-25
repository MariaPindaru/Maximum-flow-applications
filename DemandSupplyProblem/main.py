from SupplyDemandSolver import SupplyDemandSolver

if __name__ == "__main__":
    solver = SupplyDemandSolver()

    # supply_points = 2
    # supply_quantities = [35, 20]
    # demand_points = 3
    # demand_quantities = [10, 25, 15]
    # transit_points = 1

    supply_points = 2
    supply_quantities = [4, 2]
    demand_points = 2
    demand_quantities = [3, 3]

    transit_points = 4
    supply_transit = [[0], [1], [2]]
    transit_transit = [[3], [], [], []]
    transit_demand = [[0], [1], [0], [1]]

    solver.create_supply_nodes(supply_points)
    solver.create_transit_nodes(transit_points)
    solver.create_demand_nodes(demand_points)

    solver.set_constraints(supply_quantities, demand_quantities)
    solver.init_graph_edges(supply_transit, transit_transit, transit_demand)
    solver.print_solution()

    # v1, v2, v3 = Vertex('2'), Vertex('3'), Vertex('4')
    #
    # graph.add_vertex(source)
    # graph.add_vertex(v1)
    # graph.add_vertex(v2)
    # graph.add_vertex(v3)
    # graph.add_vertex(sink)

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
    # graph.add_edge(Edge(source, v1, 8))
    # graph.add_edge(Edge(source, v2, 5))
    # graph.add_edge(Edge(v1, v2, 2))
    # graph.add_edge(Edge(v1, v3, 3))
    # graph.add_edge(Edge(v1, sink, 2))
    # graph.add_edge(Edge(v2, v1, 3))
    # graph.add_edge(Edge(v2, sink, 7))
    # graph.add_edge(Edge(v3, sink, 4))

    # alg = PreFlowFIFOAlg(graph)
    # max_flow_value = alg.compute_max_flow(source, sink)
    # print(max_flow_value)

