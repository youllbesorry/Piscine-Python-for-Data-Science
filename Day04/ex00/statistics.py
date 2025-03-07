def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculate and print statistical measures based on input arguments.

    Parameters:
    *args (any): A variable number of integer arguments. All arguments
                 must be integers, otherwise a TypeError is raised.
    **kwargs (any): Keyword arguments specifying which statistics to
                    calculate. Valid values are "mean", "median",
                    "quartile", "std", and "var".

    Raises:
    TypeError: If any of the arguments in *args is not an integer.

    Prints:
    - "mean : <value>" if "mean" is in kwargs and more than one argument
      is provided.
    - "median : <value>" if "median" is in kwargs and more than one
      argument is provided.
    - "quartile : [Q1, Q3]" if "quartile" is in kwargs and more than
      three arguments are provided.
    - "std : <value>" if "std" is in kwargs and more than one argument
      is provided.
    - "var : <value>" if "var" is in kwargs and more than one argument
      is provided.
    - "ERROR" if the conditions for calculating a statistic are not met.

    Note:
    - The function does not return any value; it only prints the results.
    - The function assumes that the input data is suitable for the
      requested statistics.
    """
    for arg in args:
        if (type(arg) is not int):
            raise TypeError("You must only input int")

    sorted_args = sorted(args)
    mid_index = len(sorted_args) // 2

    if ("mean" in kwargs.values()):
        if (len(args) <= 1):
            print("ERROR")
        else:
            print("mean : ", sum(args) / len(args))
    if ("median" in kwargs.values()):
        if (len(args) <= 1):
            print("ERROR")
        elif (len(args) % 2 == 0):
            print("median : ", (sorted_args[mid_index] - 1
                                + sorted_args[mid_index]) / 2)
        else:
            print("median : ", sorted_args[mid_index])
    if ("quartile" in kwargs.values()):
        if (len(args) <= 3):
            print("ERROR")
        else:
            if (mid_index % 2 == 0):
                Q1 = (sorted_args[mid_index // 2] +
                      sorted_args[mid_index // 2]) // 2
            else:
                Q1 = sorted_args[mid_index // 2]

            if ((len(sorted_args) - mid_index) % 2 == 0):
                quart_value = sorted_args[mid_index +
                                          (len(sorted_args) - mid_index)]
                Q3 = ((quart_value - 1) + quart_value) / 2
            else:
                Q3 = sorted_args[mid_index +
                                 (len(sorted_args) - mid_index) // 2]
            print(f"quartile : [{Q1}, {Q3}]")
    if ("std" in kwargs.values()):
        if (len(args) <= 1):
            print("ERROR")
        else:
            mean_value = sum(args) / len(args)
            print("std : ", (sum((x - mean_value) ** 2
                                 for x in args) / len(args)) ** 0.5)
    if ("var" in kwargs.values()):
        if (len(args) <= 1):
            print("ERROR")
        else:
            mean_value = sum(args) / len(args)
            print("var : ", sum((x - mean_value) **
                                2 for x in args) / len(args))
