import os
from api_utilities.aidevs2_api import get_token, get_task_details, post_answer
from api_utilities.openai_api import connect_openai, moderate

TASK_NAME = 'moderation'

token = get_token(TASK_NAME)
task_details = get_task_details(token, print_task=True)
input_list = task_details['input']

score = []

for i in input_list:
    flag = moderate(i)
    print(f'{i}: {flag}')
    score.append(flag)

post_answer(token, score)
