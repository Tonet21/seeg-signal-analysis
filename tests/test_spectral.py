
import numpy as np
import pytest

from seeg_analysis.spectral import compute_psd


def test_compute_psd():
    sfreq = 4096
    signal = np.random.default_rng(42).normal(size=20480)

    frequencies, psd = compute_psd(signal, sfreq)

    assert frequencies.shape == (1025,)
    assert psd.shape == (1025,)
    assert frequencies[-1] == 2048


def test_compute_psd_frequency_resolution():
    signal = np.random.default_rng(42).normal(size=20480)

    frequencies, _ = compute_psd(signal, 4096)

    assert frequencies[1] - frequencies[0] == 2


def test_compute_psd_invalid_dimensions():
    signal = np.zeros((2, 1000))

    with pytest.raises(ValueError):
        compute_psd(signal, 4096)


def test_compute_psd_invalid_nperseg():
    signal = np.zeros(1000)

    with pytest.raises(ValueError):
        compute_psd(signal, 4096, nperseg=2048)


def test_compute_psd_invalid_sampling_frequency():
    signal = np.zeros(2048)

    with pytest.raises(ValueError):
        compute_psd(signal, 0)
