import sys

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]
  
  num_vis = 0
  with open(input_file, 'r') as f:
    lines = f.read().splitlines() 

    for i, line in enumerate(lines):
        if i == 0 or i == len(lines)-1:
            num_vis = num_vis + len(line)
        else:
            heights = list(line)
            for j, height in enumerate(heights):
                if j == 0 or j == len(line)-1:
                    num_vis = num_vis + 1
                    continue
                else:
                    # check left
                    visible = True
                    for h in heights[:j]:
                        if int(h) >= int(height):
                            visible = False
                            break
                    if visible:
                        num_vis = num_vis + 1
                        continue
                    # check right
                    visible = True
                    for h in heights[j+1:]:
                        if int(h) >= int(height):
                            visible = False
                            break
                    if visible:
                        num_vis = num_vis + 1
                        continue
                    # check up
                    visible = True
                    for ln in lines[:i]:
                        if int(ln[j]) >= int(height):
                            visible = False
                            break
                    if visible:
                        num_vis = num_vis + 1
                        continue
                    # check down
                    visible = True
                    for ln in lines[i+1:]:
                        if int(ln[j]) >= int(height):
                            visible = False
                            break
                    if visible:
                        num_vis = num_vis + 1

    print(num_vis)

if __name__ == "__main__":
    main()
