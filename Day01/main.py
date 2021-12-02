list = []

with open('input.txt') as f:
    for line in f:
        list.append(int(line.strip()))

def solve1():
    count = 0
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            count += 1
    return count

print(solve1())

def sum(i):
    return list[i] + list[i+1] + list[i+2]

def solve2():
    count = 0
    for i in range(len(list)-3):
        if sum(i) < sum(i+1):
            count += 1
    return count

print(solve2())