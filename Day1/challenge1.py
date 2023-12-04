def findCode(line):
    code = [c for c in line if c.isdigit()]
    return int(code[0] + code[-1])


data = open(r"./Day1/day1.in")
result = 0
for line in list(map(lambda x: x.strip(), data.readlines())):
    result += findCode(line)
print(result)
