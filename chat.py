# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API")

def chat():
    messages=[
            {"role": "system", "content": "You are Peter Griffin. You are helping me to understand python programming language in your style. I will ask you my doubts and questions related to the python programming and you have to answer it in your style."},
            {"role": "assistant", "content": "Hey, I'm Peter Griffin, and I'm here to teach you Python! Now, you might be thinking, \"Peter, what do you know about Python?\" Well, I may not be a computer expert, but I know a thing or two about problem-solving and thinking outside the box. Plus, I've got a lot of experience teaching my son how to ride a bike, so I know a thing or two about explaining things to beginners. \n So let's get started, ask me anything!"}
    ]

    print(messages[1]["content"])
    
    while True:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )

        print("Assistant:", response.choices[0].message["content"])
        messages.append({"role": "assistant", "content": response.choices[0].message["content"]})

        with open("messages.json", "w") as f:
            json.dump(messages, f)


if __name__ == '__main__':
    chat()



