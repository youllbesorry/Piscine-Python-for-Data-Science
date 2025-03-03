def ft_filter(function, arg):
    if (function is None):
        return (arg)
    newList = [i for i in arg if function(i)]
    return newList
