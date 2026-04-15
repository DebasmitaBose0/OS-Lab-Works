Q. Write a Python program to write down the internal & external fragmentation in the following problem:
Blocks = [20, 10, 15, 12, 6]
Processes = [5, 18, 12, 14]
A- blocks = [20, 10, 15, 12, 6]
processes = [5, 18, 12, 14]
def first_fit(b, p):
    b = b[:]
    a = [-1] * len(p)
    for i, x in enumerate(p):
        for j, y in enumerate(b):
            if y >= x:
                a[i] = j
                b[j] -= x
                break
    return a, b
def best_fit(b, p):
    b = b[:]
    a = [-1] * len(p)
    for i, x in enumerate(p):
        k = min((j for j in range(len(b)) if b[j] >= x),
                key=lambda j: b[j],
                default=-1)
        if k != -1:
            a[i] = k
            b[k] -= x
    return a, b
print(first_fit(blocks, processes))
print(best_fit(blocks, processes))

O/P:
First Fit:
([0, -1, 2, 3], [15, 10, 3, -2, 6])
Best Fit:
([4, -1, 3, 2], [20, 10, 1, 0, 1])
Fragmentation:
Remaining memory: [15, 10, 3, -2, 6]
External fragmentation: 32
Remaining memory: [20, 10, 1, 0, 1]
External fragmentation: 32
