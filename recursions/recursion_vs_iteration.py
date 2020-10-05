"""
RECURSION VS. ITERATION - CODING THROWDOWN
Rules of the Throwdown

This lesson will provide a series of algorithms and an iterative or recursive implementation.
Anything we write iteratively, we can also write recursively, and vice versa. Often, the difference
is substituting a loop for recursive calls.

"""

# 1. Factorial
####################
# runtime: Linear - O(N)


def factorial_rec(n):
    if n < 0:
        ValueError("Inputs 0 or greater only")
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


# runtime: Linear - O(N)
def factorial_ite(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i

    return fact


# 2. Fibonacci
####################
# runtime: Exponential - O(2^N)

def fibonacci_rec(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_ite(n):
    fib_list = [0, 1]
    if n < 0:
        raise ValueError("Input 0 or greater only!")
    elif n in fib_list:
        return n

    for i in range(2, n+1):
        x = fib_list[i-1]
        y = fib_list[i-2]
        fib_list.append(x+y)

    return fib_list[-1]


# 3. Sum-digits
####################
# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
    if n < 0:
        ValueError("Inputs 0 or greater only!")
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result + n


def sum_digits_rec(n):
    # Base Case
    if not n:
        return 0

    # Recursive case
    result = 0
    result += n % 10

    return result + sum_digits(n//10)


# 4. Find minimum
####################
# linear runtime, or O(N), where N is the number of elements in the list.
def find_min(my_list):
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min


def find_min_rec(my_list, mini=None):

    # Base Case
    if not my_list:
        return mini

    # Recursive Case
    x = my_list[0]
    if mini is None or x < mini:
        mini = x

    return find_min_rec(my_list[1:], mini)


# 5. Palindrome
####################
# Linear - O(N)
def is_palindrome(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
    for index in range(0, middle_index):
        opposite_character_index = string_length - index - 1
        if my_string[index] != my_string[opposite_character_index]:
            return False
    return True


def is_palindrome_rec(string, first=None, last=None):
    # Base Case
    if first is None and last is None:
        first, last = [], []
    if len(string) <= 1:
        return first == last

    # Recursive Case
    first.append(string[0])
    last.append(string[-1])

    return is_palindrome_rec(string[1:-1], first, last)


# 6. multiplication
####################
# Linear - O(N)
def multiplication(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result


def multiplication_rec(num1, num2, base=0):

    # Base Case
    if num2 < 1:
        return base

    # Recursive Case
    base += num1
    return multiplication_rec(num1, num2-1, base)


print(multiplication_rec(3,7))











