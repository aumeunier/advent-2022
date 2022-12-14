import ast
from functools import cmp_to_key

from common import parse_2by2

DEBUG = False


def compare_elements(l1, l2):
    if DEBUG:
        print(f"Compare {l1} to {l2}")
    for i in range(len(l1)):
        a = l1[i]
        if len(l2) < i+1:
            return False
        b = l2[i]
        if type(a) == type(b) == type(1):
            if a != b:
                return a < b
        elif type(a) == type(b) == type([]):
            res = compare_elements(a, b)
            if res is not None:
                return res
        else:
            res = compare_elements([a], b) if type(a) == type(1)\
                else compare_elements(a, [b])
            if res is not None:
                return res
    if len(l1) < len(l2):
        return True
    return None


def cmp(l1, l2):
    res = compare_elements(l1, l2)
    if res is None:
        return 0
    return -1 if res else 1


def compute(filename):
    lines = parse_2by2(filename)
    sum = 0
    index = 0
    for a, b in lines:
        index += 1
        first, second = ast.literal_eval(a), ast.literal_eval(b)
        result = compare_elements(first, second)
        if DEBUG:
            print(f"Comparing {first} x {second} => {result}")
        if result:
            sum += index
    if DEBUG:
        print(f"Result for {filename}={sum}")
    return sum


def sort(filename):
    lines = parse_2by2(filename)
    all_lines = [ast.literal_eval("[[2]]"), ast.literal_eval("[[6]]")]
    for a, b in lines:
        all_lines.extend([ast.literal_eval(a), ast.literal_eval(b)])
    sorted_lines = sorted(all_lines, key=cmp_to_key(cmp))
    if DEBUG:
        for e in sorted_lines:
            print(e)
    return (sorted_lines.index([[2]])+1) * (sorted_lines.index([[6]])+1)


assert(compute("13-test") == 13)
compute("13")

assert(sort("13-test") == 140)
# DEBUG = True
print(sort("13"))
