import numpy as np


def rescale(input_array: np.ndarray) -> np.ndarray:
    """Rescales an array from 0 to 1.

    Takes an array as input, and returns a corresponding array scaled
    so that 0 corresponds to the minimum and 1 to the maximum value
    of the input array.

    Parameters
    ----------
    input_array : numpy.ndarray
        The input array to be rescaled.

    Returns
    -------
    numpy.ndarray
        The rescaled array.
    
    """
    L = np.min(input_array)
    H = np.max(input_array)
    output_array = (input_array - L) / (H - L)
    return output_array

def rescale_integer(input_value: int, scaling: int) -> float:
    """Scales an integer, assuming input is integers.

    Parameters
    ----------
    input_value : int
        The input integer to be scaled.
    scaling : int
        The scaling factor.

    Returns
    -------
    float
        The scaled value.
    
    """
    return input_value / scaling
