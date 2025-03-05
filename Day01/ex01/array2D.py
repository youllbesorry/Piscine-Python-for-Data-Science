def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(family: list, start: int, end: int) -> list
    This function slice a 2D array and print his shape
    """
    if (type(family) is not list or type(start) is not int or
            type(end) is not int):
        raise ValueError("Bad type")
    if (not all(len(row) == len(family[0]) for row in family)):
        raise ValueError("All line should be of` the same size")
    print(f"My shape is ({len(family)}, {len(family[0])})")
    new_shape = len(family) - ((start - end)
                               if start != 0 else ((start - end) * -1))
    print(f"My new shape is ({new_shape}, {len(family[0])})")
    return family[start:end]
