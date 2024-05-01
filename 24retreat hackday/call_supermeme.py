import requests
import json

# # Max text length is 150 characters
# api_key = see Matt's 1pasword

def generate_meme(text):
    url = "https://app.supermeme.ai/api/v1/meme/text"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "text": text
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Meme generated successfully!")
            return response.json()['memes'][0]['image']
        else:
            print(f"Meme generation failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error generating meme:", e)