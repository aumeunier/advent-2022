import string

from common import parse

item_priority = {
    k: i+1
    for i, k in enumerate(string.ascii_letters)
}


def split(to_split, chunk_size=None, nb_chunks=2):
    chunk_size = chunk_size or len(to_split) // nb_chunks
    for i in range(0, len(to_split), chunk_size):
        yield set(to_split[i:i + chunk_size])


elves = parse(3)
rucksacks = [split(line) for line in elves]
item_in_common = [list(next(l).intersection(next(l)))[0] for l in rucksacks]
print(sum(item_priority[k] for k in item_in_common))

elf_groups = split(elves, 3)
result_2 = sum(item_priority[c]
               for e in elf_groups for c in set.intersection(*list(set(s) for s in e)))
print(result_2)
