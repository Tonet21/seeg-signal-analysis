
from pathlib import Path

import numpy as np
import pytest

from seeg_analysis.io import load_recording
from seeg_analysis.preprocessing import extract_time_window


@pytest.fixture
def raw():
    file_path = (
        Path("data/raw")
        / "sub-01"
        / "ses-01"
        / "ieeg"
        / "sub-01_ses-01_task-dcs_ieeg.vhdr"
    )
    return load_recording(file_path)


def test_extract_time_window(raw):
    data = extract_time_window(raw, 6.99823, 5.0)

    assert isinstance(data, np.ndarray)
    assert data.shape == (31, 20480)


def test_extract_time_window_invalid_start(raw):
    with pytest.raises(ValueError):
        extract_time_window(raw, -1, 5)


def test_extract_time_window_invalid_duration(raw):
    with pytest.raises(ValueError):
        extract_time_window(raw, 5, 0)


def test_extract_time_window_exceeds_recording(raw):
    with pytest.raises(ValueError):
        extract_time_window(raw, 30, 5)
