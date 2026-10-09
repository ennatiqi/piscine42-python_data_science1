from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def transpose(arrImage: np.array) -> np.array:
    """Transpose an image."""
    try:
        # Remove the color dimension
        arrImage = arrImage[:, :, 0]
        arrTransposed = np.copy(arrImage)

        # Move each pixel to its transposed position
        width = 0
        height = 0
        for x in arrImage:
            for y in x:
                arrTransposed[height][width] = y
                height += 1

            height = 0
            width += 1
    except TypeError as typeError:
        print("TypeError:", typeError)
        exit()

    return arrTransposed


def main():
    """Load, transpose, and display an image."""
    arrImage = ft_load("animal.jpeg")
    print("The shape of image is:", np.shape(arrImage))
    print(arrImage)
    arrTransposedImage = transpose(arrImage)
    print("New shape after Transpose:", np.shape(arrTransposedImage))
    print(arrTransposedImage)

    plt.imshow(arrTransposedImage, cmap="grey")
    plt.show()


if __name__ == "__main__":
    main()
