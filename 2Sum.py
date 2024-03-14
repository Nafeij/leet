
def two_sum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], i]
        d[n] = i
    return []

def two_sum_count(nums: list[int], target: int) -> int:
    d = {}
    count = 0
    for n in nums:
        if target - n in d:
            count += d[target - n]
        d[n] = d.get(n, 0) + 1
    return count

if __name__ == '__main__':
    print(two_sum([11,2,3,36,7,15], 9))
    print(two_sum_count([1,1,1,1,1], 2))