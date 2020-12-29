"""
 * This is a script that displays how to use custom keys to sort a list.
 ? Q- When is this useful?
 * This is useful when you're trying to sort elements of a list
 * based on custom parameters.
 * Like, if you wanted to sort a list, according to the
 * values obtained by some operatio on the element, such as- according to the middle digit or
 * the first digit or by the magnitude of remainders left by elements when divided by some numbers
 ? Q- How does this work?
 * Ans- the sort function lets you use a key parameter.
 * The key parameter is a function, that is called on all the elements of the list
 * and they are sorted according to the returned values and not the original values
 * format- list.sort(key = function_name)
 TODO: Make something like an interface, to separate string-based and number-based output
 TODO: Error Handling
"""


def main():
    ls = eval(input('Enter list: '))
    if ls[0].isdigit():
        print(sort_for_last_digit(ls))
        print(sort_by_largest_remainder(ls))
    else:
        print(sort_for_largest_string_in_list(ls))


def sort_for_last_digit(ls):
    """
     * This function sorts given list, based only on
     * the last digit of the numbers in the list
     * Args: ls ([list]): [list of numbers]
     ! list of strings will give errors
     ? Try this with normal functions instead of lambda
     ? Try to create more detailed search arguments
    """
    ls.sort(key=lambda num: num % 10)
    return ls


def sort_by_largest_remainder(ls):
    """
     * This function sorts given list, based only on
     * the last digit of the numbers in the list
     * Args: ls ([list]): [list of numbers]
     ! list of strings will give errors
     ? Try this with normal functions instead of lambda
     ? Try to create more detailed search arguments
    """
    num = int(input('Enter divisor with which to sort remainders: '))
    ls.sort(key=lambda x: x % num)
    return ls


def sort_for_largest_string_in_list(ls):
    """
     * This function sorts given list, based on
     * which string in list has largest length
     * Args: ls ([list]): [list of strings]
     ! list of numbers will give errors
     ? Try doing this without using len() [HINT: ]
     TODO: Handle errors
    """
    ls.sort(key=len)
    return ls


if __name__ == "__main__":
    main()
