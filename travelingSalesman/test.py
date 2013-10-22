from city import City
from population import Population
from tour import Tour
from tour_manager import TourManager
import algorithm


def parse_args():
    import argparse
    
    parser = argparse.ArgumentParser(description='Using Genetic Algorithm to solve Traveling Salesman Problem.')
    
    parser.add_argument('-g', '--generations', 
            help='Number of generations to iterate', 
            dest='generations', 
            required=True, 
            type=int)
    
    parser.add_argument('-n', '--num-cities', 
            help='Number of cities', 
            dest='num_cities', 
            required=True, 
            type=int)
    
    parser.add_argument('-p', '--population-size', 
            help='Population size', 
            dest='population_size', 
            required=True, 
            type=int)
            
    
    
    args = parser.parse_args()
    num_cities = args.num_cities
    population_size = args.population_size
    generations = args.generations
    
    return generations, num_cities, population_size

def main():
    generations, num_cities, population_size = parse_args()
    
    tour_manager = TourManager()
    tour_manager.create_tour_cities(num_cities)
    
    population = Population(population_size, True, tour_manager)
    
    print "Initial distance = %d" % (population.get_fittest().get_distance(),)
    
    for i in range(0, generations):
        population = algorithm.evolve_population(population)
        print "generation=%d shortest_distance=%d" % (i, population.get_fittest().get_distance())
    
    fittest = population.get_fittest()
    
    print """
Finished
Final distance=%d
Solution
--------
%s
""" % (fittest.get_distance(), fittest)
    
if __name__ == '__main__':
    main()