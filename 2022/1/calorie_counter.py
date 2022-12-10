import sys

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  max_cals = 0
  with open(input_file, 'r') as f:
    curr_cals = 0
    for line in f:
      if len(line.rstrip()) > 0:
        curr_cals = curr_cals + int(line.rstrip())
      else:
        if curr_cals > max_cals:
          max_cals = curr_cals
        curr_cals = 0

  print(max_cals)

if __name__ == "__main__":
  main()