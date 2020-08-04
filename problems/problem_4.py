def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest_run = 0
    for i in range(len(L)):
        print(i)
        if (i + 1) >= i:
            longest_run += L[i]
        else:
            # break
            return 'Decreasing'
    return longest_run


print(longest_run([1, 2, 3, 4]))
print(longest_run([4, 3, 2, 1]))
print(longest_run([5, 4, 10]))
