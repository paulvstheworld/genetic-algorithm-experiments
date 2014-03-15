import random

from tournament import Tournament
from genetics import crossover_pt, crossover_rand, mutate

class Individual(object):
    @staticmethod
    def get_random_genes(charset, gene_size):
        return [random.choice(charset) for _ in range(gene_size)]

    def __init__(self, genes=[]):
        self._fitness = None # cached fitness scores
        self.genes = genes[:]

    def __eq__(self, other):
        return self.genes == other.genes

    def __ne__(self, other):
        return self.genes != other.genes

    def get_fitness(self, target_individual):
        if not self._fitness:
            fitness_score = 0
            for i in range(0, len(self.genes)):
                try:
                    fitness_score += abs(ord(self.genes[i])
                                     - ord(target_individual.genes[i]))
                except:
                    import ipdb
                    ipdb.set_trace()
            self._fitness = fitness_score
        return self._fitness


class Population(object):
    @staticmethod
    def get_random_individuals(size, charset, gene_size):
        individuals = []
        for _ in range(size):
            individual = Individual()
            individual.genes = Individual.get_random_genes(charset, gene_size)
            individuals.append(individual)
        return individuals

    def __init__(self):
        self.individuals = []

    def __iter__(self):
        for individual in self.individuals:
            yield individual

    def __len__(self):
        return len(self.individuals)

    def add(self, individual):
        self.individuals.append(individual)

    def get_fittest(self, target_individual):
        fittest = self.individuals[0]
        for i in range(1, len(self.individuals)):
            curr_individual = self.individuals[i]
            curr_individual_fitness = curr_individual.get_fitness(target_individual)
            fittest_fitness = fittest.get_fitness(target_individual)
            if curr_individual_fitness < fittest_fitness:
                fittest = curr_individual
        return fittest


class Ecosystem(object):
    @staticmethod
    def get_random_population(size, charset, gene_size):
        population = Population()
        population.individuals = Population.get_random_individuals(size,
            charset,
            gene_size)
        return population

    def __init__(self, charset, target_individual,
                 tournament_size, uniform_rate=0.5, mutation_rate=0.015):
        self.generation = 1
        self.current_population = None
        self.charset = charset
        self.target_individual = target_individual
        self.tournament_size = tournament_size
        self.uniform_rate = uniform_rate
        self.mutation_rate = mutation_rate

    def set_random_current_population(self, size):
        self.current_population = Population()
        self.current_population.individuals = Population.get_random_individuals(
            size, self.charset, len(self.target_individual.genes))

    def get_current_fittest():
        self.current_population.get_fittest(self.target_individual)

    def get_tournament_fittest(self):
        tournament = Tournament()
        tournament.randomly_populate(self.current_population, self.tournament_size)
        return tournament.get_fittest(self.target_individual)

    def evolve(self, random_crossover=False):
        self.current_population = self.get_evolved_population(random_crossover)
        self.generation += 1

    def get_evolved_population(self, random_crossover):
        new_population = Population()
        population_size = len(self.current_population)
        crossover_method = crossover_rand if random_crossover else crossover_pt

        curr_fittest = self.current_population.get_fittest(self.target_individual)
        new_population.add(curr_fittest)

        for i in range(1, population_size):
            individual1 = self.get_tournament_fittest()
            individual2 = self.get_tournament_fittest()

            # create a new individual
            # (child of two elite individuals from tournaments)
            new_individual = crossover_method(individual1,
                                              individual2,
                                              self.uniform_rate)

            # mutate new individual
            mutate(new_individual, self.charset, self.mutation_rate)

            # append the new mutated individual (child of elite crossovers)
            new_population.add(new_individual)

        return new_population

    def get_current_fittest(self):
        return self.current_population.get_fittest(self.target_individual)

    def print_results(self):
        print "Generation = {0}".format(self.generation)
        print "Fittest gene = {0}".format(''.join(self.get_current_fittest().genes))

    def print_success(self):
        generation_string = "GENERATION" if self.generation == 1 else "GENERATIONS"
        print "\nTARGET REACHED AFTER {0} {1}!!!\n".format(self.generation, generation_string)
