#!/usr/bin/env python
import argparse
import os
import re
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

    parser.add_argument('-s', '--string',
                        help='string final target',
                        dest='string',
                        required=False,
                        type=str)

    parser.add_argument('-c', '--charset',
                        help='charset to use',
                        dest='charset',
                        required=False,
                        type=str)

    args = parser.parse_args()
    return args.file, args.string, args.charset


def main():
    file, target_string, charset = parse_args()

    if not file and not target_string:
        print 'ERROR: Must pass either a file containing a target string or a target string'
        sys.exit(1)

    if file:
        with open(file) as f:
            target_string = f.readline()

    if not charset:
        charset = DEFAULT_CHARSET

    # set ideal target
    target_individual = Individual()
    target_individual.genes = list(target_string)

    ecosystem = Ecosystem(charset, target_individual)
    ecosystem.set_random_current_population(50)
    
    while ecosystem.get_current_fittest() != target_individual:
        ecosystem.evolve()
        print "Currently at generation {0}".format(ecosystem.generation)
        print "Fittest gene = {0}".format(''.join(ecosystem.get_current_fittest().genes))

    print "TARGET REACHED AFTER {0} GENERATIONS!!!".format(ecosystem.generation)
    print "Target = {0}".format(''.join(ecosystem.get_current_fittest().genes))

if __name__ == '__main__':
    main()

