from functools import reduce


def findNumber(list, i):
    result = list[i]
    lowPivot = i + 1
    highPivot = i - 1
    lowEdge = False
    highEdge = False
    while not lowEdge or not highEdge:
        if lowPivot < len(list) and list[lowPivot].isdigit() and not lowEdge:
            result += list[lowPivot]
            lowPivot += 1
        else:
            lowEdge = True
        if highPivot >= 0 and list[highPivot].isdigit() and not highEdge:
            result = list[highPivot] + result
            highPivot -= 1
        else:
            highEdge = True
    return result


directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
data = list(map(lambda x: x.strip(), open(r"./Day3/day3.in").readlines()))

result = []
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == "*":
            numbers = {
                findNumber(data[i + d[0]], j + d[1])
                for d in directions
                if 0 <= i + d[0] < len(data)
                and 0 <= j + d[1] < len(line)
                and data[i + d[0]][j + d[1]].isdigit()
            }

            if len(numbers) == 2:
                result.append(
                    reduce(lambda x, y: x * y, map(lambda x: int(x), numbers))
                )
print(reduce(lambda x, y: x + y, result))
