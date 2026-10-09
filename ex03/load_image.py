from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an RGB image as a NumPy array."""
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
    print("The shape of image is:", np.shape(arrImage))
    return arrImage
