import queue
"""
FIFO: First in first out.
"""
q = queue.Queue(6)

print("04:",q.qsize())
print("05:", q.empty())
q.put(5)
q.put(9)
q.put(1)
q.put(7)
q.put(12)
q.put(3)
print("12:",q.qsize())
print("13:", q.full())

print(q.get())
print(q.get())
print(q.get())
print(q.get())

print("20:",q.qsize())
print("21:", q.full())



