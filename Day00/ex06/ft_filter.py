"""filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""


def ft_filter(function, arg):
    if (function is None):
        return (arg)
    newList = [i for i in arg if function(i)]
    return newList
