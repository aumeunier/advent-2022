
def parse():
    with open('./files/day-1.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    elves = []
    current_elf = 0
    for line in lines:
        if len(line) == 0:
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    return elves


def most_snacks(elves): return max(elves)
def most_snacks_3(elves): return sum(elves.sort(descending=True)[:3])


if __name__ == '__main__':
    elves = parse()
    print(most_snacks_3(elves))
