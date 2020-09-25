"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the number of guesses if value is in the list
or return None.
"""


def binary_search(input_array, value):
    """Your code goes here."""
    count = 0

    while len(input_array) >= 1:
        count += 1
        if len(input_array) % 2 == 1:
            guess = input_array[len(input_array) // 2]
        else:
            guess = input_array[(len(input_array) // 2)-1]
        index = input_array.index(guess)
        if guess == value:
            return count
        elif guess < value:
            input_array = input_array[index+1:]
        else:
            input_array = input_array[:index]
    print(f'Worst case guesses were: {count}')
    return None


test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#test_val1 = 25
test_val2 = 7
#print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))