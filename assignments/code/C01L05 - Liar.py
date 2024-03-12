import os
from openai import OpenAI
from api_utilities.aidevs2_api import get_token, get_task_details, post_answer, post_question
from api_utilities.openai_api import connect_openai, moderate, client_openai

'''wykonaj zadanie o nazwie liar.
Jest to mechanizm, który mówi nie na temat w 1/3 przypadków.
Twoje zadanie polega na tym, aby do endpointa /task/ wysłać swoje pytanie w języku angielskim
(dowolne, np “What is capital of Poland?’) w polu o nazwie ‘question’
(metoda POST, jako zwykłe pole formularza, NIE JSON). System API odpowie na to pytanie
(w polu ‘answer’) lub zacznie opowiadać o czymś zupełnie innym, zmieniając temat.
Twoim zadaniem jest napisanie systemu filtrującego (Guardrails), który określi (YES/NO),
czy odpowiedź jest na temat. Następnie swój werdykt zwróć do systemu sprawdzającego jako
pojedyncze słowo YES/NO. Jeśli pobierzesz treść zadania przez API bez wysyłania żadnych dodatkowych
parametrów, otrzymasz komplet podpowiedzi. Skąd wiedzieć, czy odpowiedź jest ‘na temat’?
Jeśli Twoje pytanie dotyczyło stolicy Polski, a w odpowiedzi otrzymasz spis zabytków w Rzymie,
to odpowiedź, którą należy wysłać do API to NO.'''

TASK_NAME = 'liar'

token = get_token(TASK_NAME)
task_details = get_task_details(token, print_task=True)
question = "What is capital of Poland?"

response = post_question(token, question, print_response=True)

msg = [{
    "role": "system",
    "content": "Answer the question correctly. Use a maximum of 150 tokens.",
    "role": "user",
    "content": question
}]

response_gpt = client_openai.chat.completions.create(model="gpt-3.5-turbo", messages=msg, max_tokens=300)

# print(response_gpt.choices[0].message.content)

msg2 = [{
    "role": "system",
    "content": "Compare the two sentences."
               "Rules:"
               "- If sentences are the same return YES, otherwise return only NO."
               "- You are not allow to return anything else.",
    "role": "user",
    "content": "Compare the two sentences."
               "Rules:"
               "- If sentences are the same return YES, otherwise return only NO."
               "- You are not allow to return anything else."
               "Are these sentences the same? " + str(response_gpt) + " and " + str(response)
}]

compare = client_openai.chat.completions.create(model="gpt-3.5-turbo", messages=msg2, max_tokens=350)

# print(compare.choices[0].message.content)

post_answer(token, compare.choices[0].message.content, print_answer=True)
