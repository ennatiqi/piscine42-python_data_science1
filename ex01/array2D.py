import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shapes and return a sliced list."""
    try:
        arrFamily = np.array(family)
        assert arrFamily.dtype == 'float64' or arrFamily.dtype == 'int', \
            "lists must contain only int and float elements"

        print("My shape is:", np.shape(arrFamily))

        arrFamily = arrFamily[start:end]
        print("My new shape is:", np.shape(arrFamily))
    except AssertionError as error:
        print("AssertionError:", error)
        exit()
    except TypeError as error:
        print("TypeError:", error)
        exit()

    return arrFamily.tolist()
