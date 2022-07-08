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
      print(curr.val, end='-> ')
      curr = curr.next
  
link = Linked_List()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(6)
link.append(7)
link.printList()

def middleNode(head):
  i = -1
  middle = None
  node = head
  ansmiddle = head
  while node.next != None:
    i+=1
    if i == 0:
      middle = (1+i)//2
      continue
    elif i%2 != 0:
      middle = (1+i)//2
    else:
      middle = (1+i)//2
    node = node.next

  n = 0
  while middle != n:
    ansmiddle = ansmiddle.next
    n+=1
  return ansmiddle
print('\n')
print(middleNode(link.head))