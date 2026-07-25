import streamlit as st

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

# ------------------------------
# App title and description
# ------------------------------
st.markdown("<div class='main-title'>🧠 Clariti</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Helping Reduce Cognitive Decline Through Healthy Daily Habits</div>", unsafe_allow_html=True)

st.write("")
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
st.header("📊 Today's Dashboard")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("👣 Steps", "5000")

with col2:
    st.metric("😴 Sleep","8 hrs")

with col3:
    st.metric("🧩 Games","1")

with col4:
    st.metric("⭐ Goal","Healthy")
st.divider()

st.header("✅ Daily Goals")

st.checkbox("Walk 8,000 Steps")

st.checkbox("Exercise 30 Minutes")

st.checkbox("Sleep 8 Hours")

st.checkbox("Play a Brain Game")

st.checkbox("Drink Enough Water")
st.divider()

st.markdown("""
<div class="tip">

### 💡 Brain Health Tip

Walking for 20–30 minutes every day may help improve memory,
support healthy blood flow to the brain, and reduce the risk of cognitive decline.

</div>
""", unsafe_allow_html=True)
st.divider()

st.success("🔥 Every healthy habit today helps protect your brain tomorrow.")

st.balloons()

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
# Daily Wellness Score Dashboard
# ------------------------------

st.divider()

st.header("⭐ Daily Wellness Score")

# Calculate score
score = 0

if steps >= 8000:
    score += 25

if exercise_minutes >= 30:
    score += 25

if sleep_hours >= 8:
    score += 25

if games >= 1:
    score += 25

# Dashboard cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏆 Wellness Score", f"{score}/100")

with col2:
    if score >= 75:
        st.metric("🎯 Goal", "Excellent")
    elif score >= 50:
        st.metric("🎯 Goal", "Good")
    else:
        st.metric("🎯 Goal", "Needs Work")

with col3:
    completed = score // 25
    st.metric("✅ Goals Completed", f"{completed}/4")

st.write("### Overall Progress")
st.progress(score / 100)

# Personalized feedback
if score == 100:
    st.success("🌟 Amazing! You completed every wellness goal today.")
elif score >= 75:
    st.success("🎉 Great job! Your brain health habits are on track.")
elif score >= 50:
    st.warning("👍 Nice work! Try completing one more goal today.")
else:
    st.error("💜 Every healthy choice matters. Let's improve together!")

st.divider()

# Daily Goal Checklist
st.subheader("📋 Today's Checklist")

goal1 = "✅" if steps >= 8000 else "⬜"
goal2 = "✅" if exercise_minutes >= 30 else "⬜"
goal3 = "✅" if sleep_hours >= 8 else "⬜"
goal4 = "✅" if games >= 1 else "⬜"

st.write(f"{goal1} Walk at least **8,000 steps**")
st.write(f"{goal2} Exercise for **30 minutes**")
st.write(f"{goal3} Get **8 hours of sleep**")
st.write(f"{goal4} Complete **1 brain game**")

st.divider()

# Brain Health Tip
st.info(
# ------------------------------
# Doctor referral section
# ------------------------------
    "🧠 **Brain Health Tip:** Regular exercise, quality sleep, and mentally stimulating activities can help support long-term cognitive health."
)

# ------------------------------
# Footer
# ------------------------------
st.divider()

st.caption("🧠 Clariti")

st.caption("Helping people reduce cognitive decline through healthy daily habits.")

st.caption("Sprint 1 • Cognitive Wellness Dashboard")