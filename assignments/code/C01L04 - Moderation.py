import os
from api_utilities.aidevs2_api import get_token, get_task_details, post_answer
from api_utilities.openai_api import connect_openai, moderate

'''Zastosuj wiedzę na temat działania modułu do moderacji treści i rozwiąż zadanie o nazwie “moderation” z użyciem naszego API do sprawdzania rozwiązań.
Zadanie polega na odebraniu tablicy zdań (4 sztuki), a następnie zwróceniu tablicy z informacją, które zdania nie przeszły moderacji.
Jeśli moderacji nie przeszło pierwsze i ostatnie zdanie, to odpowiedź powinna brzmieć [1,0,0,1].
Pamiętaj, aby w polu ‘answer’ zwrócić tablicę w JSON, a nie czystego stringa.
P.S. wykorzystaj najnowszą wersję modelu do moderacji (text-moderation-latest)'''

TASK_NAME = 'moderation'

token = get_token(TASK_NAME)
task_details = get_task_details(token, print_task=True)
input_list = task_details['input']

score = []

for i in input_list:
    flag = moderate(i)
    print(f'{i}: {flag}')
    score.append(flag)

post_answer(token, score, print_answer=True)
