import streamlit as st
import pandas as pd
from reddit_scraper import fetch_comments
from sentiment_analysis import analyze_sentiment
from visualize import plot_sentiment_distribution, plot_sentiment_scores, generate_wordcloud
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Audience Mood Analyzer", layout="wide")
st.markdown(
    """
    <style>
    .big-font { font-size:26px !important; font-weight:bold; }
    .section { margin-top: 30px; margin-bottom: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🧠 Audience Mood Analyzer")
st.markdown("Analyze real-time Reddit comments and visualize how people feel about your brand or topic. Powered by LLMs & live data.")

# --- Sidebar
st.sidebar.header("🧪 Analyze Subreddit")
subreddit = st.sidebar.text_input("Subreddit name (no r/ needed):", value="marketing")
limit = st.sidebar.slider("Number of comments", 10, 200, 50)

# --- Fetch & Analyze
if st.sidebar.button("🎯 Fetch & Analyze"):
    comments = fetch_comments(subreddit, limit)
    if not comments:
        st.error(f"No comments found or subreddit '{subreddit}' is restricted.")
    else:
        results = []
        for comment in comments:
            sentiment, score = analyze_sentiment(comment)
            results.append({
                "comment": comment,
                "sentiment": sentiment,
                "score": round(score, 3)
            })

        df = pd.DataFrame(results)
        df.to_csv("sentiment_output.csv", index=False)
        st.success(f"Analyzed {len(df)} comments from r/{subreddit} ✅")

        # Generate updated visuals
        plot_sentiment_distribution(df)
        plot_sentiment_scores(df)
        generate_wordcloud(df)

# --- Load data
if os.path.exists("sentiment_output.csv"):
    df = pd.read_csv("sentiment_output.csv")

    # --- Metrics section
    st.markdown("<div class='section big-font'>🔢 Sentiment Breakdown</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Positive 😊", df[df["sentiment"] == "positive"].shape[0])
    col2.metric("Neutral 😐", df[df["sentiment"] == "neutral"].shape[0])
    col3.metric("Negative 😠", df[df["sentiment"] == "negative"].shape[0])

    st.markdown("---")

    # --- Sentiment Distribution Chart
    st.markdown("<div class='section big-font'>📊 Sentiment Distribution</div>", unsafe_allow_html=True)
    st.image("sentiment_distribution.png",  use_container_width=True)

    # --- Score Distribution Chart
    st.markdown("<div class='section big-font'>📈 Score Distribution</div>", unsafe_allow_html=True)
    st.image("sentiment_scores.png",  use_container_width=True)

    # --- Word Cloud
    st.markdown("<div class='section big-font'>☁️ Word Cloud of Comments</div>", unsafe_allow_html=True)
    st.image("wordcloud.png",  use_container_width=True)

    # --- Raw Data
    st.markdown("<div class='section big-font'>📄 Raw Data Preview</div>", unsafe_allow_html=True)
    st.dataframe(df.head(25), use_container_width=True)
else:
    st.warning("Click 'Fetch & Analyze' to load live Reddit data.")

