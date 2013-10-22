from individual import Individual
from population import Population
from random import random


class Algorithm(object):
    def __init__(self):
        self.uniform_rate = 0.5
        self.mutation_rate = 0.015
        self.tournament_size = 5
        self.elitism = True
    
    def evolvePopulation(self, population):
        population_size = len(population.individuals)
        new_population = Population(population_size, initialize=False)
        
        if self.elitism:
            new_population.individuals.append(population.get_fittest())
        
        elitism_offset = 0
        if self.elitism:
            elitism_offset = 1
        
        for i in range(elitism_offset, population_size):
            individual_1 = self.tournament_selection(population)
            individual_2 = self.tournament_selection(population)
            new_individual = self.crossover(individual_1, individual_2)
            new_population.individuals.append(new_individual)
        
        for i in range(elitism_offset, len(new_population.individuals)):
            self.mutate(new_population.individuals[i])
            
        return new_population


    def tournament_selection(self, population):
        population_size = len(population.individuals)
        tournament = Population(self.tournament_size, False)
        
        for i in range(0, self.tournament_size):
            randomId = int(random() * population_size)
            tournament.individuals.append(population.individuals[randomId])
        
        return tournament.get_fittest()


    def crossover(self, individual_1, individual_2):
        crossover_individual = Individual()
        
        for i in range(0, len(crossover_individual.genes)):
            # crossover
            if random() <= self.uniform_rate:
                crossover_individual.genes[i] = individual_1.genes[i]
            else:
                crossover_individual.genes[i] = individual_2.genes[i]
        
        return crossover_individual


    def mutate(self, individual):
        for i in range(0, len(individual.genes)):
            if random() <= self.mutation_rate:
                gene = int(round(random()))
                individual.genes[i] = gene