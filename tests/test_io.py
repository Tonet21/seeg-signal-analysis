
from pathlib import Path

import mne
import pytest

from seeg_analysis.io import load_recording


def test_load_recording():
    file_path = (
        Path("data/raw")
        / "sub-01"
        / "ses-01"
        / "ieeg"
        / "sub-01_ses-01_task-dcs_ieeg.vhdr"
    )

    raw = load_recording(file_path)

    assert isinstance(raw, mne.io.BaseRaw)
    assert raw.info["sfreq"] == 4096
    assert len(raw.ch_names) == 31
    assert raw.n_times == 131072

def test_load_recording_missing_file():
    with pytest.raises(FileNotFoundError):
        load_recording("nonexistent.vhdr")


def test_load_recording_wrong_extension():
    with pytest.raises(ValueError):
        load_recording("recording.edf")