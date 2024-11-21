import unittest
import json
from gemini_api import gemini_model
from mouser_api import search_mouser


class TestPartAPI(unittest.TestCase):
    def test_valid_prompt(self):
        parts_to_search = "C0805C274K1RACTU"

        response = search_mouser(parts_to_search)
        if response['SearchResults']['NumberOfResult'] > 0:
            description = response['SearchResults']['Parts'][0]['Description']
            mfg_part_num = response['SearchResults']['Parts'][0]['ManufacturerPartNumber']
            prompt = mfg_part_num + ' ' + description
            response = gemini_model(user_prompt=prompt)
            print(response)

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

        else :
            self.fail("Didn't get Mouser response")
