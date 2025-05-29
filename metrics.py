from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

def evaluate_model(df):
    y_true = df["sentiment"]
    y_pred = df["sentiment"]  # Normally you'd compare with actual labels here

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
