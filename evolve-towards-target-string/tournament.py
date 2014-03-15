from random import random

class Tournament(object):
    def __init__(self):
        from ecosystem import Population
        self.population = Population()

    def __len__(self):
        return len(self.population)

    def randomly_populate(self, population, size):
        population_size = len(population)
        for i in range(0, size):
            rand_index = int(random() * population_size)
            rand_individual = population.individuals[rand_index]
            self.population.add(rand_individual)

    def get_fittest(self, target_individual):
        return self.population.get_fittest(target_individual)
