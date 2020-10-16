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

    try:
        assert len(nums) > 1
        nums = sorted(nums, reverse=True)
    except AssertionError:
        return False

    for i in range(len(nums)):
        if i != len(nums)-1:
            if nums[i] + nums[-1] > k:
                continue

            if nums[i] + nums[-1] == k:
                return True

        rem_len = len(nums[i:])
        _25 = int(rem_len * 0.25) + i
        _50 = int(rem_len * 0.5) + i
        _75 = int(rem_len * 0.75) + i

        if nums[i] + nums[_25] <= k:
            for j in range(_25, i, -1):
                if nums[i] + nums[j] == k:
                    return True

        elif nums[i] + nums[_50] <= k:
            for j in range(_50, _25, -1):
                if nums[i] + nums[j] == k:
                    return True

        elif nums[i] + nums[_75] <= k:
            for j in range(_75, _50, -1):
                if nums[i] + nums[j] == k:
                    return True

        else:
            for j in range(len(nums)-1, _75, -1):
                if nums[i] + nums[j] == k:
                    return True

    return False


nums = [49, 314, 264, 980, 900, 714, 433, 969, 647]
k = 1294

# print(sum_2_nums(nums,k))
# ---------------------------------------------------------------------------------------------


""" 
21st Aug
Palindrome Integer

Question 5 of 713
Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?

Example 1
Input

num = 121
Output

True

"""


def palindrome_integer(num):

    n = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return n == rev
# print(palindrome_integer(1235421))
# ---------------------------------------------------------------------------------------------


""" 
22nd Aug
Dogcat
Question 473 of 723
Given the strings text, word0, and word1, return the smallest distance
between any two occurrences of word0 and word1 in text, 
measured in number of words. If either word0 or word1 doesn't appear in text, return -1.

Constraints

word0 and word1 are different.
n ≤ 200,000 where n is the length of text.
Example 1
Input

text = "dog cat hello cat dog dog hello cat world"
word0 = "hello"
word1 = "world"
Output

1
Explanation

There's only one word "cat" in between the hello and world at the end.
"""


def dog_cat(text, word0, word1):

    try:
        texts = text.split(' ')
        ind1 = texts.index(word0)
        ind2 = texts.index(word1)
    except ValueError:
        return -1

    count0, count1 = 0, 0
    x, y = 0, 0
    lists = []
    texts = texts[min(ind1, ind2):]

    for i in range(len(texts)):
        if len(lists) == 2:
            lists.pop(lists.index(max(lists)))
        if texts[i] == word0:
            count0 += 1
            x = i
            if count1:
                lists.append(i - (y+1))
                count1 = 0

        elif texts[i] == word1:
            count1 += 1
            y = i
            if count0:
                lists.append(i - (x+1))
                count0 = 0

    return lists[0]


text = ""
word0 = "streaky"
word1 = "folkfree"

# print(dog_cat(text, word0, word1))


""" 
23rd Aug
BinarySearch.io

Strictly Increasing or Strictly Decreasing
Question 19 of 728
Given an list of numbers, determine whether the list is strictly increasing or strictly decreasing.

Example 1
Input

nums = [1, 2, 3, 4, 5]
Output

True
"""


def is_strictly_decreasing(nums):
    nums = sorted(nums, reverse=True)

    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if i > j:
                break
            else:
                return False

    return True

# nums = [5,2,1,3,4, 7]
# print(is_strictly_decreasing(nums))


def effective_branching_factor(n, d):
    """ If the total number of nodes generated by Astar
    for a particular problem is N and the solution depth
    is d, then b_star is the branching factor that a uniform
    Tree of depth d needs to have in order to contain N+1 nodes.

    b_star is the effective-branching-factor.
    A well designed heuristic should have a b_star close to 1

    :param n: The total nodes
    :param d: The solution depth
    :return: The b_star value, a float
    """
    N = n + 1  # Add 1
    epsilon = 0.005 * N

    def branching_factor(val, depth):
        # Base case
        if depth == 1:
            return val**depth

        # Recursive case
        return val**depth + branching_factor(val, depth-1)

    maxi = d
    mini = 0

    while True:
        b_star = (maxi + mini) / 2
        x = branching_factor(b_star, d)
        if x < N:
            if abs(N - x) < epsilon:
                break
            else:
                mini = b_star
        elif x > N:
            maxi = b_star

    return round(b_star, 4)


#print(effective_branching_factor(52, 5))


"""
Write a python function that confirms if a number is a perfect square.
That is, if the number is a product of 2 equal numbers.
"""


def is_perfect_squ(x):
    """Confirm if x is a perfect square

    :param x: An integer greater than 0
    :return: Boolean (True or False)
    """
    try:
        assert x > 0
        if x * x == x: return True
    except AssertionError:
        return 'ERROR: x cannot be <= 0!'

    # Now we use Binary search to confirm x

    low = 0
    high = x

    while True:
        if high - low <= 1:
            return False
        mid = (high + low) // 2
        if mid**2 > x:
            high = mid
        elif mid**2 < x:
            low = mid
        else:
            return True
print(is_perfect_squ(4225))
