#!/usr/bin/env python

from binarygeneticalgorithm import BinaryGeneticAlgorithm

def parse_args():
    import argparse
    import re
    acceptable_solution_length = 64
    
    parser = argparse.ArgumentParser(description='Simple Binary Genetic Algorithm.')
    parser.add_argument('-s', '--solution',
                        help='path to torrent file',
                        dest='solution',
                        required=True,
                        type=str)
    
    args = parser.parse_args()
    solution = args.solution
    
    if len(solution) != acceptable_solution_length:
        raise Exception('solution has invalid length of %d should be %d' % (
        len(solution), acceptable_solution_length))
    
    pattern = r'[^\.0-1]'
    if re.search(pattern, solution):
        raise Exception('solution contains invalid character %d' % (len(solution),))
        
    return solution
    
def main():
    solution = parse_args()
    binary_genetic_algo = BinaryGeneticAlgorithm(solution)
    
if __name__ == '__main__':
    main()