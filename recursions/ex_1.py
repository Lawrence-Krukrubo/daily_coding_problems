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
10. Reverse an array in place without initialising a new array
"""


def reverse_inplace(arr):

    # base case
    if not arr:
        return []

    return [arr[-1]] + reverse_inplace(arr[:-1])


# print(reverse_inplace([2, 3, 4]))

"""
11.
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
12. 
Recursive function to replace each element of a list with product
of every other element without using division operator
"""


def find_product(arr, left=1, i=0):
    if i == len(arr):
        return 1

    curr = arr[i]

    right = find_product(arr, left * curr, i + 1)

    arr[i] = left * right

    return curr * right


A = [2, 3, 4, 5]

find_product(A)

# print the modified list
# print(A)


"""
13. 
Recursive function that returns a list whose elements are the
result of multiplying corresponding elements of 2 lists of same length
"""


def multiply_vectors(vec1, vec2):
    vector = []

    # base case
    if not vec1:
        return vector

    # recursive case
    vector.append(vec1[0] * vec2[0])
    return vector + multiply_vectors(vec1[1:], vec2[1:])


# print(multiply_vectors([2, 3, 4], [2, 3, 4]))


"""
14. 
Building on 13, write a recursive function that returns a list whose elements are the
result of multiplying corresponding elements of arbitrary lists of same length
"""

"""
15. 
Write a recursive function that takes two numbers x, y and returns a number that is
the sum of the product of x raised to power y progressively.
For example if x = 3 and y = 3, then return 3^1 + 3^2 + 3**3 = 3 + 9 + 27 = 39 
"""


def branching_factor(x, y):
    # Base case
    if y == 1:
        return x**y

    # Recursive case
    return x**y + branching_factor(x, y-1)

#print(branching_factor(3, 3))


"""
16.
Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):

    # Base case
    if position in [0, 1]:
        return position

    # Recursive case
    else:
        return get_fib(position-1) + get_fib(position-2)

# print(get_fib(5))

"""
17.
Implement the factorial function recursively
"""


def fact(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n * fact(n-1)

# print(fact(5))


"""
18.
Write a recursive function that counts down a given number and prints 'Done!',
when all numbers are fully counted down.
"""


def count_down(value):
    # Base case
    if value < 1:
        print('Done!')

    # Recursive case
    else:
        print(value)
        count_down(value-1)
    return ''

# print(count_down(5))


"""
19.
Write a recursive function that takes a number and sums up all numbers,
from 1 to that number.
"""


def sum_to_one(n):
    # Base case
    if n == 1:
        return 1

    # Recursive case
    else:
        return n + sum_to_one(n-1)

# print(sum_to_one(10))


"""
20.
Write a recursive function that returns a power set containing 
every single subset of an array.
"""


def power_set(array):
    # 1. Base Case

    if not array:
        return [[]]

    # 2. Recursive Case

    first_element = [array[0]]
    # get the subset with first element for each subset of array
    subset_with_first_element = [first_element + rest for rest in power_set(array[1:])]

    return subset_with_first_element + power_set(array[1:])


uni_list = ['MIT', 'UCLA', 'NYU', 'USW']
uni_power_list = power_set(uni_list)

# for sublist in uni_power_list:
#     print(sublist)





















