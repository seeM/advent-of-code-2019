import math
from typing import Tuple


def normalize(v: Tuple[int, int]) -> Tuple[float, float]:
    if v == (0, 0):
        return v
    x, y = v
    vnorm = abs(x) + abs(y)
    return (x / vnorm, y / vnorm)


def solve(inputs: str) -> int:
    positions = []
    for i, line in enumerate(inputs.strip().split("\n")):
        for j, char in enumerate(line.strip()):
            if char == "#":
                positions.append((i, j))

    counts = {}
    for (si, sj) in positions:
        deltas = [(si - i, sj - j) for i, j in positions if (i, j) != (si, sj)]
        unit_deltas = [normalize(v) for v in deltas]
        count = len(set(unit_deltas))
        counts[(si, sj)] = count

    m = max(counts.values())
    # HACK
    p = [k for k, v in counts.items() if v == m][0]
    return (p[1], p[0]), m


assert solve(
    """
    .#..#
    .....
    #####
    ....#
    ...##
    """
) == ((3, 4), 8)

assert solve(
    """
    ......#.#.
    #..#.#....
    ..#######.
    .#.#.###..
    .#..#.....
    ..#....#.#
    #..#....#.
    .##.#..###
    ##...#..#.
    .#....####
    """
) == ((5, 8), 33)

assert solve(
    """
    #.#...#.#.
    .###....#.
    .#....#...
    ##.#.#.#.#
    ....#.#.#.
    .##..###.#
    ..#...##..
    ..##....##
    ......#...
    .####.###.
    """
) == ((1, 2), 35)

assert solve(
    """
    .#..#..###
    ####.###.#
    ....###.#.
    ..###.##.#
    ##.##.#.#.
    ....###..#
    ..#.#..#.#
    #..#.#.###
    .##...##.#
    .....#.#..
    """
) == ((6, 3), 41)

assert solve(
    """
    .#..##.###...#######
    ##.############..##.
    .#.######.########.#
    .###.#######.####.#.
    #####.##.#.##.###.##
    ..#####..#.#########
    ####################
    #.####....###.#.#.##
    ##.#################
    #####.##.###..####..
    ..######..##.#######
    ####.##.####...##..#
    .#####..#.######.###
    ##...#.##########...
    #.##########.#######
    .####.#.###.###.#.##
    ....##.##.###..#####
    .#.#.###########.###
    #.#.#.#####.####.###
    ###.##.####.##.#..##
    """
) == ((11, 13), 210)


with open("data/day10.txt") as f:
    inputs = f.read()

start, sol_a = solve(inputs)
print(sol_a)


def angle(x, y):
    a = math.atan2(x, y)
    return a if a >= 0 else a + 2 * math.pi


def solve_b(inputs: str, start) -> int:
    sx, sy = start

    positions = []
    for y, line in enumerate(inputs.strip().split("\n")):
        for x, char in enumerate(line.strip()):
            if char == "#" and (x, y) != (sx, sy):
                positions.append((x, y))

    deltas = [(x - sx, - (y - sy)) for x, y in positions]
    # unit_deltas = [normalize(v) for v in deltas]
    angles = [angle(x, y) for x, y in deltas]
    mags = [sum(vi ** 2 for vi in v) for v in deltas]

    li = list(zip(mags, angles, positions, deltas))
    li = sorted(li, key=lambda x: (x[1], x[0]))

    result = []
    prev_angle = None
    i = 0
    while li:
        if i >= len(li):
            i = 0
            prev_angle = None
        (mag, ang, pos, _) = li[i]
        if ang == prev_angle:
            i += 1
            continue

        li.pop(i)
        result.append(pos)
        prev_angle = ang

    # li = sorted(li, key=lambda x: (x[0], x[1]))

    # TODO: 1. Create a set of tuples (angle with UP, vector magnitude, xy coords?)
    #       2. Sort by first two keys.
    #       3. Select ith entry in sorted list.

    # return result
    return result


li = solve_b(
    """
    .#..##.###...#######
    ##.############..##.
    .#.######.########.#
    .###.#######.####.#.
    #####.##.#.##.###.##
    ..#####..#.#########
    ####################
    #.####....###.#.#.##
    ##.#################
    #####.##.###..####..
    ..######..##.#######
    ####.##.####...##..#
    .#####..#.######.###
    ##...#.##########...
    #.##########.#######
    .####.#.###.###.#.##
    ....##.##.###..#####
    .#.#.###########.###
    #.#.#.#####.####.###
    ###.##.####.##.#..##
    """,
    start=(11, 13)
)
assert li[0] == (11, 12)
assert li[1] == (12, 1)
assert li[2] == (12, 2)
assert li[9] == (12, 8)
assert li[19] == (16, 0)
assert li[49] == (16, 9)
assert li[99] == (10, 16)
assert li[198] == (9, 6)
assert li[199] == (8, 2)
assert li[200] == (10, 9)
assert li[298] == (11, 1)

x, y = solve_b(inputs, start)[199]
print(100 * x + y)
