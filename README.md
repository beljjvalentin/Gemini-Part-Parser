# Gemini-Part-Parser
This application automates the parsing of electronic component data by combining two APIs:

**Mouser API:**
- Accepts user-entered part numbers.
- Queries the Mouser API to retrieve detailed component descriptions and specifications.

**Gemini API:**
- Processes the component description returned by the Mouser API.
- Extracts and parses key attributes (e.g., capacitance, voltage, tolerance, and package type) into a structured JSON format.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/beljjvalentin/CSD-4503-01.git
    cd your-repo-name
   
2. **Set Up a Virtual Environment:**
    It is recommended to create a virtual environment to isolate the project dependencies

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    
3. **Install Dependencies:**
   Install the required packages using pip:

    ```bash
    pip install -r requirements.txt

4. **Run the Python server:**

    Open a new terminal and run:

    ```bash
    flask run

## How to Use

To get results from the application, send a **POST** request to the `/chat` route.

### Example Request
You can use tools like [Postman](https://www.postman.com/) or `curl` to send a POST request.

#### Example using `curl`:
```bash
curl -X POST http://your-api-url/chat \
     -H "Content-Type: application/json" \
     -d '{"prompt": "CL32B106KBVVPLE"}'
