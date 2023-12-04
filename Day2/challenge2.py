def minimum(sets) -> tuple:
    sets = [
        list(
            map(
                lambda x: (int(x[0]), x[1]),
                [tuple(dice.strip().split(" ")) for dice in set.split(",")],
            )
        )
        for set in sets
    ]

    return (
        max([[dice[0] for dice in set if "green" in dice] for set in sets])[0],
        max([[dice[0] for dice in set if "blue" in dice] for set in sets])[0],
        max([[dice[0] for dice in set if "red" in dice] for set in sets])[0],
    )


data = open(r"./DayTwo/day2.in")
result = 0
for line in list(map(lambda x: x.strip(), data.readlines())):
    game, sets = line.split(":")
    green, blue, red = minimum(sets.split(";"))
    result += green * red * blue

print(result)
