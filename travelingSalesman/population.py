from tour import Tour

class Population(object):
    def __init__(self, size, initialize, tour_manager):
        self._tours = []
        self.tour_manager = tour_manager
        
        if initialize:
            for i in range(0, size):
                tour = Tour(tour_manager)
                tour.generate_individual()
                self._tours.append(tour)
        else:
            for i in range(0, size):
                self._tours.append(None)
    
    def save_tour(self, i, tour):
        self._tours[i] = tour
    
    def get_tour(self, i):
        return self._tours[i]
    
    def get_fittest(self):
        fittest = self._tours[0]
        
        for i in range (0, len(self._tours)):
            if fittest.get_fitness() <= self.get_tour(i).get_fitness():
                fittest = self.get_tour(i)
        
        return fittest
    
    def size(self):
        return len(self._tours)