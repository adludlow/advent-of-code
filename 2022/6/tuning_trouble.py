import sys
from collections import deque

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]

  offset = 14
  with open(input_file, 'r') as f:
    data = f.read()
    buffer = deque(list(data[:offset]))
    if len(set(buffer)) == 14:
      print(f"Answer: {buffer}")
    for c in data[offset:]:
      buffer.popleft()
      buffer.append(c)
      if len(set(buffer)) == 14:
        break
      offset = offset+1
    print(f"Answer: {offset+1}: {buffer}")

if __name__ == "__main__":
  main()
