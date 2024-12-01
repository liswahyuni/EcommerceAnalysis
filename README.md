# E-commerce Data Analysis Dashboard 📊

This repository contains a data analysis dashboard built using Streamlit that analyzes e-commerce data. The dashboard provides interactive visualizations and insights from the dataset.

## 📁 Project Structure

```
SUBMISSION/
├── .vscode/
├── dashboard/
│   ├── dashboard.py
│   ├── rfm_df.csv
│   ├── segment_analysis.csv
│   └── segment_distribution.csv
├── data/
│   └── E-commerce-public-dataset.zip
├── Proyek_Analisis_Data.ipynb
├── README.md
└── requirements.txt
```

## 🛠️ Setup Instructions

You can set up this project using either Anaconda or a regular Python environment with pip. Choose the method that best suits your needs.

### Option 1: Using Anaconda

1. Create a new conda environment:
```bash
conda create --name main-ds python=3.9
```

2. Activate the conda environment:
```bash
conda activate main-ds
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

### Option 2: Using Regular Python Environment

1. Create a new project directory:
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
```

2. Set up a virtual environment using pipenv:
```bash
pipenv install
pipenv shell
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## 📊 Dataset

The project uses an E-commerce public dataset (`E-commerce-public-dataset.zip`) which is processed using the Jupyter notebook (`Proyek_Analisis_Data.ipynb`) to generate the following analysis files:
- `rfm_df.csv`: RFM (Recency, Frequency, Monetary) analysis data
- `segment_analysis.csv`: Customer segment analysis data
- `segment_distribution.csv`: Distribution of customer segments

## 🚀 Running the Dashboard

After setting up your environment, navigate to the dashboard directory and run:
```bash
cd dashboard
streamlit run dashboard.py
```

The dashboard will open in your default web browser.

## 📦 Dependencies

The main dependencies for this project are listed in `requirements.txt`. Make sure to install them before running the dashboard.

## 📧 Contact

If you have any questions or suggestions, please open an issue in this repository.