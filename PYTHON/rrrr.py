COUNT = [10]

def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left, space)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node  = self.root
            while True:
                if value >= current_node.value:
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                elif(value < current_node.value):
                    if(current_node.left == None):
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
def mergeTrees(root1, root2):
  currNode1 = root1
  currNode2 = root2
  que1 = []
  que2 = []
  que1.append(root1)
  que2.append(root2)
  while len(que1) > 0 or len(que2)>0:

    currNode1 = que1[0:1][0]
    del que1[0:1]
    currNode2 = que2[0:1][0]
    del que2[0:1]
    if currNode1.value and currNode2.value:
      currNode1.value = currNode1.value + currNode2.value
      que1.append(currNode1.right)
      que1.append(currNode1.left)
      que2.append(currNode2.right)
      que2.append(currNode2.left)
    elif currNode1.value or currNode2.value:
      currNode1.value = currNode1.value if currNode1.value else currNode2.value
      que1.append(currNode1.right)
      que1.append(currNode1.left)
      que2.append(currNode2.right)
      que2.append(currNode2.left)
    elif not currNode1.value and not currNode2.value:
      continue
  return root1



bina = BinarySearchTree()
bina.insert(1)
bina.insert(3)
bina.insert(2)
bina.insert(5)

bina2 = BinarySearchTree()
bina2.insert(2)
bina2.insert(1)
bina2.insert(3)
bina2.insert(4)
bina2.insert(7)

print2DUtil(bina.root, 2)
print2DUtil(bina2.root, 2)

ans = mergeTrees(bina.root, bina2.root)
