import requests
import os

from dotenv import load_dotenv

load_dotenv()

# Set your Mouser API key
MOUSER_API_KEY = os.environ["MOUSER_API_KEY"]  # Add your API key here or set it as an environment variable
MOUSER_API_URL = "https://api.mouser.com/api/v1/search/partnumber"


def search_mouser(parts_to_search, records=20, starting_record=0):
    """
    Search for parts in the Mouser API.

    Args:
        parts_to_search (str): The part number or keyword to search for.
        records (int): Number of records to fetch.
        starting_record (int): Starting record index for pagination.

    Returns:
        dict: Response from the Mouser API.
    """
    if not MOUSER_API_KEY:
        raise ValueError("API key is not set. Please set MOUSER_API_KEY.")

    # Payload for the API request
    payload = {
        "SearchByPartRequest": {
            "mouserPartNumber": parts_to_search
        },
        "SearchByKeywordRequest": {
            "keyword": parts_to_search,
            "records": records,
            "startingRecord": starting_record,
            "searchOptions": "None",
            "searchWithYourSignUpLanguage": False,
        }
    }

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            MOUSER_API_URL,
            headers=headers,
            params={"apiKey": MOUSER_API_KEY},
            json=payload
        )
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example part number to search
    parts_to_search = "LM317T"

    print("Searching Mouser for part:", parts_to_search)
    response = search_mouser(parts_to_search)
    if response:
        print("Search results:")
        print(response)
    else:
        print("Failed to retrieve search results.")