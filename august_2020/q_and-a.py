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
# ---------------------------------------------------------------------------------------------


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

# print(myAtoi(" b11228552307"))
# ---------------------------------------------------------------------------------------------


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

# print(solve([200,300, 200], 400))
# ---------------------------------------------------------------------------------------------


"""
16th Aug 2020
 
You're given a two-dimensional matrix of unique strings representing city blocks, 
and a list of strings blocks to visit. 
Given that you are sitting at block matrix[0][0], 
return the total Manhattan distance required to visit every block in order.

For example, given this matrix:

[["q", "b", "c"],
 ["d", "e", "z"],
 ["g", "h", "i"]]
And blocks = ["h", "b", "c"], return 6 because:

"h" is 2 blocks south and 1 block east.
"b" is 2 blocks north.
"c" is 1 block east.
Example 1
Input

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
blocks = ["h", "b", "c"]
Output

6
"""


def manhattan(matrix, blocks):

    curr_pos = [0, 0]
    cost = 0

    for i in blocks:
        for j in range(len(matrix)):
            if i in matrix[j]:
                y_axis = abs(j - curr_pos[0])
                x_axis = abs(curr_pos[1] - matrix[j].index(i))
                cost += y_axis + x_axis
                curr_pos = [j, matrix[j].index(i)]
                break
    return cost


matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

blocks = ["c", "b", "i"]

# print(manhattan(matrix, blocks))
# ---------------------------------------------------------------------------------------------


"""
17th Aug
BINARY-SEARCH

Sum of Two Numbers
Question 1 of 700
Given a list of numbers nums and a number k, 
return whether any two numbers from the list add up to k. 
You may not use the same element twice.

Note: Numbers can be negative or 0.

Example 1
Input

nums = [35, 8, 18, 3, 22]
k = 11

Output

True
Explanation

8 + 3 = 11

"""


def sum_2_nums(nums, k):

        nums = sorted(nums, reverse=True)

        for i in range(len(nums)):

            if nums[i] + nums[int(len(nums)*0.25)] <= k:
                for j in range(int(len(nums)*0.25), i, -1):
                    if nums[i] + nums[j-1] > k:
                        break
                    elif nums[i] + nums[j-1] == k:
                        return True
                    else:
                        if j == i:
                            break
                        continue

            elif nums[i] + nums[int(len(nums)*0.5)] <= k:
                for j in range(int(len(nums)*0.5), i, -1):
                    if nums[i] + nums[j-1] > k:
                        break
                    elif nums[i] + nums[j-1] == k:
                        return True
                    else:
                        if j == i:
                            break
                        continue

            elif nums[i] + nums[int(len(nums)*0.75)] <= k:
                for j in range(int(len(nums)*0.75), i, -1):
                    if nums[i] + nums[j-1] > k:
                        break
                    elif nums[i] + nums[j-1] == k:
                        return True
                    else:
                        if j == i:
                            break
                        continue

            else:
                for j in range(len(nums), i, -1):
                    if nums[i] + nums[j-1] > k:
                        break
                    elif nums[i] + nums[j-1] == k:
                        return True
                    else:
                        if j == i:
                            break
                        continue

        return False


nums = [-22, 22, -11, 11]
k = 0

print(sum_2_nums(nums, k))

# Wrong Answer- work tomorrow






