import os
import openai
import json
import requests

# Load API keys from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
AIDEVS2_API_KEY = os.environ.get("AIDEVS2_API_KEY")

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY


def get_auth_token(taskname, print_json=False):
    url = "https://zadania.aidevs.pl/token/" + taskname

    # check the following statement
    # aidevs2.api_key = AIDEVS2_API_KEY

    key = {
        "apikey": AIDEVS2_API_KEY,
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps(key)
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        if print_json:
            print(response_json)
            return response_json['token']
    else:
        print(f"Failed to get response: {response.status_code}")
