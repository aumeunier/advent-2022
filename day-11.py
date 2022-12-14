from functools import reduce

debug = False
divide_stress = 3
cycle = None


class Monkey():
    def __init__(self, items, op, test, test_true, test_false):
        self.items, self.op, self.test = items, op, test
        self.test_true, self.test_false = test_true, test_false
        self.inspections = 0

    def inspect(self, monkeys):
        while self.items:
            item = self.items.pop(0)
            self.inspections += 1
            worry = int(self.op(item) / divide_stress)
            if cycle:
                test_result = worry % cycle % self.test
                if debug:
                    print(
                        f"{item} => {worry} % {cycle} = {worry % cycle} => {test_result} -> {self.test_true if test_result else self.test_false}")
                worry = worry % cycle
            if worry % self.test == 0:
                monkeys[self.test_true].items.append(worry)
            else:
                monkeys[self.test_false].items.append(worry)


def process(monkeys, nb_iterations):
    for i in range(nb_iterations):
        for monkey in monkeys:
            monkey.inspect(monkeys)
            if debug:
                print(f"m{i}: {monkey.items}")
        if debug and ((i+1) % (nb_iterations / 100) == 0):
            print(f"Iteration {i+1}: {[m.inspections for m in monkeys]})")
        for i in range(len(monkeys)):
            monkey = monkeys[i]
    inspections = [m.inspections for m in monkeys]
    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]


nb_iterations = 20
monkeys_sample = [
    Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
    Monkey([74], lambda x: x + 3, 17, 0, 1),
]
total_test = process(monkeys_sample, nb_iterations)
assert(total_test == 10605)

monkeys = [
    Monkey([72, 97], lambda x: x * 13, 19, 5, 6),
    Monkey([55, 70, 90, 74, 95], lambda x: x*x, 7, 5, 0),
    Monkey([74, 97, 66, 57], lambda x: x+6, 17, 1, 0),
    Monkey([86, 54, 53], lambda x: x+2, 13, 1, 2),
    Monkey([50, 65, 78, 50, 62, 99], lambda x: x+3, 11, 3, 7),
    Monkey([90], lambda x: x+4, 2, 4, 6),
    Monkey([88, 92, 63, 94, 96, 82, 53, 53], lambda x: x+8, 5, 4, 7),
    Monkey([70, 60, 71, 69, 77, 70, 98], lambda x: x*7, 3, 2, 3),
]
total = process(monkeys, nb_iterations)
print(f"Result for part1: {total}")

monkeys_sample = [
    Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
    Monkey([74], lambda x: x + 3, 17, 0, 1),
]
cycle = reduce(lambda x, y: x*y, [m.test for m in monkeys_sample])
assert(cycle == 96577)
divide_stress = 1
nb_iterations = 10000
print(f"Starting part2 with cycle {cycle}")
total_test = process(monkeys_sample, nb_iterations)
assert(total_test == 2713310158)

monkeys = [
    Monkey([72, 97], lambda x: x * 13, 19, 5, 6),
    Monkey([55, 70, 90, 74, 95], lambda x: x*x, 7, 5, 0),
    Monkey([74, 97, 66, 57], lambda x: x+6, 17, 1, 0),
    Monkey([86, 54, 53], lambda x: x+2, 13, 1, 2),
    Monkey([50, 65, 78, 50, 62, 99], lambda x: x+3, 11, 3, 7),
    Monkey([90], lambda x: x+4, 2, 4, 6),
    Monkey([88, 92, 63, 94, 96, 82, 53, 53], lambda x: x+8, 5, 4, 7),
    Monkey([70, 60, 71, 69, 77, 70, 98], lambda x: x*7, 3, 2, 3),
]
cycle = reduce(lambda x, y: x*y, [m.test for m in monkeys])
total = process(monkeys, nb_iterations)
print(f"Result for part2: {total}")
