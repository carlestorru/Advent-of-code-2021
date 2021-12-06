list = []

with open('input.txt') as f:
    for line in f:
        list.append(line.strip())

def solve1():
    result = []
    numLen = len(list[0])
    for i in range(numLen):
        ones = 0
        zeros = 0
        for n in list:
            if n[i] == '0':
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            result.append(1)
        else:
            result.append(0)
    
    gamma = 0
    epsilon = 0

    for i in range(len(result)):
        if result[i] == 1:
            gamma += pow(2,(len(result)-1)-i)
        else:
            epsilon += pow(2,(len(result)-1)-i)

    return gamma * epsilon

print("Part 1:", solve1())

def solve2():
    oxygen = list
    numLen = len(oxygen[0])
    for i in range(numLen):
        one = 0
        zero = 0
        ones = []
        zeros = []
        for n in oxygen:
            if n[i] == '0':
                zero += 1
                zeros.append(n)
            else:
                one += 1
                ones.append(n)
        if zero > one:
            oxygen = zeros
        else:
            oxygen = ones
        if len(oxygen) == 1:
            break

    o2 = int(oxygen[0],2)

    scrubber = list
    for i in range(numLen):
        one = 0
        zero = 0
        ones = []
        zeros = []
        for n in scrubber:
            if n[i] == '0':
                zero += 1
                zeros.append(n)
            else:
                one += 1
                ones.append(n)
        if zero > one:
            scrubber = ones
        else:
            scrubber = zeros
        if len(scrubber) == 1:
            break
    
    co2 = int(scrubber[0],2)

    return o2 * co2 

print("Part 2:", solve2())