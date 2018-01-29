from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
a[1:3]

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print(d)
# Remove "task1" from deque
print("Handling", d.popleft())
print(d)

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# Add ruby to scores, it should be higher. LOL.
bisect.insort(scores, (300, 'ruby'))
print(scores)
