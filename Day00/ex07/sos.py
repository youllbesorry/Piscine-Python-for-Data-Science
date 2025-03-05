"""It's a morse code generator,nothing less and nothing more"""
import sys


def main(argv: list[str]):
    MORSE_CODE = {
        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
        '0': '----- ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        ' ': '/ '
    }
    result = ""
    for str in argv:
        for c in str.upper():
            if c in MORSE_CODE:
                result += MORSE_CODE[c]
    print(result.strip())
    return


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()
    try:
        assert all(c.isalnum() or c.isspace()
                   for c in sys.argv[1])
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()
    main(sys.argv[1])
