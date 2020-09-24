import time


def binary_search(num1, num2):
    try:
        assert type(num1) is type(num2) is int
        assert 0 < num1 and num2
    except:
        return 'ERROR: Numbers can only be positive whole numbers > 0.'

    try:
        assert abs(num1 - num2) > 10
    except:
        return 'ERROR: high - low, must be > 10.'

    arr = list(range(min(num1, num2), max(num1, num2) + 1))

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
                   f'Choose only one secret number and Do Not Change it...Try again.'
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
    print('Calling Binary-Search-Game with limits: 1 to 100000...')
    print()
    print(binary_search(1, 100000))

else:
    maxi = int(input('Please type a maximum number: Whole-Number'))
    mini = 1
    print(binary_search(mini, maxi))

