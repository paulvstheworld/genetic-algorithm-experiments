from algorithm import Algorithm
from individual import Individual
from population import Population
import fitness


class BinaryGeneticAlgorithm(object):
    def __init__(self, sol):
        generation_count = 0
        fitness.set_solution(sol)
        population = Population(50, initialize=True)
        
        while population.get_fittest().get_fitness() < fitness.get_max_fitness():
            print "Generation: %d" % (generation_count, )
            print "Fittest Scores: %d" % (population.get_fittest().get_fitness(),)
            print "Fittest: %s\n" % (population.get_fittest().genes.bin,)
            generation_count += 1
            population = Algorithm().evolvePopulation(population)
        
        msg = "===== SOLUTION FOUND! =====\nGENERATION: %d\nGENES: %s\n"
        print msg % (generation_count, population.get_fittest().genes.bin)
    
