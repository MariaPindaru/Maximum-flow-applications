import json
from typing import List

from EdmondsKarpAlg import EdmondsKarpAlg
from Graph.Digraph import Digraph
from Graph.Edge import Edge
from Graph.Vertex import Vertex


class ScheduleSolver:

    def __init__(self):
        self.graph: Digraph = Digraph()

        self.source: Vertex = Vertex('Source')
        self.sink: Vertex = Vertex('Sink')

        self.graph.add_vertex(self.source)
        self.graph.add_vertex(self.sink)

        self.teams: List[Vertex] = []
        self.projects: List[Vertex] = []

        self.team_work_limits: List[int] = []
        self.project_times: List[int] = []
        self.team_project_work_allowed: List[List[int]] = []

    def create_team_nodes(self, team_count):
        for index in range(team_count):
            team_vertex = Vertex('Team ' + str(index))
            self.teams.append(team_vertex)
            self.graph.add_vertex(team_vertex)

    def create_project_nodes(self, project_count):
        for index in range(project_count):
            project_vertex = Vertex('Project ' + str(index))
            self.projects.append(project_vertex)
            self.graph.add_vertex(project_vertex)

    def set_constraints(self, team_work_limits: List[int], project_times: List[int],
                        team_project_work_allowed: List[List[int]]):
        self.team_work_limits = team_work_limits
        self.project_times = project_times
        self.team_project_work_allowed = team_project_work_allowed

    def init_graph_edges(self):
        if all(len(constraint) == 0 for constraint in
               [self.teams, self.projects, self.project_times, self.team_project_work_allowed]):
            return False

        # source -> teams with team_work_limits
        for index, team in enumerate(self.teams):
            self.graph.add_edge(Edge(self.source, team, self.team_work_limits[index]))

        # project -> sink with project_times
        for index, project in enumerate(self.projects):
            self.graph.add_edge(Edge(project, self.sink, self.project_times[index]))

        # team -> project with inf
        for team_index, projects_for_team in enumerate(self.team_project_work_allowed):
            for project_index in projects_for_team:
                self.graph.add_edge(Edge(self.teams[team_index], self.projects[project_index], float('inf')))

        return True

    def compute_maximum_flow(self):
        if not self.init_graph_edges():
            print("Invalid input :(")
            return

        max_flow_finder = EdmondsKarpAlg(self.graph)
        return max_flow_finder.compute_max_flow(self.source, self.sink)

    def get_team_projects_time_distribution(self):
        distribution = {}
        for team in self.teams:
            distribution[team.name] = {}
            for project in self.projects:
                if team not in self.graph.edges[project]:
                    continue
                if edge := self.graph.get_edge_from_vertices(project, team):
                    distribution[team.name][project.name] = edge.residual_capacity

        return distribution

    def get_project_teams_time_distribution(self):
        distribution = {}
        for project in self.projects:
            distribution[project.name] = {}
            for team in self.teams:
                if team not in self.graph.edges[project]:
                    continue
                if edge:= self.graph.get_edge_from_vertices(project, team):
                    distribution[project.name][team.name] = edge.residual_capacity

        return distribution

    def print_solution(self):
        maximum_flow = self.compute_maximum_flow()
        print("Maximum flow: " + str(maximum_flow))

        project_teams_time_distribution = self.get_project_teams_time_distribution()
        for project_index in range(len(self.projects)):
            current_project_name = self.projects[project_index].name
            needed_time = self.project_times[project_index]
            solution = project_teams_time_distribution[current_project_name]
            completed_time = sum(solution.values())

            if needed_time != completed_time:
                print("The problem doesn't have a solution")
                print(f"Project {current_project_name} is not completed: {completed_time}/{needed_time} time units allocated")
                return

        print("The problem has solution")

        print(json.dumps(project_teams_time_distribution, indent=4))

        print('=========================================')

        team_projects_time_distribution = self.get_team_projects_time_distribution()
        print(json.dumps(team_projects_time_distribution, indent=4))
