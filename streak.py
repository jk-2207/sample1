from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Returns the length of the longest run of consecutive positive (>0) values.
    Empty list returns 0.
    Non-positive numbers (<=0) reset the count.
    """
    longest = 0
    current = 0

    for n in nums:
        if n > 0:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0

    return longest
