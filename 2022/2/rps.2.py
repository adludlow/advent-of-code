import sys

shape_mapping = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "loss",
  "Y": "draw",
  "Z": "win"
}

rules = {
  ("rock", "scissors"): ("loss", "rock"),
  ("scissors", "rock"): ("win", "rock"),
  ("paper", "rock"): ("loss", "paper"),
  ("rock", "paper"): ("win", "paper"),
  ("paper", "scissors"): ("win", "scissors"),
  ("scissors", "paper"): ("loss", "scissors"),
  ("scissors", "scissors"): ("draw", ""),
  ("paper", "paper"): ("draw", ""),
  ("rock", "rock"): ("draw", "")
}

points = {
  "rock": 1,
  "paper": 2,
  "scissors": 3,
  "win": 6,
  "draw": 3,
  "loss": 0
}

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  score = 0
  with open(input_file, 'r') as f:
    for line in f:
      player_1_shape = shape_mapping[line.rstrip()[0]]
      #player_2_shape = shape_mapping[line.rstrip()[-1]]
      result = shape_mapping[line.rstrip()[-1]]
      
      #result = rules[(player_1_shape, player_2_shape)]
      for shapes, outcome in rules.items():
        #print(f"{player_1_shape}, {result}")
        #print(f"{shapes}, {outcome}")
        if shapes[0] == player_1_shape and outcome[0] == result:
          score = score + points[shapes[1]] + points[result]

      #score = score + points[player_2_shape] + points[result[0]]

  print(score)

if __name__ == "__main__":
  main()