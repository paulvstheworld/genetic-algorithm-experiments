#!/usr/bin/env python
import argparse
import string
import sys

from ecosystem import Ecosystem, Individual, Population
from tournament import Tournament


DEFAULT_CHARSET = string.ascii_letters + string.digits

def parse_args():
    app_description = 'Using a genetic algorithm to match to a target string'
    parser = argparse.ArgumentParser(description=app_description)

    parser.add_argument('-f', '--file',
                        help='file containing target string',
                        dest='file',
                        required=False,
                        type=argparse.FileType('r'))

    parser.add_argument('-t', '--target',
                        help='final target string',
                        dest='target',
                        required=False,
                        type=str)

    parser.add_argument('-c', '--charset',
                        help='charset to use',
                        dest='charset',
                        required=False,
                        type=str)


    parser.add_argument('-p', '--population-size',
                        help='population size',
                        dest='population_size',
                        required=False,
                        type=int)

    parser.add_argument('-q', '--tournament-size',
                        help='tournament population size',
                        dest='tournament_size',
                        required=False,
                        type=int)

    parser.add_argument('-r', '--random-crossover',
                        help='use a random crossover over each gene',
                        dest='random_crossover',
                        action='store_true')

    parser.set_defaults(random_crossover=False)
    parser.set_defaults(charset=DEFAULT_CHARSET)
    parser.set_defaults(population_size=50)
    parser.set_defaults(tournament_size=15)
    return parser.parse_args()


def main():
    args= parse_args()
    file = args.file
    target_string = args.target
    charset = args.charset
    random_crossover = args.random_crossover
    tournament_size = args.tournament_size
    population_size = args.population_size

    if not file and not target_string:
        print 'ERROR: Must pass either a file containing a target string or a target string'
        sys.exit(1)

    if file:
        with open(file) as f:
            target_string = f.readline()

    for char in target_string:
        if char not in charset:
            print 'ERROR: Characters does not contain all characters in target string'
            sys.exit(1)
    

    # set ideal target
    target_individual = Individual(list(target_string))
    
    # set ecosystem
    ecosystem = Ecosystem(charset, target_individual, tournament_size)
    ecosystem.set_random_current_population(population_size)
    
    # evolve ecosystem until the fittest individual matches the target
    while ecosystem.get_current_fittest() != target_individual:
        ecosystem.print_results()
        ecosystem.evolve()
    ecosystem.print_results()

    # print success message
    ecosystem.print_success()


if __name__ == '__main__':
    main()
