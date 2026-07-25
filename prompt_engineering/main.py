from fastapi import FastAPI
from typing import *
from anthropic import Anthropic
#

app = FastAPI
client = Anthropic()

message = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)

# @app.post("/chat")
# def user_prompt() -> String:
#     usr = input(input("Hey!, how can I help ypou?"))
#     return



# if __name__ == "__main__":
