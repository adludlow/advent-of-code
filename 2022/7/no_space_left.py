import sys
from anytree import Node, search, PreOrderIter, PostOrderIter, Walker

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
        # need to walk up the tree adding to size
        w = Walker()
        for n in w.walk(curr_node, root):
          print(n)
          if isinstance(n, Node):
            n.size = n.size + int(parts[0])
          else:
            n[0].size = n[0].size + int(parts[0])

  for node in PreOrderIter(root):
    print(f"{node.name},{node.type},{node.size}")

if __name__ == "__main__":
  main()