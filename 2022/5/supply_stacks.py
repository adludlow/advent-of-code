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
        current_state_lines.append(line.rstrip('\n'))
        line = f.readline()
      current_state_complete = True
      move_lines.append(line.rstrip())
  
  move_lines.pop(0) # remove empty string left by empty line in input
  current_state_lines.reverse()
  return [current_state_lines, move_lines]

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]
  [ current_state_input, moves_input ] = parse_input(input_file)
  cs_field_length = 4
  rows = []
  for line in current_state_input:
    items = [line[i:i+cs_field_length].strip().strip("[]") for i in range(0, len(line), cs_field_length)]
    rows.append(items)

  stacks = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
  }
  #stacks = {
  #  1: [],
  #  2: [],
  #  3: []
  #}

  for r in rows:
    #for i in range(0, 3):
    #  if r[i] and r[i] not in ["1", "2", "3"]:
    for i in range(0, 9):
      if r[i] and r[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        stacks[i+1].append(r[i])

  for instr in moves_input:
    parts = instr.split(" ")
    num = int(parts[1])
    source = int(parts[3])
    dest = int(parts[5])

    items = stacks[source][-num:]
    #print(items)
    stacks[source] = stacks[source][:len(stacks[source])-num]
    stacks[dest] = stacks[dest] + items
    #print(stacks, "\n")
    #for i in range(0, num):
    #  val = stacks[source].pop()
    #  stacks[dest].append(val)

  print(stacks)

if __name__ == "__main__":
  main()