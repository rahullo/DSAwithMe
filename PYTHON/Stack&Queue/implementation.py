class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def peek(self):
        if self.head ==None:
            return self.tail
        else:
            return self.tail.data

    def pop(self):
        curr = self.head
        if self.head ==None:
            return "Stack is Empty"
        else:
            while curr.next.next != None:
                curr = curr.next
            
            temp = curr.next.data
            curr.next = None
            return temp

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    # def pop(self):




st = Stack()
# print(st.peek())
st.insert(3)
st.insert(4)
st.insert(5)
st.insert(6)
st.insert(7)
# print(st.peek())
st.printList()
print('\n')
print(st.pop())
print('\n')
st.printList()


