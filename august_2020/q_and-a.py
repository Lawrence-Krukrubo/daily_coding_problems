"""
11th / Aug / 2020

Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def uber_quest(arr):
    """
    This method takes an array of integers and
    returns a new array such that each element at
    index i is the product of all numbers in
    the array, except the number at i

    :param arr: An array of integers
    :return: An array of integers same lemgth as arr
    """
    y = []

    for i in range(len(arr)):
        x = arr[:]
        ini = 1
        x.pop(i)
        for j in x:
            ini *= j
        y.append(ini)

    return y


# print(uber_quest([1,2,3,4,5]))