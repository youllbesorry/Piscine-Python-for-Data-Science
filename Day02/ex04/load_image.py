import cv2
import numpy as np


def ft_load(path: str) -> list:
    """
    ft_load(path: str) -> list:
    This function load a image, print and return the shape
    and its pixels content in RGB format.
    """
    if (type(path) is not str):
        raise TypeError("The path must be an str")
    image = cv2.imread(path)

    if (image is None):
        raise ValueError("Image not found or couldn't be open")

    # image_array = np.array(image)

    return (image)
