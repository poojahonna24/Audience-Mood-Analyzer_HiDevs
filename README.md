🧠 Audience Mood Analyzer – Reddit & Twitter Sentiment Dashboard
An AI-powered tool to analyze social media comments, detect audience mood, and provide visual insights to improve marketing campaigns and audience engagement.

📌 What This Project Does
This project:

Collects real-time Reddit comments using the Reddit API

Classifies each comment as positive, negative, or neutral using an LLM (Large Language Model)

Displays mood insights visually in an interactive web dashboard

Helps marketers or campaign teams understand and adapt to audience sentiment in real time

🚀 Features
✅ Live comment fetching from any subreddit
✅ Sentiment classification using LLM (DistilBERT)
✅ “Neutral” class simulated for better real-world accuracy
✅ Interactive dashboard built with Streamlit
✅ Charts for mood distribution, sentiment scores, and word clouds
✅ Evaluation with real-world labeled data (Twitter sentiment140)
✅ Confusion matrix + classification report for model performance

🛠️ Tech Stack
Layer	Tools / Libraries
Data Source	Reddit API (via praw), Twitter dataset from Kaggle
Backend	Python, HuggingFace Transformers, Pandas
Sentiment	distilbert-base-uncased-finetuned-sst-2-english (LLM)
Frontend	Streamlit (for interactive dashboard)
Visualization	Matplotlib, Seaborn, WordCloud
Evaluation	Scikit-learn (accuracy, F1, confusion matrix)

🔍 How to Run This Project (Step-by-Step for Beginners)
1. Clone the Project

2. Install Required Libraries
bash
Copy code
pip install -r requirements.txt
If requirements.txt is not available, manually run:

bash
Copy code
pip install praw vaderSentiment matplotlib seaborn wordcloud pandas scikit-learn transformers torch streamlit
3. Setup Reddit API Access
Go to: https://www.reddit.com/prefs/apps

Click “Create another app”

Fill the form:

Name: AudienceMoodAnalyzer

App type: script

Redirect URI: http://localhost

Copy your client ID and secret

Update reddit_scraper.py:

python
Copy code
REDDIT_CLIENT_ID = 'your_client_id'
REDDIT_SECRET = 'your_client_secret'
REDDIT_USER_AGENT = 'audience-mood-analyzer by /u/your_reddit_username'
4. Fetch and Analyze Reddit Comments
bash
Copy code
python3 audience_mood_analyzer/main.py
This fetches comments, classifies sentiment, and saves the results in sentiment_output.csv.

5. Generate Visualizations
bash
Copy code
python3 audience_mood_analyzer/visualize.py
This creates:

sentiment_distribution.png

sentiment_scores.png

wordcloud.png

6. Launch the Dashboard
bash
Copy code
streamlit run dashboard.py
Visit the URL (usually http://localhost:8501) to interact with your dashboard.

7. Run Evaluation with Real Labels (Optional)
bash
Copy code
python3 evaluate.py
This compares your model predictions to real tweet labels and generates:

A classification report

A confusion matrix image

📊 Example Output
Accuracy: ~77% (zero-shot using LLM on real Twitter data)

Confusion Matrix: evaluation_confusion_matrix.png

Mood Charts: sentiment_distribution.png, sentiment_scores.png, wordcloud.png

🔬 How to Improve Accuracy
While this project uses a strong LLM (distilbert-base-uncased-finetuned-sst-2-english), you can improve accuracy further by:

Using a model fine-tuned on social media
Swap in: cardiffnlp/twitter-roberta-base-sentiment

Preprocessing input better

Remove usernames, hashtags, emojis

Normalize slang, spelling, etc.

Fine-tuning on GPU (Advanced)
If you have access to a GPU or Google Colab, you can fine-tune your own BERT/RoBERTa model using the full sentiment140 dataset.
This can push accuracy from 77% to 90%+ with the right tuning.

python
Copy code
# Example idea (not run on HiDevs):
Trainer(...).train()
📦 Folder Structure
css
Copy code
Audience-Mood-Analyzer/
├── audience_mood_analyzer/
│   ├── reddit_scraper.py
│   ├── sentiment_analysis.py
│   ├── visualize.py
│   └── main.py
├── dashboard.py
├── evaluate.py
├── sentiment_output.csv
├── evaluation_confusion_matrix.png
├── sentiment_distribution.png
├── sentiment_scores.png
├── wordcloud.png
├── requirements.txt
└── README.md
🏁 Final Outcome
This tool enables:

Marketing teams to adjust campaigns based on mood data

Analysts to track sentiment in real time from Reddit

Anyone to build and understand sentiment pipelines