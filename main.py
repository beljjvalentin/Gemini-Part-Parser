# pip install flask
# pip install python-dotenv
# pip install -q -U google-generativeai

from flask import Flask, request
from gemini_api import gemini_model
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    # Getting JSON data from POST request
    data = request.json

    # Extracting the "prompt" from the JSON data
    prompt = data["prompt"]

    # Calling the function "gemini_model" in the gemini_api.py
    output = gemini_model(user_prompt=prompt)

    # Returning the model response as the output
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)