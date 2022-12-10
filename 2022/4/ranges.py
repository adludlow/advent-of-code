import sys

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  count = 0
  with open(input_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip()
      [ a1, a2 ] = line.split(",")
      [ a11, a12 ] = a1.split("-")
      [ a21, a22 ] = a2.split("-")

      if (int(a11) >= int(a21) and int(a11) <= int(a22)) or (int(a12) >= int(a21) and int(a12) <= int(a22)):
        count = count + 1
      elif (int(a21) >= int(a11) and int(a21) <= int(a12)) or (int(a22) >= int(a11) and int(a22) <= int(a12)):
        count = count + 1

  print(count)

if __name__ == "__main__":
  main()