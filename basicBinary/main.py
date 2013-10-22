#!/usr/bin/env python

from binarygeneticalgorithm import BinaryGeneticAlgorithm

def parse_args():
    import argparse
    import re
    
    acceptable_solution_length = 64
    
    parser = argparse.ArgumentParser(description='Simple Binary Genetic Algorithm.')
    parser.add_argument('-s', '--solution', help='path to torrent file', 
            dest='solution', required=True, type=str)
                        
    parser.add_argument('--random', help='crossover bits at random locations', dest='random',action='store_true')
    parser.add_argument('--not-random',dest='random',action='store_false')
    parser.set_defaults(random=True)
    
    args = parser.parse_args()
    solution = args.solution
    random = args.random
    
    if len(solution) != acceptable_solution_length:
        raise Exception('solution has invalid length of %d should be %d' % (
        len(solution), acceptable_solution_length))
    
    pattern = r'[^\.0-1]'
    if re.search(pattern, solution):
        raise Exception('solution contains invalid character %d' % (len(solution),))
        
    return solution, random
    
def main():
    solution, random = parse_args()
    binary_genetic_algo = BinaryGeneticAlgorithm(solution, use_random_crossover=random)
    
if __name__ == '__main__':
    main()