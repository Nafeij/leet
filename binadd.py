def solution(a, b):
    if len(b) > len(a):
        return solution(b,a)
    b = b.zfill(len(a))
    carry, res = 0, ''
    for i in range(len(a)-1,-1,-1):
        val = int(a[i]) + int(b[i]) + carry
        res = str(val % 2) + res
        carry = val > 1
    if carry:
        res = '1' + res
    return res

if __name__ == '__main__':
    print(solution('1','1'))