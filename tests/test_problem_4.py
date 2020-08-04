from problems.problem_4 import longest_run


'''
If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.
'''


def test_longest_run_returns_run_strictly_increasing_list():
    assert longest_run([5, 6, 7, 8]) == 26
