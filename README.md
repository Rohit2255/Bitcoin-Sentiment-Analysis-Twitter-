# 🧠 Bitcoin Sentiment Analysis using Twitter & NLP

A real-time Bitcoin sentiment analyzer built using Streamlit, Twitter API v2, and VADER NLP. This dashboard fetches live tweets containing the keyword "Bitcoin", analyzes their sentiments (Positive, Neutral, Negative), and presents the results in an interactive, data-rich interface.

> 🔴 **Live Demo**: [https://bitcoinsentiment.streamlit.app](https://bitcoinsentiment.streamlit.app)

---

## 📌 Project Overview

As part of my **#100DaysOfFinanceDataScience** challenge, this project aims to bridge the gap between financial sentiment and real-time public opinion by analyzing live tweets related to Bitcoin.

Key objectives:
- Scrape recent tweets using Twitter API v2
- Clean and preprocess tweet text
- Analyze tweet sentiment using VADER (from NLTK)
- Visualize sentiment distribution and tweet metadata
- Deploy the app using Streamlit Cloud

---

## 🚀 Features

✅ Real-time tweet fetching for the term **"Bitcoin"**  
✅ Sentiment scoring (compound, positive, negative, neutral) using **VADER**  
✅ Clean and minimalist **Streamlit UI**  
✅ **Top 5 Positive and Negative Tweets** displayed  
✅ **Word Cloud** for frequently used terms  
✅ **Sentiment over time** interactive Plotly line chart  
✅ CSV **download** of processed tweet sentiment data  
✅ Fully **deployed** and accessible to the public

---

## 🖼️ Screenshots

### 🔹 Sentiment Distribution
Visual breakdown of positive, neutral, and negative tweets.

### 🔹 Word Cloud
Commonly used terms in live Bitcoin tweets.

### 🔹 Sentiment Over Time
How sentiment changes minute-by-minute.

### 🔹 Sample Table
| Tweet Snippet                                 | Sentiment | Score  |
|-----------------------------------------------|-----------|--------|
| Bitcoin will explode in 2025!                 | Positive  | 0.88   |
| I'm unsure about the market right now...      | Neutral   | 0.01   |
| Bitcoin crash ruined everything 😡            | Negative  | -0.72  |

---

## 🛠️ Tech Stack

| Tool          | Usage                                  |
|---------------|----------------------------------------|
| **Python**    | Core Programming Language              |
| **Streamlit** | App Interface and Deployment           |
| **Twitter API v2** | For scraping real-time Bitcoin tweets |
| **VADER**     | Sentiment analysis (lexicon + rule-based) |
| **NLTK**      | NLP preprocessing toolkit              |
| **Plotly**    | Interactive line plots                 |
| **WordCloud** | Visualization of term frequency        |
| **Pandas**    | Data manipulation                      |
| **Seaborn / Matplotlib** | Static charts (optional use)    |

---

## 🚀 Deployment

This project has been deployed using [Streamlit Cloud](https://streamlit.io/cloud). You can access and try out the live app here:

🔗 **Live App**: [Bitcoin Sentiment Analysis](https://bitcoinsentiment.streamlit.app/)

### How to Deploy on Your Own

1. Push your code to a public GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Click on "New app" and connect your GitHub repository.
4. Choose the correct branch and `app.py` as the entry file.
5. Click "Deploy".

> **Note**: Make sure to add your Bearer Token in your deployed environment as a secret:
>
> Go to **Settings > Secrets** in Streamlit Cloud and add:
> ```plaintext
> BEARER_TOKEN = your_twitter_bearer_token_here
> ```

---

## 🤝 Show Your Support

If you liked this project or found it helpful:

🌟 Give the project a star on GitHub  
📢 Share the live app link with your network  
🐛 Report any bugs or suggestions via issues

---

## 🧑‍💻 Author

**Rohit Kumar Yadav**

- [LinkedIn](https://www.linkedin.com/in/rohit-kumar-yadav-b97360194/)
- [GitHub](https://github.com/rohit2255)

---

## 📜 License

This project is licensed under the MIT License.

