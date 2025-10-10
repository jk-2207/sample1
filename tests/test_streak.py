from streak import longest_positive_streak

def test_empty_input():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    nums = [2, 3, -1, 5, 6, 7, 0, 4]
    assert longest_positive_streak(nums) == 3

def test_with_zeros_and_negatives():
    nums = [1, 0, 1, 1, -2, 3]
    assert longest_positive_streak(nums) == 2

def test_all_positive():
    nums = [1, 1, 1]
    assert longest_positive_streak(nums) == 3

def test_all_non_positive():
    nums = [0, -1, 0, -2]
    assert longest_positive_streak(nums) == 0
