from api_utilities.aidevs2_api import get_token, get_task_details, post_answer

TASK_NAME = 'helloapi'

token = get_token(TASK_NAME)
task_details = get_task_details(token)
post_answer(token, task_details['cookie'], print_answer=True)

