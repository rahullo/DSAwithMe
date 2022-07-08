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


  def printList(self, head):
    curr = head
    while curr != None:
      print(curr.val, end='-> ')
      curr = curr.next
  
link = Linked_List()
link.append(1)
link.append(2)
# link.append(3)
# link.append(4)
# link.append(5)
# link.append(6)
# link.append(7)
link.printList(link.head)

def middleNode(head, n):
  if head.next == None:
            head = None
            return head
  node = head
  prevNode = None
  x = Count(head)
  if x == n:
    head = head.next
    return head
  i = 0
  while i != (x - (n-1)-1):
    prevNode = node
    node = node.next
    i+=1
  prevNode.next = node.next
  node.next = None
  return head

def Count(head):
  i = 0
  node = head
  while node != None:
    i +=1
    node = node.next
  return i
  
print('\n')
head = middleNode(link.head, 2)
link.printList(head)