from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import requests

 
api_key = "AIzaSyAZCYEesMFWF7qwbXZz_AI22zKoxMYzx_E"  # replace it with your API key
channel_id = 'https://www.youtube.com/watch?v=xqXpBUNqkKs'  # replace it with your channel id
youtube = build('youtube', 'v3', developerKey=api_key)
#cloud flare ai
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/158e2c5ca1cb98881c848241a12f8801/ai/run/"
headers = {"Authorization": "Bearer RWG-19eYHl7tWsHDSPCk7P1j65zHHH5c8yMXKDXm"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


def get_transcript(video_url):
    # Extract video id from URL
    video_id = video_url.split('watch?v=')[-1]
    
    # Get the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # Combine each line of the transcript into a single string
    transcript_text = ' '.join([line['text'] for line in transcript])
    
    return transcript_text

# Get the transcript from a YouTube video URL
transcript = get_transcript('https://www.youtube.com/watch?v=vubxL52NlAY&ab_channel=Garbaj')

# Use the transcript as the user's message in the inputs for the run function
inputs = [
    { "role": "system", "content": "You are a Learning assistant and educator designed to facilitate a comprehensive and interactive learning experience. you serve as a digital tutor, provide educational support and resources to users across a wide range of subjects. when given a prompt you should summerize the main points and provide detailed analysis report of the prompt." },
    { "role": "user", "content": transcript}
]

output = run("@cf/meta/llama-2-7b-chat-int8", inputs)
print(output)
