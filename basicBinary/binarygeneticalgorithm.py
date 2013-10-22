from algorithm import Algorithm
from individual import Individual
from population import Population
from fitness import FitnessCalculator


class BinaryGeneticAlgorithm(object):
    def __init__(self, solution):
        generation_count = 0
        
        fitness_calc = FitnessCalculator()
        fitness_calc.set_solution(solution)

        population = Population(50, fitness_calc, initialize=True)
        
        while population.get_fittest().get_fitness() < fitness_calc.get_max_fitness():
            print "Generation: %d" % (generation_count, )
            print "Fittest Scores: %d" % (population.get_fittest().get_fitness(),)
            print "Fittest: %s\n" % (population.get_fittest().genes.bin,)
            generation_count += 1
            population = Algorithm(fitness_calc).evolvePopulation(population)
        
        msg = "===== SOLUTION FOUND! =====\nGENERATION: %d\nGENES: %s\n"
        print msg % (generation_count, population.get_fittest().genes.bin)
    
