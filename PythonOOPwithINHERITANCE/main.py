
from car import Car
from truck import Truck
from bike import Bike

def main():
    car = Car(vehicle_id="Car001", distance_traveled=150, cost_per_km=0.5)
    truck = Truck(vehicle_id="Truck001", distance_traveled=300, cost_per_km=1.0)
    bike = Bike(vehicle_id="Bike001", distance_traveled=50, cost_per_km=0.2)

    vehicles = [car, truck, bike]

    for vehicle in vehicles:
        distance = vehicle.get_distance()
        cost = vehicle.calculate_cost(distance)
        print(f"Vehicle ID: {vehicle.vehicle_id}, Distance Traveled: {distance} km, Cost: ${cost:.2f}")

if __name__ == "__main__":
    main()
