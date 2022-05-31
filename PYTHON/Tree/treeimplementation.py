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
            

    def lookup(self, value):
        if self.root == None:
            return "Tree is empty!!!"
        else:
            curr = self.root
            while curr:
                if value > curr.value:
                    curr = curr.right
                elif value < curr.value:
                    curr = curr.left
                elif value == curr.value:
                    return "FOUND"
        return "NOT FOUND"

    def remove(self, value):
        if self.root == None:
            return "Tree Is Empty"

        current_node = self.root
        parent_node = None
        while current_node != None:
            if value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                #Node has only left child
                if current_node.right == None and current_node.left != None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return
                # Node has only right child node
                elif current_node.left == None and current_node.right != None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.value > current_node.value:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return
                #Node has neither left nor right node
                elif current_node.left == None and current_node.right ==  None:
                    if parent_node == None:
                        current_node == None
                        return
                    elif parent_node.value > current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return
                # Node has both left and right node

    def breadthFirstSearch(self):
        current_node = self.root
        ans = []
        que = []
        que.append(current_node)
        while len(que) > 0:
            current_node = que[0:1][0]
            del(que[0:1])
            ans.append(current_node.value)
            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
        return ans

    def breadthFirstSearchR(self, que, ans):
        if (len(que ) == 0): 
            return ans
        current_node = que[0: 1][0]
        del(que[0:1])
        ans.append(current_node.value)
        if current_node.left:
            que.append(current_node.left)
        if current_node.right:
            que.append(current_node.right)
        return self.breadthFirstSearchR(que, ans)

            
                

bin = BinarySearchTree()
bin.insert(20)
bin.insert(25)
bin.insert(17)
bin.insert(23)
bin.insert(24)
bin.insert(15)
bin.insert(9)
bin.insert(15)
# print(bin.lookup(0))
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
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)



# bin.remove(15)
# print2D(bin.root)


# list1 = [1, 2, 3, 4, 5]
# print(list1[0:1][0])
# del(list1[0:1])
# print(list1)


print2D(bin.root)
print(bin.breadthFirstSearch())
print(bin.breadthFirstSearchR([bin.root], []))