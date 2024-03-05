import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
df = pd.read_csv("hour.csv")

# Menampilkan judul dashboard
st.title("Dashboard Bike Sharing Dataset")

# Menampilkan statistik deskriptif
st.write(df.describe())

# Grafik perbandingan cnt dengan workingday
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="workingday", y="cnt", data=df, ax=ax)
ax.set_xlabel("Hari Kerja (0: Liburan, 1: Hari Kerja)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Grafik perbandingan cnt dengan weekday
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weekday", y="cnt", data=df, ax=ax)
ax.set_xlabel("Hari")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Grafik perbandingan cnt dengan season
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="cnt", data=df, ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)


# Sidebar untuk filter data
st.sidebar.header("Filter Data")

# Filter jam
jam_awal, jam_akhir = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, value=(0, 23))

# Filter hari kerja
hari_kerja = st.sidebar.checkbox("Tampilkan Hanya Hari Kerja")

# Filter musim
musim = st.sidebar.selectbox("Pilih Musim:", ["Spring", "Summer", "Fall", "Winter"])

# Memfilter data berdasarkan pilihan pengguna
df_filtered = df.query(
    f"hr >= {jam_awal} and hr <= {jam_akhir}"
    + (f" and workingday == 1" if hari_kerja else "")
    + (f" and season == '{musim}'" if musim != "All" else "")
)

# Menampilkan data yang telah difilter
st.write(df_filtered)
