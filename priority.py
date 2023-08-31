from math import ceil

def maximumPrioritySum(priority, x, y):
    s = sorted(priority)[-x:]
    n = len(s)
    sum = 0
    for i in range(n-1, -1, -1):
        l = s[i] * ceil((y + i - n + 1) / x)
        sum += l
    return sum

if __name__ == '__main__':
    print(maximumPrioritySum([3,1,2], 2, 7))