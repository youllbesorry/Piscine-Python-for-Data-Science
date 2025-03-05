from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom():
    """
    Charge une image, effectue un zoom sur une section centrale de l'image,
    et affiche cette section en niveaux de gris.

    Le zoom est effectué en prenant une sous-partie de l'image centrée autour
    du centre de l'image originale, avec une taille de 400x400 pixels.

    La fonction utilise matplotlib pour afficher la section zoomée.
    """
    image = ft_load("./animal.jpeg")
    height, width = image.shape[:2]
    min_center_x, min_center_y = (width // 2) - 200, (height // 2) - 200
    max_center_x, max_center_y = (width // 2) + 200, (height // 2) + 200
    sub_array = image[min_center_y:max_center_y, min_center_x:max_center_x, :1]
    print("New shape after slicing: ",
          sub_array.shape, " or ", sub_array.shape[:2])
    print(sub_array)
    return (sub_array)
    
def main():
    image = zoom()
    rotated_image = []
    for i in range(len(image[0])):
        new_row = []
        for j in range(len(image)):
            new_row.append(image[j][i])
        rotated_image.append(new_row)
    rotated_image = np.array(rotated_image)
    print(rotated_image)
    plt.imshow(rotated_image, cmap='grey')
    plt.show()


if __name__ == "__main__":
    main()