import openai
from key import api_key

openai.api_key = api_key

user_message = input(">>> ")

with open('member.txt', 'a') as f:
    f.write(f"User: {user_message} \n")

with open('member.txt', 'r') as file:
    member = file.read()


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=member,
    temperature=0.25,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
)
ai_text = response["choices"][0]["text"]

with open('member.txt' 'w') as f:
    f.write(f"{ai_text} \n")

print(ai_text)