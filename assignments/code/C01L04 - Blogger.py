import os
import json
from openai import OpenAI
from api_utilities.aidevs2_api import get_token, get_task_details, post_answer
from api_utilities.openai_api import connect_openai, client_openai

'''Napisz wpis na bloga (w języku polskim) na temat przyrządzania pizzy Margherity.
Zadanie w API nazywa się ”blogger”. Jako wejście otrzymasz spis 4 rozdziałów, które muszą pojawić się we wpisie.
Jako odpowiedź musisz zwrócić tablicę (w formacie JSON) złożoną z 4 pól reprezentujących te cztery rozdziały,
np.: {"answer":["tekst 1","tekst 2","tekst 3","tekst 4"]}'''

TASK_NAME = 'blogger'

token = get_token(TASK_NAME)
task_details = get_task_details(token, print_task=True)

input_list = task_details['blog']


base = [{
    "role": "system",
    "content": "Jesteś kucharzem specjalistą w robieniu pizzy Margherity. Znasz wszystkie historyczne ciekawostki na temat pizzy. Odpisujesz zwięźle czystym tekstem, ciągniem znaków bez myślników."
}]


def prompt(title):
    return f"Napisz na bloga ciekawy i konkretny wpis na temat: {title}"


blog_posts = []

for i in input_list:

    askai = base.copy()
    askai.append({"role": "user", "content": prompt(i)})
    response = client_openai.chat.completions.create(model="gpt-3.5-turbo", messages=askai, max_tokens=500)
    blog_posts.append(response.choices[0].message.content)
    askai.clear()


post_answer(token, blog_posts, print_answer=True)
