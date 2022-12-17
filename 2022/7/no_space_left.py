import sys
from anytree import Node, search, PreOrderIter, PostOrderIter, Walker, RenderTree

def get_item(name, type, t):
  for i in t:
    if i.name == name and i.type == type:
      return i

def main():
  if len(sys.argv) != 2:
    print("Expecting input file input argument")
    sys.exit(1)

  input_file = sys.argv[1]
  
  root = Node("/", type="dir", size=0)
  curr_node = root
  with open(input_file, 'r') as f:
    output = f.read().splitlines()

    for o in output:
      parts = o.split()
      if parts[0] == "$":
        if parts[1] == "cd":
          if parts[2] == "..":
            curr_node = curr_node.parent
          elif parts[2] == "/":
            curr_node = root
          else:
            curr_node = get_item(parts[2], "dir", curr_node.children)
        elif parts[1] == "ls":
          pass
      
      elif parts[0] == "dir":
        Node(parts[1], parent=curr_node, type="dir", size=0)
      
      else:
        Node(parts[1], parent=curr_node, type="file", size=int(parts[0]))
        root.size = root.size + int(parts[0])
        # need to walk up the tree adding to size
        w = Walker()
        path = w.walk(curr_node, root)
        for n in path[0]:
          n.size = n.size + int(parts[0])

  ans_one = 0
  ans_two = 100000000
  free_space = 70000000 - root.size
  space_needed = 30000000 - free_space
  for node in PreOrderIter(root):
    if node.type == "dir":
      if node.size <= 100000:
        ans_one = ans_one + node.size
      if node.size >= space_needed:
        if node.size < ans_two:
          ans_two = node.size

  print(f"Part 1 answer: {ans_one}")
  print(f"Part 2 answer: {ans_two}")


  

if __name__ == "__main__":
  main()