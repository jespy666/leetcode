from typing import List


def remove_duplicates(nums: List[int]) -> int:
    k: int = len(set(nums))
    index = 0
    while index < len(nums):
        item = nums[index]
        if item in nums[index + 1:]:
            nums.remove(item)
        else:
            index += 1
    return k


nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums1)
print(k)
assert k == 2
k = remove_duplicates(nums2)
assert k == 5
