import sys
import string

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  priority = 0
  with open(input_file, 'r') as f:
    lines = f.read().splitlines()
    for i in range(0, len(lines), 3):
      intersection = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
      offset = 1 if list(intersection)[0].islower() else 27
      priority = priority + string.ascii_lowercase.index(list(intersection)[0].lower()) + offset

  print(priority)
if __name__ == "__main__":
  main()