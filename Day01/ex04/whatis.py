import sys

def main(argc, argv):
    try:
        num = int(argv)
        var = True
    except ValueError:
        var = False
    assert var, "argument is not an integer"
    assert argc == 1, "more than one argument is provided"
    
    if (int(argv) % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")
    

if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main(len(sys.argv) - 1, sys.argv.pop(1))
