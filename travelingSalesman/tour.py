class Tour(object):
    def __init__(self, tour_manager, tour=None):
        self.tour_manager = tour_manager
        self._tour = []
        self._fitness = 0.0
        self._distance = 0

        if tour:
            self._tour = tour
        else:
            for i in range(0, tour_manager.num_cities()):
                self._tour.append(None)


    def generate_individual(self):
        from random import shuffle
        
        for i in range(0, self.tour_manager.num_cities()):
            self.set_city(i, self.tour_manager.get_city(i))
        
        shuffle(self._tour)

    def get_city(self, i):
        return self._tour[i]

    def set_city(self, i, city):
        self._tour[i] = city
        self._fitness = 0
        self._distance = 0

    def get_fitness(self):
        if self._fitness == 0:
            self._fitness = 1/float(self.get_distance())
        return self._fitness

    def get_distance(self):
        if self._distance == 0:
            tour_distance = 0
            tour_len = len(self._tour)
            
            for i in range(0, tour_len):
                city = self._tour[i]
                dest_city = None
                
                if i+1 < tour_len:
                    dest_city = self._tour[i+1]
                else:
                    dest_city = self._tour[0]
                
                tour_distance += city.distance_to(dest_city)
            
            self._distance = tour_distance
        
        return self._distance


    def contains_city(self, city):
        return any(x is not None and x.x == city.x and x.y == city.y for x in self._tour)

    def size(self):
        return len(self._tour)

    def __str__(self):
        gene_string = []
        
        for i in range(0, len(self._tour)):
            city_string = " %s " % (self._tour[i],)
            gene_string.append(city_string)
        
        return "".join(gene_string)