
import mne
import numpy as np


def extract_time_window(
    raw: mne.io.BaseRaw,
    start_time: float,
    duration: float
) -> np.ndarray:
    """
    Extract a time window from a continuous recording.

    Parameters
    ----------
    raw : mne.io.BaseRaw
        Continuous recording.
    start_time : float
        Start time of the window in seconds.
    duration : float
        Duration of the window in seconds.

    Returns
    -------
    np.ndarray
        Extracted signal data with shape (n_channels, n_samples).
    """
    if start_time < 0:
        raise ValueError("Start time must be non-negative.")

    if duration <= 0:
        raise ValueError("Duration must be positive.")

    sfreq = raw.info["sfreq"]

    start_sample = int(round(start_time * sfreq))
    stop_sample = int(round((start_time + duration) * sfreq))

    if stop_sample > raw.n_times:
        raise ValueError("Requested time window exceeds recording duration.")

    data = raw.get_data(start=start_sample, stop=stop_sample)

    return data
