from population import Population
from tour import Tour

mutation_rate = 0.015
tournament_size = 5
elitism = True

def evolve_population(population):
    new_population = Population(population.size(), False, population.tour_manager)
    
    elitism_offset = 0
    
    # save the fittest tour
    if elitism:
        new_population.save_tour(0, population.get_fittest())
        elitism_offset = 1
    
    # crossover
    for i in range(elitism_offset, new_population.size()):
        parent_1 = tournament_selection(population)
        parent_2 = tournament_selection(population)
        
        child = crossover(parent_1, parent_2)
        new_population.save_tour(i, child)
    
    # mutate population
    for i in range(elitism_offset, new_population.size()):
        mutate(new_population.get_tour(i))
    
    return new_population


def crossover(parent_1, parent_2):
    """ crossover subsections of parent 1 and left over cities from parent2 """
    from random import random
    
    child = Tour(parent_1.tour_manager)
    
    start_pos = (int) (random() * parent_1.size())
    end_pos = (int) (random() * parent_2.size())
    
    if start_pos > end_pos:
        temp_pos = start_pos
        start_pos = end_pos
        end_pos = temp_pos
    
    for i in range(0, child.size()):
        if i > start_pos and i < end_pos:
            child.set_city(i, parent_1.get_city(i))
    
    for i in range(0, parent_2.size()):
        if not child.contains_city(parent_2.get_city(i)):
            for j in range(0, child.size()):
                if child.get_city(j) is None:
                    child.set_city(j, parent_2.get_city(i))
                    break
    
    return child


def mutate(tour):
    """ swap mutation """
    from random import random
    
    for i in range(0, tour.size()):
        if random() < mutation_rate:
            rand_pos = (int)(tour.size() * random())
            
            city_1 = tour.get_city(i)
            city_2 = tour.get_city(rand_pos)
            
            tour.set_city(rand_pos, city_1)
            tour.set_city(i, city_2)


def tournament_selection(population):
    from random import random
    tournament = Population(tournament_size, False, population.tour_manager)
    
    for i in range(0, tournament_size):
        random_id = (int) (random() * tournament_size)
        tournament.save_tour(i, population.get_tour(random_id))
    
    fittest = tournament.get_fittest()
    return fittest