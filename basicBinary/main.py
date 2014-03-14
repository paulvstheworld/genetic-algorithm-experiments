#!/usr/bin/env python
import argparse
import os
import re

from binarygeneticalgorithm import BinaryGeneticAlgorithm


def parse_args():
    parser = argparse.ArgumentParser(description='Using a genetic algorithm to match to a target string')
    parser.add_argument('-s', '--string',
                        help='string final target',
                        dest='string',
                        required=False,
                        type=str)

    parser.add_argument('-f', '--file',
                        help='file containing target string',
                        dest='file',
                        required=False,
                        type=argparse.FileType('r'))

    args = parser.parse_args()
    return args.string, args.file

def main():
    string, file = parse_args()

    binary_genetic_algo = BinaryGeneticAlgorithm(string, use_random_crossover=False)

if __name__ == '__main__':
    main()
