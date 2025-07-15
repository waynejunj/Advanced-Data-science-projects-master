from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv() #loading env file
# pip3 install openai==0.28

app = Flask(__name__)


#  OpenAI API key
openai.api_key = os.getenv('API_KEY')


def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specifies the model to be used for generating the completion
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ], # A list of message objects that simulate a conversation. Each message object has two fields:
        max_tokens=150, #The maximum number of tokens (words or parts of words) in the response. This limits the length of the generated text.
        temperature=0.7, # Controls the randomness of the response. A higher value like 0.7 makes the output more diverse
    )
    return response.choices[0].message['content'].strip() #Accesses the content of the first choice in the response. The response from the API is usually a list of choices, and we're selecting the first one.
    # .strip(): Removes any leading or trailing whitespace from the generated text to clean up the output

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        generated_text = generate_text(prompt)
        return render_template("index.html", prompt=prompt, generated_text=generated_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
