
#import the needed libraries

import random
import string
import nltk
from nltk.stem import PorterStemmer

#initialize the natural language processing token
nltk.download("punkt")
stemmer = PorterStemmer()

# define our data
data = {
    "greetings": ["hello", "hi", "hey", "howdy", "hola"],
    "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
}


#preprocessing step of the user input
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]

#generate response based on the user input
def get_response(user_input):
    user_input = preprocess(user_input)
    
    for intent, patterns in data.items():
        for pattern in patterns:
            if all(word in user_input for word in preprocess(pattern)):
                return random.choice(data[intent])
            
            
            
    return "word not in the list"

#chat loop

def chat():
    print("hello, i am your chatbot,press exit to exit")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower == "exit":
            break
        
        response =get_response(user_input)
        print("chatbot", response)


if __name__ == "__main__":
    chat()