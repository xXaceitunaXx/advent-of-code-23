def possible(sets) -> bool:
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
        max([[dice[0] for dice in set if "green" in dice] for set in sets])[0] <= 13
        and max([[dice[0] for dice in set if "blue" in dice] for set in sets])[0] <= 14
        and max([[dice[0] for dice in set if "red" in dice] for set in sets])[0] <= 12
    )


data = open(r"./Day2/day2.in")
result = 0
for line in list(map(lambda x: x.strip(), data.readlines())):
    game, sets = line.split(":")
    result += int(game.split()[1]) if possible(sets.split(";")) else 0

print(result)
