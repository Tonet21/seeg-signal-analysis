
import numpy as np
from scipy.signal import welch


def compute_psd(
    signal: np.ndarray,
    sfreq: float,
    nperseg: int = 2048
) -> tuple[np.ndarray, np.ndarray]:
    """
    Estimate the power spectral density of a signal using Welch's method.

    Parameters
    ----------
    signal : np.ndarray
        One-dimensional signal array.
    sfreq : float
        Sampling frequency in Hz.
    nperseg : int, optional
        Length of each Welch segment in samples. Default is 2048.

    Returns
    -------
    frequencies : np.ndarray
        Frequency values in Hz.
    psd : np.ndarray
        Power spectral density estimates in V²/Hz.
    """
    if signal.ndim != 1:
        raise ValueError("Signal must be one-dimensional.")

    if sfreq <= 0:
        raise ValueError("Sampling frequency must be positive.")

    if nperseg <= 0:
        raise ValueError("nperseg must be positive.")

    if nperseg > len(signal):
        raise ValueError("nperseg cannot exceed signal length.")

    frequencies, psd = welch(
        signal,
        fs=sfreq,
        nperseg=nperseg
    )

    return frequencies, psd
