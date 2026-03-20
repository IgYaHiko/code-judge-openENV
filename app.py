import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Coding RL Env", layout="centered")

st.title("🧠 Coding Judge Environment (OpenEnv)")

# Initialize session state
if "problem" not in st.session_state:
    st.session_state.problem = ""
    st.session_state.feedback = ""
    st.session_state.reward = None

# Reset button
if st.button("🔄 Reset Environment"):
    res = requests.post(f"{BASE_URL}/reset").json()
    
    st.session_state.problem = res["observation"]["problem"]
    st.session_state.feedback = res["observation"]["feedback"]
    st.session_state.reward = res["reward"]

# Show problem
if st.session_state.problem:
    st.subheader("📌 Problem")
    st.write(st.session_state.problem)

# Code input
code = st.text_area("💻 Write your function here:", height=150)

# Submit button
if st.button("🚀 Submit Code"):
    if code.strip() == "":
        st.warning("Please write some code first!")
    else:
        res = requests.post(
            f"{BASE_URL}/step",
            json={"code": code}
        ).json()

        st.session_state.feedback = res["observation"]["feedback"]
        st.session_state.reward = res["reward"]

# Show feedback
if st.session_state.feedback:
    st.subheader("📊 Feedback")
    st.write(st.session_state.feedback)

# Show reward
if st.session_state.reward is not None:
    st.subheader("🏆 Reward")
    st.write(st.session_state.reward)