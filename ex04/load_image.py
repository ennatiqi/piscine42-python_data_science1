from PIL import Image
import numpy as np


def zoom(arrImage: np.array) -> np.array:
    """Crop an image."""
    # Slice the array of the image by using Y and X axis
    arrZoomedImage = arrImage[100:500, 450:850, 0:1]
    return arrZoomedImage


def ft_load(path: str) -> np.array:
    """Load and crop an RGB image."""
    try:
        try:
            image = Image.open(path, 'r')
        except FileNotFoundError as fileNotFoundError:
            assert False, fileNotFoundError
        except IsADirectoryError as dirError:
            assert False, dirError
        except Image.UnidentifiedImageError as unidentifiedError:
            assert False, unidentifiedError
        except AttributeError as attributeError:
            assert False, attributeError

        assert image.mode == 'RGB', "image must be coded in RGB"
    except AssertionError as error:
        print("AssertionError:", error)
        exit()

    arrImage = np.array(image)
    arrImage = zoom(arrImage)
    return arrImage
