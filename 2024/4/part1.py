matrix: list[list[int]] = []
with open("test_input.txt", "r") as f:
    for i, line in enumerate(f):
        matrix.append([])
        for c in line:
            matrix[i].append(c)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        