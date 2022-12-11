import sys

def parse_input(input_filename):
  with open(input_filename, 'r') as f:
    # Split input into current state and moves
    current_state_lines = []
    current_state_complete = False
    move_lines = []
    while f:
      line = f.readline()
      if line == "":
        break
      while line not in ["\n", "\r\n"] and current_state_complete == False:
        current_state_lines.append(line.rstrip())
        line = f.readline()
      current_state_complete = True
      move_lines.append(line.rstrip())
  
  return [current_state_lines, move_lines]

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]
  [ current_state_input, moves_input ] = parse_input(input_file)
  cs_field_length = 4
  for line in current_state_input:
    items = [line[i:i+cs_field_length].strip() for i in range(0, len(line), cs_field_length)]
     
if __name__ == "__main__":
  main()