import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv')
    return df

def main():
    st.title("Dashboard Data Analysis")
    
    data = load_data()
    
    st.header("Data Overview")
    st.write(data)

    st.header("Basic Statistics")
    st.write(data.describe())

    st.header("Filter Data by Station")
    unique_stations = data['station'].unique()
    selected_station = st.selectbox("Select a Station", unique_stations)
    
    filtered_station_data = data[data['station'] == selected_station]
    st.write(filtered_station_data)

    st.header("Average PM2.5 Value Across Stations")
    avg_pm25 = data.groupby('station')['PM2.5'].mean().reset_index()
    st.write(avg_pm25)

    st.header("PM2.5 Levels Over Time")
    if 'PM2.5' in data.columns and 'day' in data.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=data, x='day', y='PM2.5', hue='station')
        plt.title("PM2.5 Levels Over Time")
        plt.xlabel("Date")
        plt.ylabel("PM2.5 Levels")
        st.pyplot(plt)

    st.header("Relations Between Various Pollutants and PM2.5")
    pollutants = ['PM10', 'SO2', 'NO2', 'CO', 'O3']
    for pollutant in pollutants:
        if pollutant in data.columns:
            plt.figure(figsize=(10, 5))
            sns.scatterplot(data=data, x=pollutant, y='PM2.5', hue='station')
            plt.title(f"Relation Between {pollutant} and PM2.5")
            plt.xlabel(pollutant)
            plt.ylabel("PM2.5 Levels")
            st.pyplot(plt)

if __name__ == "__main__":
    main()