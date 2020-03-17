from settings import *
from random import choice


class Program:
    def __init__(self, data=None):
        self.val = data if data else [choice(BASES) for _ in range(INITIAL_LENGTH)]
        self._repaired = None

    def rep_str(self):
        if not self._repaired:
            self.repair()
        return ''.join(self._repaired)

    def str(self):
        return ''.join(self.val)

    def raw(self):
        return self.val

    # Unmatched ] are removed, unmatched [ are matched with ]'s added to end
    def repair(self):
        if self._repaired:
            return self._repaired

        count = 0
        cost = 0
        self._repaired = []
        for ins in self.val:
            if ins == '[':
                count += 1
            elif ins == ']':
                if not count:
                    cost += 1
                    continue
                else:
                    count -= 1
            self._repaired.append(ins)
        cost += count
        self._repaired += [']']*count
        return self._repaired   # , cost

    def score(self):
        # repair cost + distance
        return 0
