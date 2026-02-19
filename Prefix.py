from typing import Callable


def prefix_sum(nums: list[int]) -> Callable[[int, int], int]:
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n)
    def sumRange(i: int, j: int) -> int:
        return prefix[j + 1] - prefix[i]
    return sumRange

def prefix_parity(nums: list[int]) -> Callable[[int, int], int]:
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n % 2)
    def sumRange(i: int, j: int) -> int:
        return prefix[j + 1] - prefix[i]
    return sumRange

def prefix(nums: list[int], acc: Callable[[int, int], int]) \
    -> Callable[[int, int], int]:
    prefix = [0]
    for n in nums:
        prefix.append(acc(prefix[-1],n))
    def sumRange(i: int, j: int) -> int:
        return prefix[j + 1] - prefix[i]
    return sumRange

if __name__ == '__main__':

    s = prefix_sum([1,2,3,4,5,6,7,8,9,10])
    print(s(0, 5))
    print(s(2, 7))
    print(s(0, 9))

    p = prefix_parity([1,2,3,4,5,6,7,8,9,10])
    print(p(0, 5))
    print(p(2, 7))
    print(p(0, 9))

    m = prefix([1,2,3,4,5,6,7,8,9,10], lambda x, y: (x + 1) * y)
    print(m(0, 5))
    print(m(2, 7))
    print(m(0, 9))