from individual import Individual

class Population(object):
    def __init__(self, size, initialize=False):
        self.individuals = []
        
        if initialize:
            for i in range(0, size):
                individual = Individual()
                individual.generate_individual()
                self.individuals.append(individual)
    
    
    def get_fittest(self):
        fittest = self.individuals[0]
        
        for i in range(0, len(self.individuals)):
            if fittest.get_fitness() <= self.individuals[i].get_fitness():
                fittest = self.individuals[i]
        
        return fittest