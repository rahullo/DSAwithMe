from collections import deque
# import queue

queue = deque(['rahul', 'chandan', 'yashwant'])
print(queue)
queue.append('gautam')
print(queue)
fifo = queue.popleft()
print(fifo)
print(queue)