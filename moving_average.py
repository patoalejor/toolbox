from scipy import signal
from typing import Any

def gauss_average(sig:Any, win_size:int) -> Any:    
    """
    This function applies a Gaussian average to a signal.

    Parameters:
    sig (array-like): The input signal to be averaged.
    win_size (int): The size of the Gaussian window to be used for averaging.

    Returns:
    array-like: The averaged signal after applying the Gaussian window.
    """

    # Create a Gaussian window
    window = signal.windows.gaussian(win_size, std=7)
    # Convolve the signal with the window
    convolved = signal.convolve(sig, window, mode='same') / sum(window)
    return convolved