import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Client Sentiment Radar", layout="wide")
st.title(" Client Sentiment Radar")

mode = st.radio("Input mode", ["Scrape reviews", "Manual upload"])

if mode == "Scrape reviews":
    url = st.text_input("Enter product review URL")
    pages = st.slider("Pages to scrape", 1, 5, 2)
    if st.button("Fetch Reviews"):
        with st.spinner("Scraping reviews..."):
            res = requests.get(f"{API_URL}/scrape", params={"url": url, "pages": pages})
            data = res.json()
        reviews = data["reviews"]
        st.success(f"Fetched {len(reviews)} reviews")
        st.session_state["reviews"] = reviews

if mode == "Manual upload":
    uploaded = st.file_uploader("Upload CSV or TXT", type=["csv", "txt"])
    if uploaded:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.DataFrame({"feedback": uploaded.read().decode().splitlines()})
        st.session_state["reviews"] = df["feedback"].tolist()

if "reviews" in st.session_state and st.button("Analyze Reviews"):
    with st.spinner("Analyzing feedback..."):
        resp = requests.post(f"{API_URL}/analyze/", json={"feedbacks": st.session_state["reviews"]})
        out = resp.json()

    st.subheader(" Sentiment Stats")
    stats = out["stats"]
    st.bar_chart(pd.Series(stats))

    st.subheader(" Trending Topics")
    topics = pd.DataFrame(out["topics"])
    st.dataframe(topics)

    st.subheader(" AI Summary")
    st.write(out["summary"])

    st.subheader(" Detailed Data")
    df = pd.DataFrame(out["data"])
    st.dataframe(df)
