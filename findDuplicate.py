from random import shuffle

def findDup(L):
    """Assume elements in L are in range [1, len(L)].
    Returns the first duplicate element in L, if one exists.
    Otherwise, returns None.
    """
    if len(L) < 2:
        return None

    fast = slow = 0
    while True:
        fast = L[L[fast]]
        slow = L[slow]
        if fast == slow:
            break
    fast = 0
    while True:
        fast = L[fast]
        slow = L[slow]
        if fast == slow:
            return fast

if __name__ == '__main__':
    tL = [1,2,3,4,5,6,7,8,9,10,12,12,13,14,15,15]
    shuffle(tL)
    print(tL)
    print(findDup(tL))