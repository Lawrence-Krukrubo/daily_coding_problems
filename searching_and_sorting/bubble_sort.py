"""
Bubble sort as the name implies is a sorting Algorithm that leads the biggest
Element to float like a bubble to the end of the array.

1. Bubble sort is an in-place sorting Algorithm. This means it solves the problem,
right within the array, without needing any external help or temporary representation

2. Bubble sort has a time complexity of O(n^2).
Since it goes through the array n times and for each n element 2.

3. But in terms of space, Bubble sort is very efficient with a space complexity of O(1) or constant.
Meaning we don't need any extra space or extra arrays to solve a bubble sort problem.

4. The worst case is O(n^2) and the best case is O(n), assuming the list is already sorted.
"""


# 1. Iterative Bubble-Sort
##############################
def bubble_sort(arr):
    lent = len(arr)
    stop = 0
    while True:
        if arr == sorted(arr):
            break
        if stop:
            lent -= 1
        for i in range(lent):
            for j in range(i+1, lent):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
                break

        stop += 1

    return arr


# 1. Recursive Bubble-Sort
##############################
def bubble_sort_rec(arr, i=0, j=1, lent=None):
    # Base Case
    if arr == sorted(arr):
        return arr

    if lent is None:
        lent = len(arr)

    if j == lent:
        i, j = 0, 1
        lent -= 1

    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

    # Recursive Case
    return bubble_sort_rec(arr, i + 1, j + 1, lent)


if __name__ == '__main__':
    #pass
    print(bubble_sort_rec([1, 3, 0, 3, 1, 9, 8, 0]))
