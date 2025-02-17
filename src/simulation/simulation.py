import random
from typing import List

from .city_layout import city_layout
from .vehicle import Vehicle


class Simulator:
    def __init__(self, vehicle_count: int = 10, seed: int = 42):
        self.vehicle_count = vehicle_count
        self.seed = seed
        self.city_layout = city_layout(seed=self.seed)

        self._create_vehicles()

    def _create_vehicles(self) -> None:
        streets = self.city_layout.streets
        random.seed(self.seed)
        while self.vehicle_count > 0:
            street = random.choice(streets)
            count = random.randint(1, self.vehicle_count)
            if street.create_vehicle(count):
                self.vehicle_count -= count

    def simulate(self, steps: int = 1) -> None:
        pass
