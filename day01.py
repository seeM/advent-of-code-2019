def get_fuel(mass: int) -> int:
    return mass // 3 - 2


assert get_fuel(12) == 2
assert get_fuel(14) == 2
assert get_fuel(1969) == 654
assert get_fuel(100756) == 33583

with open("data/day01.txt") as f:
    masses = [int(line) for line in f.read().strip().split("\n")]

total_fuel = sum(get_fuel(mass) for mass in masses)
print(total_fuel)


def get_recursive_fuel(mass: int) -> int:
    fuel = max(0, mass // 3 - 2)
    return fuel + get_recursive_fuel(fuel) if fuel > 0 else 0


assert get_recursive_fuel(2) == 0
assert get_recursive_fuel(14) == 2
assert get_recursive_fuel(1969) == 966
assert get_recursive_fuel(100756) == 50346

total_recursive_fuel = sum(get_recursive_fuel(mass) for mass in masses)
print(total_recursive_fuel)
