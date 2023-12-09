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
        self.adjacent_parts = []

    def __repr__(self):
        return f"val: {self.val}, coords: {self.coords}, adjacent_parts: {self.adjacent_parts}"

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
    for s in symbols:
        for n in numbers:
            if is_adjacent(n, s.coords):
                parts.append(n)
                s.adjacent_parts.append(n)

    print(sum(int(p.val) for p in parts))

    gears = [s for s in symbols if s.val == "*" and len(s.adjacent_parts) == 2]
    total_ratio = 0
    for g in gears:
        total_ratio += (int(g.adjacent_parts[0].val)*int(g.adjacent_parts[1].val))

    print(total_ratio)

if __name__ == "__main__":
    solution()
