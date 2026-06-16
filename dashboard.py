import pandas as pd
import streamlit as st
import altair as alt

DATA_FILES = {
    "Scaled Clustering Data": "data_clustering.csv",
    "Inverse Clustering Data": "data_clustering_inverse.csv",
}

st.set_page_config(
    page_title="ML Clustering Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Dashboard Clustering dan Klasifikasi")
st.markdown(
    "Gunakan dashboard ini untuk menjelajahi hasil preprocessing, clustering, dan klasifikasi dari dataset transaksi nasabah."
)

dataset_name = st.sidebar.selectbox("Pilih dataset", list(DATA_FILES.keys()))
file_path = DATA_FILES[dataset_name]

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

@st.cache_data
def summary_by_target(df):
    numeric_cols = [col for col in df.columns if df[col].dtype in ["int64", "float64"] and col != "Target"]
    return df.groupby("Target")[numeric_cols].agg(["mean", "min", "max"]).round(2)

try:
    df = load_data(file_path)
except FileNotFoundError:
    st.error(f"File not found: {file_path}. Pastikan file ini ada di folder proyek.")
    st.stop()

st.sidebar.markdown("## Filter Data")

if "Target" in df.columns:
    target_values = sorted(df["Target"].unique().tolist())
    selected_targets = st.sidebar.multiselect("Target", target_values, default=target_values)
else:
    selected_targets = []

if "AgeGroup" in df.columns:
    age_groups = sorted(df["AgeGroup"].unique().tolist())
    selected_age_groups = st.sidebar.multiselect("Age Group", age_groups, default=age_groups)
else:
    selected_age_groups = []

if "TransactionType" in df.columns:
    transaction_types = sorted(df["TransactionType"].unique().tolist())
    selected_types = st.sidebar.multiselect("Transaction Type", transaction_types, default=transaction_types)
else:
    selected_types = []

if "Location" in df.columns:
    locations = sorted(df["Location"].unique().tolist())
    selected_locations = st.sidebar.multiselect("Location", locations, default=locations)
else:
    selected_locations = []

filtered = df.copy()
if "Target" in filtered.columns and selected_targets:
    filtered = filtered[filtered["Target"].isin(selected_targets)]
if "AgeGroup" in filtered.columns and selected_age_groups:
    filtered = filtered[filtered["AgeGroup"].isin(selected_age_groups)]
if "TransactionType" in filtered.columns and selected_types:
    filtered = filtered[filtered["TransactionType"].isin(selected_types)]
if "Location" in filtered.columns and selected_locations:
    filtered = filtered[filtered["Location"].isin(selected_locations)]

st.markdown("### Ringkasan Dataset")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Baris", filtered.shape[0], f"dari {df.shape[0]}")
col2.metric("Fitur", filtered.shape[1])

if "TransactionAmount" in filtered.columns:
    col3.metric("Rata-rata Transaksi", f"{filtered['TransactionAmount'].mean():.2f}")
else:
    col3.metric("Rata-rata Transaksi", "N/A")

if "AccountBalance" in filtered.columns:
    col4.metric("Rata-rata Saldo", f"{filtered['AccountBalance'].mean():.2f}")
else:
    col4.metric("Rata-rata Saldo", "N/A")

st.markdown("### Statistik Dasar")
st.dataframe(filtered.describe(include="all").T)

st.markdown("### Distribusi dan Visualisasi")

chart_col1, chart_col2 = st.columns(2)

if "TransactionAmount" in filtered.columns:
    hist = alt.Chart(filtered).mark_bar().encode(
        alt.X("TransactionAmount", bin=alt.Bin(maxbins=40), title="Transaction Amount"),
        alt.Y("count()", title="Jumlah"),
        tooltip=[alt.Tooltip("count()", title="Jumlah")],
    ).properties(title="Distribusi Transaction Amount", width=600)
    chart_col1.altair_chart(hist, use_container_width=True)

if "AccountBalance" in filtered.columns and "CustomerAge" in filtered.columns:
    scatter = alt.Chart(filtered).mark_circle(size=60, opacity=0.7).encode(
        x=alt.X("CustomerAge", title="Customer Age"),
        y=alt.Y("AccountBalance", title="Account Balance"),
        color=alt.Color("Target:N" if "Target" in filtered.columns else "CustomerOccupation:N", title="Target"),
        tooltip=["CustomerAge", "AccountBalance", "Target"],
    ).properties(title="Customer Age vs Account Balance", width=600)
    chart_col2.altair_chart(scatter, use_container_width=True)

if "TransactionType" in filtered.columns:
    type_counts = filtered["TransactionType"].value_counts().reset_index()
    type_counts.columns = ["TransactionType", "Count"]
    bar = alt.Chart(type_counts).mark_bar().encode(
        x=alt.X("TransactionType:N", sort="-y", title="Transaction Type"),
        y=alt.Y("Count:Q", title="Count"),
        tooltip=["TransactionType", "Count"],
    ).properties(title="Jumlah Transaksi per Tipe", width=600)
    st.altair_chart(bar, use_container_width=True)

if "Target" in filtered.columns:
    st.markdown("### Ringkasan Agregasi per Target")
    agg = summary_by_target(filtered)
    st.dataframe(agg)

with st.expander("Tampilkan Data Mentah"):
    st.dataframe(filtered.reset_index(drop=True))

st.markdown("---")
st.caption("Dashboard dibuat dari file data_clustering.csv dan data_clustering_inverse.csv.")
