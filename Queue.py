from collections import deque 
 
queue = deque() 
 
queue.append(1) 
queue.append(2) 
queue.append(3) 
 
print(queue.popleft())  # 1
print(queue.popleft())  # 2
 