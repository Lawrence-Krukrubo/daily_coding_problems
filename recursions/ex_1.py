# 21st Sept
############################################################################

"""
1. Write a recursive function that returns the sum of all numbers in a list
"""


def calc_sum(arr):
    # base case
    if len(arr) == 1:
        return arr[0]
    # recursive case
    else:
        return arr[0] + calc_sum(arr[1:])

# test
# print(calc_sum([50,40,30,20,10]))


"""
2. Write a recursive func that returns the number of positive 
numbers in an arr
"""


def count_pos(arr):
    # base case
    if len(arr) == 1:
        if arr[0] % 2 == 0:
            return 1
        else:
            return 0
    # recursive case
    if arr[0] % 2 == 0:
        return 1 + count_pos(arr[1:])
    else:
        return count_pos(arr[1:])

# test
# print(count_pos([1,2,3,4,8,6]))


"""
3. Write a recursive func that returns the sum of 
All positive numbers in an arr
"""


def sum_pos_nos(arr):
    # base case
    if len(arr) == 1:
        if arr[0] % 2 == 0:
            return arr[0]
        else:
            return 0
    # recursive case
    if arr[0] % 2 == 0:
        return arr[0] + sum_pos_nos(arr[1:])
    else:
        return sum_pos_nos(arr[1:])


# test
# print(sum_pos_nos([1, 3, 9, 5, 2, 8, 3, 14, 1]))


"""
4. Write a recursive func that takes a string 
And returns the string reversed.
"""


def reverse_str(words):
    # base case
    if not words:
        return ''
    # recursive case
    else:
        return words[-1] + reverse_str(words[:-1])


# Test
# print(reverse_str('Welcome'))


"""
5. Write a recursive func that takes a string 
And returns the count of uppercase letters.
"""


def count_uppercase(words):
    # base case
    if len(words) == 1:
        return int(words[0].isupper())

    # recursive case
    if words[0].isupper():
        return 1 + count_uppercase(words[1:])
    else:
        return count_uppercase(words[1:])


# test
# print(count_uppercase('resume.CSV & income.TXT'))