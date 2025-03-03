import sys
from ft_filter import ft_filter


def filterstring(S: str, N: int) -> list:
    try:
        assert isinstance(S, str), "Wrong S Type"
        assert isinstance(N, int), "Wrong N Type"
        
        SList = S.split()
        isLongEnough = lambda x: len(x) > N
        newList = ft_filter(isLongEnough, SList)
        return (newList)
    except AssertionError as e:
        print(e)
        return



if __name__ == "__main__":
    assert len(sys.argv) == 3, "the arguments are bad"
    print(filterstring(sys.argv[1], int(sys.argv[2])))
