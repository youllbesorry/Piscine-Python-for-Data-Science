"""This programme accepts two arguments: a string(S), and an integer(N).
The program output is a list of words from S that have a length greater than N.
The Words are separated from each other by space characters.
The Strings do not contain any special characters"""
import sys
from ft_filter import ft_filter


def filterstring(S: str, N: int) -> list:
    try:
        assert isinstance(S, str)
        assert isinstance(N, int)

        SList = S.split()
        newList = ft_filter((lambda x: len(x) > N), SList)
        return (newList)
    except AssertionError:
        print("AssertionError: the arguments are bad bis")
        return


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
        print(filterstring(sys.argv[1], int(sys.argv[2])))
    except AssertionError:
        print("AssertionError: the arguments are bad")
