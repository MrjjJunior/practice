


valid_response = {
    "intent": "submit_claim",
    "confidence":0.98
}

invalid_response = "The user probably wants to submit a claim."

def validate_intent(response) -> bool:

    try:
        return contains_fields(response) and correct_data_types(response)
    
    except:
        return "Retrying to get valid response."


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
        return False

# print("intent" in valid_response)
# print(type(valid_response["intent"])== str)
# print(type(valid_response["confidence"]))

if __name__ == "__main__":
    print("Valid response:",validate_intent(valid_response))
    print("Valid response",validate_intent(invalid_response))
