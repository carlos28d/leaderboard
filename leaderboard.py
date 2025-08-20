import streamlit as st
import pandas as pd

# Google Sheet CSV link
sheet_url = st.secrets["CSV_URL"]

# Load data directly from Google Sheets
data = pd.read_csv(sheet_url)

# Sort by points
data = data.sort_values("Points", ascending=False).reset_index(drop=True)
data.index = data.index + 1

# Display leaderboard
st.title("🏆 Tournament Leaderboard 🏆")
st.table(data)

