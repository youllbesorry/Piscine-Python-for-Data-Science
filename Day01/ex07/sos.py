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
    assert len(sys.argv) == 2, "the arguments are bad"
    assert all(c.isalnum() or c.isspace() for c in sys.argv[1]), "the arguments are bad"
    main(sys.argv[1])