class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.length = 0

  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node
      self.length +=1


  def printList(self):
    curr = self.head
    while curr != None:
      print(curr.val, end=' ')
      curr = curr.next
  
link1 = Linked_List()
link2 = Linked_List()
link3 = Linked_List()

link1.append(1)
link1.append(4)
link1.append(5)

link2.append(1)
link2.append(3)
link2.append(4)

link3.append(2)
link3.append(6)



def mergeKLists(lists):
  merged = []
  for item in lists:
    currentNode = item[0]
    while currentNode != None:
      merged.append(currentNode.val)
      currentNode = currentNode.next
  merged.sort(reverse=False)
  return merged


print(mergeKLists([[link1.head], [link2.head], [link3.head]]))