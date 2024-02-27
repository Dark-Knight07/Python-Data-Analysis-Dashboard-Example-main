import tweepy
import facebook
from datetime import datetime

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Facebook Graph API access token
fb_access_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Authenticate with Facebook
graph = facebook.GraphAPI(fb_access_token)

# Function to fetch Twitter posts
def fetch_twitter_posts(username, count=10):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    return [{"text": tweet.full_text, "date": tweet.created_at} for tweet in tweets]

# Function to fetch Facebook posts
def fetch_facebook_posts(page_id, count=10):
    posts = graph.get_connections(page_id, 'posts', limit=count)
    return [{"text": post['message'], "date": datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S%z')} for post in posts['data']]

# Function to schedule a post
def schedule_post(platform, content, schedule_time):
    # Logic to schedule a post
    print(f"Scheduled post on {platform} at {schedule_time}: {content}")

# Function to analyze post engagement
def analyze_engagement(posts):
    total_posts = len(posts)
    total_likes = sum(len(post['likes']) for post in posts)
    avg_likes_per_post = total_likes / total_posts if total_posts != 0 else 0
    print(f"Total posts: {total_posts}")
    print(f"Total likes: {total_likes}")
    print(f"Avg likes per post: {avg_likes_per_post}")

# Fetching posts from Twitter
twitter_posts = fetch_twitter_posts("twitter_username")

# Fetching posts from Facebook
facebook_posts = fetch_facebook_posts("facebook_page_id")

# Displaying fetched posts
print("Twitter Posts:")
for post in twitter_posts:
    print(post)

print("\nFacebook Posts:")
for post in facebook_posts:
    print(post)

# Example of scheduling a post
schedule_post("Twitter", "This is a scheduled tweet", datetime.now())

# Example of analyzing engagement
analyze_engagement(twitter_posts + facebook_posts)
