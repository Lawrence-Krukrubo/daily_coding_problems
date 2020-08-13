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


"""
12th Aug:

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace 
character is found. Then, starting from this character, takes an optional initial plus or minus sign 
followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.Assume we are dealing with an environment 
which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""


def myAtoi(str):
    minn = -2**31
    maxx = 2**31 - 1

    try:
        assert str
    except AssertionError:
        return 0

    new_str = ''

    for i in str:
        if new_str:
            if i.isdigit():
                new_str += i
                continue
            else:
                break
        elif i in ['-', '+']:
            new_str += i
            continue
        elif i.isdigit():
            new_str += i
        elif i != ' ':
            return 0

    try:
        new_str = int(new_str)
    except ValueError:
        return 0

    if new_str < minn:
        return minn
    elif new_str > maxx:
        return maxx

    return new_str

#print(myAtoi(" b11228552307"))


"""
13th Aug
You are given a list of integers weights representing peoples' weights 
and an integer limit representing the weight limit of one rocket ship.
Each rocketship can take at most two people.
Return the minimum number of rocket ships it would take to rescue everyone to Mars.

Constraints

Length of weights is at most 5000.
Example 1
Input

weights = [200, 300, 200]
limit = 400
Output

2
Explanation:
It would take one rocket ship to take the two people whose weights are 200, 
and another to take the person whose weight is 300.
"""


def solve(weights, limit):

    try:
        assert weights
    except AssertionError:
        return 0

    ships = 0

    weights = sorted(weights, reverse=True)
    counter = 0

    for i in weights:
        counter += 1
        if i >= limit:
            ships += 1
            continue
        elif weights.index(i) == len(weights)-1:
            if i < limit:
                ships += 1
            break

        is_lower = False
        for j in weights[counter:]:
            if i + j <= limit:
                is_lower = True
                ships += 1
                weights.pop(weights.index(j))
                break

        if not is_lower:
            ships += 1

    return ships

print(solve([200,300, 200], 400))







