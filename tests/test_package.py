from seeg_analysis import (
    load_recording,
    extract_time_window,
    compute_psd,
)


def test_public_functions_are_importable():
    assert callable(load_recording)
    assert callable(extract_time_window)
    assert callable(compute_psd)