cube_count = {
    "blue": 14,
    "green": 13,
    "red": 12
}

def check_valid(game):
    for k in cube_count.keys():
        if game[k] > cube_count[k]:
            return False
    
    return True

def parse_game(g):
    [game, rounds] = g.split(": ")

    result = {
        "game_id": int(game.split(" ")[1]),
        "blue": 0,
        "green": 0,
        "red": 0
    }

    for r in rounds.split("; "):
        for c in r.split(", "):
            [count, colour] = c.split(" ")
            if int(count) > result[colour]:
                result[colour] = int(count)
    
    return result

def solution():
    with open("input_1.txt", "r") as input:
        lines = [line.rstrip() for line in input]
        games = [parse_game(l) for l in lines]

        valid_games = [
            g for g in games 
            if check_valid(g)
        ]

        print(sum([g["game_id"] for g in valid_games]))

        powers = [g["blue"]*g["green"]*g["red"] for g in games]
        print(sum(powers))
            
if __name__ == "__main__":
    solution()
