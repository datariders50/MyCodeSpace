import requests
import json

# Turbonomic API URL and Token
api_url = "https://<turbonomic-server>/vmturbo/rest/stats"  # Replace with your Turbonomic server address
token = "your_bearer_token_here"

# Headers including the Bearer token for authorization
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")