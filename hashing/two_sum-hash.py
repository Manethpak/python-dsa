from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, v in enumerate(nums):
        diff = target - v
        if diff in seen:
            return [seen[diff], i]
        seen[v] = i
