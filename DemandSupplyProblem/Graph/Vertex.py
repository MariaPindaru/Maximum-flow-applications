class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.visited = False
        self.excess = 0

    def get_name(self):
        return self.name

    def is_visited(self):
        return self.visited

    def mark_visited(self):
        self.visited = True

    def clear_visit(self):
        self.visited = False

    def __str__(self):
        return '(' + str(self.name) + ')'