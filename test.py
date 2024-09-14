import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data
df = pd.read_csv('cleaned_5250.csv')


# Function to display descriptive statistics
def display_stats(df):
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

# Function to display a scatter plot of orbital period vs. distance
def plot_orbital_period_vs_distance(df):
    st.subheader("Orbital Period vs. Distance")
    fig, ax = plt.subplots()
    sns.scatterplot(x='orbital_radius', y='distance', hue='planet_type', data=df)
    st.pyplot(fig)

# Function to display a histogram of stellar magnitude
def plot_stellar_magnitude_histogram(df):
    st.subheader("Histogram of Stellar Magnitude")
    fig, ax = plt.subplots()
    sns.histplot(x='stellar_magnitude', data=df)
    st.pyplot(fig)

# Function to display a bar chart of exoplanet types
def plot_exoplanet_types_bar_chart(df):
    st.subheader("Exoplanet Types")
    fig, ax = plt.subplots()
    sns.countplot(x='planet_type', data=df)
    st.pyplot(fig)


st.title("Chronicles of Exoplanet Exploration")


# Sidebar for user interaction
st.sidebar.title("Explore Exoplanet Data")

# Select exoplanet type
selected_planet_type = st.sidebar.selectbox(
    "Select Exoplanet Type", 
    df['planet_type'].unique()
)

# Filter the dataframe based on the selected exoplanet type
filtered_df = df[df['planet_type'] == selected_planet_type]


# Display the selected exoplanet type
st.subheader(f"Exoplanets of Type: {selected_planet_type}")
st.dataframe(filtered_df)


# Display descriptive statistics
display_stats(filtered_df)


# Plot the data
plot_orbital_period_vs_distance(filtered_df)
plot_stellar_magnitude_histogram(filtered_df)
plot_exoplanet_types_bar_chart(df)