# Creating a GPT-powered application
# pip install openai==0.28
import openai
import os
from dotenv import load_dotenv
load_dotenv() #loading env file
#  OpenAI API key
openai.api_key = os.getenv('API_KEY')

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    prompt = "Write a short story about a dragon and a wizard."
    generated_text = generate_text(prompt)
    print("Generated Text:\n", generated_text)

