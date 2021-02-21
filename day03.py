from functools import reduce


def get_points(instructions):
    points = [(0, 0)]
    for instruction in instructions:

        point, direction, distance = points[-1], instruction[0], int(instruction[1:])
        if direction == "R":
            points.extend([(point[0] + d, point[1]) for d in range(1, distance + 1)])
        elif direction == "L":
            points.extend([(point[0] - d, point[1]) for d in range(1, distance + 1)])
        elif direction == "D":
            points.extend([(point[0], point[1] - d) for d in range(1, distance + 1)])
        elif direction == "U":
            points.extend([(point[0], point[1] + d) for d in range(1, distance + 1)])
        else:
            raise RuntimeError()
    return points


def get_intersections(*points_list):
    return reduce(lambda x, y: set(x).intersection(set(y)), points_list) - {(0, 0)}


def manhattan_distance(p1, p2):
    return sum(abs(p1i - p2i) for p1i, p2i in zip(p1, p2))


def get_closest_distance(*instructions_list):
    instructions_list = map(lambda x: x.split(","), instructions_list)
    points_list = map(get_points, instructions_list)
    intersections = get_intersections(*points_list)
    distances = [manhattan_distance((0, 0), p) for p in intersections]
    return min(distances)


assert get_closest_distance("R8,U5,L5,D3", "U7,R6,D4,L4") == 6
assert (
    get_closest_distance(
        "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
    )
    == 159
)
assert (
    get_closest_distance(
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    )
    == 135
)


with open("data/day03.txt") as f:
    instructions_list = f.read().strip().split("\n")

print(get_closest_distance(*instructions_list))


def get_steps(points, end):
    return points.index(end)


def get_closest_combined_steps(*instructions_list):
    instructions_list = map(lambda x: x.split(","), instructions_list)
    points_list = list(map(get_points, instructions_list))
    intersections = get_intersections(*points_list)
    steps_list = [
        [points.index(intersection) for intersection in intersections]
        for points in points_list
    ]
    combined_steps = map(sum, zip(*steps_list))
    return min(combined_steps)


assert get_closest_combined_steps("R8,U5,L5,D3", "U7,R6,D4,L4") == 30
assert (
    get_closest_combined_steps(
        "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"
    )
    == 610
)
assert (
    get_closest_combined_steps(
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    )
    == 410
)


print(get_closest_combined_steps(*instructions_list))
