import streamlit as st
# i have committed saanvi

# ------------------------------
# Set up the page
# ------------------------------
st.set_page_config(
    page_title="Clariti - Cognitive Wellness Dashboard",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------
# Add simple custom colors
# ------------------------------
st.markdown("""
<style>
.main {
    background-color: #f8f9ff;
}
h1 {
    color: #6A0DAD;
}
h2, h3 {
    color: #5A5A5A;
}
.stButton>button {
    background-color: #FFD54F;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# App title and description
# ------------------------------
st.title("🧠 Clariti")
st.subheader("Cognitive Wellness Dashboard")

st.write("""
Welcome to **Clariti**!

Our goal is to help people build healthy daily habits that may reduce the risk
of cognitive decline by tracking important wellness activities.
""")

st.divider()

# ------------------------------
# Exercise tracking section
# ------------------------------
st.header("🏃 Exercise")

steps = st.number_input(
    "How many steps did you take today?",
    min_value=0,
    max_value=50000,
    value=5000
)

exercise_minutes = st.slider(
    "Minutes of exercise",
    0,
    180,
    30
)

st.success(f"You recorded {steps} steps and {exercise_minutes} minutes of exercise.")

st.divider()

# ------------------------------
# Sleep tracking section
# ------------------------------
st.header("😴 Sleep")

sleep_hours = st.slider(
    "Hours of sleep last night",
    0,
    12,
    8
)

if sleep_hours >= 8:
    st.success("Great! You got a healthy amount of sleep.")
elif sleep_hours >= 6:
    st.warning("Not bad. Try to get a little more rest.")
else:
    st.error("You may need more sleep for better brain health.")

st.divider()

# ------------------------------
# Brain games section
# ------------------------------
st.header("🧩 Brain Activity")

games = st.slider(
    "How many brain games did you play today?",
    0,
    10,
    1
)

st.write(f"Brain games completed today: **{games}**")

st.divider()

# ------------------------------
# Doctor referral section
# ------------------------------
st.header("👨‍⚕️ Doctor Referral")

needs_referral = st.checkbox("I would like information about seeing a doctor")

if needs_referral:
    st.info("""
Talk to your primary care doctor if you notice memory changes,
difficulty concentrating, or other concerns.

Early evaluation can be very helpful.
""")

st.divider()

# ------------------------------
# Daily wellness score
# ------------------------------
st.header("⭐ Daily Wellness Score")

score = 0

if steps >= 8000:
    score += 25

if exercise_minutes >= 30:
    score += 25

if sleep_hours >= 8:
    score += 25

if games >= 1:
    score += 25

st.progress(score / 100)

st.metric("Today's Wellness Score", f"{score}/100")

if score == 100:
    st.success("Excellent job! You completed all wellness goals today.")
elif score >= 75:
    st.success("You're doing well! Keep it up.")
elif score >= 50:
    st.warning("Good start! Try to improve one or two habits tomorrow.")
else:
    st.error("Let's work on building healthier daily habits.")

st.divider()

# ------------------------------
# Footer
# ------------------------------
st.caption("Clariti • Helping reduce cognitive decline through healthy daily habits.")