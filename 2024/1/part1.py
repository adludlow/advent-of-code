left = []
right = []
with open("input.txt", "r") as f:
    for line in f:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
left.sort()
right.sort()

print(sum([max(l, r) - min(l, r) for l, r in zip(left, right)]))
