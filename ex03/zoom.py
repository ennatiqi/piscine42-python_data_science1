from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def zoom(arrImage: np.array) -> np.array:
    """Crop an image."""
    try:
        # Crop the image
        arrZoomedImage = arrImage[100:500, 450:850, 0:1]
        print("New shape after slicing:", np.shape(arrZoomedImage))
    except TypeError as typeError:
        print("TypeError:", typeError)
        exit()

    return arrZoomedImage


def main():
    """Load, crop, and display an image."""
    arrImage = ft_load("animal.jpeg")
    print(arrImage)
    arrZoomedImage = zoom(arrImage)
    print(arrZoomedImage)

    plt.imshow(arrZoomedImage, cmap="grey")
    plt.show()


if __name__ == "__main__":
    main()
