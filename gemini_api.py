import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
import os

from dotenv import load_dotenv

load_dotenv()

instructions = """
C0805C274K1RACTU Multilayer Ceramic Capacitors MLCC - SMD/SMT 100V 0.27uF X7R 0805 10% Temp Stable
"""

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "capacitance": content.Schema(
        type = content.Type.NUMBER,
      ),
      "capacitance_units": content.Schema(
        type = content.Type.STRING,
      ),
      "case_code": content.Schema(
        type = content.Type.STRING,
      ),
      "voltage": content.Schema(
        type = content.Type.NUMBER,
      ),
      "voltage_units": content.Schema(
        type = content.Type.STRING,
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=instructions
)


def gemini_model(user_prompt):
    # response = model.generate_content(user_prompt, tools='google_search_retrieval')
    response = model.generate_content(user_prompt)
    print(response.text)
    return response.text