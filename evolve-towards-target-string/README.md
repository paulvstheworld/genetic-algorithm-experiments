#USAGE

Uses a basic genetic algorithm strategy to reach evolve towards a target string


For crossover at a certain point
    
    python main.py --target=awesome

## Arguments

    usage: main.py [-h] [-f FILE] [-t TARGET] [-c CHARSET] [-p POPULATION_SIZE] [-q TOURNAMENT_SIZE] [-r]

    Using a genetic algorithm to match to a target string

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  file containing target string
      -t TARGET, --target TARGET 
                            final target string
      -c CHARSET, --charset CHARSET
                            charset to use
      -p POPULATION_SIZE, --population-size POPULATION_SIZE
                            population size
      -q TOURNAMENT_SIZE, --tournament-size TOURNAMENT_SIZE
                            tournament population size
      -r, --random-crossover
                            use a random crossover over each gene


# OUTPUT
    Generation = 1
    Fittest gene = wsWqYlJtuJs
    Generation = 2
    Fittest gene = wsWqYqhzbvH
    Generation = 3
    Fittest gene = wsWqYqhzbvH
    Generation = 4
    Fittest gene = wsWqnqhzbvH
    Generation = 5
    Fittest gene = nsWqnqhzbvH

    ...

    Generation = 175
    Fittest gene = axesomeness
    Generation = 176
    Fittest gene = axesomeness
    Generation = 177
    Fittest gene = axesomeness
    Generation = 178
    Fittest gene = axesomeness
    Generation = 179
    Fittest gene = awesomeness

    TARGET REACHED AFTER 179 GENERATIONS!!!