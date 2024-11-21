import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Define system instructions for the model
instructions = """
You are an assistant designed to parse capacitor details into JSON format. 
When given a description of a capacitor, extract and return the following fields:
Capacitance, Capacitance Units, Voltage, Voltage Units, Dielectric Type, Case Code, Tolerance, Mount Type
If information is missing, return null for those fields.
If you have been asked any question that is not related to parsing the part, 
then answer using response exactly as "I can only parse part attributes."
"""
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

# Function to query the model and return structured JSON
def gemini_model(user_prompt):
    # Combine instructions with the user prompt
    # full_prompt = instructions + "\n\n" + user_prompt
    # print(full_prompt)

    # Generate content using the AI model
    response = model.generate_content(
        user_prompt
    )

    # Print and return the generated text
    # print(response.text)
    return response.text


# Example usage
if __name__ == "__main__":
    user_prompt = "C0805C274K1RACTU Multilayer Ceramic Capacitors MLCC - SMD/SMT 100V 0.27uF X7R 0805 10% Temp Stable"
    # user_prompt = "Who is the Prime minister of Canada?"
    response = gemini_model(user_prompt)
    print(response)
