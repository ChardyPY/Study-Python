
from vehicle import Vehicle
from cost import Cost

class Bike(Vehicle, Cost):
    def __init__(self, vehicle_id, distance_traveled, cost_per_km):
        Vehicle.__init__(self, vehicle_id, distance_traveled)
        Cost.__init__(self, cost_per_km)
