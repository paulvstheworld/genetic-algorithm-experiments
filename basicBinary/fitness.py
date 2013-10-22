from bitstring import BitArray

solution = BitArray()

def set_solution(sol):
    global solution
    solution = BitArray(bin=sol)


def get_fitness(individual):
    fitness = 0
    
    for i in range(0, len(individual.genes)):
        if individual.genes[i] == solution[i]:
            fitness += 1

    return fitness

def get_max_fitness():
    return len(solution)