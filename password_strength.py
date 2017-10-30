import argparse
import passwordmeter


def print_password_strength(password, verbose):
    password_strength, suggestions = passwordmeter.test(password)
    print("Strength of password '{}' is {:d}".format(
                                            password,
                                            int(password_strength * 10),
                                                     )
          )
    if verbose:
        if suggestions.values():
            print("Suggestions:")
            for suggestion in suggestions.values():
                print(suggestion)
        else:
            print("No suggestions")


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('password', help='Password to be evaluated')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Prints suggestions for password.'
                        )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_arguments()
    print_password_strength(args.password, args.verbose)
