import unittest
import json
from gemini_api import gemini_model


class TestGeminiAPI(unittest.TestCase):
    # this is not needed because we are creating the model instance inside the gemini_api.py
    # def setUp(self):
    #     pass

    # Valid here means questions in the scope of the instructions
    def test_valid_prompt(self):
        prompt = "C0805C274K1RACAUTO Multilayer Ceramic Capacitors MLCC - SMD/SMT 100v 0.27Uf x7r 0805 10% Temp Stable AEC-Q200"
        response = gemini_model(user_prompt=prompt)
        print(response)
        # Minimum requirements for the answer is:

        # Check if the response is not empty
        self.assertIsNotNone(response, "The response should not be None.")

        # Remove the first 4 characters ("json")
        cleaned_response = response[8:-4]
        print(cleaned_response)
        # Validate if the response is valid JSON
        try:
            parsed_response = json.loads(cleaned_response)
        except json.JSONDecodeError:
            self.fail("The response is not valid JSON.")
        print(parsed_response)
        # Additional assertions for specific fields
        expected_keys = [
            "Capacitance", "Capacitance Units", "Voltage",
            "Voltage Units", "Dielectric Type", "Case Code",
            "Tolerance", "Mount Type"
        ]
        self.assertTrue(all(key in parsed_response for key in expected_keys),
                        "Not all expected keys are present in the response.")

    # Invalid here means questions outside the scope of the instructions
    def test_invalid_prompt(self):
        prompt = "Who is the current US president?"
        response = gemini_model(user_prompt=prompt)
        print(response)
        self.assertIn("I can only parse part attributes.", response)







