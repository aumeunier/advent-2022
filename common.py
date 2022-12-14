
def parse(day):
    with open(f'./files/day-{day}.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def parse_yield(day):
    with open(f'./files/day-{day}.txt') as f:
        for line in f.readlines():
            yield line.strip()


def parse_2by2(day):
    with open(f'./files/day-{day}.txt') as f:
        lines = []
        for line in f.readlines():
            l = line.strip()
            if l == "":
                yield lines
                lines = []
            else:
                lines.append(l)
        if lines:
            yield lines
