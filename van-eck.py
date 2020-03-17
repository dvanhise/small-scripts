from itertools import count


MAX_TERM = 100000


def main():
    seq = []

    for i in count(0):
        if not len(seq):
            term = 0
        else:
            last_index = find_last(seq[i-1], seq[:-1])
            if last_index is not None:
                term = i - 1 - last_index
            else:
                term = 0

        # print(term)
        seq.append(term)

        if i == MAX_TERM:
            break

    for i in range(1000):
        if i not in seq:
            print('%d not here' % i)


def find_last(term, seq):
    for i in range(len(seq)-1, -1, -1):
        if seq[i] == term:
            return i
    return None


if __name__ == "__main__":
    main()
