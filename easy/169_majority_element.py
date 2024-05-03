from typing import List
from collections import Counter


def majority_element(nums: List[int]) -> int:
    counter = Counter(nums)
    nums.sort(key=lambda x: nums.count(x), reverse=True)
    return sorted(nums, key=lambda x: counter[x], reverse=True)[0]


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
nums3 = [6, 5, 5]
m = majority_element(nums1)
assert m == 3
m = majority_element(nums2)
assert m == 2
m = majority_element(nums3)
assert m == 5
