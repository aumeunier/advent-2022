
def parse(day):
    with open(f'./files/day-{day}.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def parse_yield(day):
    with open(f'./files/day-{day}.txt') as f:
        for line in f.readlines():
            yield line.strip()
