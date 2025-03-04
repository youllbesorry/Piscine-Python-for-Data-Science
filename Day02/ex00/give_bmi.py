def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    give_bmi(height: list[int | float],
            weight: list[int | float]) -> list[int | float]
    This function calcule the bmi for all the element in each list
    """
    result = []

    try:
        assert all(isinstance(h, (int, float)) for h in height)
        assert all(isinstance(w, (int, float)) for w in weight)
    except AssertionError:
        print("AssertionError : Argument dosen't fit")
        return result
    try:
        assert len(height) == len(weight)
    except AssertionError:
        print("AssertionError : The tow list dosen't have the same size")
        return result
    try:
        for i in range(len(weight)):
            result.append(weight[i] / (height[i] ** 2))
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return result
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    This function check if each element of the list is under or above the limit
    """
    return [False if e > limit else True for e in bmi]
