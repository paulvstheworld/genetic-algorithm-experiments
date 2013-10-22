from bitstring import BitArray
from random import random

class Individual(object):
    def __init__(self, fitness_calc):
        self._default_gene_length = 64
        self._fitness = 0
        self.fitness_calc = fitness_calc
        self.genes = BitArray()
        
        for i in range(0, self._default_gene_length):
            self.genes.bin += str('0')
        
    def generate_individual(self):
        self.genes = BitArray()
        
        for i in range(0, self._default_gene_length):
            gene = int(round(random()))
            self.genes.bin += str(gene)
        
    
    def get_fitness(self):
        if self._fitness == 0:
            self._fitness = self.fitness_calc.get_fitness(self)
        return self._fitness
    
    
    def __str__(self):
        return self.genes.bin