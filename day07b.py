from itertools import permutations
from typing import Iterable, List, Optional, Tuple

import pytest


def compute(intcode: List[int], inputs: List[int]) -> Tuple[List[int], int]:
    intcode = list(intcode)
    inputs = list(inputs)

    pos = 0
    while True:
        header = f"{intcode[pos]:05}"
        opcode = int(header[3:])
        first_mode = int(header[2])
        second_mode = int(header[1])

        try:
            first: Optional[int]
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
        except IndexError:
            first = None

        try:
            second: Optional[int]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]
        except IndexError:
            second = None

        if opcode == 1:
            assert first is not None and second is not None
            intcode[intcode[pos+3]] = first + second
            pos += 4

        elif opcode == 2:
            assert first is not None and second is not None
            intcode[intcode[pos+3]] = first * second
            pos += 4

        elif opcode == 3:
            assert first_mode == 0
            intcode[intcode[pos+1]] = yield
            pos += 2

        elif opcode == 4:
            if first is not None:
                output = first
            pos += 2

        elif opcode == 5:
            assert first is not None and second is not None
            if first:
                pos = second
            else:
                pos += 3

        elif opcode == 6:
            assert first is not None and second is not None
            if not first:
                pos = second
            else:
                pos += 3

        elif opcode == 7:
            assert first is not None and second is not None
            intcode[intcode[pos+3]] = int(first < second)
            pos += 4

        elif opcode == 8:
            assert first is not None and second is not None
            intcode[intcode[pos+3]] = int(first == second)
            pos += 4

        elif opcode == 99:
            return intcode, output

        else:
            raise RuntimeError("invalid opcode")


def circuit(intcode: List[int], settings: Iterable[int]) -> int:
    amp_intcodes = [intcode for _ in settings]

    while True:
        output = 0
        for amp_intcode, setting in zip(amp_intcodes, settings):
            amp_intcode, output = compute(amp_intcode, inputs=[setting, output])

    return output


def max_signal(intcode: List[int], n_amplifiers: int = 5) -> int:
    all_settings = permutations(range(5), 5)
    return max(circuit(intcode, settings) for settings in all_settings)


@pytest.mark.parametrize(
    "intcode,settings,expected",
    [
        ([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 43210),
        ([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 54321),
        ([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 65210),
    ]
)
def test_circuit(intcode, settings, expected):
    assert circuit(intcode, settings) == expected


@pytest.mark.parametrize(
    "intcode,expected",
    [
        ([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], 43210),
        ([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], 54321),
        ([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], 65210),
    ]
)
def test_max_signal(intcode, expected):
    assert max_signal(intcode) == expected


with open("data/day07.txt") as f:
    intcode = [int(x) for x in f.read().strip().split(",")]


print(max_signal(intcode))
