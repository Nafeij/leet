a = [1,2,3,4,5,6]
n = len(a)
s = [-1] * n * 4
def build2(id=1, l=0, r=None):
    if r is None:
        r = n
    if r - l < 2:
        s[id] = a[l]
        return
    mid = ((l+r)<<2)//5
    build2(id<<1, l, mid)
    build2(id<<1|1, mid, r)
    s[id] = s[id<<1] + s[id<<1|1]

build2()