from bitstring import BitArray


class FitnessCalculator(object):
    def __init__(self):
        self.solution = BitArray()
    
    def set_solution(self, soln):
        self.solution = BitArray(bin=soln)
    
    def get_fitness(self, individual):
        fitness = 0
        
        for i in range(0, len(individual.genes)):
            if individual.genes[i] == self.solution[i]:
                fitness += 1

        return fitness


    def get_max_fitness(self):
        return len(self.solution)