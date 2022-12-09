from common import parse


class Pos():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): return f"({self.x}, {self.y})"

    def next(self, direction):
        match(direction):
            case "U":
                return Pos(self.x, self.y + 1)
            case "D":
                return Pos(self.x, self.y - 1)
            case "R":
                return Pos(self.x + 1, self.y)
            case "L":
                return Pos(self.x - 1, self.y)

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) - 1

    def touches(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y)) <= 1


def next_position(head: Pos, tails, direction: str, debug=False):
    new_head = head.next(direction)
    new_tails = [t for t in tails]
    in_front = new_head
    if debug:
        print(f"Head: {new_head} -- {direction}")
    last_move = direction
    for i in range(len(tails)):
        tail = tails[i]
        new_tail = tail
        if new_tail.touches(in_front):
            if debug:
                print(f"Tail {i+1} doesn't move")
            in_front = new_tail
            continue
        d = new_tail.distance(in_front)
        match(d):
            case 1:
                if new_tail.x < in_front.x:
                    last_move = "R"
                elif new_tail.x > in_front.x:
                    last_move = "L"
                elif new_tail.y < in_front.y:
                    last_move = "U"
                elif new_tail.y > in_front.y:
                    last_move = "D"
                new_tail = new_tail.next(last_move)
                if debug:
                    print(
                        f"Tail {i+1} {new_tail} dist to {in_front} = {d} => {last_move}")
            case _ if d > 3:
                print("fuck")
                raise ValueError()
            case _ if d > 1:
                new_tail = new_tail.next(last_move)
                if debug:
                    print(
                        f"Tail {i+1} {new_tail} dist to {in_front} = {d} => {last_move}")
                if last_move in ["R", "L"]:
                    if tail.y < in_front.y:
                        new_tail = new_tail.next("U")
                        last_move = "U"
                    else:
                        new_tail = new_tail.next("D")
                        last_move = "D"
                else:
                    if tail.x < in_front.x:
                        new_tail = new_tail.next("R")
                        last_move = "R"
                    else:
                        new_tail = new_tail.next("L")
                        last_move = "L"
                if debug:
                    print(
                        f"Tail {i+1} {new_tail} dist to {in_front} = {d} => {last_move}")
        in_front = new_tail
        new_tails[i] = new_tail
    return new_head, new_tails


def perform(filename, nb_of_tails=1, debug=False):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    head = Pos(0, 0)
    tails = [Pos(0, 0) for i in range(nb_of_tails)]
    tail_positions = {(head.x, head.y)}
    for move in parse(filename):
        # print(f"=={move}==")
        direction, count = move.split(" ")
        for i in range(0, int(count)):
            head, tails = next_position(head, tails, direction, debug)
            tail_positions.add((tails[-1].x, tails[-1].y))
            # print(f"New pos: head: {head}, tail: {tail}")
            if debug:
                print(f"{direction}")
            max_x, max_y = max(max_x, head.x, max(t.x for t in tails)), max(
                max_y, head.y, max(t.y for t in tails))
            min_x, min_y = min(min_x, head.x, min(t.x for t in tails)), min(
                min_y, head.y, min(t.y for t in tails))
            if debug:
                for y in range(min_y, max_y+1)[::-1]:
                    line_str = ""
                    for x in range(min_x, max_x+1):
                        if x == 0 and y == 0:
                            line_str += "s"
                        elif head.x == x and head.y == y:
                            line_str += "H"
                        else:
                            flag = False
                            for i in range(len(tails)):
                                t = tails[i]
                                if t.x == x and t.y == y:
                                    flag = True
                                    line_str += f"{i+1}"
                                    break
                            if not flag:
                                line_str += "."
                    print(line_str)
    if debug:
        print("================================================================")
        for y in range(min_y, max_y+1)[::-1]:
            line_str = ""
            for x in range(min_x, max_x+1):
                if x == 0 and y == 0:
                    line_str += 's'
                elif any(t[0] == x and t[1] == y for t in tail_positions):
                    line_str += "x"
                else:
                    line_str += "."
            print(line_str)
    return len(tail_positions)


result_test = perform("9-test", 1)
print(result_test)

result_test = perform("9")
print(result_test)

result_test = perform("9-test", 9)
print(result_test)

result_test = perform("9-test2", 9)
print(result_test)

result_test = perform("9", 9)
print(result_test)
