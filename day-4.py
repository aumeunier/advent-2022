import string

from common import parse

elf_groups = [e.split(",") for e in parse(4)]
fully_overlap_count = 0
overlap_count = 0

for g in elf_groups:
    assignments = []
    for e in g:
        elf = e.split("-")
        elf_range = [int(x) for x in range(int(elf[0]), int(elf[1])+1)]
        assignments.append(set(elf_range))
    s = set.intersection(*assignments)
    overlap = len(s)
    if any(overlap == len(e) for e in assignments):
        fully_overlap_count += 1
    if overlap > 0:
        overlap_count += 1

print(fully_overlap_count)
print(overlap_count)
