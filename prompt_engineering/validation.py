




def validate_intent(response: dict) -> bool:

    try:
        return  (contains_fields(response) and 
                correct_data_types(response) and
                response["intent"] in available_intents()
                )
    except:
        return "Retrying to get valid response."


def get_valid_intent(raw_response: dict, max_retries: int=3) -> dict:
    current_response = raw_response

    for attempt in range(max_retries):
        if validate_intent(current_response):
            return current_response
        else:
            print(f"validation failed (Attempt {attempt + 1}/{max_retries}). Restructuring...")
            current_response = restructure_json(current_response)

    return {"message": "Invalid JSON format"}

def restructure_json(response) -> dict:
    """ Request AI to fix the response to need structure"""
    ...


def contains_fields(response) -> bool:
    if "intent" in response and "confidence" in response:
        return True
    else:
        return False

def correct_data_types(response) -> bool:
    try:
        return (type(response["intent"]) == str and 
            type(response["confidence"]) == float )
    except Exception as e:
        return "Malformed json"


def available_intents() -> list:
    ...
    return ["submit_claim", "update address"]

# print("intent" in valid_response)
# print(type(valid_response["intent"])== str)
# print(type(valid_response["confidence"]))

valid_response = {
    "intent": "submit_claim",
    "confidence":0.98
}

invalid_response = "The user probably wants to submit a claim."

malformed_json = "{intent:"

if __name__ == "__main__":
    print("Valid response:",validate_intent(valid_response))
    print("Valid response:",validate_intent(invalid_response))
    print("Valid response:",validate_intent(malformed_json))
