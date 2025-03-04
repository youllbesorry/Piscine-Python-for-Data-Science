from load_image import ft_load

try:
    ft_load("landscape.jpg")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
