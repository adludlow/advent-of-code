import sys

from typing import List

def calc_winnings(matches: List[int]):
    print(matches)
    if len(matches) == 0:
        return 0
    if len(matches) == 1:
        print(1)
        return 1
    print(pow(2, (len(matches)-1)))
    return pow(2, (len(matches)-1))

def solution(input_file_path: str):
    results = []
    with open(input_file_path, "r") as input:
        for line in input:
            [win, ours] = line.rstrip().split(": ")[1].split(" | ")
            result = list(set(win.split()) & set(ours.split())) 
            results.append(result)

    print(sum(calc_winnings(r) for r in results))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass a test input argument")
        sys.exit(1)

    solution(sys.argv[1])