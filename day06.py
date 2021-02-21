# TODO: Add tests
from collections import defaultdict


with open("data/day06.txt") as f:
    inputs = f.read().strip().split("\n")

# inputs = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L""".split("\n")


# inputs = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN""".split("\n")


parents = {}
for line in inputs:
    parent, child = line.split(")")
    parents[child] = parent


from pprint import pprint
pprint(parents)


def get_path(parents, end, start="COM"):

    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    return path


def get_n_orbits(parents, end, start="COM"):
    return len(get_path(parents, end, start)) - 1


def get_total_n_orbits(parents, start="COM"):
    return sum(get_n_orbits(parents, end) for end in parents)


you_path = get_path(parents, "YOU")
san_path = get_path(parents, "SAN")

# print(you_path)
# print(san_path)

intersect = list(set(you_path).intersection(san_path))
intersect_dists = [get_n_orbits(parents, e) for e in intersect]

# print(intersect)
# print(intersect_dists)

biggest = intersect[intersect_dists.index(max(intersect_dists))]

# print(biggest)

path = you_path[:you_path.index(biggest)] + [biggest] + san_path[:san_path.index(biggest):][::-1]

# print(path)
print(len(path) - 3)
# assert get_n_orbits(parents, end="D") == 3
# assert get_n_orbits(parents, end="L") == 7
# assert get_n_orbits(parents, end="COM") == 0

# print(get_total_n_orbits(parents))

# TODO: Part b: get the intersecting node (set intersection of paths)
