
def parse(day):
    with open(f'./files/day-{day}.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
