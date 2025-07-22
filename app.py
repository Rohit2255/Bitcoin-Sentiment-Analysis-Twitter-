import streamlit as st
import pandas as pd
import requests
import re
import string
import nltk
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

nltk.download('punkt')

# --------------------------
# Helper Functions
# --------------------------

def clean_tweet(text):
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"@\w+", "", text)     # remove mentions
    text = re.sub(r"#\w+", "", text)     # remove hashtags
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    return text.lower()

def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

def get_tweets(bearer_token, query, max_results=20):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "text,created_at,author_id,lang"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        st.error(f"Error fetching tweets: {response.status_code}")
        st.json(response.json())
        return pd.DataFrame()

    data = response.json().get("data", [])
    if not data:
        st.warning("No tweets found. Try a different keyword or check your token.")
        return pd.DataFrame()

    df = pd.DataFrame(data)
    df['clean_text'] = df['text'].apply(clean_tweet)
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)
    df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0.1 else 'Negative' if x < -0.1 else 'Neutral')
    return df

# --------------------------
# Streamlit UI
# --------------------------

st.set_page_config(layout="wide")
st.title("💹 Bitcoin Sentiment Analyzer (Twitter)")

with st.sidebar:
    bearer_token = st.text_input("Enter your Twitter Bearer Token", type="password")
    keyword = st.text_input("Keyword to Search", value="bitcoin")
    max_results = st.slider("Number of Tweets", min_value=10, max_value=100, value=20)
    go = st.button("Analyze")

if go:
    if not bearer_token or not keyword:
        st.error("Please enter both Bearer Token and Keyword.")
    else:
        df = get_tweets(bearer_token, f"{keyword} lang:en -is:retweet", max_results)

        if not df.empty:
            st.subheader("🔎 Sample Tweets")
            st.dataframe(df[['text', 'sentiment', 'sentiment_label']].head(10), use_container_width=True)

            st.subheader("📊 Sentiment Distribution")
            sentiment_counts = df['sentiment_label'].value_counts()
            st.bar_chart(sentiment_counts)

            st.subheader("☁️ Word Cloud")
            all_words = ' '.join(df['clean_text'])
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)

            st.subheader("📥 Download CSV")
            st.download_button("Download CSV", data=df.to_csv(index=False), file_name="tweet_sentiment.csv", mime="text/csv")
