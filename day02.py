from typing import List


def compute(intcode: List[int], pos: int = 0) -> List[int]:
    intcode = intcode[:]
    opcode = intcode[pos]
    if opcode == 1:
        intcode[intcode[pos + 3]] = (
            intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
        )
        return compute(intcode, pos + 4)
    elif opcode == 2:
        intcode[intcode[pos + 3]] = (
            intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
        )
        return compute(intcode, pos + 4)
    elif opcode == 99:
        return intcode
    else:
        raise ValueError


assert compute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert compute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert compute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


with open("data/day02.txt") as f:
    intcode = [int(x) for x in f.read().strip().split(",")]

intcode[1] = 12
intcode[2] = 2
print(compute(intcode)[0])


def compute_2(intcode, noun, verb):
    intcode = intcode[:]
    intcode[1] = noun
    intcode[2] = verb
    return compute(intcode)


for noun in range(len(intcode)):
    for verb in range(len(intcode)):
        result = compute_2(intcode, noun, verb)[0]
        if result == 19690720:
            print(100 * noun + verb)
            break
