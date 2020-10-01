import time

"""
Binary search is a searching Algorithm that seeks to find an element,
in any given half of the array.

Binary search splits the array in half on each search.

It has a time complexity of O(log(n))
"""

def binary_search(mini, maxi):
    try:
        assert type(mini) is type(maxi) is int
        assert 0 <= mini < maxi
    except:
        error = 'ERROR: mini must be >= 0 and mini must be < maxi\n' \
                'mini and maxi must be whole numbers'
        return error

    try:
        assert abs(mini - maxi) > 5
    except:
        return 'ERROR: maxi - mini, must be > 5.'

    arr = list(range(min(mini, maxi), max(mini, maxi) + 1))

    print("Hello, please what's your name?")
    name = input()
    name = name.capitalize()
    print()
    time.sleep(1)
    print(f'Welcome to the Number-Guessing Game {name}... These are the rules:-')
    time.sleep(5)
    print(f'1. Guess a number between {arr[0]} and {arr[-1]}, both limits inclusive...')
    time.sleep(5)
    print(f'2. Write the number down secretly...Do not change the number.')
    time.sleep(5)
    print()
    minn = 0
    maxx = len(arr)-1
    strr = ''

    while True:
        mid = (minn + maxx) // 2
        guess = arr[mid]

        print()
        time.sleep(4)
        print(f'Is your secret number {guess}?\n'
              f'Type Y for yes,\n'
              f'Type B if it\'s bigger,\n'
              f'Type S if it\'s smaller...')
        ans = input()

        if minn > maxx:
            strr = f'Game-Over! {name} your secret number is not in the range {arr[0]} to {arr[-1]}.\n' \
                   f'Try again. Pay attention to the rules...'
            break

        if ans in ['y', 'Y']:
            time.sleep(3)
            print()
            strr = f'Game-Over!, {name} your secret number is {guess}. Cheers!'
            return strr
        elif ans in ['b', 'B']:
            print()
            print(f'Hold on a second, {name}')
            minn = mid+1
        elif ans in ['s', 'S']:
            print()
            print(f'Working on it, {name}...')
            maxx = mid - 1
        else:
            print(f'Hold on {name}...Kindly type Y, B or S, after the next question.')

    return strr


if __name__ == '__main__':
    mini = 18
    maxi = 21
    print(f'Calling Binary-Search-Game with limits: {mini} to {maxi}...')
    print()
    print(binary_search(mini, maxi))

else:
    maxi = int(input('Please type a maximum number: Whole-Number'))
    mini = 1
    print(binary_search(mini, maxi))

