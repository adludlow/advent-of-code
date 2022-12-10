import sys

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  all_cals = []
  with open(input_file, 'r') as f:
    curr_cals = 0
    for line in f:
      if len(line.rstrip()) > 0:
        curr_cals = curr_cals + int(line.rstrip())
      else:
        all_cals.append(curr_cals)
        curr_cals = 0

  all_cals.sort(reverse=True)
  print(all_cals[0] + all_cals[1] + all_cals[2])

if __name__ == "__main__":
  main()