import queue
q = queue.Queue(10)
q.put('a')
q.put('b')
q.put('c')
print(q.get())
print(q.get())
print(q.get())