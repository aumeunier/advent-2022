from common import parse


def load_map(is_test=False):
    input = parse(f"8{'-test' if is_test else ''}")
    return [[c for c in line] for line in input]


def is_visible(line_index, column_index, map):
    height = int(map[line_index][column_index])
    line = map[line_index]
    column = [map[i][column_index] for i in range(0, len(map))]
    if line_index == 0 or column_index == 0 or line_index == len(line) - 1 or column_index == len(column) - 1:
        return True
    left = max(int(h) for index, h in enumerate(line) if index < column_index)
    right = max(int(h) for index, h in enumerate(line) if index > column_index)
    up = max(int(h) for index, h in enumerate(column) if index < line_index)
    bottom = max(int(h)
                 for index, h in enumerate(column) if index > line_index)
    return any(h < height for h in [left, right, up, bottom])


def scenic_score(line_index, column_index, map):
    height = int(map[line_index][column_index])
    line = map[line_index]
    column = [map[i][column_index] for i in range(0, len(map))]
    if line_index == 0 or column_index == 0 or line_index == len(line) - 1 or column_index == len(column) - 1:
        return 0
    # left side
    score_left = 0
    for i in line[0:column_index][::-1]:
        score_left += 1
        if int(i) >= height:
            break
    # Right side
    score_right = 0
    for i in line[column_index+1:len(line)]:
        score_right += 1
        if int(i) >= height:
            break
    # top side
    score_top = 0
    for i in column[0:line_index][::-1]:
        score_top += 1
        if int(i) >= height:
            break
    # bottom side
    score_bottom = 0
    for i in column[line_index+1:len(column)]:
        score_bottom += 1
        if int(i) >= height:
            break
    return score_left*score_right*score_top*score_bottom


map = load_map(True)
result_1 = sum(is_visible(i, j, map)
               for j in range(len(map[0])) for i in range(len(map)))
print(f"part 1 (test map): {result_1}")
assert(result_1 == 21)
test_1 = scenic_score(3, 2, map, True)
assert(test_1 == 8)
error_1 = scenic_score(2, 0, map)
assert(error_1 == 0)
best_scenic = max(scenic_score(i, j, map)
                  for j in range(len(map[0])) for i in range(len(map)))
print(f"part 2 (test map): {best_scenic}")
assert(best_scenic == 8)

map = load_map()
result_1 = sum(is_visible(i, j, map)
               for j in range(len(map[0])) for i in range(len(map)))
print(f"part 1: {result_1}")
best_scenic = max(scenic_score(i, j, map)
                  for j in range(len(map[0])) for i in range(len(map)))
print(f"part 2: {best_scenic}")
for i in range(len(map)):
    for j in range(len(map[i])):
        s = scenic_score(i, j, map)
        if s > 200000:
            print(f"{i}, {j} => {s}")
