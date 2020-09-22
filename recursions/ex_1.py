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

# 22nd Sept
############################################################################

"""
6. Write a recursive func that takes an array and if a number is negative, 
it adds 1 and for positive numbers, it divides by 2. And returns the new array
"""


def convert_negatives(arr):
    new_array = []

    # base case
    if len(arr) == 1:
        if arr[0] % 2 == 0:
            new_array.append(arr[0]//2)
        else:
            new_array.append(arr[0]+1)
        return new_array

    # recursive case
    if arr[0] % 2 == 0:
        new_array.append(arr[0]//2)
        return new_array + convert_negatives(arr[1:])
    else:
        new_array.append(arr[0]+1)
        return new_array + convert_negatives(arr[1:])


# test
# print(convert_negatives([1, 2, 3, 4, 5, 6]))

"""
7. Write a recursive func that takes an array and returns 
the array with all items reversed
"""


def reverse_array(arr):
    new_array = []
    # base case
    if len(arr) == 1:
        new_array.insert(0, arr[0])
        return new_array

    # recursive case
    else:
        new_array.insert(0, arr[-1])
        return new_array + reverse_array(arr[:-1])


# Test
# print(reverse_array([5, 'Hi!', 4, 'Hey!', 3, 'Hola!', 2, 'Go!']))

"""
8. Write a recursive func that takes an array and returns an array with all items reversed.
If an item is a string, it replaces the item with <str> and if an item is a positive number,
it replaces the item with <pos> and if an item is a negative number, it replaces the item with <neg>
if the array contains sub-arrays like lists, dictionaries, tuples, these should all be replaced with <sub-array>.
"""


def reverse_replace(arr):
    new_arr = []
    # base case
    if len(arr) == 1:
        if type(arr[0]) is str:
            new_arr.insert(0, 'str')
        elif type(arr[0]) is int:
            if arr[0] % 2 == 0:
                new_arr.insert(0, 'pos')
            else:
                new_arr.insert(0, 'neg')
        else:
            new_arr.insert(0, 'sub-array')
        return new_arr

    # recursive case
    if type(arr[-1]) is str:
        new_arr.insert(0, 'str')
        return new_arr + reverse_replace(arr[:-1])
    elif type(arr[-1]) is int:
        if arr[-1] % 2 == 0:
            new_arr.insert(0, 'pos')
        else:
            new_arr.insert(0, 'neg')
        return new_arr + reverse_replace(arr[:-1])
    else:
        new_arr.insert(0, 'sub-array')
        return new_arr + reverse_replace(arr[:-1])


# Test
# print(reverse_replace([1, 2, 4, 3, ()]))

# 23rd Sept
############################################################################

""" 
9. Find all binary strings that can be formed from given wildcard pattern
"""


def print_all_combinations(pattern, i=0):

    if i == len(pattern):
        print(''.join(pattern))
        return

    # if the current character is '?'
    if pattern[i] == '?':
        for ch in "01":

            # replace '?' with 0 and 1
            pattern[i] = ch

            # recur for the remaining pattern
            print_all_combinations(pattern, i + 1)

            # backtrack
            pattern[i] = '?'

    else:
        # if the current character is 0 or 1, ignore it and
        # recur for the remaining pattern
        print_all_combinations(pattern, i + 1)

# print(print_all_combinations(list("1?11?00?1?")))


"""
Reverse an array in place without initialising a new array
"""


def reverse_inplace(arr):

    # base case
    if not arr:
        return []

    return [arr[-1]] + reverse_inplace(arr[:-1])


# print(reverse_inplace([2, 3, 4]))

"""
Reverse an array of integers in place without initialising a new array,
with positive numbers replaced with zero and negative numbers with 1 
"""


def reverse_binary(arr):

    # base case
    if not arr:
        return []

    # recursive case
    if arr[-1] % 2 == 0:
        arr[-1] = 0
    else:
        arr[-1] = 1
    return [arr[-1]] + reverse_binary(arr[:-1])


# print(reverse_binary([2, 3, 4, 6]))

""" 
Recursive function to replace each element of a list with product
of every other element without using division operator
"""


def find_product(arr):
    n = len(arr)



