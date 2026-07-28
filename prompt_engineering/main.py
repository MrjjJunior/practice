from openai import OpenAI
import os
import sys

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url= "https://api.groq.com/openai/v1/",
)


def userPrompt()-> str:
    return input("> ")


def main():
    user = userPrompt()
    print(getUserIntent(user))
    

def getUserIntent(user) -> dict:
    """ Prompt the ai to get user intent """

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=f"""
You are an insurance assistant.

Your job is to identify the user's intent

Here is the user prompt: {user}

Available intents:
- create_claim
- update_address
- check_claim_status

Return ONLY valid JSON.

Do not explain your reasoning.

Use this json format:

  "intent": "",
  "confidence": 0,
  "parameters": 

"""
    )

    return response.output_text

if __name__ == "__main__":
    main()
