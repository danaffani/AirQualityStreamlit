import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dashboard/main_data.csv')
    except FileNotFoundError:
        df = pd.read_csv('main_data.csv')
    return df

def main():
    st.title("Dashboard Data Analysis")
    
    data = load_data()

    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
    selected_pollutant = st.selectbox("Select a pollutant to visualize:", pollutants)

    if selected_pollutant in data.columns:
        avg_pollutant = data.groupby('station')[selected_pollutant].mean().reset_index()
        plt.figure(figsize=(10, 5))
        sns.barplot(data=avg_pollutant, x='station', y=selected_pollutant, palette='viridis')
        plt.title(f'Average {selected_pollutant} Levels Across Stations')
        plt.xlabel('Station')
        plt.ylabel(f'Average {selected_pollutant} Levels')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        st.pyplot(plt)

    st.title("Pertanyaan 1")
    st.header("Percentage of Time PM2.5 Exceeded WHO Threshold (2015)")
    
    data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
    data_2016 = data[data['datetime'].dt.year == 2015]
    
    threshold = 25  # threshold limit 4th intern target set by WHO
    
    results = data_2016.groupby('station').agg(
        Total_Measurements=('PM2.5', 'count'),
        Exceeding_Count=('PM2.5', lambda x: (x > threshold).sum())
    ).reset_index()
    
    results['Percentage_Exceeding'] = (results['Exceeding_Count'] / results['Total_Measurements']) * 100
    
    plt.figure(figsize=(13, 6))
    sns.barplot(data=results, x='station', y='Percentage_Exceeding', palette='viridis', hue='station')
    plt.title('Percentage of Time PM2.5 Exceeded WHO Threshold (2015)')
    plt.xlabel('Station')
    plt.ylabel('Percentage Exceeding (%)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)

    st.title("Pertanyaan 2")
    st.header("Average PM2.5 Levels by Season Across Stations")
    data['month'] = data['datetime'].dt.month

    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    data['season'] = data['month'].apply(get_season)
    seasonal_pm25 = data.groupby(['station', 'season'])['PM2.5'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=seasonal_pm25, x='season', y='PM2.5', hue='station', palette='viridis')
    plt.title('Average PM2.5 Levels by Season Across Stations')
    plt.xlabel('Season')
    plt.ylabel('Average PM2.5 (µg/m³)')
    plt.xticks(rotation=45)
    plt.legend(title='Station', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)

if __name__ == "__main__":
    main()