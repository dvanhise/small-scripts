# The Square-Sum Problem - Numberphile https://www.youtube.com/watch?v=G1m7goLCJDY
# Using brute force

from itertools import permutations, zip_longest
from math import sqrt
import sys

n = int(sys.argv[1])

for perm in permutations(range(1, n)):
    if all(sqrt(i+j).is_integer() for i, j in zip_longest(perm[:-1], perm[1:])):
        print(perm)
