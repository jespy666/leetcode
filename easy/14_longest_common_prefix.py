from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    pass


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = []

k = longest_common_prefix(strs1)
assert k == 'fl'
k = longest_common_prefix(strs2)
assert k == ''
k = longest_common_prefix(strs3)
assert k == ''
