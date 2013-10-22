from city import City

class TourManager(object):
    def __init__(self):
        self._destination_cities = []
    
    def add_city(self, city):
        self._destination_cities.append(city)
    
    def get_city(self, i):
        return self._destination_cities[i]
    
    def num_cities(self):
        return len(self._destination_cities)
    
    def create_tour_cities(self, num_cities):
        for i in range(0, num_cities):
            city = City(create_random=True)
            self.add_city(city)