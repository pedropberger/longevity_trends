import os
import praw
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

    def fetch_subreddit_posts(self, subreddit_name, limit=10):
        """
        Fetches the latest posts from a given subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []
        for submission in subreddit.hot(limit=limit):
            posts.append({
                "id": submission.id,
                "title": submission.title,
                "score": submission.score,
                "url": submission.url,
                "num_comments": submission.num_comments,
                "created_utc": submission.created_utc,
                "selftext": submission.selftext
            })
        return posts

if __name__ == "__main__":
    # Example usage (requires .env configuration)
    scraper = RedditScraper()
    try:
        print("Fetching posts from r/longevity...")
        posts = scraper.fetch_subreddit_posts("longevity", limit=5)
        for post in posts:
            print(f"- {post['title']} ({post['score']} upvotes)")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have configured your .env file with valid Reddit API credentials.")
