class Solution:

    '''
    Generalized algorithm to find the kth element of two sorted arrays
    '''
    def kth(self, a, b, k):
        if not a: return b[k]
        if not b: return a[k]
        mida, midb = len(a) // 2, len(b) // 2
        if mida + midb < k:
            if a[mida] > b[midb]:
                return self.kth(a, b[midb + 1:], k - midb - 1)
            else:
                return self.kth(a[mida + 1:], b, k - mida - 1)
        else:
            if a[mida] > b[midb]:
                return self.kth(a[:mida], b, k)
            else:
                return self.kth(a, b[:midb], k)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([4, 5, 6, 7, 8], [3, 10, 11]))
