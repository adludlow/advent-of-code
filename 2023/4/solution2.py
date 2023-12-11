import sys

from typing import List


class Card:
    def __init__(self, card_no: int, matching_numbers: List[int]):
        self.card_no = card_no
        self.matching_numbers = matching_numbers
        self.num_matches = len(matching_numbers)

def card_from_line(card_line: str):
    [card_desc, numbers] = card_line.rstrip().split(": ")
    card_no = int(card_desc.split()[1])

    [win, ours] = numbers.split(" | ")
    matching_numbers = list(set(win.split()) & set(ours.split())) 
    return Card(card_no, matching_numbers)

def calc_winnings(matches: List[int]):
    print(matches)
    if len(matches) == 0:
        return 0
    if len(matches) == 1:
        print(1)
        return 1
    return pow(2, (len(matches)-1))

def solution(input_file_path: str):
    card_map = {}
    cards = []
    with open(input_file_path, "r") as input:
        for line in input:
            card = card_from_line(line)
            card_map[card.card_no] = 1
            cards.append(card)

    for c in cards:
        for i in range(c.card_no+1, c.card_no + c.num_matches):
            card_map[i] = card_map[i]+1

    print(card_map)
            
    



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass a test input argument")
        sys.exit(1)

    solution(sys.argv[1])