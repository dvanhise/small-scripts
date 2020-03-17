from itertools import count, cycle, repeat, starmap, chain
import numpy as np
from operator import add


def main():
    print(build_board(int(input('side:')), count(1)))


def build_board(side, count_iter):
    board = np.empty((side, side))
    x = y = side // 2
    r = chain.from_iterable(starmap(repeat, zip(cycle([(0, -1), (1, 0), (0, 1), (-1, 0)]), map(lambda n: n//2, count(2)))))

    for c in count_iter:
        try:
            board[x][y] = c
        except IndexError:
            break
        x, y = map(add, (x, y), next(r))

    return board


if __name__ == "__main__":
    main()
