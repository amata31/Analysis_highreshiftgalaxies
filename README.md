# 🌌 Analysis of high-redshift galaxies with NIRSpec

## 📌 Overview

This project focuses on the analysis of astronomical spectroscopy data obtained from the **James Webb Space Telescope (JWST)**, specifically using **NIRSpec** observations from the ** Data Archive of the Cosmic Dawn Center**.

The work involves building Python-based pipelines for:

* Data preprocessing
* Spectral analysis
* Model fitting

These tools enable the extraction of **physical parameters** and the interpretation of **high-redshift sources**, contributing to the study of galaxy formation and evolution in the early universe.

---

## 📂 Data Source

The spectral data used in this project is publicly available through the DJA archive:

🔗 https://s3.amazonaws.com/msaexp-nirspec/extractions/nirspec_graded.html?&sn50_min=3

Note: The workflow was not fully automated, as visual inspection was required due to the high variability and complexity of the objects in the dataset.
---

## ⚙️ Features

* 🔧 Automated preprocessing of JWST/NIRSpec spectra
* 📊 Spectral line identification and analysis
* 📈 Model fitting for astrophysical parameter estimation
* 🌠 Focus on high-redshift 5<z<7 (early universe) sources
* 🧪 Modular and reproducible Python pipelines

---

## 🧠 Methodology

The analysis combines observational data with theoretical modeling. In particular:

* Spectral profiles are modeled using **Voigt functions**
* Efficient approximations are implemented for performance and stability
* Special attention is given to **Lyman-α line modeling**, critical for high-redshift studies

---

## 📚 Reference

For the analytic approximation of the Voigt-Hjerting function used in Lyman-α modeling, this project follows:

> Tepper García, T. (2006). *Voigt profile fitting to quasar absorption lines: an analytic approximation to the Voigt-Hjerting function: A new method to compute Voigt profiles.*
> Monthly Notices of the Royal Astronomical Society, 369(4), 2025–2035.
> doi: 10.1111/j.1365-2966.2006.10450.x
> http://dx.doi.org/10.1111/j.1365-2966.2006.10450.x

---

## 🚀 Technologies

* Python
* NumPy / SciPy
* Astropy
* Matplotlib
* Custom spectral analysis tools

---

## 🎯 Goals

* Extract reliable physical parameters from JWST spectra
* Improve efficiency of spectral modeling pipelines
* Contribute to the understanding of early galaxy formation

---
## 📓 Notebooks

### 1. Emission Line Fitting & Star Formation Rate (SFR)

This notebook focuses on fitting emission lines and estimating the **Star Formation Rate (SFR)** using the **Hα line**:

* Gaussian fitting of emission lines (e.g., Hα)
* Flux extraction and calibration
* Conversion of Hα luminosity into SFR using standard relations

```bash
fitting.py
```

---

### 2. Neutral Hydrogen (HI) & Lyman-α Modeling

This notebook performs fitting of **neutral hydrogen absorption** using Lyman-α profiles:

* Voigt profile fitting to absorption lines
* Implementation of the **Tepper-García approximation** for efficient computation
* Estimation of HI column density and physical parameters

```bash
notebooks/02_lya_hi_fitting.ipynb
```

---

### 3. BPT Diagrams (Galaxy Classification)

This notebook generates **BPT diagnostic diagrams** to classify galaxies:

* Emission line ratio calculations (e.g., [OIII]/Hβ, [NII]/Hα)
* Star-forming vs AGN classification
* Visualization of diagnostic regions

```bash
notebooks/03_bpt_diagrams.ipynb
```

---

### 4. Data Visualization

This notebook contains tools for **data exploration and visualization**:

* Spectral plotting with Matplotlib
* Line highlighting and annotations
* Multi-panel figures for professional-quality plots

```bash
notebooks/04_visualization_matplotlib.ipynb
```
