import numpy as np

def reorder(n, m):
    ls1 = np.arange(n/2)
    ls2 = np.arange(n/2, n)
    slide = int(m % (n/2))
    return np.roll(ls1, slide), np.roll(ls2, slide)

r = reorder(10, 2)
print(r)