# Air Quality Dashboard

## Overview
This project is an interactive dashboard built using Streamlit that visualizes air quality data. The dashboard allows users to explore various pollutants, analyze PM2.5 levels, and understand the relationships between different air quality metrics.

## Features
- Display an overview of the air quality dataset.
- Filter data by specific monitoring stations.
- Calculate and display the average PM2.5 values across all stations.
- Visualize PM2.5 levels over time.
- Explore relationships between PM2.5 and other pollutants (PM10, SO2, NO2, CO, O3).

## Tools Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danaffani/AirQualityStreamlit
   cd AirQualityStreamlit
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that `main_data.csv` file is in the project directory, because this is the data the dashboard based off.
2. Run the Streamlit app:
   ```bash
   streamlit run dashboard/dashboard.py
   ```
3. Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

## Data Source
The dataset used in this project contains air quality measurements, including various pollutants and their concentrations over time. Ensure that the dataset is properly formatted and contains the necessary columns for analysis.

## Acknowledgments
- [Streamlit](https://streamlit.io/) for the framework.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for data visualization.