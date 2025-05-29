from reddit_scraper import fetch_comments
from sentiment_analysis import analyze_sentiment
import pandas as pd

def main():
    print("Fetching Reddit comments...")
    comments = fetch_comments("marketing", limit=50)
    
    print("Analyzing sentiments...")
    results = []
    for comment in comments:
        sentiment, score = analyze_sentiment(comment)
        results.append({
            "comment": comment,
            "sentiment": sentiment,
            "score": score
        })

    df = pd.DataFrame(results)
    print(df.head())

    # Save to CSV for later visualization
    df.to_csv("sentiment_output.csv", index=False)
    print("Sentiment analysis completed and saved to 'sentiment_output.csv'.")

if __name__ == "__main__":
    main()
