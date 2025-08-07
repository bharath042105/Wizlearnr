import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Load raw JSON log data (Part A format)
with open("habit_tracker_simulation_5users_30days.json", "r") as f:
    raw_data = json.load(f)

# Build dataframe: user, date, habit, completed
records = []
for entry in raw_data:
    user = entry['user']
    date = entry['date']
    for log in entry['daily_log']:
        records.append({
            "user": user,
            "date": date,
            "habit": log['habit'],
            "completed": int(log['completed'])  # 1 for completed, 0 for skipped
        })

df = pd.DataFrame(records)
df['date'] = pd.to_datetime(df['date'])

# Streamlit UI
st.title("📊 Habit Tracker Dashboard")
users = df['user'].unique()
selected_user = st.selectbox("Select a User", users)

user_df = df[df['user'] == selected_user]

# Pivot to create heatmap data: dates as rows, habits as columns
heatmap_data = user_df.pivot_table(index='date', columns='habit', values='completed')

# Plot heatmap
st.subheader(f"Habit Completion Heatmap - {selected_user}")
fig, ax = plt.subplots(figsize=(10, len(heatmap_data) * 0.4 + 1))
sns.heatmap(
    heatmap_data,
    cmap="YlGn",
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'label': 'Completed (1) / Skipped (0)'},
    ax=ax,
    annot=True,
    fmt=".0f"
)
plt.xlabel("Habit")
plt.ylabel("Date")
st.pyplot(fig)

# Show optional raw stats
st.markdown("### 📋 Optional Stats")
st.dataframe(user_df.groupby("habit")["completed"].agg(['sum', 'count']).rename(columns={'sum': 'Days Completed', 'count': 'Total Days'}))
