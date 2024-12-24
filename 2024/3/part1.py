from re import finditer

acc = 0
with open("input.txt", "r") as f:
    data = f.read()

    for match in finditer(r"mul\((\d+),(\d+)\)", data):
        acc = acc + int(match.groups()[0]) * int(match.groups()[1])

print(acc)