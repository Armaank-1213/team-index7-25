import random
from pathlib import Path

import streamlit as st

ASSETS_DIR = Path(__file__).parent / "assets"
LOGO_PATH = ASSETS_DIR / "clariti_logo.png"

# ------------------------------
# Page setup
# ------------------------------
st.set_page_config(
    page_title="Clariti - Cognitive Wellness Dashboard",
    page_icon=str(LOGO_PATH) if LOGO_PATH.exists() else "🧠",
    layout="wide"
)

# ------------------------------
# Blue / Purple theme (matches Clariti logo)
# ------------------------------
st.markdown("""
<style>
:root {
    --clariti-navy: #1B2A5B;
    --clariti-indigo: #3A2E8C;
    --clariti-purple: #7B3FE4;
    --clariti-light-purple: #A78BFA;
    --clariti-lavender: #EDE9FE;
    --clariti-bg: #F4F2FF;
}

.stApp {
    background: linear-gradient(180deg, var(--clariti-bg) 0%, #FFFFFF 45%);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--clariti-navy) 0%, var(--clariti-indigo) 55%, var(--clariti-purple) 100%);
}

section[data-testid="stSidebar"] * {
    color: #F4F2FF !important;
}

section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stCheckbox label {
    color: #EDE9FE !important;
}

h1 {
    color: var(--clariti-indigo);
}
h2, h3 {
    color: var(--clariti-purple);
}

.stButton>button {
    background: linear-gradient(90deg, var(--clariti-indigo) 0%, var(--clariti-purple) 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}
.stButton>button:hover {
    background: linear-gradient(90deg, var(--clariti-purple) 0%, var(--clariti-light-purple) 100%);
    color: white;
}

div[data-testid="stMetric"] {
    background-color: var(--clariti-lavender);
    border-radius: 12px;
    padding: 10px;
    border: 1px solid var(--clariti-light-purple);
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--clariti-indigo), var(--clariti-purple));
}

/* Memory game cards */
.mm-card button {
    font-size: 28px !important;
    height: 70px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------
header_col1, header_col2 = st.columns([1, 6])
with header_col1:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=90)
with header_col2:
    st.title("Clariti")
    st.caption("Your beacon for cognitive wellness")

# ------------------------------
# Sidebar navigation
# ------------------------------
if LOGO_PATH.exists():
    st.sidebar.image(str(LOGO_PATH), use_container_width=True)
else:
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
# 🧩 Memory Matching Game
# ------------------------------
MEMORY_EMOJIS = ["🧠", "💡", "🌙", "⭐", "💧", "🏃", "📚", "🧩"]


def new_memory_game(pairs=8):
    symbols = MEMORY_EMOJIS[:pairs] * 2
    random.shuffle(symbols)
    st.session_state.mm_cards = symbols
    st.session_state.mm_matched = set()
    st.session_state.mm_choice_one = None
    st.session_state.mm_choice_two = None
    st.session_state.mm_moves = 0
    st.session_state.mm_won = False


def select_card(idx):
    if st.session_state.mm_choice_one is not None and st.session_state.mm_choice_two is not None:
        return
    if idx in st.session_state.mm_matched or idx == st.session_state.mm_choice_one:
        return
    if st.session_state.mm_choice_one is None:
        st.session_state.mm_choice_one = idx
    elif st.session_state.mm_choice_two is None:
        st.session_state.mm_choice_two = idx


def memory_matching_game():
    if "mm_cards" not in st.session_state:
        new_memory_game()

    # Resolve a completed pair from the previous click
    if st.session_state.mm_choice_one is not None and st.session_state.mm_choice_two is not None:
        c1, c2 = st.session_state.mm_choice_one, st.session_state.mm_choice_two
        st.session_state.mm_moves += 1
        if st.session_state.mm_cards[c1] == st.session_state.mm_cards[c2]:
            st.session_state.mm_matched.add(c1)
            st.session_state.mm_matched.add(c2)
        st.session_state.mm_choice_one = None
        st.session_state.mm_choice_two = None
        if len(st.session_state.mm_matched) == len(st.session_state.mm_cards):
            st.session_state.mm_won = True

    top_col1, top_col2, top_col3 = st.columns([2, 2, 2])
    top_col1.metric("🔁 Moves", st.session_state.mm_moves)
    top_col2.metric("✅ Pairs Found", f"{len(st.session_state.mm_matched) // 2} / {len(st.session_state.mm_cards) // 2}")
    if top_col3.button("🔄 New Game"):
        new_memory_game()
        st.rerun()

    st.write("")

    cols_per_row = 4
    cards = st.session_state.mm_cards
    for row_start in range(0, len(cards), cols_per_row):
        row_cols = st.columns(cols_per_row)
        for offset, idx in enumerate(range(row_start, min(row_start + cols_per_row, len(cards)))):
            revealed = (
                idx in st.session_state.mm_matched
                or idx == st.session_state.mm_choice_one
                or idx == st.session_state.mm_choice_two
            )
            label = cards[idx] if revealed else "❓"
            with row_cols[offset]:
                st.markdown('<div class="mm-card">', unsafe_allow_html=True)
                st.button(
                    label,
                    key=f"mm_card_{idx}",
                    on_click=select_card,
                    args=(idx,),
                    disabled=idx in st.session_state.mm_matched,
                    use_container_width=True,
                )
                st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.mm_won:
        st.balloons()
        st.success(
            f"🎉 You matched every pair in {st.session_state.mm_moves} moves! "
            "Update the '🧩 Brain Games Completed' slider in the sidebar to log it."
        )


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

    st.divider()
    st.subheader("🧠 Memory Match")
    st.caption("Flip two cards at a time and find every matching pair.")
    memory_matching_game()

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
if LOGO_PATH.exists():
    st.image(str(LOGO_PATH), width=50)
st.caption("Clariti — Your beacon for cognitive wellness")
st.caption("Sprint 1 • Cognitive Wellness Dashboard")