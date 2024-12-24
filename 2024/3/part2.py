from re import finditer

acc = 0
with open("input.txt", "r") as f:
    data = f.read()

    dos_and_donts = finditer(r"don't\(\)|do\(\)", data)
    active = True
    active_start = 1
    active_ranges: list[tuple[int, int]] = []
    for i in dos_and_donts:
        if i.group() == "don't()" and active:
            active = False
            active_ranges.append((active_start, i.start()))
        elif i.group() == "do()" and not active:
            active = True
            active_start = i.start()
    if active:
        active_ranges.append((active_start, len(data)))

    for match in finditer(r"mul\((\d+),(\d+)\)", data):
        for r in active_ranges:
            if r[0] <= match.start() <= r[1]:
                acc = acc + int(match.groups()[0]) * int(match.groups()[1])

print(acc)