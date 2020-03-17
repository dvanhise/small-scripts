# Finding numbers with highest mulplicative persistence

from functools import reduce
from itertools import count


# Currently tested up to 233 digits
STARTING_DIGITS = 82


def main():
    for i in candidates2():
        steps = mp_steps(i)
        if steps > 9:
            print('%d: %d steps' % (i, steps))


def candidates():
    # Excludes:
    #   digits in [5,1,0]
    #   2+ of [2,3,4]
    #   decreasing consecutive digits

    # Yields lists of options 'num' long with no item in options coming before an earlier one
    def inc_digit_iter(num, options):
        if num > 1:
            for ndx, opt in enumerate(options):
                for next_opt in inc_digit_iter(num - 1, following_options(opt)):
                    yield [opt] + next_opt
        else:
            for opt in options:
                yield [opt]

    def following_options(opt):
        if opt in '2346':
            return ['6', '7', '8', '9']
        elif opt == '7':
            return ['7', '8', '9']
        elif opt == '8':
            return ['8', '9']
        elif opt == '9':
            return ['9']
        raise ValueError

    for digits in count(STARTING_DIGITS):
        print('Starting %d digits' % digits)
        for i in inc_digit_iter(digits, ['2', '3', '4', '6', '7', '8', '9']):
            yield int(''.join(i))


def candidates2():
    MAX_POWER = 600
    for i2 in range(190, MAX_POWER + 1):  # 351
        for i3 in range(MAX_POWER + 1):
            for i7 in range(MAX_POWER + 1):
                yield 2**i2 * 3**i3 * 7**i7
        print('2^%d - max %d digits' % (i2, len(str(2**i2 * 3**MAX_POWER * 7**MAX_POWER))))


def mp_steps(num):
    steps = 0
    while num >= 10:
        num = reduce((lambda x, y: int(x) * int(y)), [int(char) for char in str(num)])
        steps += 1
    return steps


if __name__ == "__main__":
    main()
