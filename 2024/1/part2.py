left = []
right = []
with open("input.txt", "r") as f:
    for line in f:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

print(sum([l * right.count(l) for l in left]))