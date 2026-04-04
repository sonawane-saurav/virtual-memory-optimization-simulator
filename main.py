'''
from core.fifo import fifo

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = fifo(pages, frames)

print("Page Faults:", faults)
print("Memory States:")

for step in history:
    print(step)
'''


'''
from core.lru import lru

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = lru(pages, frames)

print("\nLRU Page Faults:", faults)
for step in history:
    print(step)
'''


from core.optimal import optimal

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = optimal(pages, frames)

print("\nOptimal Page Faults:", faults)
for step in history:
    print(step)