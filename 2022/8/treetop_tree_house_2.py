import sys

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]
  
  total_scores = []
  with open(input_file, 'r') as f:
    lines = f.read().splitlines() 

    for i, line in enumerate(lines):
        heights = list(line)
        for j, height in enumerate(heights):
            # check left
            scores = []
            curr_dir_score = 0
            if j != 0:
                for h in reversed(heights[:j]):
                    if int(h) < int(height):
                        curr_dir_score = curr_dir_score + 1
                    else:
                        curr_dir_score = curr_dir_score + 1
                        break
                scores.append(curr_dir_score)
            # check right
            curr_dir_score = 0
            if j != len(heights)-1:
                for h in heights[j+1:]:
                    if int(h) < int(height):
                        curr_dir_score = curr_dir_score + 1
                    else:
                        curr_dir_score = curr_dir_score + 1
                        break
                scores.append(curr_dir_score)
            # check up
            curr_dir_score = 0
            if i != 0:
                for ln in reversed(lines[:i]):
                    if int(ln[j]) < int(height):
                        curr_dir_score = curr_dir_score + 1
                    else:
                        curr_dir_score = curr_dir_score + 1
                        break
                scores.append(curr_dir_score)
            # check down
            curr_dir_score = 0
            if i != len(lines)-1:
                for ln in lines[i+1:]:
                    if int(ln[j]) < int(height):
                        curr_dir_score = curr_dir_score + 1
                    else:
                        curr_dir_score = curr_dir_score + 1
                        break
                scores.append(curr_dir_score)

            score = 1
            for s in scores:
                if score == 0:
                    continue
                score = score * s

            total_scores.append(score)

  print(sorted(total_scores))

if __name__ == "__main__":
    main()
