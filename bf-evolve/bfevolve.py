from random import random, randint, shuffle, choice
from difflib import SequenceMatcher
from bf import evaluate
from settings import *
from program import Program


def crossover(g1, g2):
    minlen = min(len(g1), len(g2))
    pivot = randint(1, minlen-2)
    genes = [g1, g2]
    shuffle(genes)
    return genes[0][:pivot] + genes[1][pivot:]


# Single base mutation
def mutate(gene):
    for ndx in range(len(gene)):
        if random() < MUTATION_RATE:
            gene[ndx] = choice(BASES)
    return gene


# Segment duplication/delete
def mutate2(gene):
    if random() < DOUBLE_RATE:
        size = randint(1, 10)
        location = randint(0, len(gene)-size)
        if random() < .5:
            # Double
            return gene[:location] + gene[slice(location, size)] + gene[location:]
        elif len(gene) > 150:  # Minimum program size
            # Delete
            return gene[:location] + gene[location+size:]
    return gene


def score(program):
    result = evaluate(program.rep_str())
    return distance(result)


def distance(input):
    la = len(input)
    lb = len(TARGET)

    similarity = 1.0 - SequenceMatcher(None, input, TARGET).ratio()
    length = 1.0 - (abs(la - lb))/max(la, lb)
    letters = 1.0 - min(la - input.count(' '), 10)/10

    return similarity + length*.2 + letters*.2


def new_generation(pop):
    new_pop = []
    for _ in range(POP_SIZE):
        # result = crossover(choice(pop).raw(), choice(pop).raw())
        result = mutate2(choice(pop).raw())
        result = mutate(result)

        new_pop.append(Program(result))
    return new_pop


def main():
    pop = [Program() for _ in range(POP_SIZE)]
    rep_pop = pop
    for i in range(GENERATIONS):
        scores = [score(program) for program in pop]
        num_reproduce = int(POP_SIZE * FIT_RATE)
        rep_pop = [x[0] for x in sorted(zip(pop, scores), key=lambda x: x[1])][:num_reproduce]
        pop = new_generation(rep_pop)

        if i % 20 == 0:
            print('Gen:%d loss:%.2f len:%d - %s' %
                  (i, min(scores), len(rep_pop[0].str()), evaluate(rep_pop[0].rep_str())[:75]))
    print(rep_pop[0].str())


if __name__ == "__main__":
    main()
