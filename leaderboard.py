import streamlit as st
import pandas as pd

# Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/1UJ_KFzG4hqKr8Xo4Iu2E6puthvLqd0PtsBDyWOi51ok/export?format=csv"

# Load data directly from Google Sheets
data = pd.read_csv(sheet_url)

# Sort by points
data = data.sort_values("Points", ascending=False).reset_index(drop=True)

# Display leaderboard
st.title("🏆 Tournament Leaderboard 🏆")
st.table(data)

