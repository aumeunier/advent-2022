import string

from common import parse

stacks = [
    "gjz",
    "cvfwprlq",
    "rglcmpf",
    "mhpwbfl",
    "qvsfcg",
    "ltqmzjhw",
    "vbsfh",
    "szjf",
    "tbhfpdcm",
]
moves = [[int(i) for i in line.split(" ")[1::2]] for line in parse(5)]
for m in moves:
    n, i, j = m
    # stacks[j - 1] = stacks[i - 1][:n][::-1] + stacks[j - 1]  # CrateMover9000
    stacks[j - 1] = stacks[i - 1][:n] + stacks[j - 1]  # CrateMover9001
    stacks[i - 1] = stacks[i - 1][n:]

print("".join(s[0] if s else " " for s in stacks).upper())
