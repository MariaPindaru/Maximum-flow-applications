from ScheduleSolver import ScheduleSolver

if __name__ == "__main__":
    solver = ScheduleSolver()
    solver.create_team_nodes(team_count=3)
    solver.create_project_nodes(project_count=4)

    project_times = [2, 3, 4, 2]
    team_work_limits = [4, 5, 6]
    team_project_work_allowed = [[0, 1], [1, 2, 3], [0, 3]]

    solver.set_constraints(team_work_limits=team_work_limits,
                           project_times=project_times,
                           team_project_work_allowed=team_project_work_allowed)

    solver.print_solution()
