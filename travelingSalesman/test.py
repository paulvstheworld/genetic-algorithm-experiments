from city import City
from population import Population
from tour import Tour
from tour_manager import TourManager
import algorithm


def main():
    tour_manager = TourManager()
    tour_manager.create_tour_cities(20)
    
    population = Population(50, True, tour_manager)
    
    print "Initial distance = %d" % (population.get_fittest().get_distance(),)
    
    for i in range(0, 100):
        population = algorithm.evolve_population(population)
        print "generation=%d distance=%d" % (i, population.get_fittest().get_distance())
    
    fittest = population.get_fittest()
    
    print """
Finished
Final distance=%d
Solution=%s
""" % (fittest.get_distance(), fittest)
    
if __name__ == '__main__':
    main()