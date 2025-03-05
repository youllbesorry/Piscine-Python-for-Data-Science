import numpy as np
import cv2


def ft_invert(array) -> np.array:
    """
    Inverts the colors of the image.
    
    Each pixel in the image is transformed by subtracting its value from 255.
    
    Parameters:
    array (np.array): The input image as a NumPy array.
    
    Returns:
    np.array: The image with inverted colors.
    """
    inverted_array = 255 - array
    cv2.imshow("invert", inverted_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return inverted_array

def ft_red(array) -> np.array:
    """
    Retains only the red component of the image.
    
    The green and blue components of each pixel are set to zero.
    
    Parameters:
    array (np.array): The input image as a NumPy array.
    
    Returns:
    np.array: The image with only the red component.
    """
    red_array = array.copy()
    red_array[:,:,0] = 0
    red_array[:,:,1] = 0
    cv2.imshow("red", red_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return red_array

def ft_green(array) -> np.array:
    """
    Retains only the green component of the image.
    
    The red and blue components of each pixel are set to zero.
    
    Parameters:
    array (np.array): The input image as a NumPy array.
    
    Returns:
    np.array: The image with only the green component.
    """
    green_array = array.copy()
    green_array[:,:,0] = 0
    green_array[:,:,2] = 0
    cv2.imshow("green", green_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return green_array

def ft_blue(array) -> np.array:
    """
    Retains only the blue component of the image.
    
    The red and green components of each pixel are set to zero.
    
    Parameters:
    array (np.array): The input image as a NumPy array.
    
    Returns:
    np.array: The image with only the blue component.
    """
    blue_array = array.copy()
    blue_array[:,:,1] = 0
    blue_array[:,:,2] = 0
    cv2.imshow("blue", blue_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return blue_array

def ft_grey(array) -> np.array:
    """
    Converts the image to grayscale.
    
    Each pixel is transformed by setting all color components to the same value.
    
    Parameters:
    array (np.array): The input image as a NumPy array.
    
    Returns:
    np.array: The image converted to grayscale.
    """
    grey_array = array.copy()
    middle_color = grey_array[:,:,1:2]
    grey_array[:,:,:1] = middle_color
    grey_array[:,:,:3] = middle_color
    cv2.imshow("grey", grey_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return grey_array
