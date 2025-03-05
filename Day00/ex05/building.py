"""A programme that take a single string argument and displays
the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces.
If None or nothing is provided, the user is prompted to provide a string."""
import sys


def main(argc, argv):
    lowerCase = 0
    upperCase = 0
    punctuation = 0
    spaces = 0
    digits = 0
    char = 0
    try:
        assert argc == 1

        for i in argv:
            char += 1
            if (i.islower()):
                lowerCase += 1
            elif (i.isupper()):
                upperCase += 1
            elif (i.isdigit()):
                digits += 1
            elif (i.isspace()):
                spaces += 1
            else:
                if (i in "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"):
                    punctuation += 1
        print(
            f"The text contains {char} characters :\n"
            f"{upperCase} upper letters\n"
            f"{lowerCase} lower letters\n"
            f"{punctuation} punctuation marks\n"
            f"{spaces} spaces\n"
            f"{digits} digits")
    except AssertionError:
        print("AssertionError: more than one argument is provided")


if __name__ == "__main__":
    try:
        if (len(sys.argv) != 1):
            main(len(sys.argv) - 1, sys.argv.pop(1))
        else:
            arg = input("What is the text to count?\n")
            main(1, arg)
    except KeyboardInterrupt:
        pass
