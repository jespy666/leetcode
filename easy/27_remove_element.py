from typing import List
import math


def remove_element(nums: List[int], val: int) -> int:
    k = len(list(filter(lambda x: x != val, nums)))
    while val in nums:
        nums.remove(val)
    return k


nums1 = [3, 2, 2, 3]
val1 = 3
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
nums3 = [math.inf]
val3 = math.inf

k = remove_element(nums1, val1)
assert k == 2
assert len(nums1) == 2
k = remove_element(nums2, val2)
assert k == 5
assert len(nums2) == 5
