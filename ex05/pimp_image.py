import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.array) -> np.array:
    """Invert image colors."""
    try:
        # Invert RGB values
        invertedArray = np.copy(array)
        invertedArray[:, :, :3] = 255 - invertedArray[:, :, :3]
    except (IndexError, TypeError) as error:
        print("Error: Something went wrong with the given array")
        print("- ", error)
        exit()

    plt.imshow(invertedArray)
    plt.title("Inverted")
    plt.axis('off')
    plt.show()
    return invertedArray


def ft_red(array: np.array) -> np.array:
    """Keep the red channel."""
    try:
        # Keep only the red channel
        redMask = np.array([1, 0, 0])
        redArray = np.copy(array)
        redArray = redArray * redMask
    except (IndexError, TypeError) as error:
        print("Error: Something went wrong with the given array")
        print("- ", error)
        exit()

    plt.imshow(redArray)
    plt.title("Red")
    plt.axis('off')
    plt.show()
    return redArray


def ft_green(array: np.array) -> np.array:
    """Keep the green channel."""
    try:
        # Keep only the green channel
        greenArray = np.zeros_like(array)
        greenArray[:, :, 1] = array[:, :, 1]
    except (IndexError, TypeError) as error:
        print("Error: Something went wrong with the given array")
        print("- ", error)
        exit()

    plt.imshow(greenArray)
    plt.title("Green")
    plt.axis('off')
    plt.show()
    return greenArray


def ft_blue(array: np.array) -> np.array:
    """Keep the blue channel."""
    try:
        # Keep only the blue channel
        blueArray = np.zeros_like(array)
        blueArray[:, :, 2] = array[:, :, 2]
    except (IndexError, TypeError) as error:
        print("Error: Something went wrong with the given array")
        print("- ", error)
        exit()

    plt.imshow(blueArray)
    plt.title("Blue")
    plt.axis('off')
    plt.show()
    return blueArray


def ft_grey(array: np.array) -> np.array:
    """Convert an image to grayscale."""
    try:
        redMask = array[:, :, 0] / 3
        greenMask = array[:, :, 1] / 3
        blueMask = array[:, :, 2] / 3
        greyMask = redMask + greenMask + blueMask

        # Build a grayscale RGB image
        greyImage = np \
            .stack([greyMask, greyMask, greyMask], axis=2) \
            .astype(np.uint8)
    except (IndexError, TypeError) as error:
        print("Error: Something went wrong with the given array")
        print("- ", error)
        exit()

    plt.imshow(greyImage)
    plt.title("Grey")
    plt.axis('off')
    plt.show()
    return greyImage
