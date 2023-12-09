from typing import List, Tuple


def get_adjacent_coords(coords: Tuple[int, int]) -> List[Tuple[int, int]]:
    x = coords[0]
    y = coords[1]
    return [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),

        (x+1, y),
        (x+1, y+1),

        (x, y+1),
        (x-1, y+1),
        (x-1, y)
    ]

class Part:
    def __init__(self, val: str, coords: List[Tuple[int,int]]):
        self.val = val
        self.coords = coords
        self.adjacent_coords = [i for sublist in [get_adjacent_coords(c) for c in self.coords] for i in sublist]
    
    def __repr__(self):
        return f"val: {self.val}, coords: {self.coords}, adjacent: {self.adjacent_coords}"

class Symbol:
    def __init__(self, val: str, coords: Tuple[int,int]):
        self.val = val
        self.coords = coords

    def __repr__(self):
        return f"val: {self.val}, coords: {self.coords}"

def is_adjacent(part: Part, coord: Tuple[int, int]):
    return any(c == coord for c in part.adjacent_coords)

def solution():
    numbers = []
    symbols = []

    with open("input.txt", "r") as input:
        for j, l in enumerate(input):
            line = l.rstrip()

            is_part = False
            coords = []
            val = ""
            for i in range(0, len(line)):
                # print(f"{line[i]}, {line[i].isdigit()}")
                if line[i].isdigit():
                    is_part = True
                    val += line[i]
                    coords.append((i,j))
                    continue

                if is_part:
                    # create previous part number
                    numbers.append(Part(val, coords))
                    is_part = False
                    coords = []
                    val = ""
                if line[i] != ".":
                    # symbol
                    symbols.append(Symbol(line[i], (i,j)))
            if is_part:
                # create previous part number
                numbers.append(Part(val, coords))
    
    symbol_coords = [s.coords for s in symbols]

    parts = []
    for s in symbol_coords:
        for n in numbers:
            if is_adjacent(n, s):
                parts.append(n)

    print(sum(int(p.val) for p in parts))

if __name__ == "__main__":
    solution()
