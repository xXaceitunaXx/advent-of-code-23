from functools import reduce

data = list(map(lambda x: x.strip(), open(r"./Day3/day3.in").readlines()))

flags = []
number = []
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c.isdigit():
            number.append(
                (
                    c,
                    any(
                        [
                            0 <= i + d[0] < len(data)
                            and 0 <= j + d[1] < len(line)
                            and not data[i + d[0]][j + d[1]].isdigit()
                            and data[i + d[0]][j + d[1]] != "."
                            for d in directions
                        ]
                    ),
                )
            )
        else:
            flags.append(number)
            number = []
print(
    reduce(
        lambda x, y: x + y,
        [
            int(reduce(lambda x, y: x + y, [digit[0] for digit in number]))
            for number in flags
            if any(digit[1] for digit in number)
        ],
    )
)
