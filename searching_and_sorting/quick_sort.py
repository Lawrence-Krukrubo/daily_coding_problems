"""
Quick sort sorts the items in place by comparing the pivot to the items in the arr.

In worst cases, it has a time efficiency of O(n^2)

But quck sort is useful for two main reasons
1. The average and best cases have a time complexity of O(nlog(n))
2. We can configure our sort to run at both halves of the split same time.

Yet, it has a space efficiency of O(1) conastant space

By and large, if you know you're dealing with an almost-sorted array,
Then don't use quick sort atall, cos this leads to worst time complexity.
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
import random


def partition(sort_list, low, high):
    i = (low - 1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[high] = sort_list[high], sort_list[i + 1]
    return (i + 1)


def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi - 1)
        quick_sort(sort_list, pi + 1, high)


lst = [1]
size = int(input("Enter size of the list: "))
for i in range(size):
    elements = int(input("Enter an element"))
    lst.append(elements)
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)