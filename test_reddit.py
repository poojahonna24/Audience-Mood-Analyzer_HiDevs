import praw

reddit = praw.Reddit(
    client_id='Ko2yY23B5R2SpfkYF20wxg',
    client_secret='yk0qXFvyRtLT5209AssdLqDGzV5wxA',
    user_agent='audience-mood-analyzer by /u/Capital-Log2136'
)

print(reddit.read_only)  # This should print: True
