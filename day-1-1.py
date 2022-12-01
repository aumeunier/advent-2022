
def parse():
    with open('./files/day-1-1.txt') as f:
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


if __name__ == '__main__':
    elves = parse()
    print(max(elves))
