from core.fifo import fifo

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = fifo(pages, frames)

print("Page Faults:", faults)
print("Memory States:")

for step in history:
    print(step)