"""
Merge sort is a divide-and-conquer Algorithm.
It divides the array into two and sorts each part individually,
Then it compares each in one part to all the elements in the other part,
and puts the smaller element in a new array.
This is done repeatedly for all elements.

Merge sort has a time complexity of O(nlog(n))
And a space complexity of O(n)
"""


def merge_sort(array):
    returned = []
    if len(array) == 1:
        return array
    half = len(array) // 2
    lower = merge_sort(array[:half])
    upper = merge_sort(array[half:])
    lower_len = len(lower)
    upper_len = len(upper)
    i = 0
    j = 0
    while i != lower_len or j != upper_len:
        if i != lower_len and (j == upper_len or lower[i] < upper[j]):
            returned.append(lower[i])
            i += 1
        else:
            returned.append(upper[j])
            j += 1

    return returned


print(merge_sort([2, 1, 3, 0, 9, 8]))