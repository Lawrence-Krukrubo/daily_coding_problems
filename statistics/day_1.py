"""
Calculate the mean, median mode from a distribution of numbers.
It takes input from stdin and prints the mean, median, and mode
"""


def mean_median_mode():
    import numpy as np
    from scipy import stats

    numbers = list(map(int, input('Pass a few numbers sep=space').split()))
    print(np.mean(numbers))
    print(np.median(numbers))
    print(int(stats.mode(numbers)[0]))


def weighted_mean():
    nums = [int(i) for i in input('Put numbers with sep=space').split()]
    weight = [int(j) for j in input('Put weight with sep=space').split()]
    weighted = round((sum([x * y for x, y in zip(nums, weight)]) / sum(weight)), 1)
    print(weighted)


def quartiles():
    array = [int(i) for i in input('input array elements sep=space').split()]
    array.sort()

    if len(array) % 2 == 1:
        mid = len(array) // 2
        q2 = array[mid]
        lower = array[:mid]
        upper = array[mid + 1:]
        if len(lower) % 2 == 1:
            q1 = lower[len(lower) // 2]
            q3 = upper[len(upper) // 2]
        else:
            q1 = (lower[len(lower) // 2] + lower[len(lower) // 2 - 1]) // 2
            q3 = (upper[len(upper) // 2] + upper[len(upper) // 2 - 1]) // 2

    else:
        q2 = (array[len(array) // 2] + array[len(array) // 2 - 1]) // 2
        lower = array[:len(array) // 2]
        upper = array[len(array) // 2:]
        if len(lower) % 2 == 1:
            q1 = lower[len(lower) // 2]
            q3 = upper[len(upper) // 2]
        else:
            q1 = (lower[len(lower) // 2] + lower[len(lower) // 2 - 1]) // 2
            q3 = (upper[len(upper) // 2] + upper[len(upper) // 2 - 1]) // 2

    return q1, q2, q3


def inter_quartile_range():
    X = [int(i) for i in input().split()]
    F = [int(j) for j in input().split()]
    array = []

    for i in range(len(X)):
        while F[i] > 0:
            array.append(X[i])
            F[i] -= 1

    array.sort()

    if len(array) % 2 == 1:
        mid = len(array) // 2
        q2 = array[mid]
        lower = array[:mid]
        upper = array[mid + 1:]
        if len(lower) % 2 == 1:
            q1 = lower[len(lower) // 2]
            q3 = upper[len(upper) // 2]
        else:
            q1 = (lower[len(lower) // 2] + lower[len(lower) // 2 - 1]) / 2
            q3 = (upper[len(upper) // 2] + upper[len(upper) // 2 - 1]) / 2

    else:
        q2 = (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
        lower = array[:len(array) // 2]
        upper = array[len(array) // 2:]
        if len(lower) % 2 == 1:
            q1 = lower[len(lower) // 2]
            q3 = upper[len(upper) // 2]
        else:
            q1 = (lower[len(lower) // 2] + lower[len(lower) // 2 - 1]) / 2
            q3 = (upper[len(upper) // 2] + upper[len(upper) // 2 - 1]) / 2

    iqr = float(round(q3 - q1, 1))
    print(iqr)


def standard_dev():
    array = [int(i) for i in input().split()]

    mean_ = sum(array) / len(array)
    diff_squared = sum([(i - mean_) ** 2 for i in array])
    std = (diff_squared / len(array)) ** 0.5

    print(round(std, 1))