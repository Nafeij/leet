import sys
from time import time
def fib_itr(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    i = int(sys.argv[1])
    t = time()
    o = fib_itr(i)
    te = time()
    print(o)
    print("Time: %fs" % (te - t))
