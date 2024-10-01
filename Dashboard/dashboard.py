import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
day_df = pd.read_csv('https://raw.githubusercontent.com/hildaarfn/Bike-Sharing-Dicoding/refs/heads/main/Dashboard/day_data.csv')  # Sesuaikan dengan lokasi file
hour_df = pd.read_csv('https://raw.githubusercontent.com/hildaarfn/Bike-Sharing-Dicoding/refs/heads/main/Dashboard/hour_data.csv')  # Sesuaikan dengan lokasi file

# Convert 'dteday' to datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Judul utama
st.title("Bike Sharing Information")

# Pilihan pertanyaan
question = st.selectbox(
    "Pilih pertanyaan untuk dianalisis:",
    [
        "Bagaimana perubahan jumlah pengguna sepeda di setiap musim (season)?",
        "Kapan waktu (jam) penyewaan sepeda tertinggi dalam pada tahun 2011 dan 2012?"
    ]
)

if question == "Bagaimana perubahan jumlah pengguna sepeda di setiap musim (season)?":
    st.header("Demografi Jumlah Penyewaan by Season")
    
    # Analisis jumlah penyewaan berdasarkan season
    seasonal_rentals = day_df.groupby('season')['cnt'].sum().reset_index()
    seasonal_rentals.columns = ['Season', 'Total Rentals']
    
    # Menampilkan hasil
    season_notes = {
        1: "Musim Dingin (Winter)",
        2: "Musim Semi (Spring)",
        3: "Musim Panas (Summer)",
        4: "Musim Gugur (Autumn)"
    }
    for season, total in zip(seasonal_rentals['Season'], seasonal_rentals['Total Rentals']):
        st.write(f"{season_notes[season]}: {total} penyewaan.")
    
    # Membuat visualisasi
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Season', y='Total Rentals', data=seasonal_rentals, palette='viridis')
    plt.title('Total Penyewaan Sepeda Berdasarkan Musim', fontsize=16)
    plt.xlabel('Season', fontsize=14)
    plt.ylabel('Total Penyewaan', fontsize=14)
    plt.xticks(ticks=range(4), labels=[season_notes[i] for i in seasonal_rentals['Season']])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

elif question == "Kapan waktu (jam) penyewaan sepeda tertinggi dalam pada tahun 2011 dan 2012?":
    st.header("Total Waktu (Jam) Penyewaan Sepeda Tertinggi pada 2011-2012")
    
    # Menghitung total penyewaan sepeda per jam dalam kurun waktu 2011-2012
    grouped_df = hour_df.groupby('hr')['cnt'].sum().reset_index()
    
    # Membuat visualisasi per jam
    plt.figure(figsize=(12, 6))
    plt.plot(grouped_df['hr'], grouped_df['cnt'], marker='o')
    plt.title('Total Penyewaan Sepeda dalam Sehari Kurun Waktu 2011-2012')
    plt.xlabel('Jam (hr)')
    plt.ylabel('Total Peminjaman (cnt)')
    plt.xticks(grouped_df['hr'])
    plt.grid(True)
    st.pyplot(plt)

    # Membuat tab untuk tahun 2011 dan 2012
    tab1, tab2 = st.tabs(["2011", "2012"])
    
    with tab1:
        st.header("Data Penyewaan Sepeda Tahun 2011")
        data_2011 = hour_df[hour_df['dteday'].dt.year == 2011]
        grouped_2011 = data_2011.groupby('hr')['cnt'].sum().reset_index()
        
        # Visualisasi untuk tahun 2011
        plt.figure(figsize=(10, 5))
        plt.plot(grouped_2011['hr'], grouped_2011['cnt'], label='2011', marker='o', color='blue')
        plt.title('Total Penyewaan Sepeda per Jam - Tahun 2011')
        plt.xlabel('Jam')
        plt.ylabel('Total Penyewaan')
        plt.xticks(grouped_2011['hr'])
        plt.grid(True)
        st.pyplot(plt)

    with tab2:
        st.header("Data Penyewaan Sepeda Tahun 2012")
        data_2012 = hour_df[hour_df['dteday'].dt.year == 2012]
        grouped_2012 = data_2012.groupby('hr')['cnt'].sum().reset_index()
        
        # Visualisasi untuk tahun 2012
        plt.figure(figsize=(10, 5))
        plt.plot(grouped_2012['hr'], grouped_2012['cnt'], label='2012', marker='o', color='green')
        plt.title('Total Penyewaan Sepeda per Jam - Tahun 2012')
        plt.xlabel('Jam')
        plt.ylabel('Total Penyewaan')
        plt.xticks(grouped_2012['hr'])
        plt.grid(True)
        st.pyplot(plt)
