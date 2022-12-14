import ast
import os
from functools import cmp_to_key

from common import parse

DEBUG = False


def generate_map(filename, has_floor=False):
    all_rocks = parse(filename)
    # Compute size of map
    min_x, min_y = 500, 0
    max_x, max_y = 500, 0
    for rock_line in all_rocks:
        for coordinate in rock_line.split(" -> "):
            x, y = coordinate.split(",")
            x, y = int(x), int(y)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
    # Generate initial map
    max_x += 1
    max_y += 2
    min_x = min(min_x, 500-max_y)
    max_x = max(max_x, 500+max_y)
    map = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
    for rock_line in all_rocks:
        coordinates = rock_line.split(" -> ")
        previous = None
        for coordinate in coordinates:
            x, y = coordinate.split(",")
            x, y = int(x), int(y)
            if previous is None:
                previous = x, y
                map[x][y] = True
                continue
            x1, y1 = previous
            x2, y2 = x, y
            for y in range(min(y1, y2), max(y1, y2)+1):
                for x in range(min(x1, x2), max(x1, x2)+1):
                    map[x][y] = True
            previous = x2, y2
    if has_floor:
        for i in range(min_x, max_x+1):
            map[i][max_y] = True
    # Display map
    if DEBUG:
        for j in range(min_y, max_y+1):
            line = f"{j}"
            for i in range(min_x, max_x):
                line += "x" if map[i][j] else "O" if i == 500 and j == 0 else "."
            print(line)
    # Compute
    count = 0
    try:
        while True:
            i, j = 500, 0
            while not all([map[i-1][j+1], map[i][j+1], map[i+1][j+1]]):
                while(map[i][j] == False):
                    j += 1
                j -= 1
                if map[i-1][j+1] == False:
                    i -= 1
                    j += 1
                elif map[i+1][j+1] == False:
                    i += 1
                    j += 1
            count += 1
            map[i][j] = 2
            if i == 500 and j == 0:
                break
    except IndexError:
        pass
    os.system('cls')
    for j in range(min_y, max_y+1):
        line = ""
        for i in range(min_x, max_x+1):
            line += "x" if map[i][j] == True else "O" if map[i][j] == 2 else "O" if i == 500 and j == 0 else "."
        print(line)
    return count


assert(generate_map("14-test") == 24)
print(generate_map("14"))

DEBUG = True
print(generate_map("14", True))
