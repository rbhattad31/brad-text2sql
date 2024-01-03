
import os
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.base_url = os.getenv('OPENAI_API_BASE_URL')
openai.api_version = os.getenv('OPENAI_API_VERSION')
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(system_message, user_message, model="qnagpt5", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    client = AzureOpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),
        api_version=os.getenv('OPENAI_API_VERSION'),
        azure_endpoint=os.getenv('OPENAI_API_BASE_URL')
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))