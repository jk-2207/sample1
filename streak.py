from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    longest = 0
    current = 0
    for n in nums:
        if n > 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest
