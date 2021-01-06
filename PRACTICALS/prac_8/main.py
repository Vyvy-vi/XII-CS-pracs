from perfect import generate_factors, is_prime_no, is_perfect_no

def main():
    OPTIONS = [
            "1- Get factors of number",
            "2- Check if a number is prime",
            "3- Check if a number is a perfect no.",
            "4- Check if a number is prime and get factors for that no.",
            "5- Check if a number is a pefect no. and get factors for that no.",
            "6- Quit this program"
            ]
    WELCOME_MSG = "\nHello, welcome to pratical #8:\n\
Menu driven program for getting list of factors,\n\
checking if a number is prime,\n\
and to check if a number is a perfect no.\n\n"
    try:
        print(WELCOME_MSG + '\n'.join(OPTIONS) + '\n')
        choice = int(input('Enter action of your choice: '))
        if choice == 6:
            print('Bye...!')
            return
        else:
            num = int(input('Enter number: '))
        truth_eval = lambda x: 'a' if x(num) else 'not a'

        if choice == 1:
            print(f'The factors of {num} are:\n{generate_factors(num)}')
        elif choice == 2:
            print(f'The no. {num} is {truth_eval(is_prime_no)} prime no.')
        elif choice == 3:
            print(f'the no. {num} is {truth_eval(is_perfect_no)} perfect no.')
        elif choice == 4:
            print(f'The no. {num} is {truth_eval(is_prime_no)} prime no.')
            print(f'The factors of {num} are:\n{generate_factors(num)}')
        elif choice == 5:
            print(f'The factors of {num} are:\n{generate_factors(num)}')
            print(f'The no. {num} is {truth_eval(is_perfect_no)} perfect no.')
        else:
            print("That doesn't seem to be a valid option.\nPlease try again...")
        retry()
    except Exception as e:
        print(f'The factors of {num} are:\n{generate_factors(num)}')
        print(f'An error occured: {e}\nPlease try again...')
        retry()

def retry():
    to_reuse = str(input('Would you like to reuse this program? [Y/n]: '))
    if to_reuse == 'n':
        print('Bye...!')
        return
    else:
        main()
main()
