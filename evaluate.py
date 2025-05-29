import pandas as pd
from sentiment_analysis import analyze_sentiment
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
path = kagglehub.dataset_download("kazanova/sentiment140")
# Load sample Twitter sentiment dataset
def load_real_data(path, n=100):
    df = pd.read_csv(path, encoding="latin-1", header=None)
    df = df[[0, 5]]
    df.columns = ["label", "text"]
    label_map = {0: "negative", 2: "neutral", 4: "positive"}
    df["label"] = df["label"].map(label_map)
    return df.sample(n)

# Run evaluation
def evaluate_sentiment_model(data):
    y_true = []
    y_pred = []

    for _, row in data.iterrows():
        actual = row["label"]
        predicted, score = analyze_sentiment(row["text"])
        y_true.append(actual)
        y_pred.append(predicted)

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_true, y_pred, labels=["positive", "neutral", "negative"])
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=["positive", "neutral", "negative"],
                yticklabels=["positive", "neutral", "negative"], cmap="coolwarm")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig("evaluation_confusion_matrix.png")
    print("Confusion matrix saved as evaluation_confusion_matrix.png")

# Run it
if __name__ == "__main__":
    data = load_real_data(r"/home/codespace/.cache/kagglehub/datasets/kazanova/sentiment140/versions/2/training.1600000.processed.noemoticon.csv", n=100)

    evaluate_sentiment_model(data)
