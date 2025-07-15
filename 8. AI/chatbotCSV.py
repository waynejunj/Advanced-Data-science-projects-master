import random
import re
import csv

# Function to load responses from a CSV file
def load_responses_from_csv(file_path):
    responses = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pattern = row['pattern']
            responses_list = row['responses'].split(';')
            responses[pattern] = responses_list
    return responses

# Load responses from the CSV file
responses = load_responses_from_csv('chatbot.csv')
# print(load_responses_from_csv('chatbot.csv'))

def respond(message):
    for pattern, responses_list in responses.items():
        if re.search(pattern, message, re.IGNORECASE):
            return random.choice(responses_list)
    return random.choice(responses[r'(.*)'])

print("School Chatbot: Hi! How can I help you today? (type 'exit' to quit)")

while True:
    user_message = input("You: ").lower()
    
    if user_message == 'exit':
        print("School Chatbot: Goodbye!")
        break
    
    bot_response = respond(user_message)
    print("School Chatbot:", bot_response)

#an example of a Generative AI chatbot project: https://www.kaggle.com/code/omgits0mar/chatbot-from-scratch-llms-finetune