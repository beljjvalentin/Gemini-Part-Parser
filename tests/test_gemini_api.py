import unittest
from gemini_api import gemini_model


class TestGeminiAPI(unittest.TestCase):
    # this is not needed because we are creating the model instance inside the gemini_api.py
    # def setUp(self):
    #     pass

    # Valid here means questions in the scope of the instructions
    def test_valid_prompt(self):
        prompt = "How to use GitHub actions to deploy a Flask Application?"
        response = gemini_model(user_prompt=prompt)
        # print(response)
        # Minimum requirements for the answer is:
        # It must include the keywords: Flask, GitHub, Actions, Docker, Deploy
        self.assertIn("Flask", response)
        self.assertIn("GitHub", response)
        self.assertIn("Actions", response)
        self.assertIn("Docker", response)
        self.assertIn("Deploy", response)
        self.assertNotIn("Apple", response)
        self.assertNotIn("Car", response)
        self.assertNotIn("Alex", response)

    # Invalid here means questions outside the scope of the instructions
    def test_invalid_prompt(self):
        prompt = "Who is the current US president?"
        response = gemini_model(user_prompt=prompt)
        # print(response)
        self.assertIn("I can only answer questions about Flask, CI/CD, and Docker.", response)







