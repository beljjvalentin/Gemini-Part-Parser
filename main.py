# pip install flask
# pip install python-dotenv
# pip install -q -U google-generativeai

from flask import Flask, request
from gemini_api import gemini_model
from mouser_api import search_mouser
import json

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    # Getting JSON data from POST request
    data = request.json

    # Extracting the "prompt" from the JSON data
    user_prompt = data["prompt"]

    response = search_mouser(user_prompt)
    if response['SearchResults']['NumberOfResult'] > 0:
        description = response['SearchResults']['Parts'][0]['Description']
        mfg_part_num = response['SearchResults']['Parts'][0]['ManufacturerPartNumber']
        prompt = mfg_part_num + ' ' + description
        response = gemini_model(user_prompt=prompt)

        # Remove the first 4 characters ("json")
        cleaned_response = response[8:-4]

        # Validate if the response is valid JSON
        try:
            parsed_response = json.loads(cleaned_response)
        except json.JSONDecodeError:
            return "The response is not valid JSON."

    else:
        return "Didn't get Mouser response"

    # Returning the model response as the output
    return parsed_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)