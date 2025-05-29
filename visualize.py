import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def load_data():
    return pd.read_csv("sentiment_output.csv")

def plot_sentiment_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="sentiment", data=df, palette="coolwarm")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Comments")
    plt.tight_layout()
    plt.savefig("sentiment_distribution.png")
    plt.close()

def plot_sentiment_scores(df):
    plt.figure(figsize=(8, 4))
    sns.histplot(df["score"], bins=30, kde=True, color="skyblue")
    plt.title("Sentiment Score Distribution")
    plt.xlabel("Sentiment Score")
    plt.tight_layout()
    plt.savefig("sentiment_scores.png")
    plt.close()

def generate_wordcloud(df):

    text = " ".join(df["comment"].dropna())
    print(f"WordCloud text length: {len(text)}")  # Add this line for debug
    if len(text.strip()) == 0:
        print("No usable text found for word cloud.")
        return
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("wordcloud.png")
    plt.close()
    
plt.savefig("sentiment_distribution.png")
plt.savefig("sentiment_scores.png")
plt.savefig("wordcloud.png")
