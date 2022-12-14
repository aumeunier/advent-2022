import os

from common import parse


def load_map(is_test=False):
    input = parse(f"12{'-test' if is_test else ''}")
    return [[c for c in line] for line in input]


def heuristic_distance(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def heuristic_letter(letter):
    return ord("z") - ord(letter)


class State():
    def __init__(self, letter, pos, path, end):
        self.letter = letter
        self.pos = pos
        self.path = path
        self.length = len(path)
        self.dist = heuristic_distance(pos, end)
        # self.dist = heuristic_distance(pos, end) + heuristic_letter(letter)
        self.end = end

    def go_to(self, letter, pos):
        return State(letter, pos, self.path + [self.pos], self.end)


debug = False


def show_map(map, visited, start, end, x):
    os.system('cls')
    for i in range(len(map)):
        line = ""
        for j in range(len(map[i])):
            if ((i, j) == start):
                line += "S"
            elif ((i, j) == end):
                line += "E"
            elif ((i, j) == x):
                line += "x"
            elif visited[i][j]:
                line += map[i][j]
            else:
                line += "."
        print(line)


def find_path(map, reverse=False):
    # Initialize
    visited = []
    start, end = None, None
    for i in range(len(map)):
        visited.append([False for _ in range(len(map[i]))])
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                start = (i, j)
            elif map[i][j] == 'E':
                end = (i, j)
    if reverse:
        stack = [State("E", end, [], start)]
    else:
        stack = [State("S", start, [], end)]
    while stack:
        state = stack.pop(0)
        pos = state.pos
        if debug:
            show_map(map, visited, start, end, pos)
        letter = map[pos[0]][pos[1]]
        if pos == end:
            return state
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if next_pos[0] < 0 or next_pos[0] >= len(map) or next_pos[1] < 0 or next_pos[1] >= len(map[0]) or visited[next_pos[0]][next_pos[1]]:
                continue
            next_letter = map[next_pos[0]][next_pos[1]]
            if reverse:
                if next_letter == "S":
                    if letter == "z":
                        return state.go_to("S", next_pos)
                else:
                    inserted = False
                    next_state = state.go_to(next_letter, next_pos)
                    visited[next_pos[0]][next_pos[1]] = True
                    for i in range(len(stack)):
                        s = stack[i]
                        if s.length > state.length:
                            stack.insert(i, next_state)
                            inserted = True
                            break
                    if not inserted:
                        stack.append(next_state)
            else:
                if next_letter == "E":
                    if letter == "z":
                        return state.go_to("E", next_pos)
                elif letter == "S" or ((ord(next_letter) - ord(letter)) <= 1):
                    inserted = False
                    next_state = state.go_to(next_letter, next_pos)
                    visited[next_pos[0]][next_pos[1]] = True
                    for i in range(len(stack)):
                        s = stack[i]
                        if s.length > state.length:
                            stack.insert(i, next_state)
                            inserted = True
                            break
                    if not inserted:
                        stack.append(next_state)


final_path = find_path(load_map(True))
assert(len(final_path.path) == 31)

final_path = find_path(load_map(False))
print(f"Part 1 - Final path length={len(final_path.path)}")
