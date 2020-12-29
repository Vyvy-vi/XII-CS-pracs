# PRACTICAL 7
"""
Write a program to input a number and then call the functions:
    -count(n) which returns the number of digits
    -reverse(n) which returns the reverse of a number
    -hasdigit(n) which returns True if the number has a digit else False.
    -show(n) to show the number as sum of place values.
"""


def reverse(n):
    return str(n)[::-1]


def count(n):
    return len(str(n))


def hasdigit(n):
    check = '01234567890'
    # If this was intended to check for some specific digit,
    # REPLACE check with sting character of that number.
    p = [True for i in str(n) if str(i) in check]
    sets = True if True in p else False
    return sets


def show(n):
    n = str(n)
    ls = ' + '.join([n[i] + '0' * (len(n) - 1 - i) for i in range(len(n))])
    return n + ' = ' + ls

# if you want to see output, call print() on these functions:


def ui():
    num = int(input('Enter no. you want to analyse:'))
    inp = int(input('For getting count press 1\n\
For getting reversed string press 2\n\
For checking for digits press 3\n\
For getting sum of digits press 4\n\
To quit, press 0:\n'))
    if inp == 1:
        print(count(num))
    elif inp == 2:
        print(reverse(num))
    elif inp == 3:
        print(hasdigit(num))
    elif inp == 4:
        print(show(num))
    else:
        return
    ui()


ui()
