# 🌌 Analysis of high-redshift galaxies with NIRSpec

## 📌 Overview

This project focuses on the analysis of astronomical spectroscopy data obtained from the **James Webb Space Telescope (JWST)**, specifically using **NIRSpec** observations from the **JADES Data Archive (Cosmic Dawn Center)**.

The work involves building Python-based pipelines for:

* Data preprocessing
* Spectral analysis
* Model fitting

These tools enable the extraction of **physical parameters** and the interpretation of **high-redshift sources**, contributing to the study of galaxy formation and evolution in the early universe.

---

## 📂 Data Source

The spectral data used in this project is publicly available through the JADES archive:

🔗 https://s3.amazonaws.com/msaexp-nirspec/extractions/nirspec_graded.html?&sn50_min=3

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
