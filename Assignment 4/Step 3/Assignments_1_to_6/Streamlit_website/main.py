import streamlit as st
import random
import datetime
import matplotlib.pyplot as plt

# --- List of motivational quotes ---
quotes = [
    "Believe in yourself and all that you are!",
    "Your only limit is your mind!",
    "Push yourself, because no one else will do it for you!",
    "Success is not the key to happiness. Happiness is the key to success!",
    "Hardships often prepare ordinary people for an extraordinary destiny!"
]

# --- Function to get a random quote ---
def get_motivational_quote():
    return random.choice(quotes)

# --- UI Setup ---
st.title("🌟 Daily Motivation & Productivity Tracker")
st.write("Stay motivated and track your productivity every day!")

# --- Display Motivational Quote ---
st.header("📢 Today's Motivation:")
st.success(get_motivational_quote())

# --- To-Do List ---
st.header("📝 To-Do List")
tasks = st.text_area("Enter your tasks (one per line):").split("\n")
completed_tasks = st.multiselect("Mark completed tasks:", tasks)

# --- Productivity Graph ---
st.header("📊 Productivity Progress")

# Generate a simple bar chart based on completed tasks
fig, ax = plt.subplots()
ax.bar(["Completed", "Remaining"], [len(completed_tasks), len(tasks) - len(completed_tasks)], color=['green', 'red'])
ax.set_ylabel("Tasks Count")
st.pyplot(fig)

# --- Mood Tracker ---
st.header("😊 Mood Tracker")
mood = st.radio("How are you feeling today?", ["😀 Happy", "😐 Neutral", "😔 Sad"])
st.write(f"Today's mood: {mood}")

# --- Display Date & Time ---
st.write("📅 Today's Date:", datetime.date.today())

st.write("💡 Stay consistent and make every day productive!")
