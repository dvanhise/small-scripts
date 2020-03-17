# A simulation double checking the Stardew Valley wiki about ideal strategy for the wheel spin at the fair
# tl;dr the wiki is correct

from random import random
from itertools import count
import matplotlib.pyplot as plt
import math


# Probability to win
TEST_PROBS = [.51, .55, .6, .6667, .75]

# wager as percentage of total
TEST_STRATS = [float(x)/100 for x in range(10, 76)]

COIN_START = 100
COIN_TARGET = 1000
TRIALS = 1000

for prob in TEST_PROBS:
    results = []
    brokes = []
    for strat in TEST_STRATS:
        total_spins = 0
        times_broke = 0

        for trial in range(TRIALS):
            coins = COIN_START

            for spin in count(1):
                wager = math.ceil(coins * strat)
                coins += (wager if random() <= prob else -wager)

                if coins == 0:
                    times_broke += 1
                    break
                elif coins >= COIN_TARGET:
                    total_spins += spin
                    break
        results.append(total_spins / (TRIALS - times_broke))
        brokes.append(times_broke)

    # print('For wheel probability %.2f' % prob)
    # for ndx, result in enumerate(results):
    #     print('Wager %.1f%% averaged %.2f spins, lost %d times' % (TEST_STRATS[ndx]*100, result, brokes[ndx]))

    plt.plot(TEST_STRATS, results, 'bo')
    plt.plot(TEST_STRATS, brokes, 'ro')
    plt.ylabel('Times Lost/Average Spins')
    plt.xlabel('Wager Strategy')
    plt.title('Strategies for Probability %.2f - Times Lost per Mille (red), Avg Spins (blue)' % prob)
    plt.show()
