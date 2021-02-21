import itertools
import re
from itertools import combinations
from pprint import pprint
from tqdm import tqdm
# from typing import NamedTuple

import numpy as np


class Planet:

    def __init__(self, x, y, z, vx=0, vy=0, vz=0):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    @property
    def vel(self):
        return (self.vx, self.vy, self.vz)

    def potential_energy(self):
        return sum(abs(s) for s in self.pos)

    def kinetic_energy(self):
        return sum(abs(s) for s in self.vel)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __repr__(self):
        return (
            f"pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, "
            f"vel=<x={self.vx:3}, y={self.vy:3}, z={self.vz:3}>, "
            f"pe={self.potential_energy()}, "
            f"ke={self.kinetic_energy()}"
        )

    def astuple(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)

    # def move(self):
    #     self.x, self.y, self.z = (self.x + self.vx, self.y + self.vy, self.z + self.vz)


def update_dim_vel(s0, s1, v0, v1):
    if s0 == s1:
        return (v0, v1)
    if s0 > s1:
        return (v0-1, v1+1)
    if s0 < s1:
        return (v0+1, v1-1)


def apply_gravity(p0, p1):
    p0.vx, p1.vx = update_dim_vel(p0.x, p1.x, p0.vx, p1.vx)
    p0.vy, p1.vy = update_dim_vel(p0.y, p1.y, p0.vy, p1.vy)
    p0.vz, p1.vz = update_dim_vel(p0.z, p1.z, p0.vz, p1.vz)


def apply_velocity(p):
    p.x, p.y, p.z = (p.x + p.vx, p.y + p.vy, p.z + p.vz)


def solve_a(inputs, timesteps):

    pattern = r"^<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>$"

    planets = []
    for line in inputs.strip().split("\n"):
        match = re.match(pattern, line.strip())
        p = Planet(*(int(x) for x in match.groups()))
        planets.append(p)

    for t in range(timesteps):
        # print(f"After {t} steps:")
        # for p in planets:
        #     print(p)
        # print()

        for p0, p1 in combinations(planets, 2):
            apply_gravity(p0, p1)

        for p in planets:
            apply_velocity(p)

        energy = sum(p.total_energy() for p in planets)

    # print(f"After {t+1} steps:")
    # for p in planets:
    #     print(p)
    # print()

    return energy


def solve_b(inputs):

    pattern = r"^<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>$"

    planets = []
    for line in inputs.strip().split("\n"):
        match = re.match(pattern, line.strip())
        p = Planet(*(int(x) for x in match.groups()))
        planets.append(p)

    # for t in range(timesteps):
    state = tuple(p.astuple() for p in planets)
    states = set(state)
    t = 0
    for _ in tqdm(itertools.count()):
    # while True:
        for p0, p1 in combinations(planets, 2):
            apply_gravity(p0, p1)

        for p in planets:
            apply_velocity(p)

        t += 1

        state = tuple(p.astuple() for p in planets)
        if state in states:
            return t - 1

        states.add(state)


def solve_b_2(inputs):

    pattern = r"^<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>$"

    pos = []
    for line in inputs.strip().split("\n"):
        match = re.match(pattern, line.strip())
        p = tuple(int(x) for x in match.groups())
        pos.append(p)

    pos = np.array(pos)
    vel = np.zeros_like(pos)
    print(pos)

    # for t in range(timesteps):
    # state = tuple(p.astuple() for p in planets)
    # states = set(state)
    # t = 0
    # for _ in tqdm(itertools.count()):
    # # while True:
    #     for p0, p1 in combinations(planets, 2):
    #         apply_gravity(p0, p1)

    #     for p in planets:
    #         apply_velocity(p)

    #     t += 1

    #     state = tuple(p.astuple() for p in planets)
    #     if state in states:
    #         return t - 1

    #     states.add(state)


assert solve_a(
    """
    <x=-1, y=0, z=2>
    <x=2, y=-10, z=-7>
    <x=4, y=-8, z=8>
    <x=3, y=5, z=-1>
    """,
    10
) == 179


with open("data/day12.txt") as f:
    inputs = f.read()


print(solve_a(inputs, 1000))


# assert solve_b(
#     """
#     <x=-1, y=0, z=2>
#     <x=2, y=-10, z=-7>
#     <x=4, y=-8, z=8>
#     <x=3, y=5, z=-1>
#     """
# ) == 2772

# assert solve_b(
#     """
#     <x=-8, y=-10, z=0>
#     <x=5, y=5, z=10>
#     <x=2, y=-7, z=3>
#     <x=9, y=-8, z=-3>
#     """
# ) == 4686774924

print(solve_b(inputs))
