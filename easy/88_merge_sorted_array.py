from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    nums1.extend(nums2)
    nums1.sort()


array1 = [1, 2, 3, 0, 0, 0]
x1 = 3
array2 = [2, 5, 6]
x2 = 3

print(array1)
merge(array1, x1, array2, x2)
print(array1)