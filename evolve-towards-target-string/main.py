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


    parser.add_argument('-r', '--random-crossover',
                        help='use a random crossover over each gene',
                        dest='random_crossover',
                        action='store_true')

    parser.set_defaults(random_crossover=False)
    parser.set_defaults(charset=DEFAULT_CHARSET)


    args = parser.parse_args()
    return args.file, args.target, args.charset, args.random_crossover


def main():
    file, target_string, charset, random_crossover = parse_args()

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
    ecosystem = Ecosystem(charset, target_individual)
    ecosystem.set_random_current_population(50)
    
    # evolve ecosystem until the fittest individual matches the target
    while ecosystem.get_current_fittest() != target_individual:
        ecosystem.evolve(random_crossover)
        print "Generation = {0}".format(ecosystem.generation)
        print "Fittest gene = {0}".format(''.join(ecosystem.get_current_fittest().genes))

    # print success message
    generation_string = "GENERATION" if ecosystem.generation == 1 else "GENERATIONS"
    print "\nTARGET REACHED AFTER {0} {1}!!!\n".format(ecosystem.generation, generation_string)


if __name__ == '__main__':
    main()
