import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import base64

# Spotify API token endpoint
url = "https://accounts.spotify.com/api/token"

# Headers for the request
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": "09df1fdf94304abdbb0d93ed026256d6",  # Replace with your client ID
    "client_secret": "e271b28da35e4867b77d0f45060e19fb"  # Replace with your client secret
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    token = response.json().get("access_token")
else:
    print(f"Error: {response.status_code} - {response.text}")

# Define the URL
url = "https://api.spotify.com/v1/tracks/4gXX2ayvtMf4Tc5DCSHFTH"

# Add the Authorization header
headers = {
    f"Authorization": f"Bearer {token}"  # Replace with your actual access token
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    audio_features = response.json()
    print("Audio Features:", audio_features)
else:
    print(f"Error: {response.status_code} - {response.text}")


