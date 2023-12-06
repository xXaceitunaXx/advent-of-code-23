def removeVoid(arr):
    return list(filter(lambda x: x != "", arr))


def getPoints(winning, numbers):
    return (
        2 ** (len(set(winning).intersection(set(numbers))) - 1)
        if len(set(winning).intersection(set(numbers))) > 0
        else 0
    )


data = list(map(lambda x: x.strip().split("|"), open(r"./Day4/day4.in").readlines()))
result = 0

for winning, numbers in data:
    result += getPoints(
        removeVoid([*winning.split(":")[1].strip().split(" ")]), [*numbers.split()]
    )

print(result)
