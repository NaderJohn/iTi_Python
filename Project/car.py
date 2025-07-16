#Nader John

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = min(100, max(0, fuelRate))
        self.velocity = min(200, max(0, velocity))

    def run(self, distance, velocity):
        self.velocity = min(200, velocity)
        fuel_needed = distance * 0.1
        if fuel_needed <= self.fuelRate:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            traveled = self.fuelRate / 0.1
            self.fuelRate = 0
            self.stop(distance - traveled)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped with {remaining_distance} km remaining.")
        else:
            print("Car arrived at destination.")
