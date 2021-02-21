from typing import List, Optional


# input hardcoded to puzzle input = 1
def compute(intcode: List[int], input=1) -> Optional[int]:

    pos = 0
    output = None
    while True:
        header = f"{intcode[pos]:05}"
        opcode = int(header[3:])
        first_mode = int(header[2])
        second_mode = int(header[1])
        third_mode = int(header[0])

        assert third_mode == 0

        header_msg = f"{opcode} {first_mode} {second_mode} {third_mode}"
        print(f"{pos:3}    {header}    {header_msg:8}", end="    ")

        if opcode == 1:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]
            intcode[intcode[pos+3]] = first + second

            instruction_msg = f"set pos {intcode[pos+3]} = {first} + {second}"
            print(f"{instruction_msg:24}", end="    ")
            print(intcode[pos:pos+4])
            pos += 4
        elif opcode == 2:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]
            intcode[intcode[pos+3]] = first * second

            instruction_msg = f"set pos {intcode[pos+3]} = {first} * {second}"
            print(f"{instruction_msg:24}", end="    ")
            print(intcode[pos:pos+4])
            pos += 4
        elif opcode == 3:
            assert first_mode == 0
            first = intcode[intcode[pos+1]]
            intcode[intcode[pos+1]] = input

            instruction_msg = f"set pos {intcode[pos+1]} = {input}"
            print(f"{instruction_msg:24}", end="    ")
            print(intcode[pos:pos+2])
            pos += 2
        elif opcode == 4:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]

            instruction_msg = f"output {first}"
            print(f"{instruction_msg:24}", end="    ")
            print(intcode[pos:pos+2])
            output = first
            pos += 2
        elif opcode == 5:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]

            print()

            if first:
                pos = second
            else:
                pos += 3
        elif opcode == 6:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]

            print()

            if not first:
                pos = second
            else:
                pos += 3
        elif opcode == 7:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]

            print()

            intcode[intcode[pos+3]] = int(first < second)

            pos += 4
        elif opcode == 8:
            first = intcode[pos+1] if first_mode else intcode[intcode[pos+1]]
            second = intcode[pos+2] if second_mode else intcode[intcode[pos+2]]

            print()

            intcode[intcode[pos+3]] = int(first == second)

            pos += 4
        elif opcode == 99:
            print()
            return output
        else:
            raise RuntimeError("invalid opcode")


assert compute([3,9,8,9,10,9,4,9,99,-1,8], 8) == 1
assert compute([3,9,8,9,10,9,4,9,99,-1,8], 4) == 0


with open("data/day05.txt") as f:
    intcode = [int(x) for x in f.read().strip().split(",")]

# print(compute(intcode, input=1))

print(compute(intcode, input=5))
