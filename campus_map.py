import json

class CampusMap:
    def __init__(self, filename="campus.json"):
        with open(filename, "r") as file:
            data = json.load(file)
        self.nodes = data["nodes"]
        self.graph = {name: [] for name in self.nodes}
        for a, b, cost in data["edges"]:
            self.graph[a].append((b, cost))
            self.graph[b].append((a, cost))

    def get_neighbors(self, location):
        return self.graph[location]

    def get_cost(self, a, b):
        for node, cost in self.graph[a]:
            if node == b:
                return cost
        return None

    def get_coordinates(self, location):
        return self.nodes[location]["x"], self.nodes[location]["y"]
