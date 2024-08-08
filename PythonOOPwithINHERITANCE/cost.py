
class Cost:
    def __init__(self, cost_per_km):
        self.cost_per_km = cost_per_km

    def calculate_cost(self, distance):
        return self.cost_per_km * distance
