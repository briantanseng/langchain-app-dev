import os
# from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

# 1. Create a ChatOpenAI object with the desired model
llm_model="gpt-3.5-turbo-1106"
chat = ChatOpenAI(temperature=0.0, model=llm_model)

# 2. Create a prompt template
template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(template_string)
# prompt_template.messages[0].prompt
# prompt_template.messages[0].prompt.input_variables

# 3. Define the customer's style and email
customer_style = """American English \
in a calm and respectful tone
"""
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
# 4. Format the customer messages
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

# print(type(customer_messages))
# print(type(customer_messages[0]))
# print(customer_messages[0])

# 5. Call the chat method with the customer's messages
customer_response = chat(customer_messages)
print(customer_response.content)

# 6. Define the service reply and style
service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""
service_style_pirate = """\
a polite tone \
that speaks in English Pirate\
"""
# 7. Format the service messages
service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)
# print(service_messages[0].content)
service_response = chat(service_messages)
print(service_response.content)
