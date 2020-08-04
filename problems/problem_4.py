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

    increasing_count = 0
    decreasing_count = 0
    maxcount = 0
    result = 0

    for i in range(len(L) - 1):
        if L[i] <= L[i + 1]:
            increasing_count += 1
            if increasing_count > maxcount:
                maxcount = increasing_count
                result = i + 1
        else:
            increasing_count = 0
        if L[i] >= L[i + 1]:
            decreasing_count += 1
            if decreasing_count > maxcount:
                maxcount = decreasing_count
                result = i + 1
        else:
            decreasing_count = 0
    startposition = result - maxcount
    return sum(L[startposition:result + 1])

    '''
    increasing_run = []
    decreasing_run = []
    longest_run = []
    count = 0
    i = count
    increasing_run.append(L[i])
    decreasing_run.append(L[i])
    for i in range(len(L) - 1):
        if L[i] <= L[i + 1]:
            increasing_run.append(L[i + 1])
            count += 1
            if len(increasing_run) > len(longest_run):
                longest_run = increasing_run
            if L[i] >= L[i + 1]:
                increasing_run = []
        if L[i] >= L[i + 1]:
            decreasing_run.append(L[i + 1])
            count += 1
            if len(decreasing_run) > len(longest_run):
                longest_run = decreasing_run
    return longest_run


print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(len([5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]))

'''


print(longest_run([5, 6, 5, 7]))
# print(longest_run([5, 4, 10]))

a = []
b = [5, 6, 7, 8]
print(range(len(b)))
print(len(a))
print(len(b))
print(len(a) + len(b))
