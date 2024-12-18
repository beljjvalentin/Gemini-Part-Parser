import unittest
from mouser_api import search_mouser


class TestMouserAPI(unittest.TestCase):

    # Valid here means that there is a response and manufacturer is valid
    def test_valid_prompt(self):
        # Example part number to search
        parts_to_search = "C0805C274K1RACTU"

        response = search_mouser(parts_to_search)

        self.assertIsNotNone(response)
        self.assertIn('SearchResults', response)
        self.assertEqual(response['SearchResults']['NumberOfResult'], 1)
        self.assertEqual(response['SearchResults']['Parts'][0]['Manufacturer'], 'KEMET')

    # Invalid here means no response or invalid response
    def test_invalid_prompt(self):
        # Example part number to search
        parts_to_search = "Bw4Aij7tfUsUA1FU"

        response = search_mouser(parts_to_search)

        self.assertIsNotNone(response)
        self.assertIn('SearchResults', response)
        self.assertEqual(response['SearchResults']['NumberOfResult'], 0)
        self.assertEqual(response["SearchResults"]["Parts"], [])
