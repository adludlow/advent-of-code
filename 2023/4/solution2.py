import sys

from typing import List


card_map = {}
cards = []
count = 0

class Card:
    def __init__(self, card_no: int, matching_numbers: List[int]):
        self.card_no = card_no
        self.matching_numbers = matching_numbers
        self.num_matches = len(matching_numbers)

    def __repr__(self):
        return f"card: {self.card_no}, {self.num_matches}"

def card_from_line(card_line: str):
    [card_desc, numbers] = card_line.rstrip().split(": ")
    card_no = int(card_desc.split()[1])

    [win, ours] = numbers.split(" | ")
    matching_numbers = list(set(win.split()) & set(ours.split())) 
    return Card(card_no, matching_numbers)

def calc_winnings(matches: List[int]):
    if len(matches) == 0:
        return 0
    if len(matches) == 1:
        return 1
    return pow(2, (len(matches)-1))

def process_cards(cards: List[Card]):
    result = 0
    for c in cards:
        copies = [card_map[i] for i in range(c.card_no+1, c.card_no+1 + c.num_matches) if i < len(list(card_map))]
        result = result + process_cards(copies)
    return len(cards) + result

def process_card(card: Card):
    global count
    count = count+1
    global cards
    copies = [card_map[i] for i in range(card.card_no+1, card.card_no+1 + card.num_matches) if i < len(list(card_map))+1]
    cards = cards + copies

def solution(input_file_path: str):
    global count
    with open(input_file_path, "r") as input:
        for line in input:
            card = card_from_line(line)
            card_map[card.card_no] = card 
            cards.append(card)

    while len(cards) > 0:
        process_card(cards.pop())

    print(count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Pass a test input argument")
        sys.exit(1)

    solution(sys.argv[1])