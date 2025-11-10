import streamlit as st
import requests
import os

API_BASE = st.secrets.get("api_base", os.environ.get("API_BASE", "http://127.0.0.1:8000"))

st.set_page_config(page_title="AI Mini UI", layout="centered")

st.title("AI Mini — UI (Streamlit)")

st.markdown("""
Select an action, enter input (if needed), and run. The backend supports:
- **math**: evaluate a basic math expression (safe evaluator),
- **date**: return the current date/time,
- **reverse**: use AI to reverse the words in a sentence.
""")

action = st.selectbox("Action", ["math", "date", "reverse"])
payload = ""
if action in ("math", "reverse"):
    payload = st.text_input("Input", value="", placeholder=("e.g. 2+2*3" if action=="math" else "Type a sentence to reverse"))

model = st.text_input("AI model (for reverse)", value="gpt-4omini")
temperature = st.slider("Temperature (for model)", 0.0, 1.0, 0.0)

col1, col2 = st.columns(2)
with col1:
    if st.button("Submit"):
        with st.spinner("Calling backend..."):
            try:
                resp = requests.post(f"{API_BASE}/ai-action/", json={
                    "action": action,
                    "payload": payload,
                    "model": model,
                    "temperature": float(temperature),
                    "max_tokens": 60
                }, timeout=30)
                if resp.status_code == 200:
                    st.success("Success")
                    st.json(resp.json())
                else:
                    st.error(f"Error {resp.status_code}: {resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")

with col2:
    if st.button("Run basic UI tests"):
        test_results = []
        # basic test cases
        test_cases = [
            {"action": "math", "payload": "2+3*4", "expected": 14},
            {"action": "date", "payload": None, "expected": "datetime"},
            {"action": "reverse", "payload": "hello world", "expected": "world hello"},
        ]
        for t in test_cases:
            try:
                payload_value = t["payload"]
                r = requests.post(f"{API_BASE}/ai-action/", json={
                    "action": t["action"],
                    "payload": payload_value,
                    "model": model,
                    "temperature": 0.0,
                    "max_tokens": 60
                }, timeout=20)
                ok = r.status_code == 200
                test_results.append({"case": t, "status_code": r.status_code, "ok": ok, "resp": r.text})
            except Exception as e:
                test_results.append({"case": t, "ok": False, "error": str(e)})
        st.write("Test results")
        st.json(test_results)

st.markdown("---")
st.subheader("Send feedback")
rating = st.slider("Rate the last response", 1, 5, 5)
comment = st.text_area("Comment (optional)")
if st.button("Send feedback"):
    try:
        fb_resp = requests.post(f"{API_BASE}/feedback/", json={
            "action": action,
            "payload": payload,
            "response": "",  # UI could capture last model response and send here
            "rating": rating,
            "comment": comment
        }, timeout=10)
        if fb_resp.status_code == 200:
            st.success("Thanks for the feedback!")
        else:
            st.error(f"Feedback send failed: {fb_resp.text}")
    except Exception as e:
        st.error(f"Feedback request error: {e}")
