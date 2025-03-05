import sys

def main(argc, argv):
    try:
        num = int(argv)
        var = True
    except ValueError:
        var = False
    try:
        assert var
    except AssertionError:
        print("AssertionError: argument is not an integer")
        return
    try:
        assert argc == 1
    except AssertionError:
        print("AssertionError: more than one argument is provided")
        return
    
    if (int(argv) % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
    

if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main(len(sys.argv) - 1, sys.argv.pop(1))
