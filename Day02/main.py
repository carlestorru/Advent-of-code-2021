direction = []
values = []

with open('input.txt') as f:
    for line in f:
        lineSplit = line.split(" ")
        direction.append(lineSplit[0])
        values.append(int(lineSplit[1].strip()))

def solve1():
    horizontal = 0
    depth = 0
    for i in range(len(values)):
        if direction[i] == "forward":
            horizontal += values[i]
        elif direction[i] == "up":
            depth -= values[i]
        else:
            depth += values[i]
    return horizontal * depth

print(solve1())

def solve2():
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(values)):
        if direction[i] == "forward":
            horizontal += values[i]
            depth += aim * values[i]
        elif direction[i] == "up":
            aim -= values[i]
        else:
            aim += values[i]
    return horizontal * depth

print(solve2())