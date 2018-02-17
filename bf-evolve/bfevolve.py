from random import random, randint, shuffle, choice
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
    dist = distance(result)
    if not dist:
        print(program.str())
    return dist  # + cost*REPAIR_LOSS_RATE


def distance(str1):
    loss = 0.0
    length = len(ALPHABET)
    for ndx, letter in enumerate(TARGET):
        if ndx >= len(str1):
            loss += length / 2
        else:
            base_dist = abs(ALPHABET.index(letter) - ALPHABET.index(str1[ndx]))
            loss += min(base_dist, length-base_dist)*(len(TARGET)-ndx)/len(TARGET)
    return loss  # + abs(len(TARGET) - len(str1))*LENGTH_LOSS_RATE


def new_generation(pop):
    new_pop = []
    for _ in range(POP_SIZE):
        new_pop.append(Program(mutate(mutate2(crossover(choice(pop).raw(), choice(pop).raw())))))
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
            print('Gen:%d loss:%.1f len:%d - %s' % (i, min(scores), len(rep_pop[0].str()), evaluate(rep_pop[0].rep_str())[:75]))
    print(rep_pop[0].str())

if __name__ == "__main__":
    main()
