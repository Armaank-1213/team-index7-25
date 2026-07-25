import streamlit as st

# ------------------------------
# Page setup
# ------------------------------
st.set_page_config(
    page_title="Clariti - Cognitive Wellness Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #800080;
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

st.title("🧠 Clariti")
st.caption("Helping Reduce Cognitive Decline Through Healthy Daily Habits")

# ------------------------------
# Sidebar navigation
# ------------------------------
st.sidebar.title("🧠 Clariti")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🏃 Exercise",
        "😴 Sleep",
        "🧩 Brain Games",
        "👨‍⚕️ Doctor",
        "ℹ️ About"
    ]
)

# ------------------------------
# Daily inputs (kept in session_state so every page sees the same values)
# ------------------------------
st.sidebar.divider()
st.sidebar.header("📝 Today's Check-In")

steps = st.sidebar.slider("👣 Steps Walked", 0, 20000, 5000, 100)
exercise_minutes = st.sidebar.slider("🏃 Exercise (minutes)", 0, 180, 30, 5)
sleep_hours = st.sidebar.slider("😴 Hours Slept", 0.0, 12.0, 8.0, 0.5)
games = st.sidebar.slider("🧩 Brain Games Completed", 0, 10, 1)
water = st.sidebar.checkbox("💧 I drank enough water today")

# ------------------------------
# Wellness score (calculated once, used everywhere)
# ------------------------------
score = 0
if steps >= 8000:
    score += 20
if exercise_minutes >= 30:
    score += 20
if sleep_hours >= 8:
    score += 20
if games >= 1:
    score += 20
if water:
    score += 20


def feedback_message(score):
    if score == 100:
        st.success("🌟 Perfect! You completed every wellness goal today.")
    elif score >= 80:
        st.success("🎉 Great work! Keep building healthy habits.")
    elif score >= 60:
        st.warning("👍 You're doing well. Try completing one more goal today.")
    else:
        st.error("💜 Small healthy habits each day can make a difference.")


def goal_checklist():
    st.checkbox("Walk 8,000 Steps", value=steps >= 8000, disabled=True)
    st.checkbox("Exercise 30 Minutes", value=exercise_minutes >= 30, disabled=True)
    st.checkbox("Sleep 8 Hours", value=sleep_hours >= 8, disabled=True)
    st.checkbox("Complete a Brain Game", value=games >= 1, disabled=True)
    st.checkbox("Drink Enough Water", value=water, disabled=True)


def doctor_expander():
    with st.expander("👨‍⚕️ Doctor Referral"):
        referral = st.checkbox("I'd like information about seeing a doctor")
        if referral:
            st.info("""
Talk to your primary care doctor if you notice memory changes,
difficulty concentrating, or other concerns.

Early evaluation can be very helpful.
""")


# ------------------------------
# 🏠 Dashboard
# ------------------------------
if page == "🏠 Dashboard":
    st.header("📊 Today's Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👣 Steps", steps)
    col2.metric("😴 Sleep", f"{sleep_hours} hrs")
    col3.metric("🧩 Games", games)
    col4.metric("⭐ Score", f"{score}/100")

    st.progress(score / 100)

    st.divider()
    st.header("✅ Today's Goals")
    goal_checklist()

    st.divider()
    st.header("💬 Personal Feedback")
    feedback_message(score)

    st.info(
        "🧠 **Brain Health Tip:** Regular exercise, quality sleep, and mentally "
        "stimulating activities can help support long-term cognitive health."
    )

    st.divider()
    doctor_expander()

# ------------------------------
# 🏃 Exercise
# ------------------------------
elif page == "🏃 Exercise":
    st.header("🏃 Exercise")

    col1, col2 = st.columns(2)
    col1.metric("👣 Steps", steps)
    col2.metric("🏃 Minutes Exercised", exercise_minutes)

    st.checkbox("Walk 8,000 Steps", value=steps >= 8000, disabled=True)
    st.checkbox("Exercise 30 Minutes", value=exercise_minutes >= 30, disabled=True)

    st.info(
        "🧠 **Tip:** Walking for 20–30 minutes every day may help improve memory, "
        "support healthy blood flow to the brain, and reduce the risk of cognitive decline."
    )

# ------------------------------
# 😴 Sleep
# ------------------------------
elif page == "😴 Sleep":
    st.header("😴 Sleep")

    st.metric("😴 Hours Slept", f"{sleep_hours} hrs")
    st.checkbox("Sleep 8 Hours", value=sleep_hours >= 8, disabled=True)

    st.info(
        "🧠 **Tip:** Consistent, quality sleep helps the brain clear waste products "
        "and consolidate memories from the day."
    )

# ------------------------------
# 🧩 Brain Games
# ------------------------------
elif page == "🧩 Brain Games":
    st.header("🧩 Brain Games")

    st.metric("🧩 Games Completed", games)
    st.checkbox("Complete a Brain Game", value=games >= 1, disabled=True)

    st.info(
        "🧠 **Tip:** Mentally stimulating activities like puzzles, memory games, "
        "and reading may help keep your brain sharp over time."
    )

# ------------------------------
# 👨‍⚕️ Doctor
# ------------------------------
elif page == "👨‍⚕️ Doctor":
    st.header("👨‍⚕️ Doctor Referral")
    doctor_expander()

# ------------------------------
# ℹ️ About
# ------------------------------
elif page == "ℹ️ About":
    st.header("ℹ️ About Clariti")
    st.write(
        "Clariti is a cognitive wellness dashboard designed to help track daily "
        "habits — steps, exercise, sleep, brain games, and hydration — that are "
        "associated with supporting long-term brain health and reducing the risk "
        "of cognitive decline."
    )
    st.caption("Sprint 1 • Cognitive Wellness Dashboard")

# ------------------------------
# Footer
# ------------------------------
st.divider()
st.caption("🧠 Clariti")
st.caption("Helping people reduce cognitive decline through healthy daily habits.")
st.caption("Sprint 1 • Cognitive Wellness Dashboard")