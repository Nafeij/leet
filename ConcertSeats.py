"""
    See https://leetcode.com/problems/booking-concert-tickets-in-groups/description/
"""


class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
        self.total = 0
        self.mx = 0
        self.m = (start + end) // 2
        self.isLeaf = start == end

    def prop(self):
        if not self.isLeaf:
            self.mx = max(self.left.mx, self.right.mx)
            self.total = self.left.total + self.right.total

    def __str__(self):
        if self.isLeaf:
            return f"[{self.s}]: {self.total}, "
        return str(self.left) + str(self.right)


class SegTree:
    def __init__(self, start, end, val):

        def build(l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.total = node.mx = val
                return node
            node = Node(l, r)
            node.left = build(l, node.m)
            node.right = build(node.m + 1, r)
            node.prop()
            return node

        self.root = build(start, end)

    def update(self, index, val):

        def updateHelper(node):
            if node.isLeaf and node.s == index:
                node.total -= val
                node.mx -= val
                return
            if index <= node.m:
                updateHelper(node.left)
            else:
                updateHelper(node.right)
            node.prop()
            return

        updateHelper(self.root)

    def maxQuery(self, k):

        def queryHelper(node):
            if node.isLeaf:
                return node.e, node.total
            if node.left.mx >= k:
                return queryHelper(node.left)
            return queryHelper(node.right)

        return queryHelper(self.root)

    def sumQuery(self, endRow):

        def queryHelper(node, left, right):
            if left == node.s and node.e == right:
                return node.total
            if right <= node.m:
                return queryHelper(node.left, left, right)
            elif left > node.m:
                return queryHelper(node.right, left, right)
            return queryHelper(node.left, left, node.m) + queryHelper(node.right, node.m + 1, right)

        return queryHelper(self.root, 0, endRow)

    def __str__(self):
        return str(self.root)


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.seg = SegTree(0, n - 1, m)

    def gather(self, k: int, maxRow: int) -> list[int]:
        row, remain = self.seg.maxQuery(k)
        if row > maxRow or remain < k:
            return []
        self.seg.update(row, k)
        return [row, self.m - remain]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.seg.sumQuery(maxRow) < k:
            return False
        else:
            def fill(node, val):
                if val == 0:
                    return
                if node.isLeaf:
                    node.total -= val
                    node.mx -= val
                    return
                if node.left.total >= val:
                    fill(node.left, val)
                else:
                    fill(node.right, val - node.left.total)
                    fill(node.left, node.left.total)
                node.prop()

            fill(self.seg.root, k)
            return True
