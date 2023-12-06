# Maybe this might be a bit overkill, but making a queue made sense to me jajaj

from collections import deque


def getCards(cardNumber, winning, numbers):
    numCards = len(set(winning).intersection(set(numbers)))
    nextCards = list(
        map(
            lambda x: x[0] + x[1],
            list(zip([cardNumber] * numCards, list(range(numCards)))),
        )
    )
    for i in nextCards:
        data.append(rawData[i])
    return numCards


def removeVoid(arr):
    return list(filter(lambda x: x != "", arr))


rawData = list(map(lambda x: x.strip().split("|"), open(r"./Day4/day4.in").readlines()))
data = deque(rawData)
result = 0

while len(data) > 0:
    winning, numbers = data.popleft()
    winning = winning.split(":")
    cardNumber = int(winning[0].split(" ")[-1])

    result += getCards(
        cardNumber, removeVoid([*winning[1].strip().split(" ")]), [*numbers.split()]
    )
print(result + len(rawData))
