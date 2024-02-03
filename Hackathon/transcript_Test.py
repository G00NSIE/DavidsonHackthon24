from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
 
api_key = "AIzaSyAZCYEesMFWF7qwbXZz_AI22zKoxMYzx_E"  # replace it with your API key
channel_id = 'https://www.youtube.com/watch?v=xqXpBUNqkKs'  # replace it with your channel id
youtube = build('youtube', 'v3', developerKey=api_key)
 
def get_transcript(video_url):
    # Extract video id from URL
    video_id = video_url.split('watch?v=')[-1]
    
    # Get the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Print each line of the transcript
    for line in transcript:
        print(line['text'])

# Test the function with a YouTube video URL
get_transcript('https://www.youtube.com/watch?v=xqXpBUNqkKs&ab_channel=Techquickie')