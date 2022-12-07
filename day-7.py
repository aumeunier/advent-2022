from itertools import groupby
from operator import itemgetter

from common import parse_yield


class Node():
    def __init__(self, path):
        # self.parent = parent
        self.path = path
        self.children = set()
        # parent.tree_level + 1 if parent else 0
        self.tree_level = len([c for c in self.path if c == '/'])
        self.size = 0
        self.total_size = 0


current = []
all_nodes = []
tree = {}  # path: node

gen = parse_yield("7")

line = next(gen)
try:
    while True:
        if line.startswith("$"):
            l = line.split(" ")
            command = l[1]
            if command == "cd":
                cd = l[2]
                if cd == "..":
                    current.pop()
                else:
                    node_path = '/'.join(current + [cd])
                    current_node_path = '/'.join(current + [cd])
                    current_node = tree.get(current_node_path)
                    if not current_node:
                        current_node = Node(current_node_path)
                        tree[current_node_path] = current_node
                        all_nodes.append(current_node)
                    node = tree.get(node_path)
                    if not node:
                        node = Node(node_path)
                        tree[node_path] = node
                        all_nodes.append(node)
                    current.append(cd)
                line = next(gen)
            elif command == "ls":
                line = next(gen)
                parent_path = '/'.join(current)
                node = tree.get(parent_path)
                if not node:
                    node = Node(parent_path)
                    tree[parent_path] = node
                    all_nodes.append(node)
                while not line.startswith("$"):
                    what, filename = line.split(" ")
                    if what == "dir":
                        node_path = '/'.join(current + [filename])
                        child_node = tree.get(node_path)
                        if not child_node:
                            child_node = Node(node_path)
                            tree[child_node.path] = child_node
                            all_nodes.append(child_node)
                        node.children.add(child_node)
                        print(
                            f"2 New child for {node.path} = {child_node.path}")
                    else:
                        node.size += int(what)
                        print(f"{node.path} +{what} ({filename})")
                    line = next(gen)
except StopIteration as e:
    pass

disk_used = sum([n.size for n in all_nodes])
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
space_to_free = NEEDED_SPACE - (TOTAL_SPACE - disk_used)
print(
    f"========== {len(all_nodes)} nodes ({disk_used} used, need {space_to_free}) =============")
total = 0
smallest_big_enough = None
tree_levels = [[], [], [], [], [], [], [], [], [], []]
for n in all_nodes:
    lvl = n.tree_level
    tree_levels[lvl].append(n)
    # print(f"{n.path}={n.size}")
for i in list(range(len(tree_levels)))[::-1]:
    print(f"LEVEL {i} => {len(tree_levels[i])}")
    for n in tree_levels[i]:
        n.total_size = sum([c.total_size for c in n.children]) + n.size
        # print(f"{n.path}={n.total_size} {[c.path for c in n.children]}")
        if n.total_size < 100000:
            total += n.total_size
        if n.total_size >= space_to_free and (smallest_big_enough is None or n.total_size < smallest_big_enough):
            smallest_big_enough = n.total_size
print(total)
print(smallest_big_enough)
