import os
from dotenv import load_dotenv
import openai
import json
import requests

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
AIDEVS2_API_KEY = os.getenv("AIDEVS2_API_KEY")

BASE_URL = "https://zadania.aidevs.pl"
HEADERS = {"Content-Type": "application/json"}


def api_call(endpoint, method, data=None, headers=None):
    url = BASE_URL + endpoint
    if method == 'get':
        response = requests.get(url)
    elif method == 'post':
        response = requests.post(url, data=data, headers=headers)
    else:
        raise ValueError('Invalid method')
    response.raise_for_status()
    return response.json()


def get_token(task_name, print_response=False):
    """
    Get token for a specified task.

    :param task_name: The name of the task.
    :param print_response: Flag to print the response JSON. Default is False.
    :return: The token retrieved from the response JSON.
    """
    endpoint = f"/token/{task_name}"
    api_key = json.dumps({"apikey": AIDEVS2_API_KEY})
    response_json = api_call(endpoint, 'post', data=api_key, headers=HEADERS)
    if print_response:
        print(response_json)
    return response_json['token']


def get_task_details(token_key, print_task=False):
    """
    Get the details of a task.

    :param token_key: The token key of the task.
    :param print_task: Optional parameter to print the content of the task. Default is False.
    :return: The response JSON.
    """
    endpoint = f"/task/{token_key}"
    response_json = api_call(endpoint, 'get')
    if print_task:
        for key in list(response_json.keys())[1:]:
            print(f'{key}: {response_json[key]}')
    return response_json


def post_answer(token_key, answer_value, print_answer=False):
    """
    Post an answer.

    :param token_key: The token key for the answer.
    :param answer_value: The value of the answer.
    :param print_answer: Whether to print the answer data. Default is False.
    :return: None.
    """
    endpoint = f"/answer/{token_key}"
    response_data = {
        "answer": answer_value
    }
    response_json = api_call(endpoint, 'post', data=json.dumps(response_data), headers=HEADERS)
    if print_answer:
        print(f"answer:{response_json}")
