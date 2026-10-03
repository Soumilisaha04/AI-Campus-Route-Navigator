from search import greedy_best_first, a_star

class Agent:
    def __init__(self, name, search_function):
        self.name=name
        self.search_function=search_function

    def find_route(self, campus, start, destination):
        return self.search_function(campus,start,destination)

class Pathfinder(Agent):
    def __init__(self):
        super().__init__("PATHFINDER",greedy_best_first)

class Orbit(Agent):
    def __init__(self):
        super().__init__("ORBIT",a_star)
