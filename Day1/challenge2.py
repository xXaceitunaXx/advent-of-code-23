def toNumber(string):
    return {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }[string]


def findCode(line):
    l = []
    for i in range(len(line)):
        l.extend(
            [
                (line.find(aceptedDigit, i), aceptedDigit)
                for aceptedDigit in acceptedStrings
                if line.find(aceptedDigit, i) != -1
            ]
        )
    l = list(
        map(
            toNumber,
            [element[1] for element in list(sorted(set(l), key=lambda x: x[0]))],
        )
    )
    return int(l[0] + l[-1])


acceptedStrings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
data = open(r"./DayOne/day1.in")
result = 0
for line in list(map(lambda x: x.strip(), data.readlines())):
    result += findCode(line)
print(result)
