import praw

REDDIT_CLIENT_ID = 'Ko2yY23B5R2SpfkYF20wxg'
REDDIT_SECRET = 'yk0qXFvyRtLT5209AssdLqDGzV5wxA'
REDDIT_USER_AGENT = 'audience-mood-analyzer by /u/Capital-Log2136'

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_comments(subreddit_name, limit=100):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        comments = []
        for post in subreddit.hot(limit=10):
            post.comments.replace_more(limit=0)
            for comment in post.comments.list():
                if len(comments) >= limit:
                    break
                comments.append(comment.body)
        return comments
    except Exception as e:
        print(f"Error fetching from r/{subreddit_name}: {e}")
        return []

