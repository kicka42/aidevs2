import os
import requests
import json
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API keys from environments variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client_openai = OpenAI(api_key=OPENAI_API_KEY)


def connect_openai(model):
    try:
        result = client_openai.models.get_model(model)
        return result
    except Exception as e:
        return str(e)


# Function for assigment C01L04
def moderate(text_to_moderate, print_score=False):
    """Moderate the given text with OpenAI model.

    :param text_to_moderate: The text to be moderated.
    :param print_score: Option to print the moderation score (default: False).
    :return: The moderation response (0 for not flagged, 1 for flagged).
    """
    moderation_response = client_openai.moderations.create(input=text_to_moderate)
    response = int(moderation_response.results[0].flagged)
    return response

