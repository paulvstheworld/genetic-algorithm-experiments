import random

def crossover_pt(individual1, individual2, uniform_rate):
    from ecosystem import Individual
    new_individual = Individual()

    point = int(uniform_rate * len(individual1.genes))
    new_individual.genes = individual1.genes[0:point]
    new_individual.genes += individual2.genes[point:]
    return new_individual


def crossover_rand(individual1, individual2, uniform_rate):
    from ecosystem import Individual
    new_individual = Individual()

    for i in range(len(individual1.genes)):
        selected_individual = individual1 if random.random() <= uniform_rate else individual2
        new_individual.genes.append(selected_individual.genes[i])
    return new_individual


def mutate(individual, charset, mutation_rate):
    for i in range(len(individual.genes)):
        if random.random() <= mutation_rate:
            individual.genes[i] = random.choice(charset)
