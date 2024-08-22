import os
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

client = OpenAI(
  organization=os.environ['OPENAI_ORG'],
  api_key=os.environ['OPENAI_API_KEY']
)

llm_model="gpt-3.5-turbo-1106"

def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return completion.choices[0].message.content

print(get_completion("What is 1+1?"))
