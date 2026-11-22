# SEEG Signal Analysis

An ongoing learning project exploring the analysis of intracranial EEG (stereo-EEG / SEEG) recordings using Python.

## About the project

This project is part of my learning journey into computational neuroscience and neural signal processing. My goal is to develop practical skills in working with intracranial electrophysiological data, understand the principles behind common signal-analysis techniques, and gradually build a reproducible analysis workflow.

I have deliberately started with **one participant and one recording session**. Rather than immediately attempting a large-scale analysis, I wanted to understand each step of the process: exploring the dataset, loading the signals, inspecting their quality, extracting relevant time windows, and analysing their frequency content.

This is an exploratory learning project, not a completed research study. The analyses and methodological choices are provisional and may be revised as I develop my understanding and technical skills. I aim to document not only the results, but also the reasoning, assumptions, and limitations behind each step.

## Dataset

The project uses the publicly available [OpenNeuro ds006519 dataset](https://openneuro.org/datasets/ds006519), *Dataset of intracranial EEG during cortical stimulations evoking negative motor responses*.

The dataset contains intracranial EEG recordings collected during cortical electrical stimulation in patients undergoing stereo-EEG monitoring for drug-resistant epilepsy.

For this initial project, I selected one participant and one recording session to develop and test the analysis workflow.

The dataset is organised according to the Brain Imaging Data Structure (BIDS) specification.

**Dataset citation**

Barborica, A., Ghita, C., Tofan, L., Oane, I., & Mindruta, I. *Dataset of intracranial EEG during cortical stimulations evoking negative motor responses*. OpenNeuro. https://doi.org/10.18112/openneuro.ds006519.v1.0.0

**Licence:** CC0 1.0 Universal (public domain dedication).

The dataset is publicly available and is not included in this repository. Please refer to the original OpenNeuro record for access and licensing information.

## Current work

The project currently includes four Jupyter notebooks:

| Notebook | Contents |
|---|---|
| `01_dataset_exploration.ipynb` | Dataset structure, metadata, channels, electrodes, and stimulation-related annotations. |
| `02_raw_signal_inspection.ipynb` | Loading BrainVision recordings, inspecting signal properties, and visualising raw SEEG signals. |
| `03_signal_quality_assessment.ipynb` | Descriptive signal statistics and visual inspection of selected channels across annotated pre- and post-stimulation epochs. |
| `04_spectral_analysis.ipynb` | Power spectral density estimation using Welch's method and exploratory comparison of pre- and post-stimulation epochs. |

The reusable Python functions are organised in `src/seeg_analysis/` and accompanied by tests in `tests/`.

### Methods and tools

- Python
- MNE-Python
- NumPy and SciPy
- Pandas
- Matplotlib
- Jupyter Notebook
- pytest
- Git and GitHub

## Scope and limitations

The current analysis focuses on a single participant, one session, and one recording. This limited scope is intentional: it allows me to concentrate on understanding the data and the analysis methods before extending the workflow to additional recordings.

The current work is descriptive and exploratory. It does not aim to establish population-level findings, infer causal effects of stimulation, or draw clinical conclusions.

Connectivity analysis, including multivariate approaches such as **generalised partial directed coherence (gPDC)**, is a logical future direction. However, I decided not to include it in this initial version. Reliable connectivity estimation requires careful consideration of model assumptions, data length, model stability, and validation. With only one recording and short annotated epochs, attempting gPDC at this stage would be premature.

I would rather develop a sound understanding of the foundational signal-processing steps before moving towards more complex analyses.

## Future directions

This repository is intended to evolve as I continue learning computational neuroscience and signal processing.

My next step is to work through the [Neuromatch Academy Computational Neuroscience coursebook](https://compneuro.neuromatch.io/tutorials/intro.html), particularly its material on neural signals, signal processing, and linear systems.


## Project structure

```text
seeg-signal-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_raw_signal_inspection.ipynb
│   ├── 03_signal_quality_assessment.ipynb
│   └── 04_spectral_analysis.ipynb
├── src/
│   └── seeg_analysis/
│       ├── __init__.py
│       ├── io.py
│       ├── preprocessing.py
│       └── spectral.py
├── tests/
├── figures/
├── requirements.txt
└── README.md
```

## Getting started

Clone the repository and install the dependencies:

```bash
git clone <repository-url>
cd seeg-signal-analysis
pip install -r requirements.txt
```

Download the dataset from [OpenNeuro](https://openneuro.org/datasets/ds006519) into `data/raw/`. The raw dataset is not included in this repository.

Run the notebooks in numerical order to follow the analysis workflow.

To run the tests:

```bash
PYTHONPATH=src pytest -v
```

Note: the current tests include a recording-loading test and therefore require the dataset to be downloaded.

## A note on learning and reproducibility

This project reflects my current understanding of SEEG signal analysis. I am approaching it as an opportunity to learn by doing: implementing methods, examining their assumptions, checking results, and documenting limitations.

I expect the code and analyses to improve as I gain more experience. Suggestions, corrections, and constructive feedback are welcome.

## References

1. Barborica, A., Ghita, C., Tofan, L., Oane, I., & Mindruta, I. *Dataset of intracranial EEG during cortical stimulations evoking negative motor responses*. OpenNeuro. https://doi.org/10.18112/openneuro.ds006519.v1.0.0
