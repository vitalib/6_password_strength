import argparse
import getpass
import passwordmeter


def print_password_strength(password_strength, verbose):
    password_grade, suggestions = password_strength
    password_grade = int(password_grade * 10)
    print("Strength of password is {:d}".format(password_grade))
    if verbose:
        if suggestions.values():
            print("Suggestions:")
            for suggestion in suggestions.values():
                print(suggestion)
        else:
            print("No suggestions")


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Prints suggestions for password.'
                        )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()
    password = getpass.getpass()
    password_strength = passwordmeter.test(password)
    print_password_strength(password_strength, args.verbose)
