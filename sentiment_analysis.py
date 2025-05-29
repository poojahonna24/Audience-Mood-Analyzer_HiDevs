from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    try:
        result = classifier(text[:512])[0]  # Truncate to max 512 tokens
        raw_label = result['label'].lower()  # 'positive' or 'negative'
        score = result['score']

        # Simulate neutral if confidence is low
        if score < 0.6:
            return "neutral", score
        return raw_label, score

    except Exception as e:
        return "neutral", 0.0
