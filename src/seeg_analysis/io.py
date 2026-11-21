
from pathlib import Path

import mne


def load_recording(file_path: str | Path) -> mne.io.Raw:
    """
    Load a SEEG recording stored in BrainVision format.

    Parameters
    ----------
    file_path : str or Path
        Path to the BrainVision header file (.vhdr).

    Returns
    -------
    mne.io.Raw
        Loaded continuous recording.
    """
    file_path = Path(file_path)

    if file_path.suffix.lower() != ".vhdr":
        raise ValueError("Expected a BrainVision .vhdr file.")

    if not file_path.exists():
        raise FileNotFoundError(f"Recording not found: {file_path}")

    raw = mne.io.read_raw_brainvision(
        file_path,
        preload=True,
        verbose=False
    )

    return raw
